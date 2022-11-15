import os  # 判断文件内是否有值
from urllib.request import urlopen


def get_time(func):
    def wrapper():
        func()
        print("used time: XXX")

    return wrapper


@get_time
def foo():
    print("foo")


# foo = get_time(foo)
foo()


def f_a(func):
    print("f_a")

    def w_a():
        print(1)
        func()

    return w_a


def f_b(func):
    print('f_b')

    def w_b():
        print(2)
        func()

    return w_b


# @f_a
# @f_b
def f_c():
    print('f_c')
    print(3)


f_a(f_b(f_c))()


def decorator(func):
    def wrapper(**args):
        print("call function")
        return func(**args)

    return wrapper


@decorator
def foo1(**args):
    print("this is foo")
    print(args)


t = {'a': '1', 'b': '2'}
foo1(**t)


def func_out(info):
    def decorator(func):
        def wrapper():
            print(info)
            print("call function")
            return func()

        return wrapper

    return decorator


@func_out(info="hello")
def foo2():
    print("this is foo")


foo2()


def my_loop_1(func):
    def wrapper():
        for i in range(5):
            func()

    return wrapper


def my_loop_2(x):
    def decorator(func):
        def wrapper():
            for i in range(x):
                func()

        return wrapper

    return decorator


# @my_loop_1
@my_loop_2(10)
def hello():
    print("hello 2013125")


hello()


def cache(func):
    def inner(*args, **kwargs):
        if os.path.getsize('web_cache'):  # byte类型
            with open('web_cache', 'rb') as f:
                return f.read()
        ret = func(*args, **kwargs)  # get()
        with open('web_cache', 'wb') as f:  # byte类型
            f.write(b'this is web_cache' + ret)  # 加****判别是否已经存在 #由于是byte类型加上b
        return ret

    return inner


@cache
def get(url):
    code = urlopen(url).read()
    return code


str = get('https://www.baidu.com')
print(str)
str = get('https://www.baidu.com')
print(str)