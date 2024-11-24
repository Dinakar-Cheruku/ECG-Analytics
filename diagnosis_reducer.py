#!/usr/bin/env python3
import sys
from collections import defaultdict

diagnosis_count = defaultdict(int)

for line in sys.stdin:
    diagnosis, count = line.strip().split('\t')
    diagnosis_count[diagnosis] += int(count)

for diagnosis, count in diagnosis_count.items():
    print(f"{diagnosis}\t{count}")
