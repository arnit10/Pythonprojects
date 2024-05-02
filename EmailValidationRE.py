#Using REGEX

# a-z
# 0-9
# . _ => 1 time (dot can be only one time before the mandatory dot)
# @ => 1 time
# . => last fourth or last third position

import re

emailPattern = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

userEmail = input("Please Enter your email id : ")

if re.search(emailPattern , userEmail):
    print("Valid email")
else:
    print("Invalid email!!")