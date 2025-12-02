#!/usr/bin/env python3
import sys

current_product = None
total_price = 0

for line in sys.stdin:
    product, price = line.strip().split("\t", 2)
    price = float(price)

    if current_product == product:
        total_price += price
    else:
        if current_product is not None:
            print(f"{current_product}\t{total_price}")
        
        current_product = product
        total_price = price

if current_product is not None:
    print(f"{current_product}\t{total_price}")