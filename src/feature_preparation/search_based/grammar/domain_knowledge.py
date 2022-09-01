import global_vars as gv

from feature_preparation.search_based.grammar.domain_specificities.boom_bikes import (
    special_features as bb_special_features,
    ibs as bb_ibs,
)
from feature_preparation.search_based.grammar.domain_specificities.credit_g import (
    special_features as credit_special_features,
    ibs as credit_ibs,
)
from feature_preparation.search_based.grammar.domain_specificities.caesarian import (
    special_features as caesarian_special_features,
    ibs as caesarian_ibs,
)
from feature_preparation.search_based.grammar.domain_specificities.penguins import (
    special_features as penguins_special_features,
    ibs as penguins_ibs,
)



if gv.DATA_FILE == 'data/penguins.csv':
    special_features = penguins_special_features
    ibs = penguins_ibs
elif gv.DATA_FILE == 'data/caesarian.csv':
    special_features = caesarian_special_features
    ibs = caesarian_ibs
elif gv.DATA_FILE == 'data/credit_g.csv':
    special_features = credit_special_features
    ibs = credit_ibs
else:
    special_features = bb_special_features
    ibs = bb_ibs
