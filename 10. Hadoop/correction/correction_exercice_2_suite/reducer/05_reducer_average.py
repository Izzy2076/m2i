#!/usr/bin/env python3
import sys

current_state = None
total_severity = 0
total_count = 0

for line in sys.stdin:
    line = line.strip()
        
    state, value = line.split('\t')
    
    if ',' in value:
        # Format du combiner: somme,count
        try:
            severity_sum, count = value.split(',')
            severity_sum = int(severity_sum)
            count = int(count)
        except ValueError:
            continue
    else:
        try:
            severity_sum = int(value)
            count = 1
        except ValueError:
            continue
    
    if current_state == state:
        total_severity += severity_sum
        total_count += count
    else:
        if current_state is not None and total_count > 0:
            average = total_severity / total_count
            print(f"{current_state}\t{average:.2f}")

        current_state = state
        total_severity = severity_sum
        total_count = count

if current_state is not None and total_count > 0:
    average = total_severity / total_count
    print(f"{current_state}\t{average:.2f}")

