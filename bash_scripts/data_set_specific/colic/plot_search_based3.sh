export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic3 -g -out search_methods --f_score -of colic/colic3
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic3 -t -g -out search_methods --f_score -of colic/colic3

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic3 --time -v -out search_methods -p 2 -o -of colic/colic3
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn colic/colic3 --nodes -g -out search_methods -p -1 -o -of colic/colic3
