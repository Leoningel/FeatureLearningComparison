
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
    
    number_map = {
        1 : "winter",
        2 : "spring",
        3 : "summer",
        4 : "fall"
    }

@dataclass
class Season(IntCategory):
    category: Annotated[int, IntRange( 1, 4 )]
    column: SeasonCol

    
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
class Month(IntCategory):
    category: Annotated[int, IntRange( 1, 12 )]
    column: MonthCol

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
class Weekday(IntCategory):
    category: Annotated[int, IntRange( 0, 6 )]
    column: WeekdayCol

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

    
 
##-------------------------
# Should be implemented differently once dependent types are included in Genetic Engine
##-------------------------
    
class IBCategory(ABC):
    category1: int
    category2: int
    column: Col

@dataclass
class SeasonIB(IBCategory):
    category1: Annotated[int, IntRange( 1, 4 )]
    category2: Annotated[int, IntRange( 1, 4 )]
    column: SeasonCol

    
@dataclass
class YearIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 2 )]
    category2: Annotated[int, IntRange( 0, 2 )]
    column: YearCol


@dataclass
class MonthIB(IBCategory):
    category1: Annotated[int, IntRange( 1, 12 )]
    category2: Annotated[int, IntRange( 1, 12 )]
    column: MonthCol


@dataclass
class WeekdayIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 6 )]
    category2: Annotated[int, IntRange( 0, 6 )]
    column: WeekdayCol

