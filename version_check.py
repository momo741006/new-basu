#!/usr/bin/env python3
"""
版本檢查腳本
確保pillar-engine版本相容性
"""

import sys
import os
import json

# 添加pillar-engine模組路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'pillar-engine'))

def check_engine_version():
    """檢查引擎版本"""
    try:
        from pillar_engine import PillarEngine
        engine = PillarEngine()
        
        # 獲取版本信息
        result = engine.calculate_pillars(1985, 10, 6, 19)
        if result['success']:
            calc_info = result.get('calculation_info', {})
            return {
                'engine': calc_info.get('engine', 'Unknown'),
                'version': calc_info.get('version', 'Unknown'),
                'method': calc_info.get('calculation_method', 'Unknown')
            }
        else:
            return None
            
    except Exception as e:
        print(f"❌ 版本檢查失敗: {e}")
        return None

def main():
    """主函數"""
    print("🔍 檢查PillarEngine版本相容性...")
    
    version_info = check_engine_version()
    
    if version_info:
        print("✅ 版本信息:")
        print(f"   引擎: {version_info['engine']}")
        print(f"   版本: {version_info['version']}")
        print(f"   方法: {version_info['method']}")
        
        # 保存版本信息
        with open('current_version.json', 'w', encoding='utf-8') as f:
            json.dump(version_info, f, ensure_ascii=False, indent=2)
        
        print("✅ 版本信息已保存到 current_version.json")
        return True
    else:
        print("❌ 無法獲取版本信息")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
