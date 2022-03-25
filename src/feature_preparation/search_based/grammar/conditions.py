from abc import ABC
from dataclasses import dataclass

import numpy as np
from src.feature_preparation.search_based.grammar.categories import (
    Category
)

class Condition(ABC):
    def evaluate(self, **kwargs):
        return False

@dataclass
class Equals(Condition):
    input: Category

    def evaluate(self, **kwargs):
        return np.apply_along_axis(lambda x: x == self.input.category,0,kwargs[self.input.column])

    def __str__(self):
        return f"({self.input.column} == {self.input.category})"


@dataclass
class NotEquals(Condition):
    input: Category

    def evaluate(self, **kwargs):
        return kwargs[self.input.column] != self.input.category

    def __str__(self):
        return f"({self.input.column} != {self.input.category})"

