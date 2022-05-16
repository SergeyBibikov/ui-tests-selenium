#! /bin/bash
rm -rf output
pytest -n 8 -v -s -k "$1" --alluredir=output