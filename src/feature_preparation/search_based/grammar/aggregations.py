



from dataclasses import dataclass
from itertools import compress
import numpy as np
from src.feature_preparation.search_based.grammar.basic_grammar import BuildingBlock, Var
from src.feature_preparation.search_based.grammar.conditions import Condition

@dataclass
class Average(BuildingBlock):
    cond: Condition
    var: BuildingBlock
    
    def filter(self,l,fil):
        return list(compress(l,fil))
    
    def evaluate(self, **kwargs):
        vars = self.var.evaluate(**kwargs)
        fil = self.cond.evaluate(**kwargs)
        aggregate = [ np.mean(self.filter(vars[:i],fil[:i])) for i in range(len(vars)) ]
        aggregate = np.array(aggregate)
        aggregate = np.nan_to_num(aggregate)

        return aggregate
    
    def __str__(self):
        return f"average({self.var} where {self.cond})"
