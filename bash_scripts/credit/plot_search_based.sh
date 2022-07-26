export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



# run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/max_depth_12 --time -v -out search_methods_full -p 2 -o --f_score
# run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/max_depth_12 --nodes -g -out search_methods_full -p -1 -o --f_score

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn credit/max_depth_12 -g -out search_methods --f_score
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn credit/max_depth_12 -t -g -out search_methods --f_score

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/max_depth_12 -t -g -out search_methods_full --f_score
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/max_depth_12 -g -out search_methods_full --f_score
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/max_depth_12 -t -v -out search_methods_full -p 2 --f_score
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/max_depth_12 -v -out search_methods_full -p 2 --f_score
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn credit/max_depth_12 -t -v -out search_methods_full -p 2 --f_score
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn credit/max_depth_12 -v -out search_methods_full -p 2 --f_score
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn credit/max_depth_12 -t -v -out search_methods_full -p 2 -o --f_score
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn credit/max_depth_12 -v -out search_methods_full -p 2 -o --f_score
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn credit/max_depth_12 -t -v -out search_methods_full -p 2 --f_score
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn credit/max_depth_12 -v -out search_methods_full -p 2 --f_score
