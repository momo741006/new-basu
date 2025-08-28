#!/usr/bin/env python3
"""
Enhanced Smoke Tests - 驗證完整的八字系統功能
包括API路徑、完整響應結構、前後端整合
"""

import sys
import os
import json
import requests
import time
from threading import Thread

# 添加pillar-engine模組路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'pillar-engine'))

def test_engine_import():
    """測試引擎導入"""
    try:
        from pillar_engine import PillarEngine
        print("✅ PillarEngine導入成功")
        return True
    except ImportError as e:
        print(f"❌ PillarEngine導入失敗: {e}")
        return False

def test_authority_calculator():
    """測試AuthorityBaziCalculator"""
    try:
        from app import AuthorityBaziCalculator
        calculator = AuthorityBaziCalculator()
        
        # 測試完整計算
        result = calculator.calculate_bazi("測試", 1985, 10, 6, 19)
        
        if result['success']:
            # 檢查完整響應結構
            required_keys = ['pillars', 'nayins', 'ten_gods', 'day_master', 'wuxing_stats', 'shens', 'legions']
            missing_keys = [key for key in required_keys if key not in result]
            
            if not missing_keys:
                print("✅ AuthorityBaziCalculator完整功能測試通過")
                print(f"   - 四柱: {result['pillars']['year']['gan']}{result['pillars']['year']['zhi']} {result['pillars']['month']['gan']}{result['pillars']['month']['zhi']} {result['pillars']['day']['gan']}{result['pillars']['day']['zhi']} {result['pillars']['hour']['gan']}{result['pillars']['hour']['zhi']}")
                print(f"   - 十神: {result['ten_gods']}")
                print(f"   - 軍團數量: {len(result['legions'])}")
                return True
            else:
                print(f"❌ 響應結構不完整，缺少: {missing_keys}")
                return False
        else:
            print(f"❌ 計算失敗: {result.get('error')}")
            return False
            
    except Exception as e:
        print(f"❌ AuthorityBaziCalculator測試異常: {e}")
        return False

def start_flask_server():
    """啟動Flask服務器"""
    try:
        from app import app
        app.run(host='127.0.0.1', port=5002, debug=False, use_reloader=False)
    except Exception as e:
        print(f"Flask服務器啟動失敗: {e}")

def test_api_endpoints():
    """測試API端點"""
    # 啟動Flask服務器
    server_thread = Thread(target=start_flask_server, daemon=True)
    server_thread.start()
    
    # 等待服務器啟動
    time.sleep(3)
    
    try:
        base_url = "http://127.0.0.1:5002"
        
        # 測試健康檢查
        health_response = requests.get(f"{base_url}/api/health", timeout=5)
        if health_response.status_code == 200:
            print("✅ 健康檢查API正常")
        else:
            print(f"❌ 健康檢查失敗: {health_response.status_code}")
            return False
        
        # 測試兩種API路徑
        test_data = {
            "name": "測試用戶",
            "year": 1985,
            "month": 10,
            "day": 6,
            "hour": 19
        }
        
        # 測試中橫線路徑
        response1 = requests.post(f"{base_url}/api/calculate-bazi", 
                                json=test_data, timeout=10)
        
        # 測試底線路徑
        response2 = requests.post(f"{base_url}/api/calculate_bazi", 
                                json=test_data, timeout=10)
        
        if response1.status_code == 200 and response2.status_code == 200:
            result1 = response1.json()
            result2 = response2.json()
            
            if result1['success'] and result2['success']:
                print("✅ 兩種API路徑都正常工作")
                print(f"   - 中橫線路徑: {result1['pillars']['day']['gan']}{result1['pillars']['day']['zhi']}")
                print(f"   - 底線路徑: {result2['pillars']['day']['gan']}{result2['pillars']['day']['zhi']}")
                
                # 檢查完整響應結構
                required_keys = ['pillars', 'nayins', 'ten_gods', 'day_master', 'wuxing_stats', 'legions']
                if all(key in result1 for key in required_keys):
                    print("✅ API響應結構完整")
                    return True
                else:
                    print("❌ API響應結構不完整")
                    return False
            else:
                print("❌ API計算失敗")
                return False
        else:
            print(f"❌ API請求失敗: {response1.status_code}, {response2.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ API測試異常: {e}")
        return False

def test_flask_integration():
    """測試Flask整合"""
    try:
        from app import app, authority_calculator
        
        if app and authority_calculator:
            print("✅ Flask整合測試通過")
            return True
        else:
            print("❌ Flask整合失敗")
            return False
            
    except Exception as e:
        print(f"❌ Flask整合測試異常: {e}")
        return False

def run_enhanced_tests():
    """運行增強版smoke tests"""
    print("🧪 開始運行Enhanced Smoke Tests...")
    print("=" * 60)
    
    tests = [
        ("PillarEngine導入", test_engine_import),
        ("AuthorityBaziCalculator功能", test_authority_calculator),
        ("Flask整合", test_flask_integration),
        ("API端點測試", test_api_endpoints)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 測試: {test_name}")
        if test_func():
            passed += 1
        else:
            print(f"💥 {test_name} 測試失敗")
    
    print("\n" + "=" * 60)
    print(f"📊 測試結果: {passed}/{total} 通過")
    
    if passed == total:
        print("🎉 所有Enhanced Smoke Tests通過！系統完美運行")
        return True
    else:
        print("⚠️ 有測試失敗，請檢查系統配置")
        return False

if __name__ == "__main__":
    success = run_enhanced_tests()
    sys.exit(0 if success else 1)
