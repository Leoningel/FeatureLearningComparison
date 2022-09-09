export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn bb/time -t -g -out timed_search_methods -of bb/on_budget
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn bb/time -g -out timed_search_methods -of bb/on_budget

run_comparison.sh -fl 0 2 5 6 7 8 -m 0 --plot_data -fn bb/time -t -v -out timed_compare_w_classics -p 0 -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 0 --plot_data -fn bb/time -v -out timed_compare_w_classics -p 0 -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 1 --plot_data -fn bb/time -t -v -out timed_compare_w_classics -p 0 -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 1 --plot_data -fn bb/time -v -out timed_compare_w_classics -p 0 -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 2 --plot_data -fn bb/time -t -v -out timed_compare_w_classics -p 0 -o -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 2 --plot_data -fn bb/time -v -out timed_compare_w_classics -p 0 -o -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 3 --plot_data -fn bb/time -t -v -out timed_compare_w_classics -p 0 -of bb/on_budget
run_comparison.sh -fl 0 2 5 6 7 8 -m 3 --plot_data -fn bb/time -v -out timed_compare_w_classics -p 0 -of bb/on_budget

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn bb/time -t -g -out timed_search_methods_full -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn bb/time -t -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn bb/time -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn bb/time -t -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -fn bb/time -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn bb/time -t -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -fn bb/time -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn bb/time -t -v -out timed_search_methods_full -pt -of bb/on_budget
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -fn bb/time -v -out timed_search_methods_full -pt -of bb/on_budget
