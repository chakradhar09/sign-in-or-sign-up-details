import math

op = input('''chose a option:
 a) find the roots of a quadratic equation
 b) form a quadratic equation from its roots
  (option):''')
a = "a"
b = "b"
if op == a:
    instruction = "your quadratic equation is in the form of ax^2+bx+c=0"
    print(instruction)
    f = float(input("enter the value a: "))
    s = float(input("enter the value b: "))
    c = float(input("enter the value c: "))
    D = s ** 2 - 4 * f * c
    if D == 0:
        d = format(((-s + math.sqrt(D)) / 2 * f), '.2f')
        e = format(((-s - math.sqrt(D)) / 2 * f), '.2f')
        print("the roots of the equation are real and equal, the root is  ", d, e)
    if D > 0:
        a = format(((-s + math.sqrt(D)) / 2 * f), '.2f')
        b = format(((-s - math.sqrt(D)) / 2 * f), '.2f')
        print("the roots are real and different, those roots are", a, b)
    if D < 0:
        print("the given equation have imaginary roots")
if op == b:
    e = float(input("enter the first root: "))
    g = float(input("enter the second root: "))
    h = float(e + g)
    i = float(e * g)
    if h < 0 and i < 0:
        print("the quadratic equation is x^2", "+", -h, "x", "-", -i, "= 0")
    if h < 0 and i > 0:
        print("the quadratic equation is x^2", "+", -h, "x", "+", i, "= 0")
    if h > 0 and i < 0:
        print("the quadratic equation is x^2", "-", h, "x", "-", -i, "= 0")
    if h > 0 and i > 0:
        print("the quadratic equation is x^2", "-", h, "x", "+", i, "= 0")
    if h == 0 and i == 0:
        print("there is no equation")

