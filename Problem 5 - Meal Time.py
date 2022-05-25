# https://cs50.harvard.edu/python/2022/psets/1/meal/

def main():
    user_input = input("What time is it? ")
    time = convert(user_input)
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <+ 19.0:
        print("dinner time")
    else:
        print("")

def convert(time):
    hours, minutes = time.split(":")
    min_new = float(minutes) / 60
    return float(hours) + min_new



main()