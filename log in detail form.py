no1 = input("do you have a account(yes or no): ")
x = "male"
y = "female"
Y = "yes"
z = ""
no2 = "no"
if no1 == no2:
    a = input("do you want an account: ")
    if a == no2:
        print("thank you for visiting us")
    if Y == a:
        no3 = input("your first name: ")
        no4 = input("your last name: ")
        n = input("enter your email addresses: ")
        no0 = input("gender(you can skip this by pressing): ")
        z1 = input("birth day: ")
        no5 = input("username: ")
        no6 = input("password: ")
        no7 = input("confirm password: ")
        no8 = len(no5)
        no9 = len(no6)
        a1 = no3
        a2 = no4
        a3 = no6
        if no8 > 20 or no9 > 20:
            print("username or password is above 20 characters")
        if no8 < 20 or no9 < 20:
            if a3 == a1 or a3 == a1:
                print("your password cannot be a part of your name")
            if a3 != a1 and a3 != a1:
                if no6 != no7:
                    print("your password does not match with the first password")
                if no6 == no7:
                    if no0 == x:
                        print("your account has been created mister " + no3)
                        b1 = input("do you want to log in now mister " + no3 + ":")
                        if b1 == no2:
                            print("thank you for us mister " + no3)
                        if b1 == Y:
                            a4 = input("username: ")
                            a5 = input("password:")
                            b2 = len(a4)
                            b3 = len(a5)
                            c1 = a5
                            if a4 != no5 or a5 != no6:
                                print("your username or password is incorrect", no3)
                            if a4 == no5 and a5 == no6:
                                if c1 == a1 or c1 == a2:
                                    print("your password cannot be a part of your name " + no3)
                                if c1 != a1 and c1 != a2:
                                    if b2 > 20 or b3 > 20:
                                        print("your username or password is incorrect")
                                    if b2 < 20 and b3 < 20:
                                        print("you are logged in mister " + no3)
                    if no0 == y:
                        print("your account has been created miss " + no3)
                        b4 = input("do you want to log in miss " + no3 + ":")
                        if b4 == no2:
                            print("thank you for visiting us miss" + no3)
                        if b4 == Y:
                            a6 = input("username: ")
                            a7 = input("password: ")
                            b5 = len(a6)
                            b6 = len(a7)
                            c2 = a7
                            if a6 != no5 or a7 != no6:
                                print("your username or password is incorrect", no3)
                            if a6 == no5 and a7 == no6:
                                if c2 == a1 or c2 == a2:
                                    print("your password cannot be a part of your name " + no3)
                                if c2 != a1 and c2 != a2:
                                    if b5 > 20 or b6 > 20:
                                        print("your username or password is incorrect")
                                    if b5 < 20 and b6 < 20:
                                        print("you are logged in miss " + no3)
                    if no0 == z:
                        print("your account has been created " + no3)
                        b7 = input("do you want to log in " + no3 + ":")
                        if b7 == no2:
                            print("thank you for visiting us")
                        if b7 == Y:
                            a8 = input("username: ")
                            a9 = input("password: ")
                            b8 = len(a8)
                            b9 = len(a9)
                            c3 = a9
                            if a8 != no5 or c3 != no6:
                                print("your username or password is incorrect", no3)
                            if a8 == no5 and c3 == no6:
                                if c3 == a1 or c3 == a2:
                                    print("your password cannot be a part of your name ")
                                if c3 != a1 and c3 != a2:
                                    if b8 > 20 or b9 > 20:
                                        print("your username or password is incorrect")
                                    if b8 < 20 and b9 < 20:
                                        print("you are logged in " + no3)
if no1 == Y:
    c = input("do you want to log in: ")
    if c == no2:
        print("thank you for visiting us")
    if c == Y:
        h = input("first name: ")
        i = input("second name: ")
        j = h
        k = i
        d = input("username: ")
        e = input("password: ")
        f = len(d)
        g = len(e)
        m = e
        if m == j or m == k:
            print("your password cannot be a part of your name", h)
        if m != j and m != k:
            if f > 20 or g > 20:
                print("your username or password is incorrect")
            if f < 20 and g < 20:
                print("your logged in " + d)
