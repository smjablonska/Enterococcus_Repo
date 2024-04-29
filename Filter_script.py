# Filtering script
# Getting rid of entries with 0 hits

import pandas as pd
df = pd.read_csv("ARA-main/results/results/Arabidopsis_thaliana.TAIR10.ncrna/Arabidopsis_thaliana.TAIR10.ncrna.screening.analysis.stats.sorted.by.alignment.txt", sep="\t")

df = pd.DataFrame(df)
filtered = df[df['Unique_hits_perc_in_Bowtie2'] > 0]

print(filtered['Unique_hits_perc_in_Bowtie2'])