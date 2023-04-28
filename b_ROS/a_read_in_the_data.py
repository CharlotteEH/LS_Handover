import pandas as pd

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

df = pd.read_csv("../a_SQL_Data_Pull/data.csv", parse_dates=[
    "D_DateKey"])
