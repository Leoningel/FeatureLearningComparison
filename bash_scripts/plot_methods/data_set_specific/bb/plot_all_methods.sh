export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 2 5 6 7 8 -m 0 --plot_data -fn bb/max_depth_12 -t -v -out compare_w_classics -p 0 -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 0 --plot_data -fn bb/max_depth_12 -v -out compare_w_classics -p 0 -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 1 --plot_data -fn bb/max_depth_12 -t -v -out compare_w_classics -p 0 -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 1 --plot_data -fn bb/max_depth_12 -v -out compare_w_classics -p 0 -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 2 --plot_data -fn bb/max_depth_12 -t -v -out compare_w_classics -p 0 -o -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 2 --plot_data -fn bb/max_depth_12 -v -out compare_w_classics -p 0 -o -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 3 --plot_data -fn bb/max_depth_12 -t -v -out compare_w_classics -p 0 -of bb/all_methods
run_comparison.sh -fl 0 2 5 6 7 8 -m 3 --plot_data -fn bb/max_depth_12 -v -out compare_w_classics -p 0 -of bb/all_methods
