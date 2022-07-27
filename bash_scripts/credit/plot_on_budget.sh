export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



# run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn credit/time -t -g -out timed_search_methods
# run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn credit/time -g -out timed_search_methods

run_comparison.sh -fl 0 2 5 6 7 8 -m 0 --plot_data -fn credit/time -t -v -out timed_compare_w_classics -p 0 --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 0 --plot_data -fn credit/time -v -out timed_compare_w_classics -p 0 --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 1 --plot_data -fn credit/time -t -v -out timed_compare_w_classics -p 0 --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 1 --plot_data -fn credit/time -v -out timed_compare_w_classics -p 0 --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 2 --plot_data -fn credit/time -t -v -out timed_compare_w_classics -p 0 -o --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 2 --plot_data -fn credit/time -v -out timed_compare_w_classics -p 0 -o --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 3 --plot_data -fn credit/time -t -v -out timed_compare_w_classics -p 0 --f_score
run_comparison.sh -fl 0 2 5 6 7 8 -m 3 --plot_data -fn credit/time -v -out timed_compare_w_classics -p 0 --f_score

# run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/time -t -g -out timed_search_methods_full
# run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/time -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn credit/time -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn credit/time -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt
# run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn credit/time -v -out timed_search_methods_full -pt
