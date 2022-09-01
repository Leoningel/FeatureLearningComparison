from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory


@dataclass
class IslandCol(Col):
    col_name = "island"
    
    number_map = {
        0 : "Biscoe",
        1 : "Dream",
        2 : "Torgersen",
    }

@dataclass
class Island(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: IslandCol


class SexCol(Col):
    col_name = "sex"
    
@dataclass
class Sex(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: SexCol


categories = [ Col, Category, BoolCategory, IntCategory, Island, IslandCol, Sex, SexCol ]

 
##-------------------------
# Should be implemented differently once dependent types are included in Genetic Engine
##-------------------------

special_features = {
    "island"        : Island,
    "sex"           : Sex,
}

ibs = [ ]
