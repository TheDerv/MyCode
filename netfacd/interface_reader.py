#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print(f"\n**********************Deatils of Interface {i} **********************")
    try:
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']
    )

    except:
        print("could not collect adapter information")
