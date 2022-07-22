from dataclasses import dataclass
from typing import Annotated, Union
from geneticengine.metahandlers.ints import IntRange
from feature_preparation.search_based.grammar.categories import Col, IntCategory, BoolCategory, Category, IBCategory



@dataclass
class CheckingStatusCol(Col):
    col_name = "checking_status"
    
    number_map = {
        0 : "A11",
        1 : "A12",
        2 : "A13",
        3 : "A14",
    }

@dataclass
class CheckingStatus(IntCategory):
    category: Annotated[int, IntRange( 0, 3 )]
    column: CheckingStatusCol

@dataclass
class CheckingStatusIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 3 )]
    category2: Annotated[int, IntRange( 0, 3 )]
    column: CheckingStatusCol

@dataclass
class CreditHistCol(Col):
    col_name = "credit_history"
    
    number_map = {
        0 : "A30",
        1 : "A31",
        2 : "A32",
        3 : "A33",
        4 : "A34",
    }

@dataclass
class CreditHist(IntCategory):
    category: Annotated[int, IntRange( 0, 4 )]
    column: CreditHistCol

@dataclass
class CreditHistIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 4 )]
    category2: Annotated[int, IntRange( 0, 4 )]
    column: CreditHistCol
    
@dataclass
class PurposeCol(Col):
    col_name = "purpose"
    
    number_map = {
        0 : "A40",
        1 : "A41",
        2 : "A42",
        3 : "A43",
        4 : "A44",
        5 : "A45",
        6 : "A46",
        7 : "A47",
        8 : "A48",
        9 : "A49",
        10 : "A410",
    }

@dataclass
class Purpose(IntCategory):
    category: Annotated[int, IntRange( 0, 10 )]
    column: PurposeCol

@dataclass
class PurposeIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 10 )]
    category2: Annotated[int, IntRange( 0, 10 )]
    column: PurposeCol
    
@dataclass
class SavingsCol(Col):
    col_name = "savings_status"
    
    number_map = {
        0 : "A61",
        1 : "A62",
        2 : "A63",
        3 : "A64",
        4 : "A65",
    }

@dataclass
class Savings(IntCategory):
    category: Annotated[int, IntRange( 0, 4 )]
    column: SavingsCol

@dataclass
class SavingsIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 4 )]
    category2: Annotated[int, IntRange( 0, 4 )]
    column: SavingsCol
    
@dataclass
class EmploymentCol(Col):
    col_name = "employment"
    
    number_map = {
        0 : "A71",
        1 : "A72",
        2 : "A73",
        3 : "A74",
        4 : "A75",
    }

@dataclass
class Employment(IntCategory):
    category: Annotated[int, IntRange( 0, 4 )]
    column: EmploymentCol

@dataclass
class EmploymentIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 4 )]
    category2: Annotated[int, IntRange( 0, 4 )]
    column: EmploymentCol
    
@dataclass
class PersonalStatusCol(Col):
    col_name = "personal_status"
    
    number_map = {
        0 : "A91",
        1 : "A92",
        2 : "A93",
        3 : "A94",
        4 : "A95",
    }

@dataclass
class PersonalStatus(IntCategory):
    category: Annotated[int, IntRange( 0, 4 )]
    column: PersonalStatusCol

@dataclass
class PersonalStatusIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 4 )]
    category2: Annotated[int, IntRange( 0, 4 )]
    column: PersonalStatusCol
    
@dataclass
class OtherPartiesCol(Col):
    col_name = "other_parties"
    
    number_map = {
        0 : "A101",
        1 : "A102",
        2 : "A103",
    }

@dataclass
class OtherParties(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: OtherPartiesCol

@dataclass
class OtherPartiesIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 2 )]
    category2: Annotated[int, IntRange( 0, 2 )]
    column: OtherPartiesCol
    
@dataclass
class PropertyCol(Col):
    col_name = "property_magnitude"
    
    number_map = {
        0 : "A121",
        1 : "A122",
        2 : "A123",
        3 : "A124",
    }

