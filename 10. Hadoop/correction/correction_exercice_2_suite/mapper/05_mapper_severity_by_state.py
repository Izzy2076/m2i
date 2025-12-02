#!/usr/bin/env python3
import sys,csv


reader = csv.DictReader(sys.stdin)
for row in reader:
    state = (row.get("State") or "").strip()
    severity = (row.get("Severity") or "").strip()
    
    if state and severity:
        try:
            severity_value = int(severity)
            if 1 <= severity_value <= 4:
                print(f"{state}\t{severity_value}")
        except ValueError:
            continue

