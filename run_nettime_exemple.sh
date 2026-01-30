#!/bin/bash

cd path/to/nettimer

source .venv/bin/activate

python main.py >> nettime.log 2>&1
