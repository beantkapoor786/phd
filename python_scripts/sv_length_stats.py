import sys, re

vcf = sys.argv[1]
stats = sys.argv[2]

# bnd counters
bnd_sv = 0

# del counters
del_sv, del_s, del_m, del_l, del_xl, del_xxl = 0,0,0,0,0,0

# dup counters
dup_sv, dup_s, dup_m, dup_l, dup_xl, dup_xxl = 0,0,0,0,0,0

# ins counters
ins_sv, ins_s, ins_m, ins_l, ins_xl, ins_xxl = 0,0,0,0,0,0

# inv counters
inv_sv, inv_s, inv_m, inv_l, inv_xl, inv_xxl = 0,0,0,0,0,0

with open(vcf, "r") as v:
    for line in v:
        if not line.startswith("#") and not "BND" in line:
            fields = line.split("\t")
            ID = fields[2]
            test = re.search(r'\.([A-Z]{3})\.', ID)
            sv = test.group(1)
            svlen = fields[7].split(";")[2]
            test_2 = re.search(r'SVLEN=-?(\d+)', svlen)
            length = int(test_2.group(1))
            if sv == "BND":
                bnd_sv += 1
            if sv == "DEL":
                del_sv += 1
            if sv == "DUP":
                dup_sv += 1
            if sv == "INS":
                ins_sv += 1
            if sv == "INV":
                inv_sv += 1
            if sv == "DEL" and length >= 30 and length <= 1000:
                del_s += 1 
            if sv == "DEL" and length > 1000 and length <= 10000:
                del_m += 1
            if sv == "DEL" and length > 10000 and length <= 100000:
                del_l += 1
            if sv == "DEL" and length > 100000 and length <= 1000000:
                del_xl += 1
            if sv == "DEL" and length > 1000000:
                del_xxl += 1
            if sv == "DUP" and length >= 30 and length <= 1000:
                dup_s += 1
            if sv == "DUP" and length > 1000 and length <= 10000:
                dup_m += 1
            if sv == "DUP" and length > 10000 and length <= 100000:
                dup_l += 1
            if sv == "DUP" and length > 100000 and length <= 1000000:
                dup_xl += 1
            if sv == "DUP" and length > 1000000:
                dup_xxl += 1            
            if sv == "INS" and length >= 30 and length <= 1000:
                ins_s += 1
            if sv == "INS" and length > 1000 and length <= 10000:
                ins_m += 1
            if sv == "INS" and length > 10000 and length <= 100000:
                ins_l += 1
            if sv == "INS" and length > 100000 and length <= 1000000:
                ins_xl += 1
            if sv == "INS" and length > 1000000:
                ins_xxl += 1
            if sv == "INV" and length >= 30 and length <= 1000:
                inv_s += 1
            if sv == "INV" and length > 1000 and length <= 10000:
                inv_m += 1
            if sv == "INV" and length > 10000 and length <= 100000:
                inv_l += 1
            if sv == "INV" and length > 100000 and length <= 1000000:
                inv_xl += 1
            if sv == "INV" and length > 1000000:
                inv_xxl += 1

with open(stats, "w") as s:
    s.write(f"type\tcount\t30-1kb\t1kb-10kb\t10kb-100kb\t100kb-1Mb\t1Mb+\n")
    s.write(f"BND\t{bnd_sv}\t0\t0\t0\t0\t0\n")
    s.write(f"DEL\t{del_sv}\t{del_s}\t{del_m}\t{del_l}\t{del_xl}\t{del_xxl}\n")
    s.write(f"DUP\t{dup_sv}\t{dup_s}\t{dup_m}\t{dup_l}\t{dup_xl}\t{dup_xxl}\n")
    s.write(f"INS\t{ins_sv}\t{ins_s}\t{ins_m}\t{ins_l}\t{ins_xl}\t{ins_xxl}\n")
    s.write(f"INV\t{inv_sv}\t{inv_s}\t{inv_m}\t{inv_l}\t{inv_xl}\t{inv_xxl}\n")
