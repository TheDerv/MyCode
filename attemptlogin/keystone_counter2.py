#!/usr/bin/env python3

loginfail = 0
loginsuccess = 0
with open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r') as kfile:

    for line in kfile:
        if '- - - - -] Authorization failed' in line:
            loginfail += 1
            print(line.split(" ")[-1], end="")

        if '- - - - -] Loaded 2 encryption keys' in line:
            loginsuccess += 1


print(f"The number of failed login attempts is: {loginfail}")
print(f"The number of successful logins is: {loginsuccess}")


