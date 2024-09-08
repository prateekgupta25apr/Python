"""
Decorators

Question:
Create a decorator

"""


def decorator(function_ref):
    def wrapper_function(arg):
        updated_input = arg * 2

        return function_ref(updated_input)

    return wrapper_function


def argument_decorator(val):
    def decorator_function(function_ref):
        def wrapper_function(arg):
            updated_input = arg * 2 * val

            return function_ref(updated_input)

        return wrapper_function

    return decorator_function


@decorator
def actual_function(i):
    return i


print(actual_function(5))
