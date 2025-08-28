// 八字系統數據
const BaziData = {
    tiangan: [
        { name: '甲', element: '木', yinyang: '陽', color: '#32CD32' },
        { name: '乙', element: '木', yinyang: '陰', color: '#90EE90' },
        { name: '丙', element: '火', yinyang: '陽', color: '#FF6347' },
        { name: '丁', element: '火', yinyang: '陰', color: '#FF69B4' },
        { name: '戊', element: '土', yinyang: '陽', color: '#DAA520' },
        { name: '己', element: '土', yinyang: '陰', color: '#F0E68C' },
        { name: '庚', element: '金', yinyang: '陽', color: '#C0C0C0' },
        { name: '辛', element: '金', yinyang: '陰', color: '#E6E6FA' },
        { name: '壬', element: '水', yinyang: '陽', color: '#4169E1' },
        { name: '癸', element: '水', yinyang: '陰', color: '#87CEEB' }
    ],
    
    dizhi: [
        { name: '子', element: '水', yinyang: '陽', time: '23-1時', animal: '鼠' },
        { name: '丑', element: '土', yinyang: '陰', time: '1-3時', animal: '牛' },
        { name: '寅', element: '木', yinyang: '陽', time: '3-5時', animal: '虎' },
        { name: '卯', element: '木', yinyang: '陰', time: '5-7時', animal: '兔' },
        { name: '辰', element: '土', yinyang: '陽', time: '7-9時', animal: '龍' },
        { name: '巳', element: '火', yinyang: '陰', time: '9-11時', animal: '蛇' },
        { name: '午', element: '火', yinyang: '陽', time: '11-13時', animal: '馬' },
        { name: '未', element: '土', yinyang: '陰', time: '13-15時', animal: '羊' },
        { name: '申', element: '金', yinyang: '陽', time: '15-17時', animal: '猴' },
        { name: '酉', element: '金', yinyang: '陰', time: '17-19時', animal: '雞' },
        { name: '戌', element: '土', yinyang: '陽', time: '19-21時', animal: '狗' },
        { name: '亥', element: '水', yinyang: '陰', time: '21-23時', animal: '豬' }
    ],

    nayin: {
        '甲子': '海中金', '乙丑': '海中金', '丙寅': '爐中火', '丁卯': '爐中火',
        '戊辰': '大林木', '己巳': '大林木', '庚午': '路旁土', '辛未': '路旁土',
        '壬申': '劍鋒金', '癸酉': '劍鋒金', '甲戌': '山頭火', '乙亥': '山頭火',
        '丙子': '澗下水', '丁丑': '澗下水', '戊寅': '城牆土', '己卯': '城牆土',
        '庚辰': '白蠟金', '辛巳': '白蠟金', '壬午': '楊柳木', '癸未': '楊柳木',
        '甲申': '泉中水', '乙酉': '泉中水', '丙戌': '屋上土', '丁亥': '屋上土',
        '戊子': '霹靂火', '己丑': '霹靂火', '庚寅': '松柏木', '辛卯': '松柏木',
        '壬辰': '長流水', '癸巳': '長流水', '甲午': '砂中金', '乙未': '砂中金',
        '丙申': '山下火', '丁酉': '山下火', '戊戌': '平地木', '己亥': '平地木',
        '庚子': '壁上土', '辛丑': '壁上土', '壬寅': '金箔金', '癸卯': '金箔金',
        '甲辰': '覆燈火', '乙巳': '覆燈火', '丙午': '天河水', '丁未': '天河水',
        '戊申': '大驛土', '己酉': '大驛土', '庚戌': '釵釧金', '辛亥': '釵釧金',
        '壬子': '桑柘木', '癸丑': '桑柘木', '甲寅': '大溪水', '乙卯': '大溪水',
        '丙辰': '砂中土', '丁巳': '砂中土', '戊午': '天上火', '己未': '天上火',
        '庚申': '石榴木', '辛酉': '石榴木', '壬戌': '大海水', '癸亥': '大海水'
    },

    legions: {
        family: { name: '家族兵團', pillar: '年柱', colors: ['#FFD700', '#20B2AA'] },
        growth: { name: '成長兵團', pillar: '月柱', colors: ['#9ACD32', '#FFD700'] },
        self: { name: '本我兵團', pillar: '日柱', colors: ['#4169E1', '#8A2BE2'] },
        future: { name: '未來兵團', pillar: '時柱', colors: ['#FF6347', '#FF1493'] }
    },

    legionStories: {
        family: '家族兵團承載著深厚的血脈傳承，如同古老城堡的守護者，世代傳承著智慧與力量。這裡是您根基所在，祖先的庇護如影隨形，為您的人生奠定堅實基礎。',
        growth: '成長兵團象徵著學習與適應的力量，如同春日萌芽的新綠，充滿無限可能。這裡培養著您的才能，塑造著人生的方向，每一次成長都是邁向成功的階梯。',
        self: '本我兵團是整個命格的核心所在，如同王座上的君主，統領四方。這裡展現著您的真實本性，是所有決策的源泉，代表著您內在的力量與智慧。',
        future: '未來兵團指向著無限的可能性，如同夜空中的北極星，指引著前進的方向。這裡蘊含著您的潛能與未來成就，預示著光明的前程。'
    }
};

