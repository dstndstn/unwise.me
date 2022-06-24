#!/bin/bash
cd /app/unwise.me
export PYTHONPATH=$PYTHONPATH:/usr/local/astrometry/lib/python:$(pwd)
uwsgi --touch-reload wsgi.py --socket 0.0.0.0:3030 --processes 4 --wsgi-file wsgi.py
