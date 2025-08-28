# 虹靈御所八字人生兵法系統 (Hong Ling Yu Suo Ba Zi Life Strategy System)

This is a Chinese Ba Zi (八字) fortune-telling calculation system with a modular engine, Flask web application, and comprehensive deployment infrastructure.

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the information here.**

## Working Effectively

### Bootstrap and Dependencies
- Install Python dependencies: `pip install -r requirements.txt` -- takes ~10 seconds
- Python version requirement: 3.7+ (tested with 3.12.3)
- Core dependencies: Flask 3.1.2, flask-cors 6.0.1, gunicorn 21.2.0, python-dotenv 1.0.0

### Core Testing and Validation
- Test core Ba Zi engine: `python pillar_engine.py` -- takes ~2 seconds
- Run multiple test cases: `python test_engine.py` -- takes ~2 seconds  
- Full deployment health check: `python deployment_status.py` -- takes ~5 seconds. NEVER CANCEL: Set timeout to 30+ seconds
- Enhanced functionality tests: `python enhanced_smoke_tests.py` -- takes ~8 seconds. NEVER CANCEL: Set timeout to 30+ seconds
- Quick deployment status: `python answer_deployment.py` -- takes ~3 seconds

### Running the Application
- **Development server**: `python app.py` -- starts Flask development server on port 5000
- **Production server**: `gunicorn app:app --bind 0.0.0.0:5000 --workers 2 --timeout 120`
- **Application URLs**:
  - Main interface: `http://localhost:5000`
  - Health check API: `http://localhost:5000/api/health`
  - Ba Zi calculation API: `http://localhost:5000/api/calculate-bazi` (POST)
  - Alternative API path: `http://localhost:5000/api/calculate_bazi` (POST)

### Docker Deployment
- **Docker support**: Available with `Dockerfile` and `docker-compose.yml`
- **Build command**: `docker build -t bazi-app .` -- NEVER CANCEL: Takes 5-15 minutes. Set timeout to 20+ minutes
- **Docker Compose**: Use `docker compose up -d` (note: modern syntax, not `docker-compose`)
- **Known issue**: Docker build may fail in environments with SSL certificate restrictions due to PyPI access issues

### Code Quality and Syntax
- **Basic syntax check**: `python -m py_compile *.py` -- takes ~2 seconds
- **No dedicated linting**: Repository does not include configured linters (flake8, pylint, etc.)
- **Manual validation**: Always test functionality after code changes using the test scripts above

## Validation Scenarios

### CRITICAL: Manual Testing Requirements
**After making any changes, ALWAYS run this complete validation sequence:**

1. **Core engine validation**:
   ```bash
   python pillar_engine.py
   ```
   Expected output: `🎉 所有計算結果完全正確！` with Ba Zi result: `乙丑 乙酉 戊寅 壬戌`

2. **Multi-case testing**:
   ```bash
   python test_engine.py
   ```
   Expected: All 3 test cases pass with ✅ symbols

3. **Full system validation**:
   ```bash
   python enhanced_smoke_tests.py
   ```
   Expected output: `🎉 所有Enhanced Smoke Tests通過！系統完美運行`

4. **Web interface testing**:
   - Start: `python app.py`
   - Test health: `curl http://localhost:5000/api/health`
   - Test calculation: `curl -X POST http://localhost:5000/api/calculate-bazi -H "Content-Type: application/json" -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'`
   - Expected API response: JSON with `"success":true` and pillars data

5. **Complete user workflow**:
   - Navigate to `http://localhost:5000`
   - Fill form: Name="測試用戶", Gender="男性", Date=1985-10-06, Hour="戌時"
   - Click "🔮 生成命理分析"
   - Verify calculation completes (may show CDN errors in console but core functionality works)

### Expected Performance Benchmarks
- Dependency installation: ~10 seconds
- Core tests: ~2 seconds each
- Enhanced smoke tests: ~8 seconds
- Deployment status check: ~5 seconds
- Flask app startup: ~2 seconds
- Docker build: 5-15 minutes (when SSL certificates work)

## Important Files and Structure

### Core Application Files
- **`pillar_engine.py`**: Standalone Ba Zi calculation engine - the heart of the system
- **`app.py`**: Flask web application with API endpoints and web interface
- **`requirements.txt`**: Python dependencies (Flask, CORS, Gunicorn, dotenv)

### Testing and Validation
- **`test_engine.py`**: Multi-case testing for the core engine
- **`enhanced_smoke_tests.py`**: Comprehensive functionality and API testing
- **`deployment_status.py`**: Complete deployment health check tool
- **`answer_deployment.py`**: Quick deployment status checker
- **`smoke_tests.py`**: Basic smoke testing

### Frontend Assets
- **`static/js/ultimate_app.js`**: Main web application JavaScript with form validation
- **`static/js/app.js`**: Additional JavaScript functionality
- **`templates/`**: HTML templates for the web interface

### Deployment and Infrastructure
- **`Dockerfile`**: Container configuration for Python 3.11-slim with Gunicorn
- **`docker-compose.yml`**: Multi-service deployment with health checks
- **`gunicorn.conf.py`**: Gunicorn production server configuration
- **`nginx.conf`**: Nginx reverse proxy configuration
- **`Procfile`**: Heroku deployment configuration

### Documentation
- **`README.md`**: Basic project overview and usage examples
- **`DEPLOYMENT.md`**: Comprehensive deployment guide with multiple methods
- **`DEPLOYMENT_TOOLS.md`**: Documentation for deployment validation tools

## Common Tasks and Troubleshooting

### Quick Development Workflow
1. Make code changes
2. Run basic syntax check: `python -m py_compile *.py`
3. Test core functionality: `python pillar_engine.py && python test_engine.py`
4. Test web integration: `python enhanced_smoke_tests.py`
5. Manual web testing if changes affect UI/API

### API Testing Commands
```bash
# Health check
curl -s http://localhost:5000/api/health

# Ba Zi calculation (both paths work)
curl -s -X POST http://localhost:5000/api/calculate-bazi \
  -H "Content-Type: application/json" \
  -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'

curl -s -X POST http://localhost:5000/api/calculate_bazi \
  -H "Content-Type: application/json" \
  -d '{"name":"測試","year":1985,"month":10,"day":6,"hour":19}'
```

### Known Issues and Limitations
- **CDN Dependencies**: Web interface may show CDN errors for Chart.js in restricted networks, but core functionality remains operational
- **Docker SSL**: Docker builds may fail in environments with SSL certificate issues when accessing PyPI
- **GitHub Workflow**: Current workflow file (`.github/workflows/瞇`) is a placeholder and does not implement actual CI/CD

### Development Environment Setup
- **Python version**: 3.7+ required, 3.12+ recommended
- **Memory**: 2GB+ RAM recommended
- **Storage**: 1GB+ disk space
- **Network**: Internet access required for pip dependencies, optional for core functionality

### Critical Timeout Settings
- **NEVER CANCEL build operations**: Always set timeouts to 20+ minutes for Docker builds
- **NEVER CANCEL test suites**: Set timeouts to 30+ seconds for comprehensive tests
- **Flask startup**: Set timeout to 30+ seconds in case of slow environments
- **Deployment validation**: Set timeout to 60+ seconds for complete health checks

### Validation Exit Codes
- **`deployment_status.py`**: 
  - 0 = Fully deployed (all checks pass)
  - 1 = Partially deployed (80%+ checks pass)  
  - 2 = Not deployed (too many failures)
  - 3 = Check process error