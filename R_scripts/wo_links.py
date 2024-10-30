# import required modules
import re

# input and output files
file_1 = "q_alba_v3.3.0_chromosomes_vs_q_alba_177_markers_blast_results.uniq"
file_2 = "q_alba_180_snp_location.csv"

inhandle_1 = open(file_1, "r")
inhandle_2 = open(file_2, "r")
outhandle = open("links.txt", "w")

# white oak genome length in bp
wo_genome = 753599421

# white oak genetic map length in cM
wo_map = 731.6

# scaling factor
sf = wo_genome / wo_map

marker_dict = {}

for line in inhandle_1:
        fields = line.split("\t")
        contig = fields[1]
        contig = re.sub("HiC_scaffold_", "Chr", contig)
        contig_start = fields[8]
        contig_end = fields[9]
        marker = fields[0]
        marker_dict[marker] = [contig, contig_start, contig_end]

#print(marker_dict)
inhandle_1.close()

###################################
for line in inhandle_2:
	fields = line.split(",")
	lg = fields[0]
	color_code = re.sub("LG", "chr", lg)
	location = str(round(float(fields[2]) * sf))
	name = fields[1]
	if name in marker_dict:
		match_list = marker_dict[name]
		out_list = [match_list[0], match_list[1], match_list[2], lg, location, location, "color=" + color_code + "\n"]
		outhandle.write("\t".join(out_list))

inhandle_2.close()
outhandle.close()
