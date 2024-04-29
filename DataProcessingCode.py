import argparse
import csv
import pandas as pd
 
##This def function will read through the data and count the occurences of each isolation source in Row 49, isolation_source. 
# The row number may need to be changed depending on the the intial dataset. 
def count_isolations(data):
    isolation_counts = {}
    for row in data:
        isolation_source = row[49] # to be changed if needed
        if isolation_source in isolation_counts:
            isolation_counts[isolation_source] += 1 # this will add a +1 count to the isolation source if it already exsists in the dictionary
        else:
            isolation_counts[isolation_source] = 1 # this will add a new isolation source if it doesn't exists in the dicitonary and set the count to 1. 
    return isolation_counts 

# this def function will take the counts and the lotcation of the output file and save the results from the data above into the output file. The output file will be used for a Goodness of Fit Chi Sq test 
def save_chi_square_data(counts, output_file): 
    df = pd.DataFrame(counts.items(), columns=['Isolation_Source', 'Observed_Frequency']) # this line will create a pandas dataframe from the counts. It will seperate the data into 2 
                                                                                            # columns, Isolation Source and Observed Freqeuncy. 
    df.to_csv(output_file, index=False)


# Argparse syntax to run on the command line and get the file paths needed
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count isolations and save data for Chi-square test')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('output_file', type=str, help='Path to save the Chi-square data')
    args = parser.parse_args()

    with open(args.input_file, 'r') as f:
        reader = csv.reader(f)
        next(reader)  
        data = list(reader)

    counts = count_isolations(data) 
    save_chi_square_data(counts, args.output_file)