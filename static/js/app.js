// 虹靈御所八字人生兵法系統 - 增強版前端邏輯
class EnhancedBaziSystem {
    constructor() {
        console.log('🌈 虹靈御所系統啟動...');
        this.apiBase = '/api';
        this.currentData = null;
        this.wuxingChart = null;
        
        this.init();
    }

    init() {
        this.setupNavigation();
        this.setupForm();
        this.setupYearOptions();
        this.setupDayOptions();
        this.setupEncyclopedia();
    }

    // 設置導航功能
    setupNavigation() {
        const navBtns = document.querySelectorAll('.nav-btn');
        const sections = document.querySelectorAll('.section');

        navBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetSection = btn.dataset.section;
                
                // 移除所有活動狀態
                navBtns.forEach(b => b.classList.remove('active'));
                sections.forEach(s => s.classList.remove('active'));
                
                // 添加活動狀態
                btn.classList.add('active');
                const targetElement = document.getElementById(`${targetSection}-section`);
                if (targetElement) {
                    targetElement.classList.add('active');
                } else {
                    console.error(`找不到區域: ${targetSection}-section`);
                }
            });
        });
    }

    // 設置表單功能
    setupForm() {
        const form = document.getElementById('baziForm');
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.calculateBazi();
        });

        // 月份變化時更新日期選項
        const monthSelect = document.getElementById('birthMonth');
        monthSelect.addEventListener('change', () => {
            this.updateDayOptions();
        });
    }

    // 設置年份選項
    setupYearOptions() {
        const yearSelect = document.getElementById('birthYear');
        const currentYear = new Date().getFullYear();
        
        // 擴展年份範圍：1950-2025年
        for (let year = currentYear; year >= 1950; year--) {
            const option = document.createElement('option');
            option.value = year;
            option.textContent = `${year}年`;
            yearSelect.appendChild(option);
        }
    }

    // 設置日期選項
    setupDayOptions() {
        const daySelect = document.getElementById('birthDay');
        
        // 初始化1-31日
        for (let day = 1; day <= 31; day++) {
            const option = document.createElement('option');
            option.value = day;
            option.textContent = `${day}日`;
            daySelect.appendChild(option);
        }
    }

    // 根據月份更新日期選項
    updateDayOptions() {
        const monthSelect = document.getElementById('birthMonth');
        const daySelect = document.getElementById('birthDay');
        const yearSelect = document.getElementById('birthYear');
        
        const month = parseInt(monthSelect.value);
        const year = parseInt(yearSelect.value) || new Date().getFullYear();
        
        if (!month) return;
        
        // 清空現有選項
        daySelect.innerHTML = '<option value="">選擇日期</option>';
        
        // 計算該月天數
        const daysInMonth = new Date(year, month, 0).getDate();
        
        for (let day = 1; day <= daysInMonth; day++) {
            const option = document.createElement('option');
            option.value = day;
            option.textContent = `${day}日`;
            daySelect.appendChild(option);
        }
    }

    // 計算八字
    async calculateBazi() {
        const formData = this.getFormData();
        if (!this.validateFormData(formData)) {
            return;
        }

        this.showLoading(true);

        try {
            // 與後端保持一致，使用中橫線作為計算接口路徑
            const response = await fetch(`${this.apiBase}/calculate-bazi`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            if (data.success) {
                this.currentData = data;
                this.displayResults(data);
                this.switchToSection('traditional');
            } else {
                this.showError(data.error || '計算失敗');
            }
        } catch (error) {
            console.error('計算錯誤:', error);
            this.showError('網路連接錯誤，請檢查後端服務是否正常運行');
        } finally {
            this.showLoading(false);
        }
    }

    // 獲取表單數據
    getFormData() {
        return {
            name: document.getElementById('name').value,
            year: parseInt(document.getElementById('birthYear').value),
            month: parseInt(document.getElementById('birthMonth').value),
            day: parseInt(document.getElementById('birthDay').value),
            hour: parseInt(document.getElementById('birthHour').value)
        };
    }

    // 驗證表單數據
    validateFormData(data) {
        if (!data.name) {
            this.showError('請輸入姓名');
            return false;
        }
        if (!data.year || !data.month || !data.day || data.hour === undefined) {
            this.showError('請完整填寫出生時間');
            return false;
        }
        return true;
    }

    // 顯示結果
    displayResults(data) {
        this.displayTraditionalChart(data);
        this.displayLegions(data);
        this.displayAnalysis(data);
    }

    // 顯示傳統排盤
    displayTraditionalChart(data) {
        const pillars = data.pillars;
        const nayins = data.nayins;
        const tenGods = data.ten_gods;

        // 填充四柱數據
        document.getElementById('year-gan').textContent = pillars.year.gan;
        document.getElementById('year-zhi').textContent = pillars.year.zhi;
        document.getElementById('month-gan').textContent = pillars.month.gan;
        document.getElementById('month-zhi').textContent = pillars.month.zhi;
        document.getElementById('day-gan').textContent = pillars.day.gan;
        document.getElementById('day-zhi').textContent = pillars.day.zhi;
        document.getElementById('hour-gan').textContent = pillars.hour.gan;
        document.getElementById('hour-zhi').textContent = pillars.hour.zhi;

        // 填充納音
        document.getElementById('year-nayin').textContent = nayins.year;
        document.getElementById('month-nayin').textContent = nayins.month;
        document.getElementById('day-nayin').textContent = nayins.day;
        document.getElementById('hour-nayin').textContent = nayins.hour;

        // 填充十神（簡化處理）
        if (tenGods.length >= 3) {
            document.getElementById('year-ten-god').textContent = tenGods[0];
            document.getElementById('month-ten-god').textContent = tenGods[1];
            document.getElementById('hour-ten-god').textContent = tenGods[3] || tenGods[2];
        }

        // 顯示神煞
        const shensList = document.getElementById('shens-list');
        if (data.shens && data.shens.length > 0) {
            shensList.innerHTML = data.shens.map(shen => 
                `<span class="shen-tag">${shen}</span>`
            ).join('');
        } else {
            shensList.innerHTML = '<p>無特殊神煞</p>';
        }

        // 顯示五行統計
        const wuxingStats = document.getElementById('wuxing-stats');
        if (data.wuxing_stats) {
            const statsHtml = Object.entries(data.wuxing_stats)
                .map(([element, value]) => 
                    `<div class="wuxing-item">
                        <span class="element">${element}</span>
                        <span class="value">${value.toFixed(1)}</span>
                    </div>`
                ).join('');
            wuxingStats.innerHTML = statsHtml;
        }
    }

    // 顯示軍團分析
    displayLegions(data) {
        const legions = data.legions;
        
        legions.forEach((legion, index) => {
            document.getElementById(`legion-${index}-commander`).textContent = legion.commander;
            document.getElementById(`legion-${index}-strategist`).textContent = legion.strategist;
            document.getElementById(`legion-${index}-deputy`).textContent = legion.deputy;
            
            // 生成軍團故事
            const story = this.generateLegionStory(legion, index);
            document.getElementById(`legion-${index}-story`).textContent = story;
        });
    }

    // 生成軍團故事
    generateLegionStory(legion, index) {
        const stories = [
            `在${legion.name}中，${legion.commander}作為主將展現出強大的領導力，與軍師${legion.strategist}共同制定戰略。副將${legion.deputy}提供堅實的支援，形成了穩固的家族根基。`,
            `${legion.name}見證了您的成長歷程，主將${legion.commander}引導著學習的方向，軍師${legion.strategist}提供智慧的指導，副將${legion.deputy}在關鍵時刻給予支持。`,
            `在${legion.name}的核心，${legion.commander}代表著您的真實本性，軍師${legion.strategist}反映內在的智慧，副將${legion.deputy}展現潛在的能力，共同構成完整的自我。`,
            `${legion.name}指向未來的無限可能，主將${legion.commander}開拓前進的道路，軍師${legion.strategist}預見未來的機遇，副將${legion.deputy}準備迎接挑戰。`
        ];
        
        return stories[index] || `${legion.name}展現出獨特的能量組合。`;
    }

    // 顯示詳細分析
    displayAnalysis(data) {
        // 創建五行圖表
        this.createWuxingChart(data.wuxing_stats);
        
        // 生成分析文本
        this.generateAnalysisText(data);
    }

    // 創建五行圖表
    createWuxingChart(wuxingStats) {
        const chartContainer = document.getElementById('wuxingChart');
        if (!chartContainer) {
            console.warn('五行圖表容器不存在');
            return;
        }

        // 檢查 Chart.js 是否可用
        if (typeof Chart === 'undefined') {
            console.warn('Chart.js 未載入，顯示文字版五行統計');
            this.displayWuxingStats(wuxingStats);
            return;
        }

        const ctx = chartContainer.getContext('2d');
        
        if (this.wuxingChart) {
            this.wuxingChart.destroy();
        }

        const elements = Object.keys(wuxingStats);
        const values = Object.values(wuxingStats);
        
        this.wuxingChart = new Chart(ctx, {
            type: 'radar',
            data: {
                labels: elements,
                datasets: [{
                    label: '五行能量',
                    data: values,
                    backgroundColor: 'rgba(0, 212, 255, 0.2)',
                    borderColor: '#00d4ff',
                    borderWidth: 2,
                    pointBackgroundColor: '#00d4ff',
                    pointBorderColor: '#ffffff',
                    pointBorderWidth: 2,
                    pointRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#ffffff'
                        }
                    }
                },
                scales: {
                    r: {
                        beginAtZero: true,
                        ticks: {
                            color: '#b0b0b0'
                        },
                        grid: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        angleLines: {
                            color: 'rgba(255, 255, 255, 0.1)'
                        },
                        pointLabels: {
                            color: '#00d4ff',
                            font: {
                                size: 14,
                                weight: 'bold'
                            }
                        }
                    }
                }
            }
        });
    }

    // 顯示文字版五行統計（當Chart.js不可用時）
    displayWuxingStats(wuxingStats) {
        const chartContainer = document.getElementById('wuxingChart');
        if (!chartContainer) return;

        const elements = Object.keys(wuxingStats);
        const values = Object.values(wuxingStats);
        const maxValue = Math.max(...values);

        let html = '<div class="wuxing-text-stats">';
        html += '<h4 style="color: #00d4ff; margin-bottom: 15px;">五行能量分佈</h4>';
        
        elements.forEach((element, index) => {
            const value = values[index];
            const percentage = ((value / maxValue) * 100).toFixed(1);
            const barWidth = Math.max(percentage, 5); // 最小寬度5%
            
            html += `
                <div class="wuxing-item" style="margin-bottom: 10px;">
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 5px;">
                        <span style="color: #ffffff; font-weight: bold;">${element}</span>
                        <span style="color: #00d4ff;">${value}</span>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); height: 8px; border-radius: 4px; overflow: hidden;">
                        <div style="background: linear-gradient(90deg, #00d4ff, #0099cc); height: 100%; width: ${barWidth}%; transition: width 0.5s ease;"></div>
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
        chartContainer.outerHTML = `<div id="wuxingChart" style="padding: 20px;">${html}</div>`;
    }

    // 生成分析文本
    generateAnalysisText(data) {
        const dayMaster = data.day_master;
        const wuxingStats = data.wuxing_stats;
        
        // 個性分析
        document.getElementById('personality-analysis').textContent = 
            `日主${dayMaster}，性格特質體現在...（基於五行平衡的個性分析）`;
        
        // 事業分析
        document.getElementById('career-analysis').textContent = 
            `根據命盤顯示，適合發展...（基於十神關係的事業建議）`;
        
        // 愛情分析
        document.getElementById('love-analysis').textContent = 
            `感情方面，您的特質是...（基於桃花和配偶宮的分析）`;
        
        // 財運分析
        document.getElementById('wealth-analysis').textContent = 
            `財運方面，建議關注...（基於財星和財庫的分析）`;
    }

    // 設置百科功能
    setupEncyclopedia() {
        const searchInput = document.getElementById('encyclopedia-search');
        const searchBtn = document.querySelector('.search-btn');
        const cards = document.querySelectorAll('.encyclopedia-card');

        // 搜尋功能
        const performSearch = () => {
            const query = searchInput.value.toLowerCase();
            cards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (text.includes(query) || query === '') {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        };

        searchBtn.addEventListener('click', performSearch);
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                performSearch();
            }
        });

        // 卡片點擊展開功能
        cards.forEach(card => {
            card.addEventListener('click', () => {
                const details = card.querySelector('.encyclopedia-details');
                if (details.style.display === 'none' || !details.style.display) {
                    details.style.display = 'block';
                    card.style.transform = 'scale(1.02)';
                } else {
                    details.style.display = 'none';
                    card.style.transform = 'scale(1)';
                }
            });
        });
    }

    // 切換到指定區域
    switchToSection(sectionName) {
        const navBtns = document.querySelectorAll('.nav-btn');
        const sections = document.querySelectorAll('.section');
        
        navBtns.forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.section === sectionName) {
                btn.classList.add('active');
            }
        });
        
        sections.forEach(section => {
            section.classList.remove('active');
            if (section.id === `${sectionName}-section`) {
                section.classList.add('active');
            }
        });
    }

    // 顯示載入狀態
    showLoading(show) {
        const loading = document.getElementById('loading');
        if (show) {
            loading.classList.remove('hidden');
        } else {
            loading.classList.add('hidden');
        }
    }

    // 顯示錯誤信息
    showError(message) {
        alert(`錯誤：${message}`);
    }
}

// 頁面載入完成後初始化系統
document.addEventListener('DOMContentLoaded', () => {
    window.enhancedBaziSystem = new EnhancedBaziSystem();
});

// 添加一些實用的CSS樣式
const additionalStyles = `
<style>
.shen-tag {
    display: inline-block;
    background: linear-gradient(135deg, var(--neon-purple), var(--neon-pink));
    color: white;
    padding: 5px 12px;
    border-radius: 15px;
    margin: 3px;
    font-size: 0.9rem;
    font-weight: 500;
    box-shadow: 0 2px 10px rgba(179, 71, 217, 0.3);
}

.wuxing-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid var(--glass-border);
}

.wuxing-item:last-child {
    border-bottom: none;
}

.wuxing-item .element {
    font-weight: 600;
    color: var(--neon-green);
}

.wuxing-item .value {
    font-weight: bold;
    color: var(--neon-blue);
    text-shadow: 0 0 5px var(--neon-blue);
}

#wuxingChart {
    max-height: 300px;
}

.encyclopedia-details {
    display: none;
    transition: all 0.3s ease;
}
</style>
`;

document.head.insertAdjacentHTML('beforeend', additionalStyles);

