# Filtering script
import pandas as pd
import argparse #import the necessary libraries
import sys

#function to parse command line arguments
def check_args(args=None):
    parser = argparse.ArgumentParser(description='Filtering script')
    parser.add_argument('-s', '--screening_analysis',help='path to input file', required='True')
    parser.add_argument('-o','--output',help='path to output file', required='True')
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_args(sys.argv[1:])
infile = args.screening_analysis
outfile = args.output
df = pd.read_csv(infile,sep="\t")
df = pd.DataFrame(df)
# Filtering data on alignment rate in Bowtie2
# Only keeping unique hit percentages above 1.0

df = df.drop(df[df['Unique_hits_perc_in_Bowtie2'] == '-'].index)
df['Unique_hits_perc_in_Bowtie2'] = df['Unique_hits_perc_in_Bowtie2'].astype(float)
filtered = df[df['Unique_hits_perc_in_Bowtie2'] >= 1.000]
filtered = filtered[['SRA_Run_ID','Unique_hits_perc_in_Bowtie2','isolation_source']]
# Writing to file including SRA id accession number and tissue sampled for abundancy analysis
filtered.to_csv("Filtered_data.csv",sep=",")
