#!/usr/bin/env python3
import sys
from collections import defaultdict

weight_sum = defaultdict(float)
count = defaultdict(int)

for line in sys.stdin:
    diagnosis, weight = line.strip().split('\t')
    try:
        weight = float(weight)
        weight_sum[diagnosis] += weight
        count[diagnosis] += 1
    except ValueError:
        continue

for diagnosis in weight_sum:
    avg_weight = weight_sum[diagnosis] / count[diagnosis]
    print(f"{diagnosis}\t{avg_weight:.2f}")
