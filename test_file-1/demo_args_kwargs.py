# from https://www.youtube.com/watch?v=GdSJAZDsCZA


def my_func():
    print("Hello, Robert")

my_func()


def my_func():
    print("Hello, Robert")

my_func("abc")



def my_func(*args):
    print("Hello, Robert", args)

my_func("abc", "abc", 123, "abc")


def my_func(key=None, *args):
    print("Hello, Robert", args)

my_func("abc", "abc", 123, "abc", key=123)



def my_func(*args, **kwargs):
    print("Hello, Robert", args, kwargs)

my_func("abc", "abc", 123, "abc", key=123, abc=123)


def my_func(arg_1, *args, **kwargs):
    print("Hello, Robert", args, kwargs)

my_func("abc", abc=123)


def my_func(abc=None, *args, **kwargs):
    print("Hello, Robert", args, kwargs)

my_func(abc=123)


def my_func(abc=None, *args, **kwargs):
    print("Hello, Robert", args, kwargs)

my_func(abc=123, "abc")


def my_func(arg_1, *args, **kwargs):
    print("Hello, Robert", args, kwargs)

my_func("abc", abc=123)


def my_func(*args, **kwargs):
    print("hello, Robert", args, kwargs)

my_func("abc", abc=123)


def my_random_django_view(request, **kwargs):
    print(kwargs)
    #product.objects.get(id=kwargs.get('id'))

#path('my-product/:id')
my_random_django_view("request", id='some_id')
