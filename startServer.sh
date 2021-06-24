#!/bin/bash

cd /home/pi/Pimoroni

export FLASK_APP=helloServer.py

flask run --host=0.0.0.0