
from abc import ABC
from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.vars import VarRange
from geneticengine.metahandlers.ints import IntRange


class Col(ABC):
    def evaluate(self, **kwargs):
        return "x"

class Category(ABC):
    category: Union[str,int, bool]
    column: Col

@dataclass
class SeasonCol(Col):
    feature_name: Annotated[str, VarRange(["season"])]
    
    def evaluate(self, **kwargs):
        return kwargs[self.feature_name]
    
    def __str__(self, **kwargs):
        return f"\"{self.feature_name}\""

@dataclass
class Season(Category):
    category: Annotated[str, VarRange([ "winter", "spring", "summer", "fall" ])]
    column: SeasonCol

@dataclass
class HolidayCol(Col):
    feature_name: Annotated[str, VarRange(["holiday"])]
    
    def evaluate(self, **kwargs):
        return kwargs[self.feature_name]
    
    def __str__(self, **kwargs):
        return f"\"{self.feature_name}\""

@dataclass
class Holiday(Category):
    category: Annotated[int, IntRange( 0, 1 )]
    column: HolidayCol

    