from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory


@dataclass
class DeliveryTimeCol(Col):
    col_name = "Delivery time"
    
    number_map = {
        1 : "Prematurely",
        2 : "Timely",
        3 : "Latecomer",
    }

@dataclass
class DeliveryTime(IntCategory):
    category: Annotated[int, IntRange( 1, 3 )]
    column: DeliveryTimeCol


@dataclass
class BloodCol(Col):
    col_name = "Blood of Pressure"
    
    number_map = {
        0   : "Low",
        1   : "Normal",
        2   : "High",
    }

@dataclass
class Blood(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: BloodCol

@dataclass
class HeartProblemCol(Col):
    col_name = "Heart Problem"
    
@dataclass
class HeartProblem(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: HeartProblemCol


categories = [ Col, Category, BoolCategory, IntCategory, DeliveryTime, DeliveryTimeCol, Blood, BloodCol, HeartProblem, HeartProblemCol ]

 
##-------------------------
# Should be implemented differently once dependent types are included in Genetic Engine
##-------------------------

@dataclass
class DeliveryTimeIB(IBCategory):
    category1: Annotated[int, IntRange( 1, 3 )]
    category2: Annotated[int, IntRange( 1, 3 )]
    column: DeliveryTimeCol

    
@dataclass
class BloodIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 2 )]
    category2: Annotated[int, IntRange( 0, 2 )]
    column: BloodCol


inbetween_categories = [ IBCategory, DeliveryTimeIB, BloodIB ]

    
special_features = {
    "Delivery time"         : DeliveryTime,
    "Blood of Pressure"     : Blood,
    "Heart Problem"         : HeartProblem,
}

ibs = [ DeliveryTimeIB, BloodIB ]
