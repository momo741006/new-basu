#!/usr/bin/env python3
"""
PillarEngine測試腳本
"""

from pillar_engine import PillarEngine

def test_multiple_cases():
    """測試多個案例"""
    engine = PillarEngine()
    
    test_cases = [
        {
            'date': (1985, 10, 6, 19),
            'expected': '乙丑 乙酉 戊寅 壬戌',
            'description': '1985年10月6日戌時'
        },
        {
            'date': (2000, 1, 1, 12),
            'expected': None,  # 不指定期望值，只測試運行
            'description': '2000年1月1日午時'
        },
        {
            'date': (1990, 5, 15, 8),
            'expected': None,
            'description': '1990年5月15日辰時'
        }
    ]
    
    print("🧪 PillarEngine多案例測試")
    print("=" * 50)
    
    for i, case in enumerate(test_cases, 1):
        year, month, day, hour = case['date']
        result = engine.calculate_pillars(year, month, day, hour)
        
        print(f"\n測試案例 {i}: {case['description']}")
        
        if result['success']:
            print(f"✅ 計算成功: {result['bazi_string']}")
            
            if case['expected']:
                if result['bazi_string'] == case['expected']:
                    print(f"✅ 結果正確: 符合期望值")
                else:
                    print(f"❌ 結果錯誤: 期望 {case['expected']}")
        else:
            print(f"❌ 計算失敗: {result.get('error', '未知錯誤')}")

if __name__ == "__main__":
    test_multiple_cases()
