from abc import ABC
from dataclasses import dataclass
from typing import Annotated, List

from GeneticEngine.geneticengine.metahandlers.lists import ListSizeBetween
from GeneticEngine.geneticengine.metahandlers.vars import VarRange
from GeneticEngine.geneticengine.core.decorators import abstract

class Solution(ABC):
    def evaluate(self, **kwargs) -> float:
        return lambda _: 0

@dataclass
class FeatureSet(Solution):
    subset: Annotated[List[Solution], ListSizeBetween(1, 2)]
    
    def evaluate(self, **kwargs):
        return lambda x: [ el.evaluate()(x) for el in self.subset ]

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
        return lambda x: x.append(self.blocks.evaluate())
    
    
@dataclass
class Var(BuildingBlock):
    feature_name: Annotated[str, VarRange(["x" , "y"])]

    def evaluate(self, **kwargs):
        return self.feature_name
    
    def __str__(self, **kwargs):
        return self.feature_name

