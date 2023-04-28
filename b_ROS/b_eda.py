from a_read_in_the_data import df

print("\nthe head of df is:\n", df.head(5), "\n")

u = df["D_DateKey"].unique()
print("\nthe unique dates are:\n", sorted(u),"\n")

u = df["Region"].unique()
print("\nthe unique regions are:\n", sorted(u), "\n")

u = df["PT_GenealogyLevel3Description"].unique()
print("\nthe unique cola brands are:\n", sorted(u), "\n")

