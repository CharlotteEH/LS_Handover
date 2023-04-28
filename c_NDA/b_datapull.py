import pandas as pd

from a_connection import engine

sql_query = f"""


SELECT ew.Rel_Qtr,
ew.OT_CGAIdent,
ew.OI_ClientDescription,
ew.PT_GenealogyLevel3Description,
CASE WHEN OT_TL4_CGA IN ('North & NE England', 'NW England')
	THEN 'North'
	WHEN OT_TL4_CGA = ('Midlands')
	THEN 'Midlands'
	WHEN OT_TL4_CGA IN ('London & South East', 'SW England')
	THEN 'South'
	ELSE 'Other'
	END AS 'Region',
SUM(ew.F_SalesVolume_MLS) AS 'vol',
SUM(ew.[F_SalesValue_£]) AS 'val',
SUM(ew.F_SalesQuantity) AS 'quan'

FROM [WS_LIVE].[dbo].[vw_Epos_Weekly] AS ew WITH(NOLOCK)

WHERE ew.PT_ClassificationLevel2Description = 'Cola'
AND ew.PT_GenealogyLevel3Description IN ('Coca Cola', 'Pepsi')
AND ew.Rel_MAT IN (1,2)
AND ew.OT_CGAIdent > 0
AND ew.OT_StatusId = 1
AND ew.F_SalesVolume_MLS > 0 
AND ew.[F_SalesValue_£] > 0 
AND ew.OT_TL4_CGA IN ('North & NE England', 'NW England', 'Midlands', 'London & South East', 'SW England')

GROUP BY
ew.Rel_Qtr,
ew.OT_CGAIdent,
ew.OI_ClientDescription,
ew.PT_GenealogyLevel3Description,
CASE WHEN OT_TL4_CGA IN ('North & NE England', 'NW England')
	THEN 'North'
	WHEN OT_TL4_CGA = ('Midlands')
	THEN 'Midlands'
	WHEN OT_TL4_CGA IN ('London & South East', 'SW England')
	THEN 'South'
	ELSE 'Other'
	END

"""

df_sql_query = pd.read_sql(sql_query, engine)
