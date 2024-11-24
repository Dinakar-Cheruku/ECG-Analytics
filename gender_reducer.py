#!/usr/bin/env python3
import sys
from collections import defaultdict

diagnosis_gender = defaultdict(lambda: {"M": 0, "F": 0})

for line in sys.stdin:
    diagnosis, gender = line.strip().split('\t')
    if gender in ["M", "F"]:  # Valid gender values
        diagnosis_gender[diagnosis][gender] += 1

for diagnosis, counts in diagnosis_gender.items():
    print(f"{diagnosis}\tMales: {counts['M']}, Females: {counts['F']}")
