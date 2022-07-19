export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python

function run_example {
    printf "Running $@..."
    $PYTHON_BINARY $@ > /dev/null && echo "(done)" || echo "(failed)"

}

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn bb/time -t -g -out timed_search_methods
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn bb/time -g -out timed_search_methods

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn bb/time -t -g -out timed_search_methods_full
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn bb/time -t -v -out timed_search_methods_full -pt
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn bb/time -v -out timed_search_methods_full -pt
