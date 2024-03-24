# Advanced Decorators
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        result = function(args[0], args[1], args[2])
        print(f"It returned: {result}")

    return wrapper_function


@logging_decorator
def a_function(a, b, c):
    return a * b * c


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("Gaurav")
# new_user.is_logged_in = True
create_blog_post(new_user)
