flag = False


def func(fun):
    print(flag)
    return fun


@func
def fun2():
    print(flag)
    if flag:
        print("2")


@func
def fun1():
    print("1")
    global flag
    flag = True
    fun2()


fun1()
