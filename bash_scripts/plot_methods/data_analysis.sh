export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH};}./src"

python src/data_analysis/wv_analysis.py
python src/data_analysis/cg_analysis.py
python src/data_analysis/bb_analysis.py
