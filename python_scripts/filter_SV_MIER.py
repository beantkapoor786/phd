"""
This script is used to filter out SVs from a vcf file which do not follow Mendelian inheritance laws.
Usage: python filter_MI.py <input.vcf> <output.vcf>
"""

import sys

vcf_1 = sys.argv[1]
vcf_2 = sys.argv[2]

with open(vcf_1, 'r') as f, open(vcf_2, 'w+') as f2:
    for line in f:
        trio_1, trio_2, trio_3 = False, False, False
        if line.startswith('#'):
            f2.write(line)
        else:
            field = line.split('\t')
            sm1 = field[9]
            sm2 = field[10]
            sm1316 = field[11]
            sm1370 = field[12]
            ref = field[13]
            # ------------------------
            # SM1, SM2, and SM1316 trio
            # ------------------------
            if (sm1.startswith('0/0') and sm2.startswith('0/1')) and sm1316.startswith('0/0'):
                trio_1 = True
            elif (sm1.startswith('0/0') and sm2.startswith('0/1')) and sm1316.startswith('0/1'): 
                trio_1 = True
            elif (sm1.startswith('0/0') and sm2.startswith('1/1')) and sm1316.startswith('0/1'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/0')) and sm1316.startswith('0/0'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/0')) and sm1316.startswith('0/1'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/1')) and sm1316.startswith('0/0'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/1')) and sm1316.startswith('0/1'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/1')) and sm1316.startswith('1/1'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('1/1')) and sm1316.startswith('0/1'):
                trio_1 = True
            elif (sm1.startswith('0/1') and sm2.startswith('1/1')) and sm1316.startswith('1/1'):
                trio_1 = True
            elif (sm1.startswith('1/1') and sm2.startswith('0/0')) and sm1316.startswith('0/1'):
                trio_1 = True
            elif (sm1.startswith('1/1') and sm2.startswith('0/1')) and sm1316.startswith('0/1'):
                trio_1 = True
            elif (sm1.startswith('1/1') and sm2.startswith('0/1')) and sm1316.startswith('1/1'):
                trio_1 = True
            # -------------------------
            # SM1, SM2, and SM1370 trio
            # -------------------------
            if (sm1.startswith('0/0') and sm2.startswith('0/1')) and sm1370.startswith('0/0'):
                trio_2 = True
            elif (sm1.startswith('0/0') and sm2.startswith('0/1')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('0/0') and sm2.startswith('1/1')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/0')) and sm1370.startswith('0/0'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/0')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/1')) and sm1370.startswith('0/0'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/1')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('0/1')) and sm1370.startswith('1/1'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('1/1')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('0/1') and sm2.startswith('1/1')) and sm1370.startswith('1/1'):
                trio_2 = True
            elif (sm1.startswith('1/1') and sm2.startswith('0/0')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('1/1') and sm2.startswith('0/1')) and sm1370.startswith('0/1'):
                trio_2 = True
            elif (sm1.startswith('1/1') and sm2.startswith('0/1')) and sm1370.startswith('1/1'):
                trio_2 = True
            # ------------------------
            # SM1316, SM1370, AND REF trio
            # ------------------------
            if (sm1316.startswith('0/0') and sm1370.startswith('0/1')) and ref.startswith('0/0'):
                trio_3 = True
            elif (sm1316.startswith('0/0') and sm1370.startswith('0/1')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('0/0') and sm1370.startswith('1/1')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('0/1') and sm1370.startswith('0/0')) and ref.startswith('0/0'):
                trio_3 = True
            elif (sm1316.startswith('0/1') and sm1370.startswith('0/0')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('0/1') and sm1370.startswith('0/1')) and ref.startswith('0/0'):
                trio_3 = True
            elif (sm1316.startswith('0/1') and sm1370.startswith('0/1')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('0/1') and sm1370.startswith('1/1')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('1/1') and sm1370.startswith('0/0')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('1/1') and sm1370.startswith('0/1')) and ref.startswith('0/1'):
                trio_3 = True
            elif (sm1316.startswith('0/0') and sm1370.startswith('0/0')) and ref.startswith('0/0'):
                trio_3 = True
            if trio_1 and trio_2 and trio_3:
                f2.write(line)
