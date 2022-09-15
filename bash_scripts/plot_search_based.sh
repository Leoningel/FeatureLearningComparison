export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data --time -v -out search_methods_full -p 2 -o $*
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data --nodes -g -out search_methods_full -p -1 -o $*
run_comparison.sh -fl 0 1 2 -m 0 --plot_data --time -v -out search_methods -p 2 -o $*
run_comparison.sh -fl 0 1 2 -m 0 --plot_data --nodes -g -out search_methods -p -1 -o $*

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -t -g -out search_methods $*
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -g -out search_methods $*

run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -t -g -out search_methods_full $*
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -g -out search_methods_full $*
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -t -v -out search_methods_full -p 2 $*
run_comparison.sh -fl 0 1 2 3 -m 0 --plot_data -v -out search_methods_full -p 2 $*
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -t -v -out search_methods_full -p 2 $*
run_comparison.sh -fl 0 1 2 3 -m 1 --plot_data -v -out search_methods_full -p 2 $*
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -t -v -out search_methods_full -p 2 -o $*
run_comparison.sh -fl 0 1 2 3 -m 2 --plot_data -v -out search_methods_full -p 2 -o $*
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -t -v -out search_methods_full -p 2 $*
run_comparison.sh -fl 0 1 2 3 -m 3 --plot_data -v -out search_methods_full -p 2 $*
