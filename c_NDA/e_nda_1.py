import pandas as pd
from d_read_in_the_data import df


# volume by data partner
df["OI_ClientDescription2"] = df["OI_ClientDescription"]



dp_volume = df.groupby(
    [
        "Rel_Qtr", "OI_ClientDescription", "PT_GenealogyLevel3Description", "Region"
    ]
).agg(
    {
        "vol":["sum"],
        "OT_CGAIdent": pd.Series.nunique,
        "OI_ClientDescription2": pd.Series.nunique
    }
)

dp_volume.columns = dp_volume.columns.get_level_values(0)
dp_volume = dp_volume.reset_index()
dp_volume = dp_volume.rename(columns={"vol":"dp_volume",
                                      "OT_CGAIdent": "dist_client",
                                      "OI_ClientDescription2": "client_count_1"})


print(dp_volume.head())