from d_ros_2 import rosd
import pandas as pd
from pathlib import Path


rosd = rosd.groupby(
    [
        "Rel_Qtr", "PT_GenealogyLevel3Description", "Region"
    ]
).agg(
    {
        "dist": ["mean"],
        "ros_vol":["mean"],
        "ros_val":["mean"],
        "ros_quan": ["mean"],
        "avg_price": ["mean"]
    }
)
rosd.columns = rosd.columns.get_level_values(0)
rosd = rosd.reset_index()

print(rosd.head(15))
cwd = Path(__file__).parent

rosd.to_csv(cwd / "cola_ros.csv", index=False)