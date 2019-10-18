#!/usr/bin/env python3

import urllib.request
import re

print("where should we search?\n")
url = input()
print(f"Great! So we will be opeing this URL: {str(url)} to search for the phrase:\n")
searchFor = input()
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No Match!")
