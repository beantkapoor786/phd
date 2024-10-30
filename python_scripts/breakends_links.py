import sys, re, pandas as pd

file_1 = sys.argv[1]
file_2 = sys.argv[2]

# read in breakend data
df = pd.read_csv(file_1, sep = "\t", header = None)

# extract chr, start, and end column
df_clean = df.iloc[:, [0,1,4]]

# give names to columns
df_clean.columns = ["lg", "start", "mate"]

# replace LG with Chr
df_clean["lg"] = df_clean["lg"].str.replace("LG", "Chr")

# replace "N" in end column
df_clean["mate"] = df_clean["mate"].str.replace("N", "")

# remove "[" and "]"
df_clean["mate"] = df_clean["mate"].str.replace("[", "")
df_clean["mate"] = df_clean["mate"].str.replace("]", "")

# split mate_column into mate_chr and mate_point
df_clean[['mate_chr', 'mate_point']] = df_clean['mate'].str.split(":", expand = True)

# remove the mate column
df_clean.pop('mate')

# add 1 to start and mate_point columns
df_clean['end'] = df_clean['start'] + 1
df_clean['mate_point_end'] = df_clean['mate_point'].astype('int') + 1

# rearrange columns
df_clean = df_clean[['lg', 'start', 'end', 'mate_chr', 'mate_point', 'mate_point_end']]

# replace LG with Chr
df_clean["mate_chr"] = df_clean["mate_chr"].str.replace("LG", "Chr")

# save
df_clean.to_csv(file_2, header = None, index = False, sep = '\t')
