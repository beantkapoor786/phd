import sys, re

vcf = sys.argv[1]
data = sys.argv[2]

with open(vcf, "r") as f, open(data, "w+") as g:
    for line in f:
        if not line.startswith("#") and not "BND" in line:
            fields = line.split("\t")
            ID = fields[2]
            test = re.search(r'\.([A-Z]{3})\.', ID)
            sv = test.group(1)
            svlen = fields[7].split(";")[2]
            test_2 = re.search(r'SVLEN=-?(\d+)', svlen)
            length = test_2.group(1)
            g.write(f"{sv}\t{length}\n")
