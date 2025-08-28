#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌈 虹靈御所八字人生兵法系統 - 部署狀態檢查器
檢查系統部署狀態並提供詳細報告
"""

import os
import sys
import json
import time
import subprocess
import requests
from datetime import datetime
from threading import Thread

def print_banner():
    """顯示橫幅"""
    print("=" * 60)
    print("🌈 虹靈御所八字人生兵法系統 - 部署狀態檢查")
    print("=" * 60)
    print()

def check_python_environment():
    """檢查Python環境"""
    print("🐍 檢查Python環境...")
    
    # 檢查Python版本
    version = sys.version_info
    print(f"   Python版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("   ✅ Python版本符合要求 (3.7+)")
        return True
    else:
        print("   ❌ Python版本不符合要求，需要3.7+")
        return False

def check_dependencies():
    """檢查依賴包"""
    print("📦 檢查依賴包...")
    
    required_packages = ['flask', 'flask_cors', 'gunicorn']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} 未安裝")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"   缺少依賴: {', '.join(missing_packages)}")
        return False
    
    print("   ✅ 所有依賴包已安裝")
    return True

def check_application_files():
    """檢查應用文件"""
    print("📁 檢查應用文件...")
    
    required_files = [
        'app.py',
        'pillar_engine.py', 
        'requirements.txt',
        'Dockerfile',
        'docker-compose.yml',
        'DEPLOYMENT.md'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file}")
        else:
            print(f"   ❌ {file} 不存在")
            missing_files.append(file)
    
    if missing_files:
        print(f"   缺少文件: {', '.join(missing_files)}")
        return False
    
    print("   ✅ 所有必要文件存在")
    return True

def check_flask_import():
    """檢查Flask應用導入"""
    print("🚀 檢查Flask應用...")
    
    try:
        from app import app, authority_calculator
        print("   ✅ Flask應用導入成功")
        print("   ✅ 八字計算器初始化成功")
        return True
    except Exception as e:
        print(f"   ❌ Flask應用導入失敗: {e}")
        return False

def start_test_server():
    """啟動測試服務器"""
    try:
        from app import app
        app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False)
    except Exception as e:
        print(f"測試服務器啟動失敗: {e}")

def check_api_endpoints():
    """檢查API端點"""
    print("🌐 檢查API端點...")
    
    # 啟動測試服務器
    server_thread = Thread(target=start_test_server, daemon=True)
    server_thread.start()
    
    # 等待服務器啟動
    time.sleep(3)
    
    try:
        base_url = "http://127.0.0.1:5001"
        
        # 測試健康檢查
        try:
            health_response = requests.get(f"{base_url}/api/health", timeout=5)
            if health_response.status_code == 200:
                health_data = health_response.json()
                print(f"   ✅ 健康檢查API: {health_data.get('message', '正常')}")
            else:
                print(f"   ❌ 健康檢查失敗: HTTP {health_response.status_code}")
                return False
        except Exception as e:
            print(f"   ❌ 健康檢查連接失敗: {e}")
            return False
        
        # 測試八字計算API
        try:
            test_data = {
                "name": "部署測試",
                "year": 1985,
                "month": 10,
                "day": 6,
                "hour": 19
            }
            
            calc_response = requests.post(f"{base_url}/api/calculate-bazi", 
                                        json=test_data, timeout=10)
            
            if calc_response.status_code == 200:
                calc_data = calc_response.json()
                if calc_data.get('pillars'):
                    day_pillar = calc_data['pillars']['day']
                    print(f"   ✅ 八字計算API: {day_pillar['gan']}{day_pillar['zhi']} (日柱)")
                else:
                    print(f"   ❌ 八字計算API: 響應格式異常")
                    return False
            else:
                print(f"   ❌ 八字計算API失敗: HTTP {calc_response.status_code}")
                return False
                
        except Exception as e:
            print(f"   ❌ 八字計算API連接失敗: {e}")
            return False
        
        print("   ✅ 所有API端點正常工作")
        return True
        
    except Exception as e:
        print(f"   ❌ API測試異常: {e}")
        return False

def check_docker_availability():
    """檢查Docker可用性"""
    print("🐳 檢查Docker環境...")
    
    try:
        result = subprocess.run(['docker', '--version'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print(f"   ✅ Docker可用: {version}")
            return True
        else:
            print("   ❌ Docker不可用")
            return False
    except FileNotFoundError:
        print("   ❌ Docker未安裝")
        return False

def check_deployment_documentation():
    """檢查部署文檔"""
    print("📚 檢查部署文檔...")
    
    if os.path.exists('DEPLOYMENT.md'):
        with open('DEPLOYMENT.md', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 檢查關鍵部署方法
        deployment_methods = ['Docker', 'Gunicorn', '本地開發']
        found_methods = []
        
        for method in deployment_methods:
            if method in content:
                found_methods.append(method)
                print(f"   ✅ {method}部署說明")
        
        if len(found_methods) >= 2:
            print("   ✅ 部署文檔完整")
            return True
        else:
            print("   ❌ 部署文檔不完整")
            return False
    else:
        print("   ❌ 部署文檔不存在")
        return False

def generate_deployment_report(results):
    """生成部署報告"""
    print()
    print("=" * 60)
    print("📊 部署狀態總結")
    print("=" * 60)
    
    total_checks = len(results)
    passed_checks = sum(1 for result in results.values() if result)
    
    print(f"✅ 通過檢查: {passed_checks}/{total_checks}")
    print(f"⏰ 檢查時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 詳細結果
    status_icons = {True: "✅", False: "❌"}
    for check_name, result in results.items():
        print(f"{status_icons[result]} {check_name}")
    
    print()
    print("=" * 60)
    
    # 最終判斷
    if passed_checks == total_checks:
        print("🎉 系統已完全部署並正常運行！")
        print("💡 您可以使用以下命令啟動系統:")
        print("   • 開發環境: python app.py")
        print("   • Docker: docker-compose up -d")
        print("   • 生產環境: gunicorn app:app")
        deployment_status = "已部署"
    elif passed_checks >= total_checks * 0.8:
        print("⚠️  系統基本部署完成，但有些小問題需要解決")
        deployment_status = "部分部署"
    else:
        print("❌ 系統尚未完全部署，需要解決關鍵問題")
        deployment_status = "未部署"
    
    print(f"📝 部署狀態: {deployment_status}")
    print("=" * 60)
    
    return deployment_status

def main():
    """主函數"""
    print_banner()
    
    # 執行各項檢查
    results = {}
    
    results["Python環境"] = check_python_environment()
    print()
    
    results["依賴包"] = check_dependencies() 
    print()
    
    results["應用文件"] = check_application_files()
    print()
    
    results["Flask應用"] = check_flask_import()
    print()
    
    results["API端點"] = check_api_endpoints()
    print()
    
    results["Docker環境"] = check_docker_availability()
    print()
    
    results["部署文檔"] = check_deployment_documentation()
    print()
    
    # 生成最終報告
    deployment_status = generate_deployment_report(results)
    
    # 返回部署狀態
    return deployment_status, results

if __name__ == "__main__":
    try:
        status, results = main()
        
        # 根據結果設置退出碼
        if status == "已部署":
            sys.exit(0)
        elif status == "部分部署":
            sys.exit(1)
        else:
            sys.exit(2)
            
    except KeyboardInterrupt:
        print("\n⏹️  部署檢查已取消")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ 部署檢查過程中發生錯誤: {e}")
        sys.exit(3)