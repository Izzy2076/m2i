#!/usr/bin/env python3
import sys

"""
hadoop 1
hadoop 1
hadoop 1
test 1
test 1
test 1
c'est 1
un 1
"""

current_word = None
acc = 0

for line in sys.stdin:
    try :
        key, val = line.rstrip('\n').split("\t", 2)
        v = int(val)
    except ValueError:
        continue

    if key == current_word:
        acc += v
    else:
        if current_word is not None:
            print(f"{current_word}\t{acc}")

        current_word = key
        acc = v

# Traitement de la dernière clé après la fin de la boucle
if current_word is not None:
    print(f"{current_word}\t{acc}")