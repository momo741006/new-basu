# 🌈 虹靈御所八字人生兵法系統 - 部署指南

這是一個完整的八字命理分析系統，支援多種部署方式。

## 📋 系統需求

- Python 3.7+
- Flask 3.1.2
- 2GB+ RAM (推薦)
- 1GB+ 磁碟空間

## 🔍 部署狀態檢查

### 快速檢查 - 部署好了嗎？

```bash
# 快速回答部署狀態
python answer_deployment.py
```

### 完整部署檢查

```bash
# 全面的部署狀態檢查
python deployment_status.py
```

這些工具會檢查：
- ✅ Python環境和版本
- ✅ 依賴包安裝狀態
- ✅ 必要文件完整性
- ✅ Flask應用功能
- ✅ API端點可用性
- ✅ Docker環境
- ✅ 部署文檔完整性

## 🚀 快速部署

### 方法一：Docker 部署 (推薦)

```bash
# 1. 克隆專案
git clone https://github.com/momo741006/new-basu.git
cd new-basu

# 2. 使用 Docker Compose 啟動
docker-compose up -d

# 3. 訪問應用
# 主頁面: http://localhost:5000
# API健康檢查: http://localhost:5000/api/health
```

### 方法二：本地開發環境

```bash
# 1. 克隆專案
git clone https://github.com/momo741006/new-basu.git
cd new-basu

# 2. 創建虛擬環境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 啟動應用
python app.py
```

### 方法三：生產環境 (Gunicorn)

```bash
# 1. 安裝依賴
pip install -r requirements.txt

# 2. 使用 Gunicorn 啟動
gunicorn -c gunicorn.conf.py app:app

# 或使用自定義配置
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app
```

## 🌐 雲平台部署

### Heroku 部署

```bash
# 1. 安裝 Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. 登入 Heroku
heroku login

# 3. 創建應用
heroku create your-bazi-app-name

# 4. 部署
git push heroku main

# 5. 開啟應用
heroku open
```

### Railway 部署

1. 訪問 [Railway](https://railway.app)
2. 連接 GitHub 倉庫
3. 選擇此專案
4. Railway 會自動檢測 Procfile 並部署

### Render 部署

1. 訪問 [Render](https://render.com)
2. 新建 Web Service
3. 連接 GitHub 倉庫
4. 配置：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

## 🔧 環境配置

複製 `.env.example` 為 `.env` 並修改配置：

```bash
cp .env.example .env
```

主要配置項：

```env
# Flask 配置
FLASK_ENV=production
SECRET_KEY=your-secret-key-here

# 服務器配置
HOST=0.0.0.0
PORT=5000

# Gunicorn 工作進程數
WEB_CONCURRENCY=2

# 調試模式
DEBUG=False
```

## 📊 API 端點

### 健康檢查
```
GET /api/health
回應: {"status": "ok", "message": "虹靈御所八字系統運行正常"}
```

### 八字計算
```
POST /api/calculate-bazi
POST /api/calculate_bazi  # 相容底線格式

請求體:
{
  "name": "姓名",
  "year": 1985,
  "month": 10,
  "day": 6,
  "hour": 19
}

回應:
{
  "success": true,
  "name": "姓名",
  "bazi": "乙丑 乙酉 戊寅 壬戌",
  "pillars": {...},
  "analysis": {...}
}
```

## 🔍 健康檢查與監控

### Docker 健康檢查

Docker 容器內建健康檢查，每30秒檢查一次：

```bash
# 檢查容器健康狀態
docker ps

# 查看健康檢查日誌
docker inspect --format='{{json .State.Health}}' container_name
```

### 手動健康檢查

```bash
# 檢查服務是否正常
curl http://localhost:5000/api/health

# 測試八字計算功能
curl -X POST http://localhost:5000/api/calculate-bazi \
  -H "Content-Type: application/json" \
  -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'
```

## 🛠️ 故障排除

### 常見問題

1. **端口被佔用**
   ```bash
   # 查找佔用端口的進程
   lsof -i :5000
   # 或使用其他端口
   PORT=8000 python app.py
   ```

2. **Python 模組未找到**
   ```bash
   # 確認在正確的虛擬環境中
   pip list
   # 重新安裝依賴
   pip install -r requirements.txt
   ```

3. **Docker 構建失敗**
   ```bash
   # 清理 Docker 快取
   docker system prune -a
   # 重新構建
   docker-compose build --no-cache
   ```

### 日誌查看

```bash
# Docker 日誌
docker-compose logs -f

# Gunicorn 日誌
tail -f gunicorn.log

# Heroku 日誌
heroku logs --tail
```

## 🔒 安全性建議

1. **更改預設密鑰**
   ```bash
   # 生成安全的密鑰
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

2. **使用 HTTPS**
   - 生產環境建議使用 Nginx + SSL 證書
   - 雲平台通常提供免費 SSL

3. **環境變數**
   - 敏感資訊放在環境變數中
   - 不要提交 `.env` 文件到版本控制

## 📈 性能優化

1. **工作進程數調整**
   ```
   # 推薦公式: 2 * CPU核心數 + 1
   workers = (2 * CPU_COUNT) + 1
   ```

2. **快取設置**
   - 靜態文件快取
   - API 響應快取（適當情況下）

3. **資料庫連接池**
   - 如果未來加入資料庫，配置連接池

## 🔬 部署驗證工具

### 1. 快速部署狀態檢查

```bash
python answer_deployment.py
```

**輸出範例:**
```
🌈 虹靈御所八字人生兵法系統
❓ 問題: 部署好了嗎？
✅ 答案: 是的，已經部署好了！

📊 系統狀態:
   🟢 應用文件: 完整
   🟢 依賴包: 已安裝
   🟢 Flask應用: 可正常啟動
```

### 2. 完整部署狀態檢查

```bash
python deployment_status.py
```

**檢查項目:**
- ✅ Python環境和版本 (3.7+)
- ✅ 依賴包安裝狀態 (Flask、CORS、Gunicorn)
- ✅ 必要文件完整性 (app.py、Dockerfile等)
- ✅ Flask應用導入和初始化
- ✅ API端點可用性 (健康檢查、八字計算)
- ✅ Docker環境可用性
- ✅ 部署文檔完整性

**退出碼:**
- `0`: 完全部署 (7/7檢查通過)
- `1`: 部分部署 (80%以上檢查通過)
- `2`: 未部署 (檢查失敗過多)
- `3`: 檢查過程異常

### 3. 自動化測試

```bash
# 運行enhanced smoke tests
python enhanced_smoke_tests.py

# 基本smoke tests
python smoke_tests.py
```

這些工具可以幫助您：
- 🎯 快速確認部署狀態
- 🔧 識別部署問題
- 📊 獲得詳細的系統健康報告
- 🚀 驗證所有功能正常工作

## 🆘 支援

如遇到部署問題，請：

1. 運行 `python deployment_status.py` 獲取詳細診斷
2. 檢查系統日誌
3. 確認依賴版本
4. 查看防火牆設置
5. 提交 Issue 到 GitHub，附上部署檢查結果

---

**🌟 恭喜！虹靈御所八字人生兵法系統已成功部署！**