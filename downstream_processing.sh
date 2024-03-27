#!/bin/bash
## WORKING SCRIPT FOR DOWNSTREAM PROCESSING OF SEARCHSRA RESULTS ##

# first, download the results
# Copy the url of the results zip archive
curl -Lo results.zip http://141.18.18.16/results/0e1c6dd49b2/results.zip

# uncompress the zip file
unzip results.zip

# combine all results directories
# change number based on how many files are in unzipped file
mkdir bamfiles
for i in $(seq 1 45); do mv $i/* bamfiles/; rmdir $i; done

# remove empty bamfiles
find  . -size- 421c | xargs rm -f

# remake index files
rm -f *.bai
for bamfile in *.bam; do samtools index $bamile; done
