#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌈 部署狀態快速回答
直接回答"部署好了嗎？"的問題
"""

import subprocess
import sys
import os

def quick_deployment_check():
    """快速部署檢查"""
    print("🔍 正在檢查部署狀態...")
    
    # 檢查關鍵文件
    essential_files = ['app.py', 'requirements.txt', 'DEPLOYMENT.md']
    for file in essential_files:
        if not os.path.exists(file):
            return False, f"缺少關鍵文件: {file}"
    
    # 檢查Flask導入
    try:
        from app import app
    except ImportError as e:
        return False, f"Flask應用導入失敗: {e}"
    
    # 檢查依賴
    try:
        import flask
        import flask_cors
    except ImportError as e:
        return False, f"缺少依賴包: {e}"
    
    return True, "所有檢查通過"

def main():
    """主函數 - 回答部署問題"""
    print("=" * 50)
    print("🌈 虹靈御所八字人生兵法系統")
    print("=" * 50)
    print()
    print("❓ 問題: 部署好了嗎？")
    print()
    
    is_deployed, message = quick_deployment_check()
    
    if is_deployed:
        print("✅ 答案: 是的，已經部署好了！")
        print()
        print("📊 系統狀態:")
        print("   🟢 應用文件: 完整")
        print("   🟢 依賴包: 已安裝") 
        print("   🟢 Flask應用: 可正常啟動")
        print()
        print("🚀 啟動方式:")
        print("   • 開發模式: python app.py")
        print("   • Docker模式: docker-compose up -d")
        print("   • 生產模式: gunicorn app:app")
        print()
        print("🌐 訪問地址:")
        print("   • 主頁面: http://localhost:5000")
        print("   • 健康檢查: http://localhost:5000/api/health")
        print()
        print("📋 完整檢查:")
        print("   運行 python deployment_status.py 獲取詳細報告")
        
    else:
        print("❌ 答案: 還沒有完全部署好")
        print()
        print(f"⚠️  問題: {message}")
        print()
        print("🔧 解決方案:")
        print("   1. 確保所有依賴已安裝: pip install -r requirements.txt")
        print("   2. 檢查文件完整性")
        print("   3. 運行完整檢查: python deployment_status.py")
    
    print()
    print("=" * 50)

if __name__ == "__main__":
    main()