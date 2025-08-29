# 🌈 虹靈御所八字人生兵法系統 - GitHub Copilot Instructions

## 系統概述
這是一個中國傳統八字命理分析系統，使用Flask構建，提供精確的八字計算和命理分析功能。

### 核心技術棧
- **後端**: Python 3.7+, Flask 3.1.2, Gunicorn
- **前端**: HTML5, CSS3, JavaScript
- **部署**: Docker, Heroku, Railway, Render

## 關鍵文件
- `app.py` - 主Flask應用程序
- `pillar_engine.py` - 核心八字計算引擎  
- `smoke_tests.py` - 基礎煙霧測試
- `enhanced_smoke_tests.py` - 增強版測試
- `deployment_status.py` - 部署狀態檢查

## 開發環境設置
```bash
# 1. 克隆項目並設置環境
git clone https://github.com/momo741006/new-basu.git
cd new-basu
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python app.py
```

### 環境變量 (.env)
```env
SECRET_KEY=your-secret-key
DEBUG=True
```

## 測試工作流程

### 基礎測試
```bash
python smoke_tests.py          # 4個基礎功能測試
python enhanced_smoke_tests.py # 完整系統測試  
python test_engine.py         # 引擎計算測試
```

### 部署驗證
```bash
python answer_deployment.py   # 快速狀態檢查
python deployment_status.py   # 完整部署驗證
```

## API 端點

### 健康檢查
```
GET /api/health
Response: {"status": "ok", "message": "虹靈御所八字系統運行正常"}
```

### 八字計算（支持兩種路徑）
```
POST /api/calculate-bazi
POST /api/calculate_bazi

Request:
{
  "name": "姓名",
  "year": 1985,
  "month": 10, 
  "day": 6,
  "hour": 19
}

Response:
{
  "success": true,
  "bazi_string": "乙丑 乙酉 戊寅 壬戌",
  "pillars": {
    "year": {"gan": "乙", "zhi": "丑", "pillar": "乙丑"},
    "month": {"gan": "乙", "zhi": "酉", "pillar": "乙酉"},
    "day": {"gan": "戊", "zhi": "寅", "pillar": "戊寅"},
    "hour": {"gan": "壬", "zhi": "戌", "pillar": "壬戌"}
  },
  "wuxing_stats": {...},
  "shishen_analysis": {...}
}
```

## 部署程序

### Docker 部署（推薦）
```bash
docker-compose up -d        # 啟動服務
docker-compose ps          # 檢查狀態
docker-compose logs -f     # 查看日誌
```

### 生產環境
```bash
gunicorn -c gunicorn.conf.py app:app
# 或自定義: gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

### 雲平台部署
```bash
# Heroku
heroku create your-app-name
git push heroku main

# Railway/Render: 通過Git連接自動部署
```

## 驗證命令

### 本地測試
```bash
# 檢查服務健康
curl http://localhost:5000/api/health

# 測試八字計算
curl -X POST http://localhost:5000/api/calculate-bazi \
  -H "Content-Type: application/json" \
  -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'
```

### 生產環境測試  
```bash
curl https://your-domain.com/api/health
curl -X POST https://your-domain.com/api/calculate-bazi \
  -H "Content-Type: application/json" \
  -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'
```

## 故障排除

### 常見問題
1. **導入錯誤**: `pip install -r requirements.txt`
2. **端口衝突**: `lsof -ti:5000 | xargs kill -9`
3. **計算錯誤**: 檢查輸入數據格式和範圍

### 日誌查看
```bash
docker-compose logs -f     # Docker日誌
tail -f gunicorn.log       # Gunicorn日誌
heroku logs --tail         # Heroku日誌
```

### 除錯模式
在 `.env` 設置: `DEBUG=True` 和 `FLASK_ENV=development`

## 代碼審查重點

### 1. 計算準確性
- 驗證八字計算邏輯正確性
- 確保節氣計算精確
- 檢查五虎遁月公式實現

### 2. API 一致性  
- 檢查雙端點支持: `/api/calculate-bazi` 和 `/api/calculate_bazi`
- 驗證錯誤處理和響應格式
- 確保輸入驗證完整

### 3. 前端整合
- 檢查JavaScript調用的API路徑
- 驗證前端表單數據格式
- 確保錯誤信息正確顯示

### 4. 測試覆蓋率
- 新功能必須有對應測試
- 運行smoke_tests.py確保基本功能
- 檢查enhanced_smoke_tests.py的API測試

### 5. 部署相容性
- 確保Docker配置正確
- 檢查requirements.txt版本固定
- 驗證環境變量處理

## 性能優化
1. **緩存**: 重複計算結果緩存
2. **並發**: 使用Gunicorn workers提高並發
3. **靜態資源**: CDN加速
4. **數據庫**: 考慮歷史結果存儲

## 安全考慮
1. **輸入驗證**: 嚴格驗證用戶輸入
2. **CORS配置**: 正確配置跨域請求  
3. **環境變量**: 敏感信息環境變量管理
4. **錯誤處理**: 避免洩露內部系統信息

## 維護要點
- 定期檢查依賴包安全更新
- Python版本兼容性測試
- 測試用例完整性驗證

遵循這些指南，GitHub Copilot能更好地理解和協助開發八字命理分析系統。