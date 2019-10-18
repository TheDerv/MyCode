#!/usr/bin/env python3

import os

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
        return result

lookfor = input("what am I looking for? ")
lookwhere = input("Where should I be looking? ")

a = find_all(lookfor, lookwhere)

for x in a:
    print(x)
