@echo off
rd /s /q output
pytest -n 8 -v -s -k "%1" --alluredir=output