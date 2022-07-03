
from abc import ABC
from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.vars import VarRange
from geneticengine.metahandlers.ints import IntRange
from geneticengine.core.decorators import abstract


class Col(ABC):
    col_name = "No column name defined"
    
    def evaluate(self, **kwargs):
        return kwargs[self.col_name]
    
    def __str__(self, **kwargs):
        return f"\"{self.col_name}\""
    
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
    col_name = "season"
    
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
    col_name = "yr"
    
@dataclass
class Year(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: YearCol


@dataclass
class MonthCol(Col):
    col_name = "mnth"
    
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
    col_name = "holiday"
    
@dataclass
class Holiday(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: HolidayCol


@dataclass
class WeekdayCol(Col):
    col_name = "weekday"
    
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
    col_name = "workingday"
    
@dataclass
class WorkingDay(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: WorkingDayCol

@dataclass
class WeatherSitCol(Col):
    col_name = "weathersit"
    
    number_map = {
        1 : "Clear",
        2 : "Misty",
        3 : "Light rain",
    }

@dataclass
class WeatherSit(IntCategory):
    category: Annotated[int, IntRange( 1, 3 )]
    column: WeatherSitCol

categories = [ Col, Category, BoolCategory, IntCategory, Season, SeasonCol, Year, YearCol, Month, MonthCol, Weekday, WeekdayCol, WeatherSit, WeatherSitCol, Holiday, HolidayCol, WorkingDay, WorkingDayCol ]

 
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

@dataclass
class WeatherSitIB(IBCategory):
    category1: Annotated[int, IntRange( 1, 3 )]
    category2: Annotated[int, IntRange( 1, 3 )]
    column: WeatherSitCol

inbetween_categories = [ IBCategory, SeasonIB, YearIB, MonthIB, WeekdayIB, WeatherSitIB ]

