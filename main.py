def main():
   import function
   user_start = function.get_start()
   user_end = function.get_end(user_start)
   for i in range(user_start, user_end + 1):
       if (i % 3 == 0) and (i % 5 == 0):
           print("FizzBuzz")
       elif i % 3 == 0:
           print("Fizz")
       elif i % 5 == 0:
           print("Buzz")
       else:
           print(i)
main()