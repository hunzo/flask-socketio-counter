#!/bin/bash
APP_PORT=${PORT:-5000}

/opt/venv/bin/gunicorn main:app --worker-class gevent --bind "0.0.0.0:${APP_PORT}" -w 1 
