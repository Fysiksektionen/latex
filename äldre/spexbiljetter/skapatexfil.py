# -*- coding: utf-8 -*-

import os, sys

# Funktion för att bygga upp LaTeX-kommandot
# \biljett{<sektion>}{<bänk>}{<plats>}
def biljettstring(section, rowandside, seat):
	return '\\biljett{{{0}}}{{{1}}}{{{2}}}\\newpage'.format(section, rowandside, seat)

def cleanside(string):
    return string.replace('Höger', '\\hoger').replace('Vänster', '\\vanster')

# Namnet på listan med platser på teatern tas från första kommandoargumentet
theatredef = sys.argv[1]

theatre = []
with open(theatredef, 'r') as f:
    for l in f.readlines():
        # För att kommentera i listan fungerar både # (som i python) och % (som i LaTeX)
        if l.startswith('#') or l.startswith('%'):
            continue

        # Hämta ut informationen från innevarande rad...
        section, row, seat, side = cleanside(l.strip()).split(',')
        # ...och spara den i en lätthanterad tuppel
        theatre.append((section, row + ' ' + side, seat))

# Bygg upp en gigantisk sträng med kommandon för alla biljetterna
biljetter = ''
for location in theatre:
    section, rowandside, seat = location
    biljetter += biljettstring(section, rowandside, seat)

# Kopiera biljettmall.tex till stdout, och ersätt \biljetter med
# den gigantiska strängen.
with open('biljettmall.tex', 'r') as template:
    for line in template.readlines():
        print line.replace("\\biljetter", biljetter)
            

