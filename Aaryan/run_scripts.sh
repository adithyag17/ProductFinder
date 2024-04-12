#!/bin/sh

python3 final_scraper.py &

PID=$!

sleep 2700

kill $PID

python3 searcher.py
