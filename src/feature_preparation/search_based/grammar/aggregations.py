from dataclasses import dataclass
from typing import Annotated

import time
import numpy as np

from geneticengine.metahandlers.vars import VarRange
import pandas as pd

from src.feature_preparation.search_based.grammar.basic_grammar import BuildingBlock, Var
from src.feature_preparation.search_based.grammar.categories import Col
import src.global_vars as gv

@dataclass
class Average(BuildingBlock):
    col: Col
    aggregation_col: Annotated[str, VarRange(["target"])]
    
    # def get_relevant_vals_old(self, historical_data, dp, col_val):
    #     cond = (historical_data[gv.TIME_COLUMN] < dp) & (historical_data[self.col.col_name] == col_val)
    #     relevant_vals = historical_data[cond]
    #     relevant_vals = relevant_vals[self.aggregation_col].values
                
    #     return relevant_vals
    
    def get_relevant_vals(self, data, historical_data,instants):
        data = data.merge(historical_data,how='left')

        first_data_instant = data[gv.TIME_COLUMN].min()
        historical_data = historical_data[historical_data[gv.TIME_COLUMN] < first_data_instant] # TODO: Only historical data from here on
        a = [ inst not in data[gv.TIME_COLUMN].values for inst in historical_data[gv.TIME_COLUMN]]
        if a:
            historical_data = historical_data[a]

        means = historical_data.groupby(self.col.col_name).mean()[self.aggregation_col]
        uns = data[self.col.col_name].unique()
        def missing_mean_zero(un):
            try:
                return means[un]
            except:
                return 0
        aggs = [ missing_mean_zero(un) for un in uns ]
        mapping = dict(zip(uns,aggs))
        def fill_nans(row):
            if row[self.aggregation_col] == np.nan:
                return mapping[row[self.col.col_name]]
            else:
                return row[self.aggregation_col]
        data[self.aggregation_col] = data.apply(lambda row: fill_nans(row), axis=1)

        combined_data = pd.concat([historical_data,data])
        
        relevant_vals = combined_data.set_index(gv.TIME_COLUMN).sort_index().groupby(self.col.col_name).rolling(window=len(combined_data), min_periods=1, closed='left').mean()
        relevant_vals = relevant_vals.reset_index().set_index(gv.TIME_COLUMN).sort_index()
        relevant_vals = relevant_vals[self.aggregation_col].filter(instants)
                
        return relevant_vals
    
    def evaluate(self, **kwargs):
        historical_data = kwargs['data']
        historical_data = historical_data[[gv.TIME_COLUMN, self.col.col_name, self.aggregation_col]]
        instants = kwargs[gv.TIME_COLUMN].astype(int)
        
        # data = zip(instants,self.col.evaluate(**kwargs))

        # aggregates = [ np.mean(self.get_relevant_vals_old(historical_data,instant,col_val)) for (instant, col_val) in data ]
        # aggregates = np.array(aggregates)
        # aggregates_old = np.nan_to_num(aggregates)
        
        data = pd.DataFrame({gv.TIME_COLUMN:instants, self.col.col_name: self.col.evaluate(**kwargs)}).astype('int64')

        aggregates = self.get_relevant_vals(data=data, historical_data=historical_data, instants=instants)
        aggregates = np.nan_to_num(aggregates)

        return aggregates
    
    def __str__(self):
        return f"average(\"{self.aggregation_col}\" for historic {self.col})"
