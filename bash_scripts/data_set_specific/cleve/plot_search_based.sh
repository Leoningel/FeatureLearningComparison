export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn cleve -g -out search_methods --f_score -of cleve
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn cleve -t -g -out search_methods --f_score -of cleve

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn cleve --time -v -out search_methods -p 2 -o -of cleve
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn cleve --nodes -g -out search_methods -p -1 -o -of cleve
