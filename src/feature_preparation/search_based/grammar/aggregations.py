from dataclasses import dataclass
from typing import Annotated

import numpy as np

from geneticengine.metahandlers.vars import VarRange

from src.feature_preparation.search_based.grammar.basic_grammar import BuildingBlock, Var
from src.feature_preparation.search_based.grammar.categories import Col
import src.global_vars as gv

@dataclass
class Average(BuildingBlock):
    col: Col
    aggregation_col: Annotated[str, VarRange(["target"])]
    
    time_column = "instant"
    
    def get_relevant_vals(self, historical_data, instant, col_val):
        cond = (historical_data[self.time_column] < instant) & (historical_data[self.col.col_name] == col_val)
        relevant_vals = historical_data[cond]
        relevant_vals = relevant_vals[self.aggregation_col].values
                
        return relevant_vals
    
    def evaluate(self, **kwargs):
        historical_data = kwargs['data']
        historical_data = historical_data[[self.time_column, self.aggregation_col, self.col.col_name]]
        instants = zip(kwargs[self.time_column], self.col.evaluate(**kwargs))
        
        aggregates = [ np.mean(self.get_relevant_vals(historical_data,instant,col_val)) for (instant, col_val) in instants ]
        aggregates = np.array(aggregates)
        aggregates = np.nan_to_num(aggregates)
        
        return aggregates
    
    def __str__(self):
        return f"average(\"{self.aggregation_col}\" for historic {self.col})"
