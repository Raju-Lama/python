def last_name_decorator(method):
    def wrapper(self):
        method(self)
        # prints first name

        print("last name")
        # prints last name

    
    return wrapper


class Person:
    def __init__(self, name):
        self.name = name


    @last_name_decorator
    def first_name(self):
        print(f"First name: {self.name}")


per1 = Person("Ram")

per1.first_name()  # This will call the decorated method