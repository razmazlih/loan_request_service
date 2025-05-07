import pandas as pd
import ast

def load_data(file_path):
    df = pd.read_csv(
        file_path,
        converters={"incomes": ast.literal_eval, "assets": ast.literal_eval},
    )
    return df
