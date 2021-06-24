#!/bin/bash

PINGS=2
TESTIP=8.8.8.8

if ( ping -c $PINGS $TESTIP > /dev/null ) then
    echo "you are online"

    cd /home/pi/InkyPyProj
    sudo git remote add upstream https://github.com/Charliezhu5/InkyPyProj.git
    sudo git pull upstream master

    export FLASK_APP=helloServer.py

    flask run --host=0.0.0.0
else
    echo "you are offline, will try again after 30s"
    sleep 30
    if ( ping -c $PINGS $TESTIP > /dev/null ) then
        echo "you are online"
        cd /home/pi/InkyPyProj
        sudo git remote add upstream https://github.com/Charliezhu5/InkyPyProj.git
        sudo git pull upstream master

        export FLASK_APP=helloServer.py

        flask run --host=0.0.0.0
    else
        echo "Internet issue, can't initiate functions."
    fi
fi
