#!/bin/bash

## WORKING SCRIPT TO FILTER SEARCHSRA OUTPUT DATA ##

set -euo pipefail
results="results"
zipfile="results.zip"
mapq=3
length=50
verbose=n
version=0.1
outdir="./"

usage=$(cat <<-EOF
$0
Version $version

Please provide one of either:
-z --zip      The path to the file (usually called results.zip) that you downloaded from SearchSRA
-r --results  The directory with the uncompressed results (e.g. if you have extracted results.zip)
-o --outdir   The directory to write the results (default: $outdir)

-l --length   Minimum alignment length for the sequences to keep the alignment. Default: $length
-m --mapq     Minimum MAPQ (mapping quality) score to keep the alignment. Default $mapq

-v --verbose  More output

-h --help     Print this message and exit

EOF
)
