#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
虹靈御所八字人生兵法系統 - Flask部署版本
整合前端界面和後端API的完整應用
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os
import sys
import json
import math

# 載入環境變數
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # 如果沒有安裝 python-dotenv，跳過環境變數載入
    pass

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# 配置設定
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('DEBUG', 'False').lower() == 'true'

# 權威八字計算引擎類 (基於AuthorityBaziCalculator)
class AuthorityBaziCalculator:
    def __init__(self):
        self.gans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
        self.zhis = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
        
        # 六十甲子順序表
        self.sixtyJiazi = [
            "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
            "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
            "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
            "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
            "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
            "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"
        ]
        
        # 五鼠遁時表
        self.wushuDun = {
            "甲": "甲", "己": "甲",
            "乙": "丙", "庚": "丙",
            "丙": "戊", "辛": "戊",
            "丁": "庚", "壬": "庚",
            "戊": "壬", "癸": "壬"
        }
        
        # 五虎遁月表
        self.wuhuDun = {
            "甲": "丙", "己": "丙",
            "乙": "戊", "庚": "戊",
            "丙": "庚", "辛": "庚",
            "丁": "壬", "壬": "壬",
            "戊": "甲", "癸": "甲"
        }
        
        # 修正的時辰對應表
        self.hourZhiMap = {
            23: "子", 0: "子",
            1: "丑", 2: "丑",
            3: "寅", 4: "寅",
            5: "卯", 6: "卯",
            7: "辰", 8: "辰",
            9: "巳", 10: "巳",
            11: "午", 12: "午",
            13: "未", 14: "未",
            15: "申", 16: "申",
            17: "酉", 18: "酉",
            19: "戌", 20: "戌",
            21: "亥", 22: "亥"
        }
        
        # 納音五行對照表
        self.nayinTable = {
            "甲子": "海中金", "乙丑": "海中金", "丙寅": "爐中火", "丁卯": "爐中火",
            "戊辰": "大林木", "己巳": "大林木", "庚午": "路旁土", "辛未": "路旁土",
            "壬申": "劍鋒金", "癸酉": "劍鋒金", "甲戌": "山頭火", "乙亥": "山頭火",
            "丙子": "澗下水", "丁丑": "澗下水", "戊寅": "城牆土", "己卯": "城牆土",
            "庚辰": "白鑞金", "辛巳": "白鑞金", "壬午": "楊柳木", "癸未": "楊柳木",
            "甲申": "泉中水", "乙酉": "泉中水", "丙戌": "屋上土", "丁亥": "屋上土",
            "戊子": "霹靂火", "己丑": "霹靂火", "庚寅": "松柏木", "辛卯": "松柏木",
            "壬辰": "長流水", "癸巳": "長流水", "甲午": "沙中金", "乙未": "沙中金",
            "丙申": "山下火", "丁酉": "山下火", "戊戌": "平地木", "己亥": "平地木",
            "庚子": "壁上土", "辛丑": "壁上土", "壬寅": "金箔金", "癸卯": "金箔金",
            "甲辰": "覆燈火", "乙巳": "覆燈火", "丙午": "天河水", "丁未": "天河水",
            "戊申": "大驛土", "己酉": "大驛土", "庚戌": "釵釧金", "辛亥": "釵釧金",
            "壬子": "桑柘木", "癸丑": "桑柘木", "甲寅": "大溪水", "乙卯": "大溪水",
            "丙辰": "沙中土", "丁巳": "沙中土", "戊午": "天上火", "己未": "天上火",
            "庚申": "石榴木", "辛酉": "石榴木", "壬戌": "大海水", "癸亥": "大海水"
        }
        
        # 十神關係表（以日干為主）
        self.ten_gods_table = {
            '甲': {'甲': '比肩', '乙': '劫財', '丙': '食神', '丁': '傷官', '戊': '偏財', '己': '正財', '庚': '七殺', '辛': '正官', '壬': '偏印', '癸': '正印'},
            '乙': {'甲': '劫財', '乙': '比肩', '丙': '傷官', '丁': '食神', '戊': '正財', '己': '偏財', '庚': '正官', '辛': '七殺', '壬': '正印', '癸': '偏印'},
            '丙': {'甲': '偏印', '乙': '正印', '丙': '比肩', '丁': '劫財', '戊': '食神', '己': '傷官', '庚': '偏財', '辛': '正財', '壬': '七殺', '癸': '正官'},
            '丁': {'甲': '正印', '乙': '偏印', '丙': '劫財', '丁': '比肩', '戊': '傷官', '己': '食神', '庚': '正財', '辛': '偏財', '壬': '正官', '癸': '七殺'},
            '戊': {'甲': '七殺', '乙': '正官', '丙': '偏印', '丁': '正印', '戊': '比肩', '己': '劫財', '庚': '食神', '辛': '傷官', '壬': '偏財', '癸': '正財'},
            '己': {'甲': '正官', '乙': '七殺', '丙': '正印', '丁': '偏印', '戊': '劫財', '己': '比肩', '庚': '傷官', '辛': '食神', '壬': '正財', '癸': '偏財'},
            '庚': {'甲': '偏財', '乙': '正財', '丙': '七殺', '丁': '正官', '戊': '偏印', '己': '正印', '庚': '比肩', '辛': '劫財', '壬': '食神', '癸': '傷官'},
            '辛': {'甲': '正財', '乙': '偏財', '丙': '正官', '丁': '七殺', '戊': '正印', '己': '偏印', '庚': '劫財', '辛': '比肩', '壬': '傷官', '癸': '食神'},
            '壬': {'甲': '食神', '乙': '傷官', '丙': '偏財', '丁': '正財', '戊': '七殺', '己': '正官', '庚': '偏印', '辛': '正印', '壬': '比肩', '癸': '劫財'},
            '癸': {'甲': '傷官', '乙': '食神', '丙': '正財', '丁': '偏財', '戊': '正官', '己': '七殺', '庚': '正印', '辛': '偏印', '壬': '劫財', '癸': '比肩'}
        }
        
        # 五行屬性
        self.wuxing_map = {
            '甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土',
            '己': '土', '庚': '金', '辛': '金', '壬': '水', '癸': '水',
            '子': '水', '丑': '土', '寅': '木', '卯': '木', '辰': '土',
            '巳': '火', '午': '火', '未': '土', '申': '金', '酉': '金',
            '戌': '土', '亥': '水'
        }

    def isLeapYear(self, year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def getDaysInMonth(self, year, month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and self.isLeapYear(year):
            return 29
        return days[month - 1]

    def isValidDate(self, year, month, day):
        if year < 1900 or year > 2100:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1 or day > self.getDaysInMonth(year, month):
            return False
        return True

    def getDayOfYear(self, year, month, day):
        daysInMonth = [31, self.isLeapYear(year) and 29 or 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dayOfYear = day
        for i in range(month - 1):
            dayOfYear += daysInMonth[i]
        return dayOfYear

    def calculateSolarTerms(self, year):
        isLeap = self.isLeapYear(year)
        
        baseTerms = {
            '立春': {'month': 2, 'day': 4},
            '驚蟄': {'month': 3, 'day': 6},
            '清明': {'month': 4, 'day': 5},
            '立夏': {'month': 5, 'day': 6},
            '芒種': {'month': 6, 'day': 6},
            '小暑': {'month': 7, 'day': 7},
            '立秋': {'month': 8, 'day': 8},
            '白露': {'month': 9, 'day': 8},
            '寒露': {'month': 10, 'day': 9},
            '立冬': {'month': 11, 'day': 8},
            '大雪': {'month': 12, 'day': 7},
            '小寒': {'month': 1, 'day': 6}
        }
        
        terms = {}
        for termName in baseTerms:
            day = baseTerms[termName]['day']
            
            if termName in ['立春', '小寒']:
                if isLeap:
                    day += 1
            elif isLeap:
                day -= 1
            
            yearsSince1950 = year - 1950
            trendAdjustment = round((yearsSince1950 / 100) * 0.7)
            day += trendAdjustment
            
            monthNum = baseTerms[termName]['month']
            day = max(1, min(day, self.getDaysInMonth(year, monthNum)))
            
            terms[termName] = {'month': monthNum, 'day': day}
        
        return terms

    def calculateYearPillar(self, year, month, day):
        solarTerms = self.calculateSolarTerms(year)
        lichun = solarTerms['立春']
        
        actualYear = year
        if month < lichun['month'] or (month == lichun['month'] and day < lichun['day']):
            actualYear = year - 1
        
        sequence = (actualYear - 1984 + 1) % 60
        if sequence <= 0:
            sequence += 60
        
        pillar = self.sixtyJiazi[sequence - 1]
        
        return {
            'gan': pillar[0],
            'zhi': pillar[1],
            'pillar': pillar,
            'nayin': self.nayinTable.get(pillar, "未知"),
            'actual_year': actualYear,
            'lichun_info': lichun,
            'method': "修正公式"
        }

    def calculateMonthPillar(self, year, month, day, yearPillar):
        # 使用正確的節氣與月支對應表
        solarTermToZhi = {
            '小寒': '丑',  # 小寒後為丑月（十二月）
            '立春': '寅',  # 立春後為寅月（正月）
            '驚蟄': '卯',  # 驚蟄後為卯月（二月）
            '清明': '辰',  # 清明後為辰月（三月）
            '立夏': '巳',  # 立夏後為巳月（四月）
            '芒種': '午',  # 芒種後為午月（五月）
            '小暑': '未',  # 小暑後為未月（六月）
            '立秋': '申',  # 立秋後為申月（七月）
            '白露': '酉',  # 白露後為酉月（八月）
            '寒露': '戌',  # 寒露後為戌月（九月）
            '立冬': '亥',  # 立冬後為亥月（十月）
            '大雪': '子'   # 大雪後為子月（十一月）
        }
        
        solarTerms = self.calculateSolarTerms(year)
        
        # 根據月份確定當月節氣
        monthTermMap = {
            1: '小寒', 2: '立春', 3: '驚蟄', 4: '清明',
            5: '立夏', 6: '芒種', 7: '小暑', 8: '立秋',
            9: '白露', 10: '寒露', 11: '立冬', 12: '大雪'
        }
        
        currentTerm = monthTermMap[month]
        termDay = solarTerms[currentTerm]['day']
        
        # 判斷是否已過當月節氣
        if day >= termDay:
            # 已過節氣，使用當月節氣對應的月支
            monthZhi = solarTermToZhi[currentTerm]
        else:
            # 未過節氣，使用上月節氣對應的月支
            prevMonth = month - 1 if month > 1 else 12
            prevTerm = monthTermMap[prevMonth]
            monthZhi = solarTermToZhi[prevTerm]
        
        # 五虎遁月
        yearGan = yearPillar['gan']
        monthGanBase = self.wuhuDun[yearGan]
        monthGanBaseIndex = self.gans.index(monthGanBase)
        monthZhiIndex = self.zhis.index(monthZhi)
        # 修正：從寅月(索引2)開始計算月序
        monthOrder = (monthZhiIndex - 2) % 12
        monthGanIndex = (monthGanBaseIndex + monthOrder) % 10
        monthGan = self.gans[monthGanIndex]

        pillar = monthGan + monthZhi

        return {
            'gan': monthGan,
            'zhi': monthZhi,
            'pillar': pillar,
            'nayin': self.nayinTable.get(pillar, "未知"),
            'term_info': {'term': currentTerm, 'day': termDay, 'is_after': day >= termDay},
            'method': "節氣分月+五虎遁月"
        }

    def calculateDayPillar(self, year, month, day):
        # 使用正確的甲子日基準：1985年9月22日
        baseDate = datetime(1985, 9, 22)  # 1985年9月22日是甲子日
        targetDate = datetime(year, month, day)
        
        daysDiff = (targetDate - baseDate).days
        
        # 計算干支索引
        ganIndex = daysDiff % 10
        zhiIndex = daysDiff % 12
        
        # 處理負數索引
        if ganIndex < 0:
            ganIndex += 10
        if zhiIndex < 0:
            zhiIndex += 12
            
        dayGan = self.gans[ganIndex]
        dayZhi = self.zhis[zhiIndex]
        pillar = dayGan + dayZhi

        return {
            'gan': dayGan,
            'zhi': dayZhi,
            'pillar': pillar,
            'nayin': self.nayinTable.get(pillar, "未知"),
            'method': "甲子基準日算法",
            'base_date': "1985-09-22",
            'days_diff': daysDiff
        }

    def calculateHourPillar(self, year, month, day, hour, dayPillar):
        hourZhi = self.hourZhiMap.get(hour)
        if not hourZhi:
            raise ValueError(f"無效的時辰: {hour}時")
        
        dayGan = dayPillar['gan']
        hourGanBase = self.wushuDun[dayGan]
        
        hourGanBaseIndex = self.gans.index(hourGanBase)
        hourZhiIndex = self.zhis.index(hourZhi)
        hourGanIndex = (hourGanBaseIndex + hourZhiIndex) % 10
        hourGan = self.gans[hourGanIndex]
        
        pillar = hourGan + hourZhi
        
        return {
            'gan': hourGan,
            'zhi': hourZhi,
            'pillar': pillar,
            'nayin': self.nayinTable.get(pillar, "未知"),
            'wushu_info': {'dayGan': dayGan, 'base': hourGanBase, 'formula': "五鼠遁時法"}
        }

    def get_nayin(self, gan, zhi):
        """獲取納音"""
        pillar = gan + zhi
        return self.nayinTable.get(pillar, '未知')

    def get_ten_god(self, day_gan, target_gan):
        """獲取十神"""
        return self.ten_gods_table[day_gan][target_gan]

    def calculate_wuxing_stats(self, pillars):
        """計算五行統計"""
        wuxing_count = {'金': 0, '木': 0, '水': 0, '火': 0, '土': 0}
        
        for pillar_name, pillar in pillars.items():
            gan_wuxing = self.wuxing_map[pillar['gan']]
            zhi_wuxing = self.wuxing_map[pillar['zhi']]
            wuxing_count[gan_wuxing] += 1.2
            wuxing_count[zhi_wuxing] += 0.8
        
        return wuxing_count

    def find_shens(self, pillars):
        """查找神煞"""
        return []  # 簡化版本

    def generate_legions(self, pillars, nayins, ten_gods):
        """生成四時軍團"""
        legions = [
            {
                'name': '家族兵團',
                'commander': f"{pillars['year']['gan']}({ten_gods[0]})",
                'strategist': pillars['year']['zhi'],
                'deputy': nayins['year']
            },
            {
                'name': '成長兵團',
                'commander': f"{pillars['month']['gan']}({ten_gods[1]})",
                'strategist': pillars['month']['zhi'],
                'deputy': nayins['month']
            },
            {
                'name': '本我兵團',
                'commander': f"{pillars['day']['gan']}(日主)",
                'strategist': pillars['day']['zhi'],
                'deputy': nayins['day']
            },
            {
                'name': '未來兵團',
                'commander': f"{pillars['hour']['gan']}({ten_gods[3]})",
                'strategist': pillars['hour']['zhi'],
                'deputy': nayins['hour']
            }
        ]
        return legions

    def calculate_bazi(self, name, year, month, day, hour):
        """計算八字主函數"""
        try:
            if not self.isValidDate(year, month, day):
                raise ValueError(f"無效的日期: {year}年{month}月{day}日")
            
            if hour < 0 or hour > 23:
                raise ValueError(f"無效的時辰: {hour}時")
            
            # 使用AuthorityBaziCalculator的精確計算方法
            yearPillar = self.calculateYearPillar(year, month, day)
            monthPillar = self.calculateMonthPillar(year, month, day, yearPillar)
            dayPillar = self.calculateDayPillar(year, month, day)
            hourPillar = self.calculateHourPillar(year, month, day, hour, dayPillar)
            
            pillars = {
                'year': {'gan': yearPillar['gan'], 'zhi': yearPillar['zhi']},
                'month': {'gan': monthPillar['gan'], 'zhi': monthPillar['zhi']},
                'day': {'gan': dayPillar['gan'], 'zhi': dayPillar['zhi']},
                'hour': {'gan': hourPillar['gan'], 'zhi': hourPillar['zhi']}
            }
            
            # 計算納音
            nayins = {
                'year': self.get_nayin(yearPillar['gan'], yearPillar['zhi']),
                'month': self.get_nayin(monthPillar['gan'], monthPillar['zhi']),
                'day': self.get_nayin(dayPillar['gan'], dayPillar['zhi']),
                'hour': self.get_nayin(hourPillar['gan'], hourPillar['zhi'])
            }
            
            # 計算十神
            day_gan = dayPillar['gan']
            ten_gods = [
                self.get_ten_god(day_gan, yearPillar['gan']),
                self.get_ten_god(day_gan, monthPillar['gan']),
                '日主',
                self.get_ten_god(day_gan, hourPillar['gan'])
            ]
            
            # 計算五行統計
            wuxing_stats = self.calculate_wuxing_stats(pillars)
            
            # 查找神煞
            shens = self.find_shens(pillars)
            
            # 生成軍團
            legions = self.generate_legions(pillars, nayins, ten_gods)
            
            return {
                'success': True,
                'name': name,
                'pillars': pillars,
                'nayins': nayins,
                'ten_gods': ten_gods,
                'day_master': day_gan,
                'wuxing_stats': wuxing_stats,
                'shens': shens,
                'legions': legions
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'計算錯誤: {str(e)}'
            }

# 導入正確的計算引擎
from pillar_engine import PillarEngine

# 創建計算引擎實例
engine = PillarEngine()

# 初始化權威計算器
#
# 為了讓前端能夠獲取完整的命盤資訊（包括納音、十神、五行統計、神煞和四時軍團），
# 需要使用 AuthorityBaziCalculator 來進行計算。此前 API 只返回 PillarEngine
# 的簡易結果，無法滿足豐富數據需求。另外，前端調用的路徑使用了
# "calculate_bazi"（底線命名），而原後端只提供了 "calculate-bazi"（中
# 橫線命名），導致調用失敗。下面創建 AuthorityBaziCalculator 的實例，並
# 在 API 路由中使用它來完成完整計算，同時註冊兩個路由以兼容不同命名方式。
authority_calculator = AuthorityBaziCalculator()

@app.route('/')
def index():
    """首頁"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """健康檢查"""
    return jsonify({'status': 'ok', 'message': '虹靈御所八字系統運行正常'})

# 兼容下劃線和中橫線兩種命名的 API 路由
@app.route('/api/calculate-bazi', methods=['POST'])
@app.route('/api/calculate_bazi', methods=['POST'])
def calculate_bazi():
    """八字計算API

    接收用戶提交的出生信息並返回完整命理分析結果。
    該接口同時支持以中橫線（calculate-bazi）或下劃線
    （calculate_bazi）命名的路徑，避免前端調用時出現 404 錯誤。
    """
    try:
        data = request.get_json(force=True) if request.is_json else request.form
        name = data.get('name', '')
        # 將輸入轉換為整型，如果缺失則保持 None
        try:
            year = int(data.get('year'))
        except Exception:
            year = None
        try:
            month = int(data.get('month'))
        except Exception:
            month = None
        try:
            day = int(data.get('day'))
        except Exception:
            day = None
        try:
            hour = int(data.get('hour'))
        except Exception:
            hour = None

        # 檢查必填字段
        if not name or year is None or month is None or day is None or hour is None:
            return jsonify({'success': False, 'error': '請提供完整的出生信息'})

        # 使用 AuthorityBaziCalculator 提供完整的命理分析
        result = authority_calculator.calculate_bazi(name, year, month, day, hour)

        return jsonify(result)
    except Exception as e:
        # 捕獲所有異常並返回錯誤信息
        return jsonify({'success': False, 'error': f'服務器錯誤: {str(e)}'})

@app.route('/static/<path:filename>')
def static_files(filename):
    """靜態文件服務"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    print("🌈 虹靈御所八字人生兵法系統啟動中...")
    
    # 從環境變數獲取配置
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    print(f"📡 API服務地址: http://{host}:{port}")
    print(f"🎯 前端界面: http://{host}:{port}")
    print(f"🔧 調試模式: {'開啟' if debug else '關閉'}")
    
    app.run(host=host, port=port, debug=debug)

