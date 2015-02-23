# GetBibitem.py
# A quick script to extract all \bibitem{...} entry names from a
# LaTeX file. (Shame on you for not using BibTeX.)
# Flip Tanedo, 11 March 2014
#
# Usage: ./GetBibitem.py input.tex
# For use with (for example) Spires.app which allows easy import of
# bibliographies. (e.g. go to the paper, click on 'refers to',
# highlight all, and press cmnd-b to import all biblio data. Then
# use cmnd-1 to enter "auto update bib" mode, now just use the
# bib items extracted with this script.)

import sys # module for accessing arguments

inputfile = open(sys.argv[1],'r')	# Open spectrum file for reading
output = ''

print "\n"

print "########################################################"
print "## GetBibitem.py                                      ##"
print "##  by Flip Tanedo, flip.tanedo@uci.edu               ##"
print "########################################################\n"

for line in inputfile: 
    if line.startswith('\\bibitem') | line.startswith('%\\bibitem'):
        temp = line.split('{')[1].split('}')[0]
        # print temp+','
        output = output + temp + ', '
        
print output