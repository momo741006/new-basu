# 虹靈御所八字人生兵法系統 (Chinese Bazi Fortune-Telling System)

虹靈御所八字人生兵法系統是一個基於Python Flask的中國八字命理分析網頁應用程式，提供精確的八字計算、納音五行分析、十神關係、五行統計和四時軍團生成功能。

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Dependencies
- Install Python dependencies:
  ```bash
  pip3 install -r requirements.txt
  ```
  - Takes 30 seconds. NEVER CANCEL.

### Core Engine Testing
- Test the PillarEngine core functionality:
  ```bash
  python3 pillar_engine.py
  ```
  - Takes 15 seconds. Expected output: "🎉 所有計算結果完全正確！"
  
- Test multiple calculation cases:
  ```bash
  python3 test_engine.py
  ```
  - Takes 15 seconds. Should show 3 test cases all passing.

### Application Testing
- Run basic smoke tests:
  ```bash
  python3 smoke_tests.py
  ```
  - Takes 30 seconds. NEVER CANCEL. Expected: "🎉 所有Smoke Tests通過！"

- Run enhanced smoke tests with full integration:
  ```bash
  python3 enhanced_smoke_tests.py
  ```
  - Takes 90 seconds. NEVER CANCEL. Set timeout to 120+ seconds.
  - Tests PillarEngine, AuthorityBaziCalculator, Flask integration, and API endpoints.
  - Expected: "🎉 所有Enhanced Smoke Tests通過！系統完美運行"

### Running the Application
- Development server:
  ```bash
  python3 app.py
  ```
  - Starts in 5 seconds on http://0.0.0.0:5000
  - Access main interface: http://127.0.0.1:5000
  - Access ultimate interface: http://127.0.0.1:5000/ultimate

- Production server with Gunicorn:
  ```bash
  gunicorn --bind 127.0.0.1:5000 --workers 2 --timeout 120 app:app
  ```
  - Starts in 5 seconds. Expected log: "🌈 虹靈御所八字人生兵法系統 Gunicorn服務器準備就緒"

### Docker Deployment
- Build Docker image:
  ```bash
  docker build -t bazi-system .
  ```
  - **WARNING**: May fail due to SSL certificate issues in some environments. This is a known limitation.
  - If build fails with SSL errors, use local Python deployment instead.

- Run with Docker Compose:
  ```bash
  docker-compose up -d
  ```
  - Only use if Docker build succeeds.

## Validation

### Manual Validation Requirements
ALWAYS manually validate any new code changes by running through complete user scenarios:

1. **Health Check Validation**:
   ```bash
   curl -s http://127.0.0.1:5000/api/health
   ```
   - Expected response containing: `"status":"ok"`

2. **API Calculation Validation**:
   ```bash
   curl -s -X POST http://127.0.0.1:5000/api/calculate_bazi \
     -H "Content-Type: application/json" \
     -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'
   ```
   - Expected: `"success":true` with complete pillars, nayins, ten_gods, and legions data.
   - Should return 乙丑年 乙酉月 戊寅日 壬戌時 for the test case.

3. **Frontend Interface Validation**:
   - Access http://127.0.0.1:5000 and verify the homepage loads by checking for the title "虹靈御所 - 八字人生兵法".
   - Access http://127.0.0.1:5000/ultimate and verify the ultimate interface loads with title containing "終極戰略分析系統".
   - Test form submission with valid birth data (year: 1985, month: 10, day: 6, hour: 19).
   - Verify results display shows four pillars, nayin elements, ten gods, and military legions.

4. **End-to-End Scenario Testing**:
   - Start the application
   - Submit a birth date calculation request
   - Verify complete response with all calculated elements
   - Check that both API endpoints (/api/calculate-bazi and /api/calculate_bazi) work

### Deployment Validation Tools
- Quick deployment status check:
  ```bash
  python3 answer_deployment.py
  ```
  - Takes 10 seconds. Provides simple yes/no deployment status.

- Complete deployment validation:
  ```bash
  python3 deployment_status.py
  ```
  - Takes 30 seconds. NEVER CANCEL. Runs comprehensive 7-point validation.
  - Expected: "🎉 系統已完全部署並正常運行！"
  - Checks Python environment, dependencies, files, Flask app, API endpoints, Docker, and documentation.

## Common Tasks

### Repository Structure
```
/home/runner/work/new-basu/new-basu/
├── app.py                    # Main Flask application
├── pillar_engine.py          # Core 八字 calculation engine  
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose setup
├── Procfile                 # Heroku deployment config
├── gunicorn.conf.py         # Gunicorn production config
├── templates/               # HTML templates
│   ├── index.html          # Main interface
│   └── ultimate_index.html # Ultimate interface
├── static/                  # Frontend assets
│   ├── css/                # Stylesheets
│   └── js/                 # JavaScript files
├── DEPLOYMENT.md           # Comprehensive deployment guide
└── DEPLOYMENT_TOOLS.md     # Deployment validation tools guide
```

### Key Files to Monitor
- `app.py`: Main Flask application with AuthorityBaziCalculator integration
- `pillar_engine.py`: Core calculation engine (PillarEngine class)
- `static/js/ultimate_app.js`: Frontend JavaScript for form validation and API calls
- Always check `deployment_status.py` after making changes to validate deployment readiness

### API Endpoints
- `GET /api/health`: Health check endpoint
- `POST /api/calculate-bazi`: Calculate 八字 (hyphen version)
- `POST /api/calculate_bazi`: Calculate 八字 (underscore version - both paths supported)
- `GET /`: Main interface
- `GET /ultimate`: Ultimate analysis interface

### Expected Calculation Results
For the standard test case (1985-10-06 19:00):
- 年柱 (Year): 乙丑
- 月柱 (Month): 乙酉  
- 日柱 (Day): 戊寅
- 時柱 (Hour): 壬戌
- Full result: "乙丑 乙酉 戊寅 壬戌"

### Timing Expectations
- **CRITICAL**: Set appropriate timeouts for all commands. NEVER CANCEL builds or long-running operations.
- Dependencies installation: 30 seconds
- Core engine tests: 15 seconds each
- Smoke tests: 30 seconds
- Enhanced smoke tests: 90 seconds (timeout: 120+ seconds)
- Flask startup: 5 seconds
- Gunicorn startup: 5 seconds
- Deployment validation: 30 seconds
- Docker build: May fail due to SSL issues - use local deployment instead

### Environment Requirements
- Python 3.7+ (tested with 3.12.3)
- Flask 3.1.2
- flask-cors 6.0.1
- gunicorn 21.2.0
- python-dotenv 1.0.0

### Troubleshooting
- If Docker build fails with SSL certificate errors, use local Python deployment
- Both `/api/calculate-bazi` and `/api/calculate_bazi` endpoints are supported for compatibility
- Always run `python3 deployment_status.py` to diagnose issues
- Use `python3 enhanced_smoke_tests.py` for comprehensive system validation

## Critical Reminders
- **NEVER CANCEL** any build, test, or deployment command
- Always validate changes with manual end-to-end testing
- Both API endpoint naming conventions (hyphen and underscore) are supported
- The system includes comprehensive self-validation tools - use them
- Focus on the complete user workflow: form input → API calculation → result display