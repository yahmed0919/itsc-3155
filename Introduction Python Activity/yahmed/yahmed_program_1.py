x = str(input("Please enter a string: "))


def p1(x):
    y = len(x)
    if y > 2:
        print(x[:2], x[y - 2:], sep='')
    else:
        if y == 2:
            print(x[:2], x[:2], sep='')
        else:
            print("Your string is too short!")


p1(x)
