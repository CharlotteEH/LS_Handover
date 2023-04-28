from b_eda import df
import pandas as pd

print("\nthe head of df is:\n", df.head(5), "\n")


rosd = df.groupby(
    [
        "D_DateKey", "Rel_Qtr", "PT_GenealogyLevel3Description", "Region"
    ]
).agg(
    {
        "vol":["sum"],
        "val":["sum"],
        "quan": ["sum"],
        "OT_CGAIdent": pd.Series.nunique
    }
)
rosd.columns = rosd.columns.get_level_values(0)
rosd = rosd.reset_index()

rosd = rosd.rename(columns={
    "vol": "total_vol",
    "val": "total_val",
    "quan": "total_quan",
    "OT_CGAIdent": "dist"})


print(rosd.head(15))