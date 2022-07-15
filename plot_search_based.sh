export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python

function run_example {
    printf "Running $@..."
    $PYTHON_BINARY $@ > /dev/null && echo "(done)" || echo "(failed)"

}

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn franklin -t -g -out search_methods
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn franklin -g -out search_methods

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn franklin -t -g -out search_methods_full
run_comparison.sh -fl 0 1 2 3 5 -m 0 --plot_data -fn franklin -g -out search_methods_full
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn franklin -t -v -out search_methods_full
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn franklin -v -out search_methods_full
