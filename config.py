from os import environ

PORT = int(environ.get("PORT", 8081))
DEBUG_MODE = int(environ.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)
workers = 1
threads = 1
