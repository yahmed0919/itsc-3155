x = int(input("Please enter first number: "))
y = int(input("Please enter second number: "))


def p2(x, y):
    global z
    z = ""
    for a in range(x, y+1):
        if a % 7 == 0 and a % 5 != 0:
            z += str(a)+","
    z = z[:-1]


p2(x, y)
print(z)
