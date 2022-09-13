export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn caesarian -g -out search_methods --f_score -of caesarian
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn caesarian -t -g -out search_methods --f_score -of caesarian

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn caesarian --time -v -out search_methods -p 2 -o -of caesarian
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn caesarian --nodes -g -out search_methods -p -1 -o -of caesarian
