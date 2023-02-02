#!/bin/bash
python3 -m pip install -r requirements.txt
# mkdir logs
mkdir plots
mkdir results
mkdir results_temp

# bash run_comparison.sh --clean_results --dest=bb
# bash run_comparison.sh --clean_results --dest=caesarian
# bash run_comparison.sh --clean_results --dest=cleve
# bash run_comparison.sh --clean_results --dest=colic
# bash run_comparison.sh --clean_results --dest=credit
# bash run_comparison.sh --clean_results --dest=web_visits
mkdir plots/bb
mkdir plots/caesarian
mkdir plots/cleve
mkdir plots/colic
mkdir plots/credit
mkdir plots/web_visits
