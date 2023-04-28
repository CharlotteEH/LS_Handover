from e_nda_1 import dp_volume
import pandas as pd

# total volume

total_volume = dp_volume.groupby(
    [
        "Rel_Qtr", "PT_GenealogyLevel3Description", "Region"
    ]
).agg(
    {
        "dp_volume": ["sum"],
        "client_count_1": ["sum"],
        "dist_client": ["sum"]
    }
)
total_volume.columns = total_volume.columns.get_level_values(0)
total_volume = total_volume.reset_index()

total_volume = total_volume.rename(columns={"dp_volume": "total_volume",
                                            "client_count_1": "client_count",
                                            "dist_client": "dist"})

print(total_volume.head(15))