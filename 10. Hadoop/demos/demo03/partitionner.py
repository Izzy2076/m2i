#!/usr/bin/env python3
import sys, hashlib

nb_reducers = int(sys.argv[1]) if (sys.argv) > 1 else 3

for line in sys.stdin:
    product, price = line.strip().split("\t")

    partition = hash(product[0]) % nb_reducers
    print(f"{partition}\t{product}\t{price}")