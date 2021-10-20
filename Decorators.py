# Defining a decorator
def input_upper(function_name):

    # Defining a wrapper
    def wrapper(function_input):

        # Changing function input to uppercase
        function_input_upper = function_input.upper()

        # Updating value of __name__ for wrapper
        setattr(wrapper, "__name__", getattr(function_name, "__name__"))

        # Calling the function
        function_name(function_input_upper)

    # Returning wrapper
    return wrapper


# Using decorator
@input_upper
def print_input(input_string):
    print(input_string)


# Taking input
a = input("Enter your name\n")

# A call to function print_input()
print_input(a)

print(type(print_input))
print(type(input_upper))