// 系統類
class BaziSystem {
    constructor() {
        this.currentMode = 'traditional';
        this.baziResult = null;
        this.initializeEventListeners();
        this.populateSelects();
    }

    initializeEventListeners() {
        // 模式切換
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchMode(e.target.dataset.mode));
        });

        // 生成按鈕 - 確保事件監聽器正確綁定
        const generateBtn = document.getElementById('generateBtn');
        if (generateBtn) {
            generateBtn.addEventListener('click', (e) => {
                e.preventDefault();
                console.log('生成按鈕被點擊');
                this.generateBazi();
            });
        }

        // 知識庫標籤
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchKnowledgeTab(e.target.dataset.tab));
        });

        // 表單驗證 - 修復驗證邏輯
        this.setupFormValidation();
    }

    populateSelects() {
        // 傳統模式下拉選單
        this.populateYearSelect();
        this.populateMonthSelect();
        this.populateDaySelect();
        this.populateHourSelect();

        // 專家模式下拉選單
        this.populateStemSelects();
        this.populateBranchSelects();
    }

    populateYearSelect() {
        const yearSelect = document.getElementById('birthYear');
        if (!yearSelect) return;
        
        const currentYear = new Date().getFullYear();
        for (let year = currentYear; year >= currentYear - 100; year--) {
            const option = document.createElement('option');
            option.value = year;
            option.textContent = `${year}年`;
            yearSelect.appendChild(option);
        }
    }

    populateMonthSelect() {
        const monthSelect = document.getElementById('birthMonth');
        if (!monthSelect) return;
        
        for (let month = 1; month <= 12; month++) {
            const option = document.createElement('option');
            option.value = month;
            option.textContent = `${month}月`;
            monthSelect.appendChild(option);
        }
    }

    populateDaySelect() {
        const daySelect = document.getElementById('birthDay');
        if (!daySelect) return;
        
        for (let day = 1; day <= 31; day++) {
            const option = document.createElement('option');
            option.value = day;
            option.textContent = `${day}日`;
            daySelect.appendChild(option);
        }
    }

    populateHourSelect() {
        const hourSelect = document.getElementById('birthHour');
        if (!hourSelect) return;
        
        const hours = [
            { value: '子', text: '子時 (23:00-1:00)' },
            { value: '丑', text: '丑時 (1:00-3:00)' },
            { value: '寅', text: '寅時 (3:00-5:00)' },
            { value: '卯', text: '卯時 (5:00-7:00)' },
            { value: '辰', text: '辰時 (7:00-9:00)' },
            { value: '巳', text: '巳時 (9:00-11:00)' },
            { value: '午', text: '午時 (11:00-13:00)' },
            { value: '未', text: '未時 (13:00-15:00)' },
            { value: '申', text: '申時 (15:00-17:00)' },
            { value: '酉', text: '酉時 (17:00-19:00)' },
            { value: '戌', text: '戌時 (19:00-21:00)' },
            { value: '亥', text: '亥時 (21:00-23:00)' }
        ];

        hours.forEach(hour => {
            const option = document.createElement('option');
            option.value = hour.value;
            option.textContent = hour.text;
            hourSelect.appendChild(option);
        });
    }

    populateStemSelects() {
        const stemSelects = ['yearStem', 'monthStem', 'dayStem', 'hourStem'];
        stemSelects.forEach(selectId => {
            const select = document.getElementById(selectId);
            if (!select) return;
            
            BaziData.tiangan.forEach(stem => {
                const option = document.createElement('option');
                option.value = stem.name;
                option.textContent = `${stem.name}（${stem.element}${stem.yinyang}）`;
                select.appendChild(option);
            });
        });
    }

    populateBranchSelects() {
        const branchSelects = ['yearBranch', 'monthBranch', 'dayBranch', 'hourBranch'];
        branchSelects.forEach(selectId => {
            const select = document.getElementById(selectId);
            if (!select) return;
            
            BaziData.dizhi.forEach(branch => {
                const option = document.createElement('option');
                option.value = branch.name;
                option.textContent = `${branch.name}（${branch.animal}）`;
                select.appendChild(option);
            });
        });
    }

    switchMode(mode) {
        this.currentMode = mode;
        console.log('切換到模式:', mode);
        
        // 更新按鈕狀態
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });

        // 切換輸入界面
        const traditionalMode = document.getElementById('traditionalMode');
        const expertMode = document.getElementById('expertMode');
        
        if (traditionalMode && expertMode) {
            traditionalMode.classList.toggle('hidden', mode !== 'traditional');
            expertMode.classList.toggle('hidden', mode !== 'expert');
        }
    }

    setupFormValidation() {
        const inputs = document.querySelectorAll('.form-control');
        inputs.forEach(input => {
            input.addEventListener('change', () => this.validateForm());
            input.addEventListener('input', () => this.validateForm());
        });
        
        // 初始驗證
        setTimeout(() => this.validateForm(), 100);
    }

    validateForm() {
        const generateBtn = document.getElementById('generateBtn');
        if (!generateBtn) return;
        
        let isValid = false;

        if (this.currentMode === 'traditional') {
            const name = document.getElementById('name')?.value?.trim();
            const year = document.getElementById('birthYear')?.value;
            const month = document.getElementById('birthMonth')?.value;
            const day = document.getElementById('birthDay')?.value;
            const hour = document.getElementById('birthHour')?.value;
            
            isValid = name && year && month && day && hour;
            console.log('傳統模式驗證:', { name, year, month, day, hour, isValid });
        } else {
            const stems = ['yearStem', 'monthStem', 'dayStem', 'hourStem'];
            const branches = ['yearBranch', 'monthBranch', 'dayBranch', 'hourBranch'];
            
            const stemValues = stems.map(id => document.getElementById(id)?.value).filter(Boolean);
            const branchValues = branches.map(id => document.getElementById(id)?.value).filter(Boolean);
            
            isValid = stemValues.length === 4 && branchValues.length === 4;
            console.log('專家模式驗證:', { stemValues, branchValues, isValid });
        }

        generateBtn.disabled = !isValid;
        generateBtn.style.opacity = isValid ? '1' : '0.6';
        generateBtn.style.cursor = isValid ? 'pointer' : 'not-allowed';
        
        return isValid;
    }

    async generateBazi() {
        console.log('開始生成八字...');
        
        if (!this.validateForm()) {
            alert('請完整填寫所有必填欄位');
            return;
        }
        
        this.showLoading();
        
        try {
            // 模擬計算時間
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            let baziData;
            if (this.currentMode === 'traditional') {
                baziData = this.calculateFromTraditional();
            } else {
                baziData = this.calculateFromExpert();
            }
            
            console.log('計算結果:', baziData);
            this.baziResult = baziData;
            this.displayResults();
            
        } catch (error) {
            console.error('生成命盤時發生錯誤:', error);
            alert('生成命盤時發生錯誤，請檢查輸入資料。');
        } finally {
            this.hideLoading();
        }
    }

    calculateFromTraditional() {
        const name = document.getElementById('name').value;
        const year = parseInt(document.getElementById('birthYear').value);
        const month = parseInt(document.getElementById('birthMonth').value);
        const day = parseInt(document.getElementById('birthDay').value);
        const hour = document.getElementById('birthHour').value;

        console.log('傳統模式輸入:', { name, year, month, day, hour });

        // 簡化的八字計算邏輯
        const yearStemIndex = (year - 4) % 10;
        const yearBranchIndex = (year - 4) % 12;
        const monthStemIndex = (yearStemIndex * 2 + month) % 10;
        const monthBranchIndex = (month + 1) % 12;
        const dayStemIndex = (year * 12 + month * 31 + day) % 10;
        const dayBranchIndex = (year * 12 + month * 31 + day) % 12;
        
        const hourBranchIndex = BaziData.dizhi.findIndex(b => b.name === hour);
        const hourStemIndex = (dayStemIndex * 2 + Math.floor(hourBranchIndex / 2)) % 10;

        return {
            name: name,
            year: {
                stem: BaziData.tiangan[yearStemIndex].name,
                branch: BaziData.dizhi[yearBranchIndex].name
            },
            month: {
                stem: BaziData.tiangan[monthStemIndex].name,
                branch: BaziData.dizhi[monthBranchIndex].name
            },
            day: {
                stem: BaziData.tiangan[dayStemIndex].name,
                branch: BaziData.dizhi[dayBranchIndex].name
            },
            hour: {
                stem: BaziData.tiangan[hourStemIndex].name,
                branch: hour
            }
        };
    }

    calculateFromExpert() {
        return {
            year: {
                stem: document.getElementById('yearStem').value,
                branch: document.getElementById('yearBranch').value
            },
            month: {
                stem: document.getElementById('monthStem').value,
                branch: document.getElementById('monthBranch').value
            },
            day: {
                stem: document.getElementById('dayStem').value,
                branch: document.getElementById('dayBranch').value
            },
            hour: {
                stem: document.getElementById('hourStem').value,
                branch: document.getElementById('hourBranch').value
            }
        };
    }

    displayResults() {
        console.log('開始顯示結果...');
        this.displayBaziChart();
        this.displayLegions();
        this.displayAnalysis();
        this.showResultSections();
    }

    displayBaziChart() {
        const chartContainer = document.getElementById('baziChart');
        if (!chartContainer) return;
        
        chartContainer.innerHTML = '';

        const pillars = ['year', 'month', 'day', 'hour'];
        const pillarNames = ['年柱', '月柱', '日柱', '時柱'];

        pillars.forEach((pillar, index) => {
            const pillarDiv = document.createElement('div');
            pillarDiv.className = 'pillar-display';
            
            const stemBranch = `${this.baziResult[pillar].stem}${this.baziResult[pillar].branch}`;
            const nayin = BaziData.nayin[stemBranch] || '未知納音';

            pillarDiv.innerHTML = `
                <div class="pillar-name">${pillarNames[index]}</div>
                <div class="pillar-chars">
                    <span class="pillar-char">${this.baziResult[pillar].stem}</span>
                    <span class="pillar-char">${this.baziResult[pillar].branch}</span>
                </div>
                <div class="nayin-text">${nayin}</div>
            `;
            
            chartContainer.appendChild(pillarDiv);
        });

        // 顯示神煞
        this.displayShensha();
    }

    displayShensha() {
        const shenshaDisplay = document.getElementById('shenshaDisplay');
        if (!shenshaDisplay) return;
        
        const shensha = ['天乙貴人', '文昌', '桃花', '劫煞', '亡神'];
        
        shenshaDisplay.innerHTML = `
            <h4 style="color: var(--text-accent); margin-bottom: 1rem;">神煞標記</h4>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                ${shensha.map(sha => `
                    <span class="status status--info" style="font-size: 0.8rem;">${sha}</span>
                `).join('')}
            </div>
        `;
    }

    displayLegions() {
        const legionsGrid = document.getElementById('legionsGrid');
        if (!legionsGrid) return;
        
        legionsGrid.innerHTML = '';

        const legionTypes = ['family', 'growth', 'self', 'future'];
        const pillars = ['year', 'month', 'day', 'hour'];

        legionTypes.forEach((type, index) => {
            const legion = BaziData.legions[type];
            const pillarData = this.baziResult[pillars[index]];
            
            const legionCard = document.createElement('div');
            legionCard.className = `card legion-card ${type}`;
            
            legionCard.innerHTML = `
                <h3 class="legion-title" style="color: ${legion.colors[0]};">
                    ${legion.name}
                </h3>
                <div class="legion-roles">
                    <div class="role-item">
                        <span class="role-name">主將（天干）</span>
                        <span class="role-value">${pillarData.stem}</span>
                    </div>
                    <div class="role-item">
                        <span class="role-name">軍師（地支）</span>
                        <span class="role-value">${pillarData.branch}</span>
                    </div>
                    <div class="role-item">
                        <span class="role-name">戰場（納音）</span>
                        <span class="role-value">${BaziData.nayin[pillarData.stem + pillarData.branch] || '未知'}</span>
                    </div>
                </div>
                <div class="legion-story">
                    <p class="typewriter-text" data-text="${BaziData.legionStories[type]}"></p>
                </div>
            `;
            
            legionsGrid.appendChild(legionCard);
        });

        // 啟動打字機效果
        this.startTypewriterEffect();
    }

    startTypewriterEffect() {
        const typewriterTexts = document.querySelectorAll('.typewriter-text');
        typewriterTexts.forEach((element, index) => {
            const text = element.dataset.text || element.textContent;
            element.textContent = '';
            
            setTimeout(() => {
                let i = 0;
                const typeInterval = setInterval(() => {
                    element.textContent += text.charAt(i);
                    i++;
                    if (i > text.length) {
                        clearInterval(typeInterval);
                    }
                }, 50);
            }, index * 1000);
        });
    }

    displayAnalysis() {
        this.createWuxingChart();
        this.createYinyangChart();
        this.displayRecommendations();
        this.displayStrengthAnalysis();
    }

    createWuxingChart() {
        const canvas = document.getElementById('wuxingChart');
        if (!canvas) return;
        
        // Check if Chart.js is available
        if (typeof Chart === 'undefined') {
            console.log('Chart.js not available, using fallback display');
            this.createWuxingFallback(canvas);
            return;
        }
        
        const ctx = canvas.getContext('2d');
        
        // 計算五行分布
        const wuxingCount = { 木: 0, 火: 0, 土: 0, 金: 0, 水: 0 };
        
        Object.values(this.baziResult).forEach(pillar => {
            if (pillar && typeof pillar === 'object' && pillar.stem && pillar.branch) {
                const stemElement = BaziData.tiangan.find(t => t.name === pillar.stem)?.element;
                const branchElement = BaziData.dizhi.find(d => d.name === pillar.branch)?.element;
                
                if (stemElement) wuxingCount[stemElement]++;
                if (branchElement) wuxingCount[branchElement]++;
            }
        });

        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['木', '火', '土', '金', '水'],
                datasets: [{
                    data: Object.values(wuxingCount),
                    backgroundColor: ['#32CD32', '#FF6347', '#DAA520', '#C0C0C0', '#4169E1'],
                    borderColor: '#FFFFFF',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#FFFFFF',
                            font: { weight: 'bold' }
                        }
                    }
                }
            }
        });
    }

    createYinyangChart() {
        const canvas = document.getElementById('yinyangChart');
        if (!canvas) return;
        
        // Check if Chart.js is available
        if (typeof Chart === 'undefined') {
            console.log('Chart.js not available, using fallback display');
            this.createYinyangFallback(canvas);
            return;
        }
        
        const ctx = canvas.getContext('2d');
        
        let yangCount = 0, yinCount = 0;
        
        Object.values(this.baziResult).forEach(pillar => {
            if (pillar && typeof pillar === 'object' && pillar.stem && pillar.branch) {
                const stemYinyang = BaziData.tiangan.find(t => t.name === pillar.stem)?.yinyang;
                const branchYinyang = BaziData.dizhi.find(d => d.name === pillar.branch)?.yinyang;
                
                if (stemYinyang === '陽') yangCount++;
                else yinCount++;
                
                if (branchYinyang === '陽') yangCount++;
                else yinCount++;
            }
        });

        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['陽', '陰'],
                datasets: [{
                    data: [yangCount, yinCount],
                    backgroundColor: ['#FFD700', '#8A2BE2'],
                    borderColor: '#FFFFFF',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#FFFFFF',
                            font: { weight: 'bold' }
                        }
                    }
                }
            }
        });
    }

    createWuxingFallback(canvas) {
        // Create a simple text-based fallback for wuxing distribution
        const fallbackDiv = document.createElement('div');
        fallbackDiv.className = 'chart-fallback';
        fallbackDiv.innerHTML = `
            <h4 style="color: #FFFFFF; text-align: center; margin: 20px 0;">五行分布</h4>
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; text-align: center;">
                <div style="background: #32CD32; padding: 10px; border-radius: 5px; color: white;">木</div>
                <div style="background: #FF6347; padding: 10px; border-radius: 5px; color: white;">火</div>
                <div style="background: #DAA520; padding: 10px; border-radius: 5px; color: white;">土</div>
                <div style="background: #C0C0C0; padding: 10px; border-radius: 5px; color: black;">金</div>
                <div style="background: #4169E1; padding: 10px; border-radius: 5px; color: white;">水</div>
            </div>
        `;
        canvas.parentNode.replaceChild(fallbackDiv, canvas);
    }

    createYinyangFallback(canvas) {
        // Create a simple text-based fallback for yin/yang distribution
        const fallbackDiv = document.createElement('div');
        fallbackDiv.className = 'chart-fallback';
        fallbackDiv.innerHTML = `
            <h4 style="color: #FFFFFF; text-align: center; margin: 20px 0;">陰陽分布</h4>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; text-align: center;">
                <div style="background: #FFD700; padding: 20px; border-radius: 50%; color: black;">陽</div>
                <div style="background: #8A2BE2; padding: 20px; border-radius: 50%; color: white;">陰</div>
            </div>
        `;
        canvas.parentNode.replaceChild(fallbackDiv, canvas);
    }

    displayRecommendations() {
        const recommendationsDiv = document.getElementById('recommendations');
        if (!recommendationsDiv) return;
        
        recommendationsDiv.innerHTML = `
            <div class="recommendation-item">
                <h4 style="color: var(--text-success);">✅ 有利方位</h4>
                <p>東方、南方有助於事業發展</p>
            </div>
            <div class="recommendation-item">
                <h4 style="color: var(--text-warning);">🎨 幸運顏色</h4>
                <p>綠色、紅色、藍色能提升運勢</p>
            </div>
            <div class="recommendation-item">
                <h4 style="color: var(--text-accent);">💎 適合職業</h4>
                <p>文化、教育、科技、藝術相關工作</p>
            </div>
            <div class="recommendation-item">
                <h4 style="color: var(--text-danger);">⚠️ 注意事項</h4>
                <p>避免衝動決策，宜深思熟慮</p>
            </div>
        `;
    }

    displayStrengthAnalysis() {
        const strengthDiv = document.getElementById('strengthAnalysis');
        if (!strengthDiv) return;
        
        strengthDiv.innerHTML = `
            <div class="strength-item">
                <span>日主強度</span>
                <div class="strength-bar">
                    <div class="strength-fill" style="width: 75%; background: var(--text-success);"></div>
                </div>
                <span>強</span>
            </div>
            <div class="strength-item">
                <span>財運指數</span>
                <div class="strength-bar">
                    <div class="strength-fill" style="width: 60%; background: var(--text-warning);"></div>
                </div>
                <span>中等</span>
            </div>
            <div class="strength-item">
                <span>事業運勢</span>
                <div class="strength-bar">
                    <div class="strength-fill" style="width: 80%; background: var(--text-accent);"></div>
                </div>
                <span>佳</span>
            </div>
            <div class="strength-item">
                <span>感情運勢</span>
                <div class="strength-bar">
                    <div class="strength-fill" style="width: 65%; background: var(--text-danger);"></div>
                </div>
                <span>良好</span>
            </div>
        `;
    }

    showResultSections() {
        const sections = ['chartSection', 'legionsSection', 'analysisSection'];
        sections.forEach(id => {
            const section = document.getElementById(id);
            if (section) {
                section.classList.remove('hidden');
            }
        });
        
        // 平滑滾動到結果區域
        const chartSection = document.getElementById('chartSection');
        if (chartSection) {
            setTimeout(() => {
                chartSection.scrollIntoView({ 
                    behavior: 'smooth', 
                    block: 'start' 
                });
            }, 100);
        }
    }

    switchKnowledgeTab(tabName) {
        // 更新標籤按鈕狀態
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.tab === tabName);
        });

        // 更新內容顯示
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.toggle('active', content.id === `${tabName}Tab`);
        });
    }

    showLoading() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.classList.remove('hidden');
        }
    }

    hideLoading() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.classList.add('hidden');
        }
    }
}

