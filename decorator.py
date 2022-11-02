def f1(func):

    def wrapper(*args, **kwargs):
        print("wrapper started")
        func(*args, **kwargs)
        print("wrapper ended")

    return wrapper


@f1
def f(a):
    print(a)


f("Hi")
