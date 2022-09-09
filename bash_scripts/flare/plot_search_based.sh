export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare/max_depth_12 -g -out search_methods --f_score -of flare
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare/max_depth_12 -t -g -out search_methods --f_score -of flare

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare/max_depth_12 --time -v -out search_methods -p 2 -o -of flare
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare/max_depth_12 --nodes -g -out search_methods -p -1 -o -of flare