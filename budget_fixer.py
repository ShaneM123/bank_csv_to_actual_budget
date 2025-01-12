#!/usr/bin/env python3
import csv

input_file = '<INPUT_FILE>.csv'
output_file = '<WHATEVER_PTAH_YOU_WANT>/formatted_budget.csv'

with open(input_file, 'r', encoding='latin1') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter=';')
    writer = csv.writer(outfile)
    
    # Write the header for the output CSV
    writer.writerow(['Date', 'Payee', 'Notes', 'Category', 'Amount'])
    
    # Skip the initial lines until the transactions start
    for _ in range(10):
        next(reader)
    
    # Process each transaction line
    for row in reader:
        if len(row) < 9:
            continue
        date = row[0]
        payee = row[2]
        notes = row[3] + ' ' + row[4]
        category = 'Unknown'  # You can set a default category or map it based on the payee or notes
        amount = row[7].replace('.', '').replace(',', '.')
        
        writer.writerow([date, payee, notes, category, amount])

print(f"Formatted CSV saved to {output_file}")