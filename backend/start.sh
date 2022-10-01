#!/usr/bin/env bash

python init-sql.py

python -m flask run --host=0.0.0.0
