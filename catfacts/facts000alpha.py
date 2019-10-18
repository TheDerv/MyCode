#!/usr/bin/env python3

import requests

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    c = 1
    for catfact in r.json()['all']:
        print(f"\nCat Fact #{c}: {catfact.get('text')}")
        c +=1
        s = 0
        for i in catfact.get('text'):
            s +=1

        while s >= 0:
            print("#", end="")
            s -=1
        print("\n")
main()
