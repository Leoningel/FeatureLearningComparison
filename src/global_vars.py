DELIMITER = ','
TIME_COLUMN = "instant"
RESULTS_FOLDER = "./results/"
TEMP_RESULTS_FOLDER = "./results_temp/"
SPLITS = [ 0.5, 0.66, 0.83 ]
MAX_DEPTH = 12
ELITISMS = [ 1, 5 ]
NOVELTIES = [ 0, 20, 50, 100 ]
MUTATION_PROBS = [ 0.1, 0.25, 0.5, 0.6 ]
CROSSOVER_PROBS = [ 0.8, 0.9, 1 ]
POPULATION_SIZE = 200
TIME_LIMIT = 1200
N_SEEDS = 30   
TRAIN_PROPORTION = 0.75


# DATA_FILE = "data/boom_bikes_14-01-2022_without_casual_and_registered.csv"
# TARGET_COLUMN = 'cnt'
# SCORING = 'mse'

# DATA_FILE = "data/credit_g.csv"
# TARGET_COLUMN = 'target'
# SCORING = 'f_score'

# DATA_FILE = "data/caesarian.csv"
# TARGET_COLUMN = 'target'
# SCORING = 'f_score'

# DATA_FILE = "data/penguins.csv"
# TARGET_COLUMN = 'target'
# SCORING = 'f_score'

DATA_FILE = "data/flare.csv"
TARGET_COLUMN = 'target'
SCORING = 'f_score'

DATA_FILE = "data/cleve.csv"
TARGET_COLUMN = 'target'
SCORING = 'f_score'

DATA_FILE = "data/colic2.csv"
TARGET_COLUMN = 'target'
SCORING = 'f_score'

DATA_FILE = "data/colic3.csv"
TARGET_COLUMN = 'target'
SCORING = 'f_score'
