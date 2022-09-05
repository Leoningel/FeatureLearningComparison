from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory


@dataclass
class ClassCCol(Col):
    col_name = "class code"
    
    number_map = {
        0 : "A",
        1 : "B",
        2 : "C",
        3 : "D",
        4 : "E",
        5 : "F",
    }

@dataclass
class ClassC(IntCategory):
    category: Annotated[int, IntRange( 0, 5 )]
    column: ClassCCol

@dataclass
class LargestSpotCol(Col):
    col_name = "largest spot code"
    
    number_map = {
        0 : "X",
        1 : "R",
        2 : "S",
        3 : "A",
        4 : "H",
        5 : "K",
    }

@dataclass
class LargestSpot(IntCategory):
    category: Annotated[int, IntRange( 0, 5 )]
    column: LargestSpotCol

@dataclass
class SpotDistCol(Col):
    col_name = "largest spot code"
    
    number_map = {
        0 : "X",
        1 : "O",
        2 : "I",
        3 : "C",
    }

@dataclass
class SpotDist(IntCategory):
    category: Annotated[int, IntRange( 0, 3 )]
    column: SpotDistCol


class ActivityCol(Col):
    col_name = "Activity"

    r_map = {
        1 : "reduced",
        2 : "unchanged",
    }
    
@dataclass
class Activity(BoolCategory):
    category: Annotated[int, IntRange( 1, 2 )]
    column: ActivityCol

class EvolutionCol(Col):
    col_name = "Evolution"

    r_map = {
        1 : "decay",
        2 : "no growth",
        3 : "growth",
    }
    
@dataclass
class Evolution(BoolCategory):
    category: Annotated[int, IntRange( 1, 3 )]
    column: EvolutionCol

class Previous24Col(Col):
    col_name = "Previous 24 hour code"

    r_map = {
        1 : "< M1",
        2 : "M1",
        3 : "> M1",
    }
    
@dataclass
class Previous24(BoolCategory):
    category: Annotated[int, IntRange( 1, 3 )]
    column: Previous24Col

class HistoricallyComplexCol(Col):
    col_name = "Historically-complex"

    r_map = {
        1 : "Yes",
        2 : "No",
    }
    
@dataclass
class HistoricallyComplex(BoolCategory):
    category: Annotated[int, IntRange( 1, 2 )]
    column: HistoricallyComplexCol

class BecomeHistComplexCol(Col):
    col_name = "become complex"

    r_map = {
        1 : "Yes",
        2 : "No",
    }
    
@dataclass
class BecomeHistComplex(BoolCategory):
    category: Annotated[int, IntRange( 1, 2 )]
    column: BecomeHistComplexCol

class AreaCol(Col):
    col_name = "Area"

    r_map = {
        1 : "small",
        2 : "large",
    }
    
@dataclass
class Area(BoolCategory):
    category: Annotated[int, IntRange( 1, 2 )]
    column: AreaCol

class AreaLargestSpotCol(Col):
    col_name = "Area of the largest spot"

    r_map = {
        1 : "< 5",
        2 : "> 5",
    }
    
@dataclass
class AreaLargestSpot(BoolCategory):
    category: Annotated[int, IntRange( 1, 2 )]
    column: AreaLargestSpotCol
    


categories = [ Col, Category, BoolCategory, IntCategory, ClassC, ClassCCol, LargestSpot, LargestSpotCol, SpotDist, SpotDistCol, Activity, ActivityCol, Evolution, EvolutionCol, Previous24, Previous24Col, HistoricallyComplex, HistoricallyComplexCol, BecomeHistComplex, BecomeHistComplexCol, Area, AreaCol, AreaLargestSpot, AreaLargestSpotCol ]

 
##-------------------------
# Should be implemented differently once dependent types are included in Genetic Engine
##-------------------------

special_features = {
    "class code"            	: ClassC,
    "largest spot code"     	: LargestSpot,
    "spot dist code"        	: SpotDist,
    "Activity"                  : Activity,
    "Evolution"                 : Evolution,
    "Previous 24 hour code"     : Previous24,
    "Historically-complex"      : HistoricallyComplex,
    "become complex"            : BecomeHistComplex,
    "Area"                      : Area,
    "Area of the largest spot"  : AreaLargestSpot,
}


@dataclass
class EvolutionIB(IBCategory):
    category1: Annotated[int, IntRange( 1, 3 )]
    category2: Annotated[int, IntRange( 1, 3 )]
    column: EvolutionCol

@dataclass
class Previous24IB(IBCategory):
    category1: Annotated[int, IntRange( 1, 3 )]
    category2: Annotated[int, IntRange( 1, 3 )]
    column: Previous24Col

ibs = [ EvolutionIB, Previous24 ]
