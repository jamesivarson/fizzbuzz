def get_start():
    user_input = int(input("Please enter a number: "))
    if user_input < 0:
        print("Number must be greater than 0")
        user_input = int(input("Please enter a number: "))
    return user_input

def get_end(user_start):
    user_input = int(input("Please enter a number greater than " + str(user_start) + ": "))
    if user_input < user_start:
        print("Number must be greater than " + str(user_start))
        user_input = int(input("Please enter a number greater than " + str(user_start) + ": "))
    return user_input