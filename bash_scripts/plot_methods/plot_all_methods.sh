export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 3 7 8 -m 0 --plot_data -t -v -out compare_w_classics -p 0 $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 0 --plot_data -v -out compare_w_classics -p 0 $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 1 --plot_data -t -v -out compare_w_classics -p 0 $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 1 --plot_data -v -out compare_w_classics -p 0 $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 2 --plot_data -t -v -out compare_w_classics -p 0 -o $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 2 --plot_data -v -out compare_w_classics -p 0 -o $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 3 --plot_data -t -v -out compare_w_classics -p 0 $*
run_comparison.sh -fl 0 1 2 3 7 8 -m 3 --plot_data -v -out compare_w_classics -p 0 $*
