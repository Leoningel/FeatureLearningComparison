from abc import ABC
from dataclasses import dataclass
from typing import Union

import numpy as np
from src.feature_preparation.search_based.grammar.categories import (
    Category,
    IntCategory,
)

class Condition(ABC):
    def evaluate(self, **kwargs):
        return False

@dataclass
class Equals(Condition):
    input: Category

    def evaluate(self, **kwargs):
        return np.apply_along_axis(lambda x: x == self.input.category,0,self.input.column.evaluate(**kwargs))

    def __str__(self):
        return f"({self.input.column} == {self.input.category})"


@dataclass
class NotEquals(Condition):
    input: Category

    def evaluate(self, **kwargs):
        return np.apply_along_axis(lambda x: x != self.input.category,0,self.input.column.evaluate(**kwargs))

    def __str__(self):
        return f"({self.input.column} != {self.input.category})"

