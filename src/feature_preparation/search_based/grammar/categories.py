
from abc import ABC
from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.vars import VarRange
from geneticengine.metahandlers.ints import IntRange


class Col(ABC):
    def evaluate(self, **kwargs):
        return "\"x\""

class Category(ABC):
    category: Union[int, bool]
    column: Col

# class Category(Category):
#     category: int

@dataclass
class SeasonCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["season"]
    
    def __str__(self, **kwargs):
        return "\"season\""

@dataclass
class Season(Category):
    category: Annotated[int, IntRange( 1, 4 )]
    column: SeasonCol

    
@dataclass
class YearCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["yr"]
    
    def __str__(self, **kwargs):
        return "\"yr\""

@dataclass
class Year(Category):
    category: Annotated[int, IntRange( 0, 2 )]
    column: YearCol


@dataclass
class MonthCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["mnth"]
    
    def __str__(self, **kwargs):
        return "\"mnth\""

@dataclass
class Month(Category):
    category: Annotated[int, IntRange( 1, 12 )]
    column: MonthCol


@dataclass
class HolidayCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["holiday"]
    
    def __str__(self, **kwargs):
        return "\"holiday\""

@dataclass
class Holiday(Category):
    category: Annotated[int, IntRange( 0, 1 )]
    column: HolidayCol


@dataclass
class WeekdayCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["weekday"]
    
    def __str__(self, **kwargs):
        return "\"weekday\""

@dataclass
class Weekday(Category):
    category: Annotated[int, IntRange( 0, 6 )]
    column: WeekdayCol


@dataclass
class WorkingDayCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["workingday"]
    
    def __str__(self, **kwargs):
        return "\"workingday\""

@dataclass
class WorkingDay(Category):
    category: Annotated[int, IntRange( 0, 1 )]
    column: WorkingDayCol

    