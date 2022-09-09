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
from feature_preparation.search_based.grammar.domain_specificities.flare import (
    special_features as flare_special_features,
    ibs as flare_ibs,
)
from feature_preparation.search_based.grammar.domain_specificities.cleve import (
    special_features as cleve_special_features,
    ibs as cleve_ibs,
)

from feature_preparation.search_based.grammar.domain_specificities.colic import (
    special_features as colic_special_features,
    ibs as colic_ibs,
)


class DomainKnowledge():
    def __init__(self) -> None:
        if gv.DATA_FILE == 'data/penguins.csv':
            self.special_features = penguins_special_features
            self.ibs = penguins_ibs
        if gv.DATA_FILE == 'data/flare.csv':
            self.special_features = flare_special_features
            self.ibs = flare_ibs
        elif gv.DATA_FILE == 'data/caesarian.csv':
            self.special_features = caesarian_special_features
            self.ibs = caesarian_ibs
        elif gv.DATA_FILE == 'data/credit_g.csv':
            self.special_features = credit_special_features
            self.ibs = credit_ibs
        elif gv.DATA_FILE == 'data/cleve.csv':
            self.special_features = cleve_special_features
            self.ibs = cleve_ibs
        elif gv.DATA_FILE == 'data/colic/colic2.csv':
            self.special_features = colic_special_features
            self.ibs = colic_ibs
        elif gv.DATA_FILE == 'data/colic/colic3.csv':
            self.special_features = colic_special_features
            self.ibs = colic_ibs
        else:
            self.special_features = bb_special_features
            self.ibs = bb_ibs
