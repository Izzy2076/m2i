#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    product, price = line.split(",")
    print(f"{product}\t{price}")