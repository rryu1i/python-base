#!/usr/bin/env python3

import sys
import os
import logging
import time

log = logging.Logger("errors")

# LBYL - Look Before You leap

# if os.path.exists("names.txt"):
#     print("O arquivo existe")
#     input("...")  # Race Condition
#     names = open("names.txt").readlines()
# else:
#     print("[Error] File names.txt not found.")
#     sys.exit(1)

# if len(names) >= 3:
#     print(names[2])
# else:
#     print("[Error] Missing name in the list")
#     sys.exit(1)

# EAFP - Easy to Ask forgiveness than permission

def try_to_open_a_file(filepath, retry = 1):
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()  # mesmo se o retry fosse 10, se o return for bem sucessido ele da o break.
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
            time.sleep(2)
        else:  # so ocorre quando nao entra no except
            print("Sucesso!!")
        finally:  # sempre vai rodar
            print("Execute isso sempre!")
    return []


for line in try_to_open_a_file("names.txt"):
    print(line)