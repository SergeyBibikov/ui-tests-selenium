@echo off
set HEADLESS=1
pytest -v -s -k "%1"