#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) > 8:
        diagnosis_categories = ['NORM', 'MI', 'STTC', 'HYP', 'CD']
        try:
            weight = float(parts[4])  # weight column
            for i, diagnosis in enumerate(diagnosis_categories, start=8):  # diagnosis columns
                if int(parts[i]) == 1:
                    print(f"{diagnosis}\t{weight}")
        except ValueError:
            continue