@dataclass
class Property(IntCategory):
    category: Annotated[int, IntRange( 0, 3 )]
    column: PropertyCol

@dataclass
class PropertyIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 3 )]
    category2: Annotated[int, IntRange( 0, 3 )]
    column: PropertyCol
    
@dataclass
class OtherInstallmentsCol(Col):
    col_name = "other_payment_plans"
    
    number_map = {
        0 : "A141",
        1 : "A142",
        2 : "A143",
    }

@dataclass
class OtherInstallments(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: OtherInstallmentsCol

@dataclass
class OtherInstallmentsIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 2 )]
    category2: Annotated[int, IntRange( 0, 2 )]
    column: OtherInstallmentsCol
    
@dataclass
class HousingCol(Col):
    col_name = "housing"
    
    number_map = {
        0 : "A151",
        1 : "A152",
        2 : "A153",
    }

@dataclass
class Housing(IntCategory):
    category: Annotated[int, IntRange( 0, 2 )]
    column: HousingCol

@dataclass
class HousingIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 2 )]
    category2: Annotated[int, IntRange( 0, 2 )]
    column: HousingCol
    
@dataclass
class JobCol(Col):
    col_name = "job"
    
    number_map = {
        0 : "A171",
        1 : "A172",
        2 : "A173",
        3 : "A174",
    }

@dataclass
class Job(IntCategory):
    category: Annotated[int, IntRange( 0, 3 )]
    column: JobCol

@dataclass
class JobIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 3 )]
    category2: Annotated[int, IntRange( 0, 3 )]
    column: JobCol
    
@dataclass
class TelephoneCol(Col):
    col_name = "own_telephone"
    
    number_map = {
        0 : "A191",
        1 : "A192",
    }

@dataclass
class Telephone(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: TelephoneCol

@dataclass
class TelephoneIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 1 )]
    category2: Annotated[int, IntRange( 0, 1 )]
    column: TelephoneCol
    
@dataclass
class ForeignWorkerCol(Col):
    col_name = "foreign_worker"
    
    number_map = {
        0 : "A201",
        1 : "A202",
    }

@dataclass
class ForeignWorker(BoolCategory):
    category: Annotated[int, IntRange( 0, 1 )]
    column: ForeignWorkerCol

@dataclass
class ForeignWorkerIB(IBCategory):
    category1: Annotated[int, IntRange( 0, 1 )]
    category2: Annotated[int, IntRange( 0, 1 )]
    column: ForeignWorkerCol
    
    
    
    
    
special_features = {
    "checking_status"       : CheckingStatus,
    "credit_history"        : CreditHist,
    "purpose"               : Purpose,
    "savings_status"        : Savings,
    "employment"            : Employment,
    "personal_status"       : PersonalStatus,
    "other_parties"         : OtherParties,
    "property_magnitude"    : Property,
    "other_payment_plans"   : OtherInstallments,
    "housing"               : Housing,
    "job"                   : Job,
    "own_telephone"         : Telephone,
    "foreign_worker"        : ForeignWorker,
}

ibs = [ CheckingStatusIB, CreditHistIB, PurposeIB, SavingsIB, EmploymentIB, PersonalStatusIB, OtherPartiesIB, PropertyIB, OtherInstallmentsIB, HousingIB, JobIB, TelephoneIB, ForeignWorkerIB ]

categories = [ 
              Col,
              Category,
              BoolCategory,
              IntCategory,
              CheckingStatus,
              CheckingStatusCol,
              CreditHist,
              CreditHistCol,
              Purpose,
              PurposeCol, 
              Savings,
              SavingsCol, 
              Employment,
              EmploymentCol, 
              PersonalStatus,
              PersonalStatusCol, 
              OtherParties,
              OtherPartiesCol, 
              Property,
              PropertyCol, 
              OtherInstallments,
              OtherInstallmentsCol, 
              Housing,
              HousingCol, 
              Job,
              JobCol, 
              Telephone,
              TelephoneCol, 
              ForeignWorker,
              ForeignWorkerCol, 
              ]

