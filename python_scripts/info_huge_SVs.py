import sys, re

vcf = sys.argv[1]
output = sys.argv[2]

with open(vcf, "r") as v, open(output, "w+") as o:
    for line in v:
        if not line.startswith('#'):
            field = line.split('\t')
            ID = field[2]
            svlen = field[7].split(";")[2]
            test = re.search(r'SVLEN=-?(\d+)', svlen)
            length = int(test.group(1))
            if length > 1000000:
                o.write(f"{ID}\n")
