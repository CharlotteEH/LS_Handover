import pandas as pd
from e_nda_1 import dp_volume
from f_nda_2 import total_volume
from pathlib import Path

nda = pd.merge(
    dp_volume, total_volume,
    left_on=["Rel_Qtr", "PT_GenealogyLevel3Description", "Region"],
    right_on=["Rel_Qtr", "PT_GenealogyLevel3Description", "Region"],
    how="inner"
)

nda["dp_volume_share"] = nda["dp_volume"]/nda["total_volume"]

nda["rank"] = nda.groupby(
    [
        "Rel_Qtr", "PT_GenealogyLevel3Description", "Region"
    ])["dp_volume_share"].rank(ascending=False)

nda = nda.loc[nda["rank"]==1]

nda = nda.rename(columns={"OI_ClientDescription":"client_with_max_share",
                          "dp_volume_share":"max_share"})

nda = nda[["Rel_Qtr", "PT_GenealogyLevel3Description", "Region", "max_share", "client_with_max_share", "dist", "client_count"]]

print(nda.head(15))
cwd = Path(__file__).parent

nda.to_csv(cwd / "cola_nda.csv", index=False)