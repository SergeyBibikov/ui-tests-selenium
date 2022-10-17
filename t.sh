#! /bin/bash
rm -rf output
pytest -n 6 -v -s -k "$1" --alluredir=output --reruns 3