from dataclasses import dataclass
from itertools import compress
from typing import Annotated

import numpy as np
import pandas as pd

from geneticengine.metahandlers.vars import VarRange

from src.feature_preparation.search_based.grammar.basic_grammar import BuildingBlock, Var
from src.feature_preparation.search_based.grammar.categories import Col
import src.feature_preparation.search_based.utils as utils


@dataclass
class Average(BuildingBlock):
    col: Col
    aggregation_col: Annotated[str, VarRange(["target"])]
    
    file_path = "data/boom_bikes_14-01-2022_without_casual_and_registered.csv"
    delimiter = ','
    
    def get_relevant_vals(self, data, instant, col_val):
        cond = (data["instant"] < instant) & (data[self.col.col_name] == col_val)
        relevant_vals = data[cond]
        
        return relevant_vals[self.aggregation_col].values
    
    def evaluate(self, **kwargs):
        data = pd.read_csv(self.file_path, delimiter=self.delimiter)
        data = data[["instant", self.aggregation_col, self.col.col_name]]
        instants = zip(kwargs["instant"], self.col.evaluate(**kwargs))
        
        aggregates = [ np.mean(self.get_relevant_vals(data,instant,col_val)) for (instant, col_val) in instants ]
        aggregates = np.array(aggregates)
        aggregates = np.nan_to_num(aggregates)
        
        return aggregates
    
    def __str__(self):
        return f"average({self.aggregation_col} for historic {self.col})"
