from a_read_in_the_data import df

print("\nthe head of df is:\n", df.head(5), "\n")

u = df["D_DateKey"].unique()
print("\nthe unique dates are:\n", sorted(u),"\n")

