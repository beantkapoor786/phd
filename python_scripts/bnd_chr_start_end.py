import sys, re, pandas as pd, numpy as np

data = sys.argv[1]
output = sys.argv[2]

df = pd.read_csv(data, sep = "\t", header = None)

bnd = df.iloc[:, [0, 1, 2, 4]]

bnd.columns = ["chr", "start", "name", "mate"]

# Remove "N" in mate column, we don't need this info
bnd["mate"] = bnd["mate"].str.replace("N", "")

# split mate_column into mate_chr and mate_point
bnd[['mate_chr', 'mate_point']] = bnd['mate'].str.split(":", expand=True)

# remove the mate column
bnd.pop('mate')

# remove "[" from mate_chr column
bnd['mate_chr'] = bnd['mate_chr'].str.replace('[', '')

# remove "]" from mate_chr column
bnd['mate_chr'] = bnd['mate_chr'].str.replace(']', '')

# copy the mate_point column
bnd['mate_start'] = bnd.loc[:, 'mate_point']

# remove the "[" from mate_start column
bnd['mate_start'] = bnd['mate_start'].str.replace('[', '')

# remove the "]" from mate_start column
bnd['mate_start'] = bnd['mate_start'].str.replace(']', '')

# convert character type mate_start column to integer type
bnd['mate_start'] = bnd['mate_start'].astype('int')

# add or subtract 1 from mate_start column based on the square brackets present in mate_point column
bnd['mate_end'] = np.where(bnd['mate_point'].str.contains(']'), bnd['mate_start'] - 1, bnd['mate_start'] + 1)

# remove the mate_point column
bnd.pop('mate_point')

# create a separate dataframe for first breakend pair
bnd_1 = bnd[['chr', 'start', 'name']]

# create end column for first breakend pait
bnd_1['end'] = bnd['start'] + 1

# rearrange columns
bnd_1 = bnd_1[['chr', 'start', 'end', 'name']]

# add "_1" to name column to indicate it's the first breakend pair
bnd_1["name"] = bnd["name"] + "_1"

# create a separete df for second breakend pair
bnd_2 = bnd[["mate_chr", "mate_start", "mate_end", "name"]]
bnd_2.columns = ['chr', 'start', 'end', 'name']

# So bedtools doesn't like if start column's number is higher than end column which makes sense, so we will try to solve that
bnd_2['start'],bnd_2['end'] = np.where(bnd_2['start'] > bnd_2['end'], (bnd_2['end'], bnd_2['start']), (bnd_2['start'], bnd_2['end'])) 

# add "_2" to name column to indicate it's second breakend pair
bnd_2["name"] = bnd_2["name"] + "_2"

# concat two dataframes
bnd_bed = pd.concat([bnd_1, bnd_2], ignore_index=True)

# sort dataframe
bnd_bed = bnd_bed.sort_values(by=['chr', 'start'])

# remove BNDs on same chr and start position (keep the first one)
bnd_bed = bnd_bed.drop_duplicates(subset = ["chr", "start"], keep = "first")

# write this dataframe to tsv file without header and row indices
bnd_bed.to_csv(output, sep = "\t", header=False, index=False)
