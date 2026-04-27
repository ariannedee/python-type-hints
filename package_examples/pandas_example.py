""" Type hinting example for Pandas
pip install pandas
pip install pandas-stubs <- type stub file
"""
import pandas as pd

# Basic DataFrame and Series
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def get_column(df: pd.DataFrame, name: str) -> pd.Series:
    return df[name]

def filter_data(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    return df[df['value'] > threshold]

# %% Supply dataframe schema with TypedDict (documentation only)
from typing import TypedDict

class UserSchema(TypedDict):  # Not enforced
    user_id: int
    name: str
    age: int

# %% Restrict column names with Literal
from typing import Literal

def get_column_w_literal(
    df: pd.DataFrame,
    col: Literal['user_id', 'name', 'age', 'email']
) -> pd.Series:
    """Type checker ensures only valid column names are passed."""
    return df[col]

# Usage
df = pd.read_csv('users.csv')
user_ids = get_column_w_literal(df, 'user_id')
names = get_column_w_literal(df, 'invalid')   # mypy

# %% Runtime validation w/ Pandera - pip install pandera
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series

# Define schema with validation rules
class PaUserSchema(pa.DataFrameModel):
    user_id: Series[int] = pa.Field(gt=0)
    name: Series[str]
    age: Series[int] = pa.Field(ge=0, le=120)
    email: Series[str] = pa.Field(str_matches=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    signup_date: Series[str]

    class Config:
        strict = True  # No extra columns allowed

# Type-checked function with runtime validation
@pa.check_types
def process_users(df: DataFrame[PaUserSchema]) -> DataFrame[PaUserSchema]:
    return df[df['age'] > 18]


# Validates at runtime
df = pd.read_csv('users.csv')
validated_df = UserSchema.validate(df)