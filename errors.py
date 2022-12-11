#!/usr/bin/env python3

import sys
import os

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

try:
    names = open("names.txt").readlines()
# except:  # Bare Except
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:  # so ocorre quando nao entra no except
    print("Sucesso!!")
finally:  # sempre vai rodar
    print("Execute isso sempre!")


try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)