from dataclasses import dataclass
from typing import Annotated
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory

"""
Did not categorize the following columns due to the large amount of zeros without documentation : 
    > temp_extremities (65 zeros)           - (27 zeros on colic2.csv)
    > peripheral_pulse (83 zeros) 
    > mucous_membranes (48 zeros)           - (18 zeros on colic2.csv)
    > capillary_refill_time (96 zeros)
    > peristalsis (52 zeros)                - (18 zeros on colic2.csv)
    > abdominal_distension (65 zeros)       - (26 zeros on colic2.csv)
    > nasogastric_tube (131 zeros)
    > nasogastric_reflux (45 zeros)         - (40 zeros on colic2.csv)
    > rectal_examination (128 zeros)
    > abdomen (143 zeros)
    > abdominocentesis_appearance (194 zeros)
    
Deleted the data points that pain, surgery and outcome were ZERO from the data set

"""


"""
surgery
1 = Yes, it had surgery
2 = It was treated without surgery
"""
@dataclass
class SurgeryCol(Col):
    col_name = "surgery"

    number_map = {
        1: "Treated with surgery",
        2: "Treated without surgery",
    }

@dataclass
class Surgery(IntCategory):
    category: Annotated[int, IntRange(1, 2)]
    column: SurgeryCol
    

"""
Age
1 = Adult horse 
2 = Young (< 6 months)
"""
@dataclass
class AgeCol(Col):
    col_name = "Age"

    number_map = {
        0: "Adult Horse",
        1: "Young Horse",
    }


@dataclass
class Age(IntCategory):
    category: Annotated[int, IntRange(0, 1)]
    column: AgeCol
    
    
"""
temp_extremities
1 = Normal
2 = Warm
3 = Cool
4 = Cold
"""
@dataclass
class TempExtremitiesCol(Col):
    col_name = "temp_extremities"

    number_map = {
        1: "Normal",
        2: "Warm",
        3: "Cool",
        4: "Cold",
    }


@dataclass
class TempExtremities(IntCategory):
    category: Annotated[int, IntRange(1, 4)]
    column: TempExtremitiesCol


""" 
mucous_membranes
1 = normal pink
2 = bright pink
3 = pale pink
4 = pale cyanotic
5 = bright red / injected
6 = dark cyanotic
"""
@dataclass
class MucousMembraneCol(Col):
    col_name = "mucous_membranes"

    number_map = {
        1: "Normal Pink",
        2: "Bright Pink",
        3: "Pale Pink",
        4: "Pale Cyanotic",
        5: "Bright Red / Injected",
        6: "Dark Cyanotic",
    }


@dataclass
class MucousMembrane(IntCategory):
    category: Annotated[int, IntRange(1, 6)]
    column: MucousMembraneCol

"""
peristalsis
1 = hypermotile
2 = normal
3 = hypomotile
4 = absent
"""
@dataclass
class PeristalsisCol(Col):
    col_name = "peristalsis"

    number_map = {
        1: "Hypermotile",
        2: "Normal",
        3: "Hypomotile",
        4: "Absent",
    }


@dataclass
class Peristalsis(IntCategory):
    category: Annotated[int, IntRange(1, 4)]
    column: PeristalsisCol

"""
abdominal_distension
1 = none
2 = slight
3 = moderate
4 = severe
"""
@dataclass
class AbdominalDistensionCol(Col):
    col_name = "abdominal_distension"

    number_map = {
        1: "None",
        2: "Slight",
        3: "Moderate",
        4: "Severe",
    }


@dataclass
class AbdominalDistension(IntCategory):
    category: Annotated[int, IntRange(1, 4)]
    column: AbdominalDistensionCol
    
    
"""
nasogastric_reflux
1 = none
2 = > 1 liter
3 = < 1 liter
"""
@dataclass
class NasogastricRefluxCol(Col):
    col_name = "nasogastric_reflux"

    number_map = {
        1: "None",
        2: "GT 1 Liter",
        3: "LT 1 Liter",
    }


@dataclass
class NasogastricReflux(IntCategory):
    category: Annotated[int, IntRange(1, 3)]
    column: NasogastricRefluxCol

"""
pain
1 = alert, no pain
2 = depressed
3 = intermittent mild pain
4 = intermittent severe pain
5 = continuous severe pain
"""
@dataclass
class PainCol(Col):
    col_name = "pain"

    number_map = {
        1 : "alert, no pain" ,
        2 : "depressed" ,
        3 : "intermittent mild pain",
        4 : "intermittent severe pain",
        5 : "continuous severe pain" ,
    }


@dataclass
class Pain(IntCategory):
    category: Annotated[int, IntRange(1, 5)]
    column: PainCol
    
"""
outcome
1 = lived
2 = died
3 = was euthanized
"""
@dataclass
class OutcomeCol(Col):
    col_name = "outcome"

    number_map = {
        1 : "lived",
        2 : "died" ,
        3 : "was euthanized",
    }


@dataclass
class Outcome(IntCategory):
    category: Annotated[int, IntRange(1, 3)]
    column: OutcomeCol
    
    
    
"""-----------------------------------------------------------------------------"""
categories = [Col, Category, BoolCategory, IntCategory,
            SurgeryCol, Surgery, AgeCol, Age, PainCol, Pain, OutcomeCol, Outcome, 
            TempExtremitiesCol, TempExtremities, MucousMembraneCol, MucousMembrane, PeristalsisCol, Peristalsis, 
            AbdominalDistensionCol, AbdominalDistension, NasogastricRefluxCol, NasogastricReflux]

special_features = {
    "surgery": Surgery,
    "Age": Age,
    "pain" : Pain,
    "outcome": Outcome,
    "temp_extremities": TempExtremities,
    "mucous_membranes": MucousMembrane,
    "peristalsis": Peristalsis,
    "abdominal_distension": AbdominalDistension,
    "nasogastric_reflux": NasogastricReflux,
    
}

ibs = []


