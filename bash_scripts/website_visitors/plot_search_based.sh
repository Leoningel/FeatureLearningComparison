export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn website_visitors -g -out search_methods --f_score -of website_visitors
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn website_visitors -t -g -out search_methods --f_score -of website_visitors

run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn website_visitors --time -v -out search_methods -p 2 -o -of website_visitors
run_comparison.sh -fl 0 1 2 -m 0 --plot_data -fn website_visitors --nodes -g -out search_methods -p -1 -o -of website_visitors
