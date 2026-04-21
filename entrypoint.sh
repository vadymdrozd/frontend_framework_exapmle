#!/bin/bash
echo "GUI tests start..."
source ./venv/bin/activate
export REVISION=$(date +'%F')
# sleep infinity
python -m pytest . --alluredir allure-results/${REVISION}
