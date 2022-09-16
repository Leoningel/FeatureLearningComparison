from dataclasses import dataclass
from typing import Annotated
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory


@dataclass
class WeekdayCol(Col):
    col_name = "Day.Of.Week"

    number_map = {
        1: "Sunday",
        2: "Monday",
        3: "Tueday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }


@dataclass
class Weekday(IntCategory):
    category: Annotated[int, IntRange(1, 7)]
    column: WeekdayCol


@dataclass
class MonthCol(Col):
    col_name = "Month"

    number_map = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }


@dataclass
class Month(IntCategory):
    category: Annotated[int, IntRange(1, 12)]
    column: MonthCol


categories = [Col, Category, BoolCategory,
            IntCategory, Weekday, WeekdayCol, Month, MonthCol]

#TODO:  day/month combo(e.g., 9/Feb or 9/2) , Returning.visits


@dataclass
class WeekdayIB(IBCategory):
    category1: Annotated[int, IntRange(1, 7)]
    category2: Annotated[int, IntRange(1, 7)]
    column: WeekdayCol


@dataclass
class MonthIB(IBCategory):
    category1: Annotated[int, IntRange(1, 12)]
    category2: Annotated[int, IntRange(1, 12)]
    column: MonthCol


inbetween_categories = [IBCategory, WeekdayIB, MonthIB]


special_features = {
    "Day.Of.Week": Weekday,
    "Month": Month,
}

ibs = [WeekdayIB, MonthIB]
