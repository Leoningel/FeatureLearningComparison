export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn penguins -g -out search_methods --f_score -of penguins
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn penguins -t -g -out search_methods --f_score -of penguins

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn penguins --time -v -out search_methods -p 2 -o -of penguins
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn penguins --nodes -g -out search_methods -p -1 -o -of penguins
