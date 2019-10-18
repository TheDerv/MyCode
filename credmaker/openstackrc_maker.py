#!/usr/bin/env python3

outFile = open("admin.rc", 'a')
osAUTH = input("What is the OS_AUTH_URL?")
print(f"Export OS_AUTH_URL {osAUTH}", file=outFile)

print("export OS_IDENTITY_API_VERSION=3", file=outFile)

osPROJ = input("What is the OS_PROJECT_NAME?")
print(f"export OS_PROJECT_NAME= {osPROJ}", file=outFile)

osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME?")
print(f"export OS_PROJECT_DOMAIN_NAME= {osPROJDOM}", file=outFile)

osUser = input("What is the OS_USERNAME?")
print(f"export OS_USErNAME= {osUser}", file=outFile)

osUSERDOM = input("What is the OS_USER_DOMAIN_NAME?")
print(f"export OS_USER_DOMAIN_NAME= {osUSERDOM}", file=outFile)

osPASS = input("What is the OS_PASSWORD?")
print(f"export OS_PASSWORD= {osPASS}", file=outFile)

