#!/bin/bash
#SBATCH --job-name=leon_ingelse_thesis  # Job name
#SBATCH --nodes=1                       # Run all processes on a single node	
#SBATCH --ntasks=1                      # Run a single task		
#SBATCH --cpus-per-task=1               # Number of CPU cores per task
#SBATCH --mem=1gb                       # Job memory request
#SBATCH --time=48:00:00                 # Time limit hrs:min:sec
#SBATCH --output=logs/parallel_%j.log   # Standard output and error log

#SBATCH --array=0-539                   # iterate values between 0 and 59, inclusive

bash setup.sh
python src/run_single.py -s $(expr $SLURM_ARRAY_TASK_ID % 30) -f $(expr $SLURM_ARRAY_TASK_ID / 120) -m $(expr $(expr $SLURM_ARRAY_TASK_ID / 30) % 4) $*