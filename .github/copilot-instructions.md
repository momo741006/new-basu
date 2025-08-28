# 🌈 虹靈御所八字人生兵法系統 - GitHub Copilot Instructions

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## 🎯 Project Overview

This is a Chinese BaZi (八字) fortune-telling calculation engine built with Python and Flask. The system provides both a web interface and REST APIs for calculating traditional Chinese astrological charts based on birth date and time.

**Core Components:**
- `pillar_engine.py` - Core calculation engine for BaZi pillars
- `app.py` - Flask web application with APIs and web interface
- Multiple test suites for validation
- Docker deployment support
- Comprehensive deployment validation tools

## 🚀 Bootstrap and Build Process

### System Requirements
- Python 3.7+ (tested with 3.12.3)
- 2GB+ RAM recommended
- 1GB+ disk space

### Essential Setup Commands

**NEVER CANCEL these commands. Always wait for completion:**

```bash
# Install dependencies - takes 30 seconds, NEVER CANCEL
pip3 install -r requirements.txt
```

**No build process required** - this is a pure Python application that runs directly.

## 🧪 Testing and Validation

### Core Engine Tests

```bash
# Test main engine - takes <1 second
python3 pillar_engine.py
# Expected output: "八字結果: 乙丑 乙酉 戊寅 壬戌" and "🎉 所有計算結果完全正確！"

# Run engine test cases - takes 1 second  
python3 test_engine.py
# Expected: 3 test cases all showing "✅ 計算成功" and "✅ 結果正確"
```

### Smoke Tests

```bash
# Basic smoke tests - takes 2 seconds
python3 smoke_tests.py  
# Expected: "📊 測試結果: 4/4 通過" and "🎉 所有Smoke Tests通過！"

# Enhanced smoke tests - takes 3 seconds
python3 enhanced_smoke_tests.py
# Expected: "📊 測試結果: 4/4 通過" and "🎉 所有Enhanced Smoke Tests通過！"
```

### Syntax Validation

```bash
# Python syntax check - takes <1 second
python3 -m py_compile *.py
echo "Python syntax check passed"
```

## 🌐 Running the Application

### Development Server

```bash
# Start Flask development server - starts immediately
python3 app.py
# Server runs on http://localhost:5000
# NEVER CANCEL - let it run until you explicitly stop it with Ctrl+C
```

### Production Server

```bash
# Start with Gunicorn - starts immediately  
gunicorn app:app
# Server runs on http://localhost:8000
```

## 🔍 API Testing and Validation

**Always test these endpoints after making changes:**

### Health Check
```bash
curl -s http://localhost:5000/api/health
# Expected: {"message":"虹靈御所八字系統運行正常","status":"ok"}
```

### BaZi Calculation API
```bash
curl -s -X POST -H "Content-Type: application/json" \
  -d '{"name": "測試", "year": 1985, "month": 10, "day": 6, "hour": 19}' \
  http://localhost:5000/api/calculate-bazi
# Expected: JSON response with "success": true and pillars showing "乙丑 乙酉 戊寅 壬戌"
```

Both `/api/calculate-bazi` and `/api/calculate_bazi` work (hyphen and underscore versions).

## 🏥 Deployment Status Validation

### Quick Deployment Check

```bash
# Fast deployment verification - takes 1 second
python3 answer_deployment.py
# Expected: "✅ 答案: 是的，已經部署好了！"
```

### Comprehensive Deployment Check

```bash
# Full deployment validation - takes 8 seconds, NEVER CANCEL
python3 deployment_status.py  
# Expected: "✅ 通過檢查: 7/7" and "🎉 系統已完全部署並正常運行！"
```

## 🐳 Docker Deployment

### Local Development
```bash
# Docker Compose - LIMITATION: may fail in some environments due to SSL issues
docker-compose up -d
# If this fails, use Python directly instead
```

### Docker Build Issues
**KNOWN LIMITATION:** Docker builds may fail in sandboxed environments due to SSL certificate verification errors when accessing PyPI. This is expected in certain development environments.

**Workaround:** Use direct Python execution instead:
```bash
python3 app.py  # Development
gunicorn app:app  # Production
```

## 🎯 Manual Validation Scenarios

**CRITICAL: Always run these validation scenarios after making changes:**

