export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 2 4 -m 0 --plot_data --nodes -g -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 0 1 2 3 --plot_data --time -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 0 --plot_data -t -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 0 --plot_data -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 1 --plot_data -t -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 1 --plot_data -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 2 --plot_data -t -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 2 --plot_data -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 3 --plot_data -t -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 3 --plot_data -v -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 0 --plot_data -t -g -out jb_gengy_depth_12 -p -1 -o $*
run_comparison.sh -fl 2 4 -m 0 --plot_data -g -out jb_gengy_depth_12 -p -1 -o $*

