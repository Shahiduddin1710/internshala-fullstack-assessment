#!/bin/bash

URL="https://raw.githubusercontent.com/datasets/s-and-p-500-companies/refs/heads/main/data/constituents.csv"

curl -s "$URL" | python3 -c '
import sys
import csv

reader = csv.DictReader(sys.stdin)

rows = []

for row in reader:
    rows.append((
        row["Name"],
        row["Location"],
        row["Founded"]
    ))

for name, location, year in sorted(rows, key=lambda x: x[2]):
    print(f"{name} | {location} | {year}")
'
