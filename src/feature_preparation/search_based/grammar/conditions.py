from abc import ABC
from dataclasses import dataclass
from typing import Union

import numpy as np
from src.feature_preparation.search_based.grammar.categories import (
    Category,
    IBCategory,
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
        cat = self.input.category
        if hasattr(self.input.column,"number_map"):
            cat = self.input.column.number_map[cat]
        return f"({self.input.column} == {cat})"


@dataclass
class NotEquals(Condition):
    input: Category

    def evaluate(self, **kwargs):
        return np.apply_along_axis(lambda x: x != self.input.category,0,self.input.column.evaluate(**kwargs))

    def __str__(self):
        cat = self.input.category
        if hasattr(self.input.column,"number_map"):
            cat = self.input.column.number_map[cat]
        return f"({self.input.column} != {cat})"


@dataclass
class InBetween(Condition):
    input: IBCategory

    def evaluate(self, **kwargs):
        if self.input.category1 <= self.input.category2:
            return np.apply_along_axis(lambda x: (x >= self.input.category1) & (x <= self.input.category2),0,self.input.column.evaluate(**kwargs))
        else:
            return np.apply_along_axis(lambda x: (x <= self.input.category1) & (x >= self.input.category2),0,self.input.column.evaluate(**kwargs))

    def __str__(self):
        cat1 = self.input.category1
        cat2 = self.input.category2
        if hasattr(self.input.column,"number_map"):
            cat1 = self.input.column.number_map[cat1]
            cat2 = self.input.column.number_map[cat2]
        if self.input.category1 <= self.input.category2:
            return f"({self.input.column} inbetween ({cat1},{cat2}))"
        else:
            return f"({self.input.column} inbetween ({cat2},{cat1}))"

