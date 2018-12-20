#!/bin/bash
cd /opt/calendario
source venv/bin/activate
cd /opt/calendario/calendario
gunicorn calendario.wsgi -t 600 -b 127.0.0.1:8002 -w 6 --user=servidor --group=servidor --log-file=/opt/calendario/gunicorn.log 2>>/opt/calendario/gunicorn.log

