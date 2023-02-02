# Feature Learning Methods Comparison
## Setup

Run the setup file: ``./setup.sh``.

## Choose example to run

In ``./src/global_vars.py`` you can choose one of the examples to run by changing the parameter NAME.

## Steps to run the different models

Execute the run comparisons file: ``./run_comparison.sh``.

Specify that you want to run the models and/or plot the data: ``./run_comparison.sh --run_models --plot_data``.
 
If you want to run all the seeds in parallel, you can run the ``./parallel_comparison.sh`` script.

## Steps to plot the figures

Execute the ``plot_all.sh`` file in the bash script folder for each example. For example, for the Boom Bikes example, the results are in the bb folder. Making sure the output folder exists in the plots folder (in the case, say, bb), we can run:

``bash bash_scripts/plot_all.sh -fn bb -of bb``

Or run ```generate_all_plots.sh`` to generate all plots.
