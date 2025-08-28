#!/usr/bin/env python3
"""
Smoke Tests - 最小化驗證測試
確保PillarEngine在系統中正常運行
"""

import sys
import os

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

def test_engine_basic_calculation():
    """測試基本計算功能"""
    try:
        from pillar_engine import PillarEngine
        engine = PillarEngine()
        
        # 測試標準案例
        result = engine.calculate_pillars(1985, 10, 6, 19)
        
        if result['success']:
            expected = '乙丑 乙酉 戊寅 壬戌'
            actual = result['bazi_string']
            
            if actual == expected:
                print(f"✅ 基本計算測試通過: {actual}")
                return True
            else:
                print(f"❌ 計算結果錯誤: 期望 {expected}, 實際 {actual}")
                return False
        else:
            print(f"❌ 計算失敗: {result.get('error')}")
            return False
            
    except Exception as e:
        print(f"❌ 計算測試異常: {e}")
        return False

def test_engine_version():
    """測試引擎版本"""
    try:
        from pillar_engine import PillarEngine
        engine = PillarEngine()
        
        # 檢查版本信息
        result = engine.calculate_pillars(1985, 10, 6, 19)
        if result['success']:
            calc_info = result.get('calculation_info', {})
            engine_name = calc_info.get('engine', 'Unknown')
            version = calc_info.get('version', 'Unknown')
            
            print(f"✅ 引擎版本檢查: {engine_name} v{version}")
            return True
        else:
            print("❌ 無法獲取版本信息")
            return False
            
    except Exception as e:
        print(f"❌ 版本檢查異常: {e}")
        return False

def test_flask_integration():
    """測試Flask整合"""
    try:
        from app import app, engine
        
        # 測試Flask應用創建
        if app and engine:
            print("✅ Flask整合測試通過")
            return True
        else:
            print("❌ Flask整合失敗")
            return False
            
    except Exception as e:
        print(f"❌ Flask整合測試異常: {e}")
        return False

def run_all_tests():
    """運行所有smoke tests"""
    print("🧪 開始運行Smoke Tests...")
    print("=" * 50)
    
    tests = [
        ("引擎導入", test_engine_import),
        ("基本計算", test_engine_basic_calculation),
        ("版本檢查", test_engine_version),
        ("Flask整合", test_flask_integration)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 測試: {test_name}")
        if test_func():
            passed += 1
        else:
            print(f"💥 {test_name} 測試失敗")
    
    print("\n" + "=" * 50)
    print(f"📊 測試結果: {passed}/{total} 通過")
    
    if passed == total:
        print("🎉 所有Smoke Tests通過！系統可以安全運行")
        return True
    else:
        print("⚠️ 有測試失敗，請檢查系統配置")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
