export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare -g -out search_methods --f_score -of flare
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare -t -g -out search_methods --f_score -of flare

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare --time -v -out search_methods -p 2 -o -of flare
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn flare --nodes -g -out search_methods -p -1 -o -of flare
