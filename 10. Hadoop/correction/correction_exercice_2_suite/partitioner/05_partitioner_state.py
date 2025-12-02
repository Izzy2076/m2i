#!/usr/bin/env python3
import sys, hashlib

num_reducers = int(sys.argv[1]) if len(sys.argv) > 1 else 3

for line in sys.stdin:
    line = line.strip()
    state, _ = line.split('\t')
    partition = hash(state) % num_reducers
    
    print(f"{partition}\t{line}")

