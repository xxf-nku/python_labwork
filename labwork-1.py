

def f_scale2c_scale(x):
    print("温度（摄氏度）为：{result:.2f}".format(result=5*(x-32)/9))
    return


def main_1():
    print("请输入温度（华氏度）：")
    x = int(input())
    f_scale2c_scale(x)
    return


def is_leapyear(x):
    if x<0:
        print("请输入大于0的年份")
        return
    if (x%4)!=0:
        print("{year}为平年".format(year = x))
        return
    if (x%100)==0 and (x%400)!=0:
        print("{year}为平年".format(year=x))
        return
    print("{year}为润年".format(year=x))
    return


def main_2():
    print("请输入要判断的年份：")
    x = int(input())
    is_leapyear(x)
    return


def getBmi(x, y):
    return y/(x*x)


def getBodyFatPercentage(bmi, age, sex):
    return 1.2 * bmi + 0.23 * age - 5.4 - 10.8 * sex


def printresult(result, sex):
    if sex == 1 and result > 0.18:
        print("先生您好，请注意，您的身体偏胖")
        return
    elif sex == 1 and result < 0.15:
        print("先生您好，请注意，您的身体偏瘦")
        return
    elif sex == 1:
        print("先生您好，恭喜你，身体非常健康，请继续保持")
        return
    elif sex == 0 and result > 0.28:
        print("女士您好，请注意，您的身体偏胖")
        return
    elif sex == 0 and result < 0.25:
        print("女士您好，请注意，您的身体偏瘦")
        return
    else:
        print("女士您好，恭喜你，身体非常健康，请继续保持")
        return



def check_BodyFat(d):
    l = []
    for i in d:
        l.append(float(i))

    if l[0] != 1 and l[0] != 0:
        print("疑似输入性别有误，请检查后再次输入")
        return

    if l[1] <= 0 or l[1] >= 150:
        print("疑似输入年龄有误，请检查后再次输入")
        return
    if l[2] <= 0 or l[2] >= 3:
        print("疑似输入身高有误，请检查后再次输入")
        return
    if l[3] <= 0 or l[3] >= 300:
        print("疑似输入体重有误，请检查后再次输入")
        return
    bim = getBmi(l[2], l[3])
    result = getBodyFatPercentage(bim, l[1], l[0])
    print('%.2f'%result, end="")
    print(' ', end='')
    printresult(result, sex=l[0])
    return


def main_3():
    print("请分别输入性别，年龄，身高(m)，体重(kg)")
    print("其中性别为男，用 1 来表示")
    print("其中性别为女，用 0 来表示")
    print("中间用英语逗号和空格隔开")
    print("这是示例：1, 20, 1.82, 75")
    x = input()
    d = x.split(", ")
    check_BodyFat(d)
    return


def sum_One2Onehundred():
    s = 50*(100+1)
    print(s)


def main_4():
    print("将打印1到100的所有数的和")
    sum_One2Onehundred()
    return


def nine_nine_table():
    for i in range(1,10):
        for j in range(1, i+1):
            print("   {r} * {s} = {k}".format(r=j, s=i, k= i*j),end="")
        print(" ")
    return


def main_5():
    print("将打印九九乘法口诀表")
    nine_nine_table()
    return

def isPrimeNumber(x):
    if(x <= 0):
        print("请输入大于一的自然数")
        return
    i = x**(1/2) +1
    for j in range(1, j):
        if (x%j) == 0:
            print("%d不是素数"%x)
            return
    print("%d是素数"%x)
    return

def main_6():
    print("请输入一个大于一的自然数，我们将判断它是否为素数")
    x = int(input())
    isPrimeNumber(x)
    return


def moveOne(a, c):
    print("%c"%a, " ---> %c"%c)
    return


def tower_hanoi(x, a, b, c):
   if x == 1:
       moveOne(a, c)
       return
   else:
       tower_hanoi(x-1, a, c, b)
       moveOne(a, c)
       tower_hanoi(x-1, b, a, c)
       return
def main_6():
    print("请输入盘子总个数")
    x = int(input())
    tower_hanoi(x, a='A',b='B', c='C')
    return


def main():
    print("一共六个实验程序，分别对应序号 1 2 3 4 5 6")
    while(True):
        print("请输入序号来执行对应程序")
        x = int(input())
        if x == 1:
            main_1()
            continue
        elif x == 2:
            main_2()
            continue
        elif x == 3:
            main_3()
            continue
        elif x == 4:
            main_4()
            continue
        elif x == 5:
            main_5()
            continue
        elif x == 6:
            main_6()
            continue
        else:
            print("请输入正确的序号")
            continue

if __name__ == '__main__':
    main()
