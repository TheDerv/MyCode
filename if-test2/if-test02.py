#!/usr/bin/env python3

ipchk = input("Apply an IP Address: ")

ipverify = ipchk.split(".")

count = 0

while count < 3:
    if ipverify[count] <= "255":
        count+1
    else:
        print("Please enter an acutal IPv4 Address")
        count = 3 
else:
    
    if ipchk == "192.168.70.1":
        print(f"Looks like the IP Address of the gateway was set: {ipchk}, this is not recommended")
     
    elif ipchk:    
        print(f"Looks like the IP address was set to: {ipchk}")
    
    else:    
        print("YOU DID NOT PROVIDE INPUT!")


print("Exiting Script")
