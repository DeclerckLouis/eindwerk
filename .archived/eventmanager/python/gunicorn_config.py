import os

# Number of worker processes (this should generally be 2n+1, where n is the number of CPU cores)
workers = int(os.getenv('GUNICORN_WORKERS', '3'))

# Number of threads per worker process
threads = int(os.getenv('GUNICORN_THREADS', '2'))

# The socket to bind to (this can be an IP address and port number or a Unix socket)
bind = os.getenv('GUNICORN_BIND', '0.0.0.0:5000')

# The maximum number of simultaneous clients that each worker process can handle
worker_connections = int(os.getenv('GUNICORN_WORKER_CONNECTIONS', '1000'))

# The type of worker processes to use
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'sync') # Setting this to Sync means that every worker process will handle one request at a time

# The maximum number of requests a worker process will handle before being restarted
max_requests = int(os.getenv('GUNICORN_MAX_REQUESTS', '1000'))

# Whether to daemonize the Gunicorn process
daemon = os.getenv('GUNICORN_DAEMON', 'False').lower() in ['true', 'yes', '1']