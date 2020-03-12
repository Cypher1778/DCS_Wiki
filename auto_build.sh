#!/bin/sh

if [ ! -d .venv ]; then
    python3 -m venv .venv
    . .venv/bin/activate
    pip install --upgrade pip
    pip install -r ./requirements.txt
fi

. .venv/bin/activate

mkdocs serve
