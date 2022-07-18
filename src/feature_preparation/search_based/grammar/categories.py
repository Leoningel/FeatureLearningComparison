
from abc import ABC
from typing import Union
from geneticengine.core.decorators import abstract


class Col(ABC):
    col_name = "No column name defined"
    
    def evaluate(self, **kwargs):
        return kwargs[self.col_name]
    
    def __str__(self, **kwargs):
        return f"\"{self.col_name}\""
    
class Category(ABC):
    category: Union[int,bool]
    column: Col

@abstract
class IntCategory(Category):
    category: int
    column: Col

@abstract
class BoolCategory(Category):
    category: int
    column: Col

   
class IBCategory(ABC):
    category1: int
    category2: int
    column: Col


