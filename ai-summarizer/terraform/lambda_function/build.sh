#!/bin/bash
cd $(dirname $0)  # Ensure script runs from its directory
pip install -r requirements.txt -t .
zip -r ../lambda_function.zip . -x "*.pyc" -x "*.DS_Store"
