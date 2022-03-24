
from abc import ABC
from dataclasses import dataclass
from typing import Annotated
from geneticengine.metahandlers.vars import VarRange

class Category(ABC):
    category: str
    column: str
    pass


class Col(ABC):
    def evaluate(self, **kwargs):
        return "x"

@dataclass
class SeasonCol(Col):
    feature_name: Annotated[str, VarRange(["season"])]
    
    def evaluate(self, **kwargs):
        return str(kwargs[self.feature_name])
    
    def __str__(self, **kwargs):
        return f"\"{self.feature_name}\""

@dataclass
class Season(Category):
    category: Annotated[str, VarRange([ "winter", "spring", "summer", "fall" ])]
    column: SeasonCol

    