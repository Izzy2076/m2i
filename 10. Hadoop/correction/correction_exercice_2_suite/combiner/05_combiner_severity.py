#!/usr/bin/env python3
import sys

current_state = None
total_severity = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    state, severity = line.split('\t')

    try:
        severity_value = int(severity)
    except ValueError:
        continue
    
    if current_state == state:
        total_severity += severity_value
        count += 1
    else:
        if current_state is not None:
            print(f"{current_state}\t{total_severity},{count}")
        
        current_state = state
        total_severity = severity_value
        count = 1

if current_state is not None:
    print(f"{current_state}\t{total_severity},{count}")

