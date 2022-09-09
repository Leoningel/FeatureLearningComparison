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



categories = [Col, Category, BoolCategory, IntCategory,Weekday, WeekdayCol]



@dataclass
class WeekdayIB(IBCategory):
    category1: Annotated[int, IntRange(1, 7)]
    category2: Annotated[int, IntRange(1, 7)]
    column: WeekdayCol


inbetween_categories = [IBCategory, WeekdayIB]


special_features = {
    "Day.Of.Week": Weekday,
}

ibs = [ WeekdayIB]
