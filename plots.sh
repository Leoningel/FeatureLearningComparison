export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python

function run_example {
    printf "Running $@..."
    $PYTHON_BINARY $@ > /dev/null && echo "(done)" || echo "(failed)"

}

run_comparison.sh -fl 2 4 -m 0 1 --plot_data -fn franklin -t -v -out jb_gengy_dt_rf -p -1
run_comparison.sh -fl 2 4 -m 0 1 --plot_data -fn franklin -v -out jb_gengy_dt_rf -p -1
run_comparison.sh -fl 2 4 -m 2 --plot_data -fn franklin -t -v -out jb_gengy_mlp -p -1
run_comparison.sh -fl 2 4 -m 2 --plot_data -fn franklin -v -out jb_gengy_mlp -p -1
run_comparison.sh -fl 2 4 -m 3 --plot_data -fn franklin -t -v -out jb_gengy_svm -p -1
run_comparison.sh -fl 2 4 -m 3 --plot_data -fn franklin -v -out jb_gengy_svm -p -1
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn franklin -t -g -out jb_gengy -p -1
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn franklin -g -out jb_gengy -p -1

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn franklin -t -g -out search_methods
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn franklin -g -out search_methods

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn franklin -t -g -out search_methods_full
run_comparison.sh -fl 0 1 2 3 5 -m 0 --plot_data -fn franklin -g -out search_methods_full
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn franklin -t -v -out search_methods_full
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -fn franklin -v -out search_methods_full

run_comparison.sh -fl 0 5 6 7 8 -m 0 --plot_data -fn franklin -t -v -out compare_w_classics -p 0
run_comparison.sh -fl 0 5 6 7 8 -m 0 --plot_data -fn franklin -v -out compare_w_classics -p 0
