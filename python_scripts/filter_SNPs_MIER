# import required packages
import sys, pandas as pd

# function for each genotype configuration that makes biological sense
def genotype_config(df, father, mother, child):
    """Return variants which make biological sense. df is the vcf pandas dataframe without comment lines. father is the one of 
    the parents columns as string type. mother is the second parents column as string type. child is the child column of 
    dataframe as string type."""

    trusted_1 = df[df[father].str.startswith('0/0') & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith('0/0')]
    trusted_2 = df[df[father].str.startswith('0/0') & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_3 = df[df[father].str.startswith('0/0') & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_4 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith('0/0') & df[child].str.startswith('0/0')]
    trusted_5 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith('0/0') & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_6 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith('0/0')]
    trusted_7 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_8 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith(('1/1', '1|1'))]
    trusted_9 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith(('1/1', '1|1')) & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_10 = df[df[father].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[mother].str.startswith(('1/1', '1|1')) & df[child].str.startswith(('1/1', '1|1'))]
    trusted_11 = df[df[father].str.startswith(('1/1', '1|1')) & df[mother].str.startswith('0/0') & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_12 = df[df[father].str.startswith(('1/1', '1|1')) & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith(('0/1', "1/0", "0|1", "1|0"))]
    trusted_13 = df[df[father].str.startswith(('1/1', '1|1')) & df[mother].str.startswith(('0/1', "1/0", "0|1", "1|0")) & df[child].str.startswith(('1/1', '1|1'))]
    trusted_14 = df[df[father].str.startswith('0/0') & df[mother].str.startswith('0/0') & df[child].str.startswith('0/0')]

    trusted = pd.concat([trusted_1, trusted_2, trusted_3, trusted_4, trusted_5, trusted_6, trusted_7, trusted_8, trusted_9,
               trusted_10, trusted_11, trusted_12, trusted_13, trusted_14])

    return trusted

# provide positional arguments for the script
vcf = sys.argv[1]
filtered = sys.argv[2]

# read in vcf file as pandas dataframe, remove header lines
df = pd.read_csv(vcf, comment = "#", sep = "\t", header = None).dropna(how = "all")

# provide column names
df.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'SM1', 'SM2', 'SM1316', 'SM1370', 'ref_pacbio']

# use function to filter out variants for SM1, SM2, and SM1316 trio family
trio_1 = genotype_config(df, "SM1", "SM2", "SM1316")

# use function to filter out variants for SM1, SM2, and SM1370 trio family
trio_2 = genotype_config(trio_1, "SM1", "SM2", "SM1370")

# use function to filter out variants for SM1316, SM1370, and F2 trio family
trio_3 = genotype_config(trio_2, "SM1316", "SM1370", "ref_pacbio")

# combine all dataframes
final = pd.concat([trio_1, trio_2, trio_3])

# sort dataframe by chromosome and pos
final = final.sort_values(by = ["CHROM", "POS"], ascending = [True, True])

# drop any variants which are completely identical to each other
final = final.drop_duplicates()

# save dataframe as tsv without index
final.to_csv(filtered, sep = "\t", header = False, index = False)