// 初始化系統
document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM 載入完成，初始化八字系統...');
    new BaziSystem();
    
    // 添加額外樣式
    const style = document.createElement('style');
    style.textContent = `
        .recommendation-item, .strength-item {
            margin-bottom: 1rem;
            padding: 0.75rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .recommendation-item:last-child, .strength-item:last-child {
            border-bottom: none;
        }
        
        .recommendation-item h4 {
            margin-bottom: 0.5rem;
            font-size: 1rem;
            font-weight: 600;
        }
        
        .recommendation-item p {
            color: var(--text-secondary);
            margin: 0;
            font-weight: 500;
            text-shadow: 0 0 3px rgba(0,0,0,0.8);
        }
        
        .strength-item {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .strength-item span:first-child {
            min-width: 80px;
            color: var(--text-primary);
            font-weight: 600;
        }
        
        .strength-item span:last-child {
            min-width: 50px;
            color: var(--text-accent);
            font-weight: 600;
            text-align: right;
        }
        
        .strength-bar {
            flex: 1;
            height: 10px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            overflow: hidden;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);
        }
        
        .strength-fill {
            height: 100%;
            transition: width 2s ease;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        }
        
        .generate-btn:disabled {
            background: rgba(255, 255, 255, 0.1) !important;
            color: rgba(255, 255, 255, 0.5) !important;
            border-color: rgba(255, 255, 255, 0.2) !important;
            box-shadow: none !important;
        }
        
        .status--info {
            background-color: rgba(65, 105, 225, 0.2);
            color: #4169E1;
            border: 1px solid rgba(65, 105, 225, 0.3);
        }
    `;
    document.head.appendChild(style);
});