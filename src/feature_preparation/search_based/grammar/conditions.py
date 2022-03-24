from abc import ABC
from dataclasses import dataclass
from src.feature_preparation.search_based.grammar.categories import (
    Category
)

class Condition(ABC):
    pass

@dataclass
class Equals(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] == self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} == {self.input.category})"


@dataclass
class NotEquals(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] != self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} != {self.input.category})"


@dataclass
class GreaterThan(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] > self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} > {self.input.category})"


@dataclass
class GreaterOrEqualThan(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] >= self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} >= {self.input.category})"


@dataclass
class LessThan(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] < self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} < {self.input.category})"


@dataclass
class LessOrEqualThan(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] <= self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} <= {self.input.category})"


@dataclass
class Is(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] is self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} is {self.input.category})"


@dataclass
class IsNot(Condition):
    input: Category

    def evaluate(self, **kwargs) -> bool:
        return kwargs[self.input.column] is not self.input.category

    def __str__(self):
        return f"({self.input.column.upper()} is not {self.input.category})"


all_operators = [
    Equals,
    NotEquals,
    GreaterOrEqualThan,
    GreaterThan,
    LessOrEqualThan,
    LessThan,
    Is,
    IsNot,
]
