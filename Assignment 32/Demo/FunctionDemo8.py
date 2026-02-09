# # Accept: Multiple Parameters
# # Return: Multiple Values

def Marvellous1(Value1,Value2):  # Positional Arguments; Sequence is maintained
    print("Inside Marvellous1 :", Value1,Value2)
    return 11,21,51 #python can return multiple values as tuple. Internally python handles it by
   
def main():
   Result1 = None
   Result2 = None
   Result3 = None

   Result1,Result2,Result3 = Marvellous1("Python",21)
   print("Return value are:", Result1,Result2,Result3)
   
if __name__ == "__main__":
    main()
    

# Notes:
# 1. In Python, functions can accept multiple parameters and return multiple values.
# 2. When returning multiple values, Python automatically packs them into a tuple.
# 3. You can unpack the returned tuple into separate variables when calling the function.
# 4. Can a funtion return another function?Explain Concetually.
# -> Yes, a function can return another function in Python. This is can be explained conceptually as follows:
#    1. Functions are first-class citizens in Python, meaning they can be treated like any other object (e.g., integers, strings).
#    2. When a function returns another function, it is essentially returning a reference to that function.
#    3. This allows for higher-order functions, which can take functions as arguments or return them as results.
#    4. This concept is often used in decorators, callbacks, and functional programming paradigms.  
# 6. This demonstrates how functions can return other functions, enabling dynamic and flexible code structures.                                                