"""
This script takes a vcf file produced by Sniffles and outputs a table for a count of types of SVs per chromosome.
Usage: python SVs_per_chr.py <vcf> <output>
"""

import sys, re, pandas as pd

vcf = sys.argv[1]
stats = sys.argv[2]

# read in records leaving out the header part of the vcf file
df = pd.read_csv(vcf, comment = "#", sep = "\t", header = None).dropna(how = "all")

# extract chromosome and SV type column in a separate dataframe
chr_sv = df.iloc[:, [0,2]].copy()

# give column names
chr_sv.columns = ["chr", "type"]

# Let's use the regular expressions to extract just the information we need. So, if you will look closely at the Type column, the type of SVs is written between the two dots and always is in capital letters. We will use this property to capture the substring we need.
chr_sv["sv"] = chr_sv["type"].str.extract("\.([A-Z]+)\.")

# delete the second column
chr_sv.pop("type")

# add a column of 1
chr_sv['count'] = 1

# Now, let's sum the "sv" column per "chr" column
chr_sv_grouped = chr_sv.groupby(["chr", "sv"]).sum().reset_index()

# pivot for a better format
chr_sv_types = chr_sv_grouped.pivot(index = "chr", columns = "sv", values = "count")

# convert it to a normal dataframe
chr_sv_types = pd.DataFrame(chr_sv_types.to_records())

# save results in a tsv file
chr_sv_types.to_csv(stats, sep = "\t")