### 1. Core Engine Validation
```bash
python3 pillar_engine.py
# Verify output shows: "八字結果: 乙丑 乙酉 戊寅 壬戌"
```

### 2. Web Application Validation
1. Start server: `python3 app.py`
2. Open browser to http://localhost:5000
3. Verify web interface loads
4. Test API health check (see API Testing section above)
5. Test BaZi calculation with known values (see API Testing section above)

### 3. Full Integration Test
```bash
# Run this complete sequence:
python3 smoke_tests.py && \
python3 enhanced_smoke_tests.py && \
python3 deployment_status.py
# All should show "通過" (pass) results
```

## ⏱️ Timing Expectations and Timeouts

**NEVER CANCEL any of these operations. Always use appropriate timeouts:**

- **Dependency Installation**: 30 seconds (use 60+ second timeout)
- **Core Engine Tests**: <1 second (use 30 second timeout)  
- **Smoke Tests**: 2-3 seconds (use 30 second timeout)
- **Deployment Status Check**: 8 seconds (use 60 second timeout)
- **Application Startup**: Immediate (use 30 second timeout)
- **API Response Time**: <1 second (use 10 second timeout)

## 📁 Key File Locations

### Core Files
- `/pillar_engine.py` - Main calculation engine
- `/app.py` - Flask web application  
- `/requirements.txt` - Python dependencies

### Test Files
- `/test_engine.py` - Engine test cases
- `/smoke_tests.py` - Basic integration tests
- `/enhanced_smoke_tests.py` - Comprehensive integration tests

### Deployment Files  
- `/deployment_status.py` - Full deployment checker
- `/answer_deployment.py` - Quick deployment checker
- `/Dockerfile` - Docker configuration
- `/docker-compose.yml` - Docker Compose setup

### Documentation
- `/README.md` - Project overview and usage
- `/DEPLOYMENT.md` - Detailed deployment guide
- `/DEPLOYMENT_TOOLS.md` - Deployment tool documentation

## 🔧 Development Workflow

**Always follow this sequence when making changes:**

1. **Make your code changes**
2. **Validate syntax**: `python3 -m py_compile *.py`
3. **Test core engine**: `python3 pillar_engine.py`
4. **Run smoke tests**: `python3 smoke_tests.py`
5. **Test Flask integration**: `python3 enhanced_smoke_tests.py`
6. **Start application**: `python3 app.py`
7. **Test APIs manually** (see API Testing section)
8. **Run deployment validation**: `python3 deployment_status.py`

## 🚫 What NOT to Do

- **DO NOT** cancel builds or tests early - wait for completion
- **DO NOT** try to "fix" Docker SSL issues in sandboxed environments  
- **DO NOT** skip the manual validation scenarios
- **DO NOT** assume the system works without running the full test suite
- **DO NOT** modify core calculation logic without validating against the reference case (1985/10/6/19)

## 💡 Troubleshooting Common Issues

### Port Already in Use
```bash
# Check what's using port 5000
lsof -i :5000
# Use different port if needed
PORT=8000 python3 app.py
```

### Import Errors
```bash
# Verify dependencies are installed
pip3 list | grep -E "(flask|gunicorn)"
# Reinstall if needed
pip3 install -r requirements.txt
```

### API Not Responding
1. Confirm server is running: `curl http://localhost:5000/api/health`
2. Check server logs in terminal
3. Restart server: Stop with Ctrl+C, then `python3 app.py`

## 📊 Reference Data

### Known Good Test Case
- **Input**: 1985年10月6日19時 (Year: 1985, Month: 10, Day: 6, Hour: 19)
- **Expected Output**: 乙丑 乙酉 戊寅 壬戌
- **API JSON**: `{"name": "測試", "year": 1985, "month": 10, "day": 6, "hour": 19}`

### Directory Structure Quick Reference
```
/home/runner/work/new-basu/new-basu/
├── pillar_engine.py          # Core calculation engine
├── app.py                    # Flask web application
├── requirements.txt          # Dependencies
├── test_engine.py           # Engine tests
├── smoke_tests.py           # Basic integration tests
├── enhanced_smoke_tests.py  # Advanced integration tests
├── deployment_status.py     # Deployment validator
├── static/                  # Web assets
├── templates/               # HTML templates
└── .github/                 # This instructions file
```

Remember: **Always validate your changes with the complete test suite before considering your work complete.**