export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn credit/time -t -g -out timed_search_methods --f_score
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn credit/time -g -out timed_search_methods --f_score

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/time -t -g -out timed_search_methods_full --f_score
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn credit/time -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn credit/time -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn credit/time -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn credit/time -t -v -out timed_search_methods_full -pt --f_score
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn credit/time -v -out timed_search_methods_full -pt --f_score
