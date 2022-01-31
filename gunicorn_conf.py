import multiprocessing as mp
import os

_workers = mp.cpu_count() * 2 + 1

# GUNICORN SETTINGS
# +info at https://docs.gunicorn.org/en/stable/settings.html

# activates log
# accesslog="-" 
# errorlog="-"

# workers configurations
workers = os.getenv("WORKERS", _workers)
worker_class = os.getenv("WORKER_CLASS", "gevent")
worker_connections = os.getenv("WORKER_CONNECTIONS", 1000)

# timeouts
timeout=os.getenv("TIMEOUT", "60")

# listen address
bind = os.getenv("DJANGO_LISTEN", "127.0.0.1:8000")
# prom_port = os.getenv("PROM_PORT", "8001")
