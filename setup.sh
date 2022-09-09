#!/bin/bash
python3 -m pip install -r requirements.txt
mkdir logs
mkdir plots
mkdir results
mkdir results_temp
bash run_comparison.sh --clean_results --dest=-