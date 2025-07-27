# decorators in python allows to modify the behavior of functions or methods
# they are often used for logging, access control, instrumentation, caching, etc.

def decorator_function(any_function):
    def wrapper_function():
        print("Something is happening before the function is called.")
        any_function()
        print("Something is happening after the function is called.")

    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

# when we call say_hello(), it will be wrapped by the decorator_function
say_hello()