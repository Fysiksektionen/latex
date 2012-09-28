# -*- coding: ISO-8859-10 -*-
# Ett litet script som gör en "sångbladsfil" till ett färdigt sångblad i pdf-format
# Färdigt att skrivas ut dubbelsidigt och bara vikas.
# Skrivet av Emil Ringh, F-08, eringh@kth.se

# python Sangblad.py MinSangbladsfil.dvi

import os
import sys

filen=sys.argv[1];
str="dvips -o tempfil.ps " +filen
os.system(str)
os.system("psbook tempfil.ps > tempfil2.ps")
os.system("psnup -W11.5cm -H29.7cm -2 -pa4 tempfil2.ps > Sangblad.ps")
os.system("ps2pdf Sangblad.ps")

os.remove("tempfil.ps")
os.remove("tempfil2.ps")
os.remove("Sangblad.ps")
