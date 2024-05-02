#e-mail validation

email = input("Please enter your email id :  ")

j , k , d = 0 , 0 , 0

if len(email) >=6:  #g@g.in
    if email[0].isalpha():  #a@g.com => as e-mail can only consist of first character as alphabet only.
        if ("@" in email) and (email.count("@") == 1): #email should consist of one compulsory '@'
            if (email[-4] == ".") ^ (email[-3] == "."): #.in or .com two possibility
                for i in email:
                    if i == i.isspace():    #email can't consist space
                        j = 1
                    elif i.isalpha():
                        if i ==  i.upper(): #email can't consist uppercase letters
                           k = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "@" or i == "." :
                        continue
                    else :
                        d = 1
                if j == 1 or k == 1 or d == 1:
                    print("Invalid email!! #5")
                else : 
                    print("Valid email") 
            else:
                print("Invalid email!! #4")
        else :
            print("Invalid email!! #3")
    else:
        print("Invalid email!! #2")
else:
    print("Invalid email!! #1")