from collections import Counter
x = input("Input first dictionary: ")
y = input("Input second dictionary: ")

def p3(x, y):
    global z
    z = Counter(x) + Counter(y)
p3(x, y)   
print(z)
