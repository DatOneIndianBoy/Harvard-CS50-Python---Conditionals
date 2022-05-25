# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

user_input = input("Expression: ")

x, y, z = user_input.split()

x_new = float(x)
z_new = float(z)

if y == "+":
    print(x_new+z_new)
elif y == "-":
    print(x_new-z_new)
elif y == "*":
    print(x_new*z_new)
elif y == "/":
    print(x_new/z_new)