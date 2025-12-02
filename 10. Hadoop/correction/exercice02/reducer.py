#!/usr/bin/env python3
import sys

cur = None
acc = 0

for line in sys.stdin:
    try:
        key, val = line.rstrip("\n").split("\t", 2)
        v = int(val)
    except ValueError:
        continue

    if key == cur:
        acc += v
    else:
        if cur is not None:
            print(f"{cur}\t{acc}")
        
        cur = key
        acc = v

if cur is not None:
    print(f"{cur}\t{acc}")