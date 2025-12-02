#!/usr/bin/env python3
# Shebang : indique que le script doit être exécuté en python3
import sys, re
# Pour accéder aux flux d'entrée/sortie

word_re = re.compile(r"\w+", flags=re.UNICODE)
# re.UNICODE => pour prendre en compte les caractères speciaux

for line in sys.stdin:
    for word in word_re.findall(line.lower()):
        print(f"{word}\t1")