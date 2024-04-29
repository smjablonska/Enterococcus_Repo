# Filtering script
import pandas as pd
df = pd.read_csv("ARA-main/results/results/Arabidopsis_thaliana.TAIR10.ncrna/Arabidopsis_thaliana.TAIR10.ncrna.screening.analysis.stats.sorted.by.alignment.txt", sep="\t")

df = pd.DataFrame(df)
# Filtering data on alignment rate in Bowtie2
# Only keeping alignment rates above 70%
filtered = df[df['Unique_hits_perc_in_Bowtie2'] > 70]
filtered = filtered[['SRA_Run_ID','Unique_hits_perc_in_Bowtie2']]

filtered.to_csv("Filtered_data.csv",sep=",")
