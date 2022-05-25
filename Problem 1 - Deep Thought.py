# https://cs50.harvard.edu/python/2022/psets/1/deep/

user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user_input = user_input.lower()

if user_input == "42":
    print("Yes")
elif user_input == "forty two":
    print("Yes")
elif user_input == "forty-two": 
    print("Yes")
else:
    print("No")