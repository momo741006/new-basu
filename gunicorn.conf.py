# 虹靈御所八字人生兵法系統 - Gunicorn配置
import os

# 服務器套接字
bind = f"0.0.0.0:{os.environ.get('PORT', '5000')}"
backlog = 2048

# 工作進程配置
workers = int(os.environ.get('WEB_CONCURRENCY', 2))
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 2

# 重啟設置
max_requests = 1000
max_requests_jitter = 50
preload_app = True

# 日誌配置
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# 進程命名
proc_name = "bazi_system"

# 安全設置
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# 性能優化
def when_ready(server):
    server.log.info("🌈 虹靈御所八字人生兵法系統 Gunicorn服務器準備就緒")

def worker_int(worker):
    worker.log.info("⚠️ Worker收到中斷信號")

def on_exit(server):
    server.log.info("🔚 虹靈御所八字系統服務器關閉")