
from abc import ABC
from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.vars import VarRange
from geneticengine.metahandlers.ints import IntRange
from geneticengine.core.decorators import abstract


class Col(ABC):
    def evaluate(self, **kwargs):
        return "\"x\""
    
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



@dataclass
class SeasonCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["season"]
    
    def __str__(self, **kwargs):
        return "\"season\""

@dataclass
class Season(IntCategory):
    category: Annotated[int, IntRange( 1, 4 )]
    column: SeasonCol
    
    number_map = {
        1 : "winter",
        2 : "spring",
        3 : "summer",
        4 : "fall"
    }

    
@dataclass
class YearCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["yr"]
    
    def __str__(self, **kwargs):
        return "\"yr\""

@dataclass
class Year(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: YearCol


@dataclass
class MonthCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["mnth"]
    
    def __str__(self, **kwargs):
        return "\"mnth\""

@dataclass
class Month(IntCategory):
    category: Annotated[int, IntRange( 1, 12 )]
    column: MonthCol

    number_map = {
        1   : "January",
        2   : "February",
        3   : "March",
        4   : "April",
        5   : "May",
        6   : "June",
        7   : "July",
        8   : "August",
        9   : "September",
        10  : "October",
        11  : "November",
        12  : "December",
    }

@dataclass
class HolidayCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["holiday"]
    
    def __str__(self, **kwargs):
        return "\"holiday\""

@dataclass
class Holiday(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: HolidayCol


@dataclass
class WeekdayCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["weekday"]
    
    def __str__(self, **kwargs):
        return "\"weekday\""

@dataclass
class Weekday(IntCategory):
    category: Annotated[int, IntRange( 0, 6 )]
    column: WeekdayCol

    number_map = {
        0 : "Sunday",
        1 : "Monday",
        2 : "Tueday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
    }

@dataclass
class WorkingDayCol(Col):
    def evaluate(self, **kwargs):
        return kwargs["workingday"]
    
    def __str__(self, **kwargs):
        return "\"workingday\""

@dataclass
class WorkingDay(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: WorkingDayCol

    