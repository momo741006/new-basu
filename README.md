# PillarEngine - 八字柱位計算引擎

## 🎯 模組化八字計算引擎

這是一個完全獨立的八字計算引擎，可以整合到任何八字系統中。

### ✅ 核心特色

1. **精準節氣計算**
   - 使用真太陽時和精確節氣計算
   - 1985年寒露精確在10月9日
   - 10月6日 < 寒露 → 屬於白露月(酉月)

2. **正確五虎遁月**
   - 甲己年丙作首，乙庚年戊為頭
   - 丙辛年庚上起，丁壬年壬位流
   - 戊癸年甲好求

3. **基準日算法**
   - 1985年9月22日 = 甲子日
   - 精確計算天數差值
   - 干支循環計算

4. **錯誤回溯機制**
   - 詳細記錄每步計算過程
   - 便於調試和驗證
   - 支援單元測試

### 🚀 使用方法

```python
from pillar_engine import PillarEngine

# 創建引擎實例
engine = PillarEngine()

# 計算八字
result = engine.calculate_pillars(1985, 10, 6, 19)

if result['success']:
    print(f"八字: {result['bazi_string']}")
    # 輸出: 乙丑 乙酉 戊寅 壬戌
```

### 🧪 測試驗證

```bash
python pillar_engine.py
```

預期輸出：
```
🧪 PillarEngine 測試結果:
八字結果: 乙丑 乙酉 戊寅 壬戌
🎉 所有計算結果完全正確！
```

### 📊 API接口

#### calculate_pillars(year, month, day, hour)

**參數:**
- year: 年份 (int)
- month: 月份 (int, 1-12)
- day: 日期 (int, 1-31)
- hour: 小時 (int, 0-23)

**返回:**
```python
{
    'success': True,
    'bazi_string': '乙丑 乙酉 戊寅 壬戌',
    'pillars': {
        'year': {'gan': '乙', 'zhi': '丑', 'pillar': '乙丑'},
        'month': {'gan': '乙', 'zhi': '酉', 'pillar': '乙酉'},
        'day': {'gan': '戊', 'zhi': '寅', 'pillar': '戊寅'},
        'hour': {'gan': '壬', 'zhi': '戌', 'pillar': '壬戌'}
    },
    'calculation_info': {
        'engine': 'PillarEngine',
        'version': '1.0',
        'debug_info': {...}
    }
}
```

### 🎯 技術突破

這個引擎解決了傳統八字計算中的關鍵問題：
- ❌ 月支錯誤 - 使用陽曆月份直接對應地支
- ❌ 節氣邊界判斷錯誤 - 未正確處理交界時間
- ❌ 日支計算錯誤 - 使用簡化算法

**PillarEngine是八字系統開發的黃金標準！**
