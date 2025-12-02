#!/usr/bin/env python3
import sys, re

IP_reg = re.compile(r"^\S+")
REQ_reg = re.compile(r'"([^"]*)"')
CODE_reg = re.compile(r"\s(\d{3})\s")

for line in sys.stdin:
    ip_search = IP_reg.search(line)
    req_search = REQ_reg.search(line)
    code_search = CODE_reg.search(line)

    if not (ip_search and req_search and code_search):
        continue

    ip = ip_search.group(0)
    req = req_search.group(1)
    code = code_search.group(1)

    # IP
    print(f"IP:{ip}\t1")

    if code.startswith(("4", "5")):
        print("ERR:ALL\t1")
        print(f"ERR:{code}\t1")

    split_req = req.split(" ")
    if split_req[0] == "POST" and split_req[1] == "/wp-login.php":
        print(f"WPLOGIN:{ip}\t1")
    