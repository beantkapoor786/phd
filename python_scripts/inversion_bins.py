import sys, pandas as pd

file_1 = sys.argv[1]
file_2 = sys.argv[2]

df = pd.read_csv(file_1, header = None, sep = "\t")

# we just need first two columns
df_clean = df.iloc[:, [0, 1]]

# name these columns
df_clean.columns = ['chr', 'pos']

# create an interval index object
bins = pd.interval_range(start = 0, end = 91000000, freq = 1000000, closed = 'right')
#print(bins)

# create a new column with 1 Mb bins
df_clean['bins'] = pd.cut(df_clean.loc[:, 'pos'], bins, include_lowest = True)

# just keep chr and bins columns
df_clean = df_clean.iloc[:, [0,2]]

# create a new column with counts of SVs per bins per chr
df_clean = df_clean.value_counts(["chr", "bins"]).sort_index().reset_index(name = "count")

# convert bins into str column
df_clean.bins = df_clean.bins.astype("string")

# split bins column into two
df_clean[["start", "end"]] = df_clean.bins.str.split(",", expand = True)

# pop out bins column
df_clean.pop("bins")

# remove brackets in start and end columns and convert them to integer type columns. Add 1 to start column to keep boundaries of bins separate.
df_clean['start'] = df_clean['start'].str.replace('(', '').astype('int') + 1
df_clean['end'] = df_clean['end'].str.replace(']', '').astype('int')

# reorder columns
df_clean = df_clean[["chr", "start", "end", "count"]]

# replace "LG" with "Chr"
df_clean["chr"] = df_clean["chr"].str.replace("LG", "Chr")

# save as tab separated file
df_clean.to_csv(file_2, header = None, index = False, sep = "\t")
