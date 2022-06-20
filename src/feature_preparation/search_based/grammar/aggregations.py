from dataclasses import dataclass
from typing import Annotated

import time
import numpy as np

from geneticengine.metahandlers.vars import VarRange
from geneticengine.metahandlers.ints import IntList
import pandas as pd

from feature_preparation.search_based.grammar.basic_grammar import BuildingBlock, Var
from feature_preparation.search_based.grammar.categories import Col
import global_vars as gv

@dataclass
class Average(BuildingBlock):
    col: Col
    aggregation_col: Annotated[str, VarRange(["target"])]
    window_length: Annotated[int, IntList([10, 25, 50, 75, 100, 150, 200, 300, 400, 600, 800])]
    
    def assign_target_values_to_data(self, data, historical_data):
        data = data.merge(historical_data,how='left')
        first_data_instant = data[gv.TIME_COLUMN].min()
        historical_data = historical_data[historical_data[gv.TIME_COLUMN] < first_data_instant]

        means = historical_data.groupby(self.col.col_name).mean()[self.aggregation_col]
        uns = data[self.col.col_name].unique()
        
        def missing_mean_zero(un):
            try:
                return means[un]
            except:
                return 0
        mapping = dict([ (un,missing_mean_zero(un)) for un in uns ])
        def fill_nans(row):
            if np.isnan(row[self.aggregation_col]):
                return mapping[row[self.col.col_name]]
            else:
                return row[self.aggregation_col]
        data[self.aggregation_col] = data.apply(lambda row: fill_nans(row), axis=1)
        # -----------
        combined_data = pd.concat([historical_data,data])

        return combined_data
    
    def aggregate(self, combined_data, instants, window_length):
        aggregated_vals = combined_data.set_index(gv.TIME_COLUMN).sort_index().groupby(self.col.col_name).rolling(window=window_length, min_periods=1, closed='left').mean()
        aggregated_vals = aggregated_vals.reset_index().set_index(gv.TIME_COLUMN).sort_index()
        aggregated_vals = aggregated_vals[self.aggregation_col].filter(instants)
                
        return aggregated_vals
    
    def evaluate(self, **kwargs):
        historical_data = kwargs['data']
        historical_data = historical_data[[gv.TIME_COLUMN, self.col.col_name, self.aggregation_col]]
        instants = kwargs[gv.TIME_COLUMN].astype(int)
        
        data = pd.DataFrame({gv.TIME_COLUMN:instants, self.col.col_name: self.col.evaluate(**kwargs)}).astype('int64')

        combined_data = self.assign_target_values_to_data(data, historical_data)
        aggregates = self.aggregate(combined_data, instants, self.window_length)
        
        aggregates = np.nan_to_num(aggregates)

        return aggregates
    
    def __str__(self):
        return f"average(\"{self.aggregation_col}\" for historic {self.col})"
