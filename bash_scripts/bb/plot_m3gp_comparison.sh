export PYTHONPATH="${PYTHONPATH:+${PYTHONPATH}:}."

PYTHON_BINARY=python



run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_12 --nodes -g -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 0 1 2 3 --plot_data -fn bb/max_depth_12 --time -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_12 -t -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_12 -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 1 --plot_data -fn bb/max_depth_12 -t -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 1 --plot_data -fn bb/max_depth_12 -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 2 --plot_data -fn bb/max_depth_12 -t -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 2 --plot_data -fn bb/max_depth_12 -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 3 --plot_data -fn bb/max_depth_12 -t -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 3 --plot_data -fn bb/max_depth_12 -v -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_12 -t -g -out jb_gengy_depth_12 -p -1 -o
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_12 -g -out jb_gengy_depth_12 -p -1 -o

run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_7 -t -g -out jb_gengy_depth_7 -p -1 -o
run_comparison.sh -fl 2 4 -m 0 --plot_data -fn bb/max_depth_7 -g -out jb_gengy_depth_7 -p -1 -o
