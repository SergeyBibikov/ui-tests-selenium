@echo off
set HEADLESS=0
pytest -v -s -k "%1"