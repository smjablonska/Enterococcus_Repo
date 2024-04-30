# Need input from docker
# Outputs png image of bar plot and results of chi squared analysis
import argparse #import the necessary libraries
import sys
import os

#function to parse command line arguments
def check_args(args=None):
    parser = argparse.ArgumentParser(description='Enterococcus wrapper script')
    parser.add_argument('-s', '--screening_analysis',help='path to input file', required='True')
    parser.add_argument('-o','--output',help='path to output file', required='True')
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_args(sys.argv[1:])
infile = args.screening_analysis
outfile = args.output

# Running filtering script
os.system("python3 Filter_script.py -s {} -o Filtered_data.csv".format(infile))

# Running isolation source counting script
os.system("python3 DataProcessingCode.py Filtered_data.csv isolation_counts.csv")

# Running statistics script

os.system("Rscript Chi\ Sq\ R\ Script -f isolation_counts.csv -o {}".format(outfile))