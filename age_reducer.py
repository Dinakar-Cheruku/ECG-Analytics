#!/usr/bin/env python3
import sys
from collections import defaultdict

diagnosis_ages = defaultdict(list)

for line in sys.stdin:
    diagnosis, age = line.strip().split('\t')
    try:
        diagnosis_ages[diagnosis].append(float(age))
    except ValueError:
        continue

for diagnosis, ages in diagnosis_ages.items():
    avg_age = sum(ages) / len(ages)
    print(f"{diagnosis}\t{avg_age:.2f}")
