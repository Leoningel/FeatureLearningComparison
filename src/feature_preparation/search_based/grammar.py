from abc import ABC
from dataclasses import dataclass
from typing import Annotated, List
import numpy as np

from geneticengine.metahandlers.lists import ListSizeBetween
from geneticengine.metahandlers.vars import VarRange
from geneticengine.core.decorators import abstract

class Solution(ABC):
    def evaluate(self, **kwargs) -> float:
        return lambda _: 0

@dataclass
class FeatureSet(Solution):
    subset: Annotated[List[Solution], ListSizeBetween(1, 2)]
    
    def evaluate(self, **kwargs):
        return [ el.evaluate(**kwargs) for el in self.subset ]

    def __str__(self, **kwargs):
        s = "["
        for feat in self.subset:
            s += str(feat) + ","
        s = s[:-1] + "]"
        return s

class BuildingBlock(ABC):
    def evaluate(self, **kwargs):
        return 0

@dataclass
class EngineeredFeature(Solution):
    blocks: BuildingBlock
    
    def evaluate(self, **kwargs):
        return self.blocks.evaluate(**kwargs)

    def __str__(self, **kwargs):
        return f"{self.blocks}"
    
    
@dataclass
class Var(BuildingBlock):
    feature_name: Annotated[str, VarRange(["x" , "y"])]
    
    def evaluate(self, **kwargs):
        return kwargs[self.feature_name]
    
    def __str__(self, **kwargs):
        return f"\"{self.feature_name}\""

@dataclass
class Plus(BuildingBlock):
    left: BuildingBlock
    right: BuildingBlock
    
    def evaluate(self, **kwargs):
        return self.left.evaluate(**kwargs) + self.right.evaluate(**kwargs)
    
    def __str__(self, **kwargs):
        return f"({self.left} + {self.right})"    

@dataclass
class Minus(BuildingBlock):
    left: BuildingBlock
    right: BuildingBlock
    
    def evaluate(self, **kwargs):
        return self.left.evaluate(**kwargs) - self.right.evaluate(**kwargs)
    
    def __str__(self, **kwargs):
        return f"({self.left} - {self.right})"    

@dataclass
class Mult(BuildingBlock):
    left: BuildingBlock
    right: BuildingBlock
    
    def evaluate(self, **kwargs):
        return self.left.evaluate(**kwargs) * self.right.evaluate(**kwargs)
    
    def __str__(self, **kwargs):
        return f"({self.left} * {self.right})"    

@dataclass
class SafeDiv(BuildingBlock):
    left: BuildingBlock
    right: BuildingBlock
    
    def evaluate(self, **kwargs):
        d1 = self.left.evaluate(**kwargs)
        d2 = self.right.evaluate(**kwargs)
        try:
            with np.errstate(divide="ignore", invalid="ignore"):
                return np.where(d2 == 0, np.ones_like(d1), d1 / d2)
        except ZeroDivisionError:
            # In this case we are trying to divide two constants, one of which is 0
            # Return a constant.
            return 1.0
    
    
    def __str__(self, **kwargs):
        return f"({self.left} / {self.right})"    

