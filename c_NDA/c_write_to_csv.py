from pathlib import Path

from b_datapull import df_sql_query

cwd = Path(__file__).parent

df_sql_query.to_csv(cwd / "data.csv", index=False)