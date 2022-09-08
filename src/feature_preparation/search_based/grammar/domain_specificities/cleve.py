from dataclasses import dataclass
from typing import Annotated
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory


@dataclass
class SexCol(Col):
    col_name = "Sex"

    number_map = {
        0: "female",
        1: "male",
    }

@dataclass
class Sex(IntCategory):
    category: Annotated[int, IntRange(0, 1)]
    column: SexCol
    

@dataclass
class ChestPainCol(Col):
    col_name = "Chest pain type"

    number_map = {
        0: "typical angina",
        1: "atypical angina",
        2: "non-anginal pain",
        3: "asymptomatic",
    }

@dataclass
class ChestPain(IntCategory):
    category: Annotated[int, IntRange(0, 3)]
    column: ChestPainCol
    
    
# The answers were 0-No , 1-Yes  so I treted this as a bool 
@dataclass
class ExerciseInducedAnginaCol(Col):
    col_name = "Exercise induced angina"

@dataclass
class ExerciseInducedAngina(BoolCategory):
    category: Annotated[int, IntRange(0, 1)]
    column: ExerciseInducedAnginaCol
    

@dataclass
class SlopeCol(Col):
    col_name = "Slope"
    
    number_map = {
        0: "upsloping",
        1: "flat",
        2: "downsloping",
    }


@dataclass
class Slope(IntCategory):
    category: Annotated[int, IntRange(0, 2)]
    column: SlopeCol
    
    
#The answers are 1,2,3, but the documentation has different value, 3 = normal; 6 = fixed defect; 7 = reversable defect
#I assume that 1=3 , 2=6, 3=7 
@dataclass
class ThalCol(Col):
    col_name = "Thal"

    number_map = {
        1: "normal",
        2: "fixed defect",
        3: "reversable defect",
    }


@dataclass
class Thal(IntCategory):
    category: Annotated[int, IntRange(1, 3)]
    column: ThalCol
    

@dataclass
class FastingBloodSugarCol(Col):
    col_name = "Fasting blood sugar gt 120"


@dataclass
class FastingBloodSugar(BoolCategory):
    category: Annotated[int, IntRange(0, 1)]
    column: FastingBloodSugarCol

    
categories = [Col, Category, BoolCategory, IntCategory, 
            Sex, SexCol, ChestPain, ChestPainCol, ExerciseInducedAngina, ExerciseInducedAnginaCol, 
            Slope, SlopeCol, ThalCol, Thal, FastingBloodSugarCol, FastingBloodSugar]

special_features = {
    "Sex": Sex,
    "Chest pain type": ChestPain,
    "Exercise induced angina": ExerciseInducedAngina,
    "Slope": Slope,
    "Thal": Thal,
    "Fasting blood sugar gt 120" :FastingBloodSugar,
}

ibs = [ ]
