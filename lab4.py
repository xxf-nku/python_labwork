from functools import reduce


def f(x):
    return x*x


def main1():
    r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    s = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(type(r))
    print(type(s))
    print(list(s))
    print(list(r))
    return


def add(x, y):
    return x+y


def main2():
    result = reduce(add, [1, 3, 5, 7, 9])
    print(type(result))
    print(result)
    return


def fn(x, y):
    return x*10+y


def char2int(s):
    return {'0': 0, '1': 1, '2': 2,
            '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def main3():
    result = reduce(fn, map(char2int, '13579'))
    print(result)
    return


def not_empty(s):
    return s and s.strip()


def is_odd(n):
    return n % 2 == 1


def main4():
    result = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
    print(type(result))
    print(list(result))
    print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
    return


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


def main5():
    f = lazy_sum(1, 3, 5, 7, 9)
    print(type(f))
    print(f())
    return


def square(num):
    return num**2


def main6():
    it = [1, 2, 3, 4]
    # squared = list(map(square, it))
    # print(squared)
    # return
    print(list(map(lambda x: x**2, it)))
    return


def main7():
    m = [1, 2, 3, 4]
    res = filter(lambda x: x % 2 == 1, m)
    print(type(res))
    return


def find_prime_number_by_fliter():
    l = []
    for i in range(1, 100):
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i - 1:
                l.append(i)
    return l


def sum_by_reduce(l):
    return reduce(lambda x, y: x + y, l)


def main8():
    l = find_prime_number_by_fliter()
    # print(l)
    s = sum_by_reduce(l)
    print(s)
    return


def normalize_name_by_map():
    print(list(map(lambda x: x.capitalize(), ['lisa', 'JACK', 'Adam'])))
    return


def mysort_by_sorted():
    print(list(sorted([(1,'byd'),(3,'xiaopeng'),(2,'tesla'),(4,'weilai')])))
    return


def count_steps(original_steps=0):
    def wrapper(new_steps):
        nonlocal original_steps
        total_steps = original_steps + new_steps
        original_steps = total_steps
        return original_steps
    return wrapper


def main9():
    count_step = count_steps(10)
    print(count_step(5))
    print(count_step(5))
    print(count_step(8))
    return
if __name__ == '__main__':
    def func_4():
        list_funcs = []
        for i in range(1, 5):
            def wrapper(i):
                print(i)
            list_funcs.append(wrapper(i))
        print(list_funcs)
        return list_funcs

    func_4()