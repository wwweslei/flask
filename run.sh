#!/bin/bash
source //home/weslei/Projects/FlaskSite/.env_flask/bin/activate.fish
python wsgi.py & 
sleep 2
firefox http://0.0.0.0:8000/



