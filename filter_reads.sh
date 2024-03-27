#!/bin/bash

## WORKING SCRIPT TO FILTER SEARCHSRA OUTPUT DATA ##

# clone searchSRA ToolKit Github
git clone https://github.com/linsalrob/SearchSRAToolKit.git

#run filter reads script from toolkit
#filters for matches with a MAPQ alignment >= 20, and an alignment >= 100 nucleotides
./filter_reads.sh -m 20 -l 100 -v -o FILTERED
