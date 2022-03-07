no1 = float(input("enter the first value: "))
no2 = float(input("enter the second value: "))
option = input('''
chose your option
(a) addition
(b) subtraction
(c) multiplication
(d) division
(e) exponent
option: ''')
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"

if option == a:
    print("your answer is ", no1 + no2)
if option == b:
    if no1 < no2:
        print("your answer is", no2 - no1)
    if no1 > no2:
        print("your answer is", no1 - no2)
if option == c:
    print("your answer is", no1 * no2)
if option == d:
    if no1 < no2:
        print("your answer is", no2 / no1)
    if no1 > no2:
        print("your answer is", no1 / no2)
if option == e:
    f = float(input("enter the power value: "))
    e = float(input("enter the base value: "))
    print("your answer is", e ** f)



