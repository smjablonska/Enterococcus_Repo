import argparse
import csv
import pandas as pd

def count_isolations(data):
    isolation_counts = {}
    for row in data:
        isolation_source = row[3] # to be changed later 
        if isolation_source in isolation_counts:
            isolation_counts[isolation_source] += 1
        else:
            isolation_counts[isolation_source] = 1
    return isolation_counts

def save_chi_square_data(counts, output_file):
    df = pd.DataFrame(counts.items(), columns=['Isolation Source', 'Observed Frequency'])
    df.to_csv(output_file, index=False)

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