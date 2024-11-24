#!/usr/bin/env python3
import sys

# Columns of interest
diagnosis_columns = {
    "NORM": 8,
    "MI": 9,
    "STTC": 10,
    "HYP": 11,
    "CD": 12
}

for line in sys.stdin:
    fields = line.strip().split(',')
    for condition, index in diagnosis_columns.items():
        try:
            if fields[index] == '1':  # If the condition is present
                print(f"{condition}\t1")
        except IndexError:
            continue
