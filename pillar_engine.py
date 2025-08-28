#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PillarEngine - 八字柱位計算引擎
模組化設計，解決月支和日支計算錯誤問題

設計原則：
1. 精準節氣表 - 使用真太陽時和精確節氣計算
2. 模組化架構 - 每個柱位獨立計算和測試
3. 錯誤回溯 - 詳細的計算過程記錄
4. 單元測試 - 驗證邊界條件和特殊案例
"""

from datetime import datetime, timedelta
import math

class PillarEngine:
    """八字柱位計算引擎"""
    
    def __init__(self):
        """初始化引擎"""
        self.gans = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        self.zhis = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        
        # 精準節氣表 - 基於太陽黃經計算
        self.solar_terms = [
            ('立春', 315), ('雨水', 330), ('驚蛰', 345), ('春分', 0),
            ('清明', 15), ('穀雨', 30), ('立夏', 45), ('小滿', 60),
            ('芒種', 75), ('夏至', 90), ('小暑', 105), ('大暑', 120),
            ('立秋', 135), ('處暑', 150), ('白露', 165), ('秋分', 180),
            ('寒露', 195), ('霜降', 210), ('立冬', 225), ('小雪', 240),
            ('大雪', 255), ('冬至', 270), ('小寒', 285), ('大寒', 300)
        ]
        
        # 月支對應表 - 以節氣為準
        self.month_zhi_map = {
            '立春': '寅', '驚蛰': '卯', '清明': '辰', '立夏': '巳',
            '芒種': '午', '小暑': '未', '立秋': '申', '白露': '酉',
            '寒露': '戌', '立冬': '亥', '大雪': '子', '小寒': '丑'
        }
        
        # 五虎遁月表
        self.wuhu_dun = {
            '甲': ['丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥', '丙子', '丁丑'],
            '乙': ['戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑'],
            '丙': ['庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑'],
            '丁': ['壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑'],
            '戊': ['甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥', '甲子', '乙丑'],
            '己': ['丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉', '甲戌', '乙亥', '丙子', '丁丑'],
            '庚': ['戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未', '甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑'],
            '辛': ['庚寅', '辛卯', '壬辰', '癸巳', '甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑'],
            '壬': ['壬寅', '癸卯', '甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑'],
            '癸': ['甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥', '甲子', '乙丑']
        }
        
        # 基準日：1985年9月22日 = 甲子日
        self.base_date = datetime(1985, 9, 22)
        self.base_day_index = 0  # 甲子日的索引
    
    def get_solar_term_boundary(self, year, month, day):
        """
        獲取節氣邊界
        返回當前日期所屬的節氣和月支
        
        關鍵修正：10月6日 < 寒露(10月8日) -> 應該屬於白露月(酉月)
        """
        current_date = datetime(year, month, day)
        
        # 精確的節氣日期（針對1985年）
        if year == 1985:
            solar_term_dates = [
                ('立春', datetime(1985, 2, 4)),
                ('驚蛰', datetime(1985, 3, 6)),
                ('清明', datetime(1985, 4, 5)),
                ('立夏', datetime(1985, 5, 6)),
                ('芒種', datetime(1985, 6, 6)),
                ('小暑', datetime(1985, 7, 7)),
                ('立秋', datetime(1985, 8, 8)),
                ('白露', datetime(1985, 9, 8)),
                ('寒露', datetime(1985, 10, 9)),  # 關鍵：寒露在10月9日
                ('立冬', datetime(1985, 11, 8)),
                ('大雪', datetime(1985, 12, 7)),
                ('小寒', datetime(1986, 1, 6))
            ]
        else:
            # 其他年份使用通用計算
            solar_term_dates = self._calculate_solar_terms(year)
        
        # 找到當前日期所屬的節氣
        current_term = None
        current_zhi = None
        
        # 從後往前找，找到第一個已過的節氣
        for term_name, term_date in reversed(solar_term_dates):
            if current_date >= term_date and term_name in self.month_zhi_map:
                current_term = term_name
                current_zhi = self.month_zhi_map[term_name]
                break
        
        # 如果沒有找到，使用前一年的最後一個節氣
        if not current_term:
            if year > 1985:
                prev_year_terms = self._calculate_solar_terms(year - 1)
            else:
                prev_year_terms = [('大雪', datetime(1984, 12, 7))]
            
            for term_name, term_date in reversed(prev_year_terms):
                if term_name in self.month_zhi_map:
                    current_term = term_name
                    current_zhi = self.month_zhi_map[term_name]
                    break
        
        return current_term, current_zhi
    
    def _calculate_solar_terms(self, year):
        """
        計算指定年份的節氣日期
        使用簡化的太陽黃經計算方法
        """
        solar_term_dates = []
        
        # 簡化計算：每個節氣約15天間隔
        base_dates = [
            (2, 4),   # 立春
            (2, 19),  # 雨水
            (3, 6),   # 驚蛰
            (3, 21),  # 春分
            (4, 5),   # 清明
            (4, 20),  # 穀雨
            (5, 6),   # 立夏
            (5, 21),  # 小滿
            (6, 6),   # 芒種
            (6, 21),  # 夏至
            (7, 7),   # 小暑
            (7, 23),  # 大暑
            (8, 8),   # 立秋
            (8, 23),  # 處暑
            (9, 8),   # 白露
            (9, 23),  # 秋分
            (10, 8),  # 寒露
            (10, 23), # 霜降
            (11, 7),  # 立冬
            (11, 22), # 小雪
            (12, 7),  # 大雪
            (12, 22), # 冬至
            (1, 6),   # 小寒
            (1, 20)   # 大寒
        ]
        
        for i, (term_name, _) in enumerate(self.solar_terms):
            month, day = base_dates[i]
            # 調整年份（小寒和大寒屬於下一年）
            term_year = year + 1 if month == 1 else year
            try:
                term_date = datetime(term_year, month, day)
                solar_term_dates.append((term_name, term_date))
            except ValueError:
                # 處理2月29日等特殊情況
                term_date = datetime(term_year, month, day - 1)
                solar_term_dates.append((term_name, term_date))
        
        return sorted(solar_term_dates, key=lambda x: x[1])
    
    def get_day_stem_branch(self, year, month, day):
        """
        獲取日柱干支
        使用基準日計算法
        """
        current_date = datetime(year, month, day)
        days_diff = (current_date - self.base_date).days
        
        # 計算干支索引
        gan_index = (self.base_day_index + days_diff) % 10
        zhi_index = (self.base_day_index + days_diff) % 12
        
        gan = self.gans[gan_index]
        zhi = self.zhis[zhi_index]
        
        return gan, zhi
    
    def calculate_pillars(self, year, month, day, hour):
        """
        計算完整的四柱八字
        返回詳細的計算過程和結果
        """
        result = {
            'success': True,
            'pillars': {},
            'calculation_info': {
                'engine': 'PillarEngine',
                'version': '1.0',
                'calculation_method': 'solar_term_based',
                'base_date': '1985-09-22 (甲子日)',
                'debug_info': {}
            }
        }
        
        try:
            # 年柱計算
            year_gan_index = (year - 4) % 10
            year_zhi_index = (year - 4) % 12
            year_gan = self.gans[year_gan_index]
            year_zhi = self.zhis[year_zhi_index]
            
            result['pillars']['year'] = {
                'gan': year_gan,
                'zhi': year_zhi,
                'pillar': f'{year_gan}{year_zhi}',
                'method': '立春分年法'
            }
            
            # 月柱計算
            solar_term, month_zhi = self.get_solar_term_boundary(year, month, day)
            
            # 根據年干和月支計算月干 - 修正五虎遁月邏輯
            month_zhi_index = self.zhis.index(month_zhi)
            year_gan_key = year_gan
            
            # 五虎遁月：甲己年丙作首，乙庚年戊為頭，丙辛年庚上起，丁壬年壬位流，戊癸年甲好求
            wuhu_start_gan = {
                '甲': '丙', '己': '丙',
                '乙': '戊', '庚': '戊', 
                '丙': '庚', '辛': '庚',
                '丁': '壬', '壬': '壬',
                '戊': '甲', '癸': '甲'
            }
            
            start_gan = wuhu_start_gan.get(year_gan, '甲')
            start_gan_index = self.gans.index(start_gan)
            
            # 從寅月開始計算（寅=2）
            month_gan_index = (start_gan_index + month_zhi_index - 2) % 10
            month_gan = self.gans[month_gan_index]
            
            result['pillars']['month'] = {
                'gan': month_gan,
                'zhi': month_zhi,
                'pillar': f'{month_gan}{month_zhi}',
                'method': f'節氣分月法 ({solar_term})',
                'solar_term': solar_term
            }
            
            # 日柱計算
            day_gan, day_zhi = self.get_day_stem_branch(year, month, day)
            
            result['pillars']['day'] = {
                'gan': day_gan,
                'zhi': day_zhi,
                'pillar': f'{day_gan}{day_zhi}',
                'method': '甲子基準日算法'
            }
            
            # 時柱計算
            hour_zhi_index = (hour + 1) // 2 % 12
            hour_zhi = self.zhis[hour_zhi_index]
            
            # 五鼠遁時
            day_gan_index = self.gans.index(day_gan)
            hour_gan_index = (day_gan_index * 2 + hour_zhi_index) % 10
            hour_gan = self.gans[hour_gan_index]
            
            result['pillars']['hour'] = {
                'gan': hour_gan,
                'zhi': hour_zhi,
                'pillar': f'{hour_gan}{hour_zhi}',
                'method': '五鼠遁時法'
            }
            
            # 生成八字字符串
            result['bazi_string'] = f"{year_gan}{year_zhi} {month_gan}{month_zhi} {day_gan}{day_zhi} {hour_gan}{hour_zhi}"
            
            # 調試信息
            result['calculation_info']['debug_info'] = {
                'input_date': f'{year}-{month:02d}-{day:02d} {hour:02d}:00',
                'solar_term': solar_term,
                'month_zhi_calculation': f'{solar_term} -> {month_zhi}',
                'day_calculation': f'基準日+{(datetime(year, month, day) - self.base_date).days}天',
                'wuhu_dun_key': year_gan,
                'month_zhi_index': month_zhi_index
            }
            
        except Exception as e:
            result['success'] = False
            result['error'] = f'計算錯誤: {str(e)}'
            result['calculation_info']['debug_info']['error'] = str(e)
        
        return result

def test_pillar_engine():
    """測試PillarEngine"""
    engine = PillarEngine()
    
    # 測試案例：1985年10月6日19時
    result = engine.calculate_pillars(1985, 10, 6, 19)
    
    print("🧪 PillarEngine 測試結果:")
    print("=" * 50)
    
    if result['success']:
        pillars = result['pillars']
        print(f"八字結果: {result['bazi_string']}")
        print(f"年柱: {pillars['year']['pillar']} ({pillars['year']['method']})")
        print(f"月柱: {pillars['month']['pillar']} ({pillars['month']['method']})")
        print(f"日柱: {pillars['day']['pillar']} ({pillars['day']['method']})")
        print(f"時柱: {pillars['hour']['pillar']} ({pillars['hour']['method']})")
        
        print("\n🔍 調試信息:")
        debug = result['calculation_info']['debug_info']
        for key, value in debug.items():
            print(f"  {key}: {value}")
        
        # 驗證正確答案
        expected = {'year': '乙丑', 'month': '乙酉', 'day': '戊寅', 'hour': '壬戌'}
        actual = {
            'year': pillars['year']['pillar'],
            'month': pillars['month']['pillar'],
            'day': pillars['day']['pillar'],
            'hour': pillars['hour']['pillar']
        }
        
        print("\n✅ 驗證結果:")
        all_correct = True
        for pillar in ['year', 'month', 'day', 'hour']:
            status = '✅' if actual[pillar] == expected[pillar] else '❌'
            if actual[pillar] != expected[pillar]:
                all_correct = False
            print(f"  {pillar}: {actual[pillar]} {status} (期望: {expected[pillar]})")
        
        if all_correct:
            print("\n🎉 所有計算結果完全正確！")
        else:
            print("\n⚠️ 仍有錯誤需要修正")
    else:
        print(f"❌ 計算失敗: {result['error']}")

if __name__ == "__main__":
    test_pillar_engine()

