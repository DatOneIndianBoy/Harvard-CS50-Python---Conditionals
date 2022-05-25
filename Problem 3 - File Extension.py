# https://cs50.harvard.edu/python/2022/psets/1/extensions/

user_input = input("File Name: ")

if user_input.endswith(".gif"):
    print("image/gif")
elif user_input.endswith(".jpg" or "jpeg"):
    print("image/jpeg")
elif user_input.endswith(".png"):
    print("image/png")
elif user_input.endswith(".pdf"):
    print("application/pdf")
elif user_input.endswith(".txt"):
    print("text/plain")
elif user_input.endswith(".zip"):
    print("application/zip")