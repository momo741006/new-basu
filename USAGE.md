# 🌈 虹靈御所八字人生兵法系統 - 使用指南

> **怎麼用？** 這是一份完整的使用指南，讓您輕鬆掌握這個專業的八字命理分析系統。

## 📖 目錄

1. [系統簡介](#-系統簡介)
2. [快速開始](#-快速開始)
3. [功能詳解](#-功能詳解)
4. [操作指南](#-操作指南)
5. [API 使用](#-api-使用)
6. [安裝部署](#-安裝部署)
7. [常見問題](#-常見問題)
8. [進階功能](#-進階功能)

---

## 🎯 系統簡介

虹靈御所八字人生兵法系統是一個基於傳統中國命理學的現代化Web應用程序，提供精確的八字分析和命運解讀服務。

### ✨ 核心特色

- **🎭 美觀界面**: 深色主題配合宇宙星空背景，提供沉浸式體驗
- **⚡ 精確計算**: 使用VSOP87天文算法和儒略日計算，確保八字排盤精度
- **🛡️ 隱私保護**: 所有計算均在本地進行，不上傳個人資料
- **📱 響應式設計**: 支持桌面、平板和手機等各種設備
- **🔮 AI軍團故事**: 獨創的四時軍團分析，為命理增添生動色彩

### 🎨 系統界面預覽

系統提供兩種界面風格，滿足不同用戶的喜好：

#### 經典界面 (主頁)
![經典界面](https://github.com/user-attachments/assets/126c959c-acf4-400b-9a8a-ff9f41c5e046)

#### Ultimate Edition 界面
![Ultimate Edition](https://github.com/user-attachments/assets/5cd68926-87f1-4ebf-bb6f-4292999a4776)

**訪問方式:**
- 經典界面: `http://localhost:5000/`
- Ultimate版本: `http://localhost:5000/ultimate`

---

## 🚀 快速開始

### 第一步：選擇界面版本

系統提供兩個版本的界面：

**🌟 經典版本** (`/`)
- 星空主題背景
- 簡潔的導航設計
- 適合初次使用者

**⚔️ Ultimate版本** (`/ultimate`)
- 專業級界面設計
- 傳統模式與專家模式切換
- 內建八字兵法知識庫
- 適合進階使用者

### 第二步：訪問系統

1. 在瀏覽器中打開系統網址
2. 選擇合適的界面版本
3. 等待系統加載完成

### 第三步：輸入個人信息

根據您選擇的界面版本，填寫個人出生信息：

#### 經典版本表單
![經典版表單](https://github.com/user-attachments/assets/548eaf9f-113d-452d-8d92-955f0904037e)

#### Ultimate版本表單
![Ultimate版表單](https://github.com/user-attachments/assets/5cd68926-87f1-4ebf-bb6f-4292999a4776)

1. **姓名**: 輸入您的姓名（用於個性化顯示）
2. **性別**: 選擇男性或女性
3. **出生年份**: 從下拉菜單選擇出生年份（1950-2025年）
4. **出生月份**: 選擇出生月份（1-12月）
5. **出生日期**: 選擇出生日期（1-31日）
6. **出生時辰**: 選擇出生時辰，系統提供12個時辰選項：
   - 子時 (23:00-00:59)
   - 丑時 (01:00-02:59)
   - 寅時 (03:00-04:59)
   - 卯時 (05:00-06:59)
   - 辰時 (07:00-08:59)
   - 巳時 (09:00-10:59)
   - 午時 (11:00-12:59)
   - 未時 (13:00-14:59)
   - 申時 (15:00-16:59)
   - 酉時 (17:00-18:59)
   - 戌時 (19:00-20:59)
   - 亥時 (21:00-22:59)

**填寫項目:**

1. 驗證輸入信息的完整性
2. 計算八字四柱（年柱、月柱、日柱、時柱）
3. 分析五行分佈
4. 生成詳細的命理報告

---

## 🎛️ 功能詳解

### 界面功能對比

| 功能 | 經典版 | Ultimate版 |
|------|--------|------------|
| 基本輸入 | ✅ | ✅ |
| 專家模式 | ❌ | ✅ |
| 內建知識庫 | ❌ | ✅ |
| 模式切換 | ❌ | ✅ |
| 導航區域 | 5個功能區 | 智能切換 |
| 界面主題 | 星空風格 | 專業深色 |

### 經典版導航區域

| 按鈕 | 功能說明 |
|------|----------|
| 🎯 資料輸入 | 輸入出生信息的主界面 |
| 📊 傳統排盤 | 顯示傳統八字排盤結果 |
| ⚔️ 四時軍團 | 獨創的軍團故事分析 |
| 📈 詳細分析 | 五行統計、十神分析等 |
| 📚 八字百科 | 命理知識百科全書 |

### Ultimate版特色功能

#### 📚 八字兵法知識庫
內建完整的命理學習資源：

| 標籤 | 內容 |
|------|------|
| 基礎概念 | 十天干、十二地支、十神、神煞 |
| 高級理論 | 進階命理理論和應用 |
| 實例分析 | 真實案例解析和學習 |

### 數據輸入功能

#### 表單驗證
- 實時驗證輸入完整性
- 必填項目檢查
- 合理性驗證（如日期範圍）

#### 隱私保護
- 本地計算，無數據上傳
- 不保存用戶個人信息
- 安全提示顯示在界面底部

---

## 📋 操作指南

### 基本操作流程

```
1. 選擇界面版本 → 2. 填寫表單 → 3. 選擇模式 → 4. 點擊生成 → 5. 查看結果 → 6. 瀏覽分析
```

### 詳細操作步驟

#### 1. 界面選擇建議

**選擇經典版 (`/`) 如果您:**
- 首次使用該系統
- 喜歡簡潔的星空主題
- 只需要基本的八字分析功能

**選擇Ultimate版 (`/ultimate`) 如果您:**
- 是命理學習者或專業人士
- 需要專家模式功能
- 想要訪問內建知識庫
- 喜歡專業級的界面設計

#### 2. 信息輸入技巧

- **姓名輸入**: 建議使用真實姓名，系統會在報告中使用
- **時辰選擇**: 如果不確定具體時辰，可選擇最接近的時間段
- **信息修改**: 可隨時修改任何輸入項，重新生成分析

#### 3. 模式切換操作（Ultimate版）

**傳統模式 → 專家模式:**
1. 點擊界面頂部的"專家模式"按鈕
2. 界面自動切換為四柱輸入表單
3. 分別選擇年、月、日、時的天干地支

**專家模式 → 傳統模式:**
1. 點擊"傳統模式"按鈕
2. 返回日期時間輸入界面
3. 之前的專家模式輸入會被清除

#### 4. 結果查看方式

生成結果後，系統會顯示導航選項卡：

- **點擊各個選項卡**: 查看不同類型的分析內容
- **滾動瀏覽**: 詳細內容可能較長，請耐心滾動查看
- **保存結果**: 可使用瀏覽器的打印功能保存為PDF

#### 5. 實際使用示例

**示例1: 一般用戶使用經典版**
```
1. 訪問 http://localhost:5000/
2. 填寫: 張三、男性、1985年10月6日戌時
3. 點擊"🔮 生成命理分析"
4. 查看五個導航區域的詳細分析結果
```

#### 6. 功能區域介紹

##### 📊 傳統排盤
- 顯示完整的八字四柱
- 天干地支組合
- 納音五行信息
- 十神關係圖表

##### ⚔️ 四時軍團
系統獨創功能，將八字轉化為軍團故事：
- 年柱代表"統帥軍團"
- 月柱代表"謀略軍團"  
- 日柱代表"核心軍團"
- 時柱代表"先鋒軍團"

##### 📈 詳細分析
- 五行分佈統計圖表
- 陰陽平衡分析
- 強弱分析
- 用神建議

##### 📚 八字百科
- 天干地支知識
- 五行相生相剋
- 十神含義解釋
- 納音歌訣

---

## 🔌 API 使用

### 健康檢查端點

```bash
GET /api/health
```

**響應示例:**
```json
{
  "status": "ok",
  "message": "虹靈御所八字系統運行正常"
}
```

### 八字計算端點

```bash
POST /api/calculate-bazi
Content-Type: application/json
```

**請求參數:**
```json
{
  "name": "張三",
  "year": 1985,
  "month": 10,
  "day": 6,
  "hour": 19
}
```

**響應示例:**
```json
{
  "success": true,
  "name": "張三",
  "pillars": {
    "year": {"gan": "乙", "zhi": "丑", "pillar": "乙丑"},
    "month": {"gan": "乙", "zhi": "酉", "pillar": "乙酉"},
    "day": {"gan": "戊", "zhi": "寅", "pillar": "戊寅"},
    "hour": {"gan": "壬", "zhi": "戌", "pillar": "壬戌"}
  },
  "nayins": {
    "year": "海中金",
    "month": "泉中水", 
    "day": "城墻土",
    "hour": "大海水"
  },
  "ten_gods": ["傷官", "傷官", "日主", "正印"],
  "day_master": "戊",
  "wuxing_stats": {
    "金": 2,
    "木": 2,
    "水": 2,
    "火": 0,
    "土": 2
  },
  "legions": [...]
}
```

### API 使用示例

#### Python 示例

```python
import requests
import json

# 準備數據
data = {
    "name": "李四",
    "year": 1990,
    "month": 5,
    "day": 15,
    "hour": 14
}

# 發送請求
response = requests.post(
    "http://localhost:5000/api/calculate-bazi",
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)
)

# 處理響應
if response.status_code == 200:
    result = response.json()
    if result["success"]:
        print(f"八字: {result['pillars']['year']['pillar']} "
              f"{result['pillars']['month']['pillar']} "
              f"{result['pillars']['day']['pillar']} "
              f"{result['pillars']['hour']['pillar']}")
    else:
        print(f"計算失敗: {result['error']}")
else:
    print(f"請求失敗: {response.status_code}")
```

#### JavaScript 示例

```javascript
const calculateBazi = async (userData) => {
    try {
        const response = await fetch('/api/calculate-bazi', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            console.log('八字計算成功:', result);
            return result;
        } else {
            console.error('計算失敗:', result.error);
            return null;
        }
    } catch (error) {
        console.error('網絡錯誤:', error);
        return null;
    }
};

// 使用示例
const userData = {
    name: "王五",
    year: 1988,
    month: 12,
    day: 25,
    hour: 8
};

calculateBazi(userData).then(result => {
    if (result) {
        // 處理成功結果
        displayResults(result);
    }
});
```

---

## 🛠️ 安裝部署

詳細的安裝部署說明請參考 [DEPLOYMENT.md](./DEPLOYMENT.md) 文件。

### 快速部署命令

```bash
# Docker 方式（推薦）
git clone https://github.com/momo741006/new-basu.git
cd new-basu
docker-compose up -d

# 訪問應用
open http://localhost:5000
```

### 本地開發環境

```bash
# 安裝依賴
pip install -r requirements.txt

# 啟動應用
python app.py

# 訪問地址
http://localhost:5000
```

---

## ❓ 常見問題

### Q1: 為什麼點擊"生成分析"後出現錯誤？

**A1**: 可能的原因和解決方案：

1. **網絡連接問題**: 
   - 檢查是否能正常訪問 `/api/health` 端點
   - 確認後端服務正在運行中
   
2. **信息未填完整**: 
   - 確保所有必填項都已填寫
   - 經典版: 姓名、性別、年月日時
   - Ultimate版: 根據選擇的模式填寫相應信息
   
3. **瀏覽器兼容性**: 
   - 建議使用Chrome、Firefox或Safari最新版本
   - 清除瀏覽器緩存後重試
   
4. **服務器問題**: 
   - 檢查控制台是否有錯誤信息
   - 嘗試重新啟動應用服務

### Q2: 兩個界面版本有什麼區別？

**A2**: 詳細對比：

| 功能項目 | 經典版 (`/`) | Ultimate版 (`/ultimate`) |
|----------|-------------|-------------------------|
| 界面主題 | 星空風格 | 專業深色主題 |
| 輸入方式 | 僅傳統模式 | 傳統+專家雙模式 |
| 知識庫 | 無 | 內建八字兵法知識庫 |
| 按鈕文字 | "生成命理分析" | "生成命盤戰略" |
| 目標用戶 | 一般用戶 | 專業用戶 |
| 學習資源 | 基本介紹 | 完整理論學習 |

### Q3: 專家模式如何使用？

**A3**: 專家模式使用指南：

**訪問方式:**
1. 必須使用Ultimate版界面 (`/ultimate`)
2. 點擊頁面頂部的"專家模式"按鈕

**輸入方法:**
1. **年柱**: 選擇天干（甲-癸）+ 地支（子-亥）
2. **月柱**: 同樣方式選擇天干地支
3. **日柱**: 選擇日柱天干地支組合
4. **時柱**: 選擇時柱天干地支組合

**適用場景:**
- 已知完整八字，需要驗證系統計算準確性
- 學習特定八字組合的命理特徵
- 專業命理師快速排盤和分析

**注意事項:**
- 確保輸入的八字組合在曆法上是合理的
- 系統會進行基本的有效性檢查
- 專家模式不會自動計算，需要手動輸入準確信息

### Q4: 如何訪問知識庫功能？

### Q5: 時辰不確定怎麼辦？

**A5**: 如果不知道確切的出生時辰：

1. **查詢戶口本**: 部分戶口本記錄有出生時間
2. **詢問家人**: 向父母或長輩詢問
3. **估算時間**: 根據大致的時間段選擇最接近的時辰
4. **專業諮詢**: 尋找專業命理師協助確定

### Q6: 結果準確性如何保證？

**A6**: 系統準確性保證：

1. **天文算法**: 使用VSOP87精確天文算法
2. **傳統算法**: 遵循傳統八字排盤規則
3. **多重驗證**: 關鍵計算經過多重驗證
4. **開源透明**: 計算邏輯完全開源，可供驗證

### Q7: 手機上可以使用嗎？

**A7**: 完全支持移動設備：

1. **響應式設計**: 自動適配各種屏幕尺寸
2. **觸控優化**: 針對觸屏設備優化操作
3. **性能優化**: 在移動設備上流暢運行
4. **離線計算**: 支持離線狀態下的計算功能

### Q8: 可以保存結果嗎？

**A8**: 結果保存方法：

1. **瀏覽器書籤**: 保存當前頁面地址
2. **截圖保存**: 使用手機或電腦截圖功能
3. **打印PDF**: 使用瀏覽器打印功能保存為PDF
4. **複製文本**: 選中文本內容進行復制

---

## 🎓 進階功能

### 專家模式

系統提供專家模式，允許直接輸入天干地支：

1. 在輸入界面點擊"專家模式"
2. 直接選擇四柱的天干地支組合
3. 適合已知八字的專業用戶使用

### 批量計算

如果需要批量計算多個八字，可以使用API接口：

```python
# 批量計算示例
import asyncio
import aiohttp

async def batch_calculate(data_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for data in data_list:
            task = session.post('/api/calculate-bazi', json=data)
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        results = []
        for response in responses:
            result = await response.json()
            results.append(result)
        
        return results
```

### 自定義樣式

系統支持自定義CSS樣式，您可以：

1. 修改 `static/css/` 目錄下的樣式文件
2. 調整顏色主題
3. 修改字體大小
4. 調整佈局間距

### 數據導出

計算結果支持多種格式導出：

```javascript
// 導出為JSON
const exportJSON = (result) => {
    const dataStr = JSON.stringify(result, null, 2);
    const dataBlob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'bazi_result.json';
    link.click();
};

// 導出為CSV
const exportCSV = (result) => {
    const csvContent = convertToCSV(result);
    const blob = new Blob([csvContent], {type: 'text/csv'});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'bazi_result.csv';
    link.click();
};
```

---

## 📞 支持與反饋

- **GitHub Issues**: [提交問題](https://github.com/momo741006/new-basu/issues)
- **功能建議**: 歡迎提交新功能建議
- **Bug報告**: 發現問題請及時反饋
- **文檔改進**: 歡迎完善使用文檔

---

## 📄 版權信息

本系統基於開源協議發佈，詳細信息請查看 LICENSE 文件。

**免責聲明**: 本系統僅供娛樂和學習參考，不構成任何形式的人生建議或決策依據。

---

*最後更新: 2024年12月*

*版本: v9.3 Ultimate Edition*