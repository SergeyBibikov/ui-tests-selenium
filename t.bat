@echo off
rd /s /q output
pytest -n 2 -v -s -k "%1" --alluredir=output