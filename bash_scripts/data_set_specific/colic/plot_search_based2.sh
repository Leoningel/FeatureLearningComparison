export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic2 -g -out search_methods --f_score -of colic/colic2
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic2 -t -g -out search_methods --f_score -of colic/colic2

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic2 --time -v -out search_methods -p 2 -o -of colic/colic2
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic2 --nodes -g -out search_methods -p -1 -o -of colic/colic2
