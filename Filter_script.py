# Filtering script
import pandas as pd
df = pd.read_csv("ARA-main/MZ.screening.analysis.stats.sorted.by.alignment.txt",sep="\t")
df = pd.DataFrame(df)
# Filtering data on alignment rate in Bowtie2
# Only keeping alignment rates above 70%
df['Unique_hits_perc_in_Bowtie2'] = df['Unique_hits_perc_in_Bowtie2'] != '-'
df['Unique_hits_perc_in_Bowtie2'] = df['Unique_hits_perc_in_Bowtie2'].astype(float)
filtered = df[df['Unique_hits_perc_in_Bowtie2'] > 0]
filtered = filtered[['SRA_Run_ID','Unique_hits_perc_in_Bowtie2','isolation_source']]
# Writing to file including SRA id accession number and tissue sampled for abundancy analysis
filtered.to_csv("Filtered_data.csv",sep=",")