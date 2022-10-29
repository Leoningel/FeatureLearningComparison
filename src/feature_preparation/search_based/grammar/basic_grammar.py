from abc import ABC
from dataclasses import dataclass
from textwrap import indent
from typing import Annotated, List
import numpy as np

from geneticengine.metahandlers.lists import ListSizeBetween
from geneticengine.metahandlers.vars import VarRange
from geneticengine.metahandlers.ints import IntRange
from geneticengine.core.decorators import abstract

from feature_preparation.search_based.grammar.conditions import Condition

class Solution(ABC):
    def evaluate(self, **kwargs) -> float:
        raise NotImplementedError()

class BuildingBlock(ABC):
    def evaluate(self, **kwargs):
        raise NotImplementedError()

@dataclass
class FeatureSet(Solution):
    subset: Annotated[list[BuildingBlock], ListSizeBetween(1,15)]
    
    def evaluate(self, **kwargs):
        return [ el.evaluate(**kwargs) for el in self.subset ]

    def __str__(self, **kwargs):
        s = "["
        for feat in self.subset:
            s += str(feat) + ","
        s = s[:-1] + "]"
        return s
    
    
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
        if hasattr(d1,"dtype"):
            if d1.dtype == "O":
                d1 = d1.astype(float)
        if hasattr(d2,"dtype"):
            if d2.dtype == "O":
                d2 = d2.astype(float)
        try:
            with np.errstate(divide="ignore", invalid="ignore"):
                return np.where(abs(d2) < 0.0001, np.ones_like(d1), d1 / d2)
        except ZeroDivisionError:
            # In this case we are trying to divide two constants, one of which is 0
            # Return a constant.
            return 1.0
    
    
    def __str__(self, **kwargs):
        return f"({self.left} / {self.right})"    

@dataclass
class Literal(BuildingBlock):
    val: Annotated[int, IntRange(0, 1)]
    
    def evaluate(self, **kwargs):
        data_size = len(list(kwargs.items())[0][1])
        return np.full(data_size,self.val)
    
    def __str__(self, **kwargs):
        return f"{self.val}"
    
    


@dataclass
class IfThenElse(BuildingBlock):
    cond: Condition
    then: BuildingBlock
    elze: BuildingBlock
    
    def if_statement(self,x):
        if x[0]:
            y = x[1]
        else:
            y = x[2]
        return y
    
    def evaluate(self, **kwargs):
        y = np.apply_along_axis(
                self.if_statement,
                0,
                np.array([
                    self.cond.evaluate(**kwargs),
                    self.then.evaluate(**kwargs),
                    self.elze.evaluate(**kwargs)
                    ])
                )
        return y
    
    def __str__(self):
        return "if {}:\n{}\nelse:\n{}".format(
            self.cond, indent(str(self.then), "\t"), indent(str(self.elze), "\t")
        )

standard_gp_grammar = [ Plus, SafeDiv, Mult, Minus, BuildingBlock]

