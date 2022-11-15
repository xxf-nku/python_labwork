
def problem1(x):
    return [(1+x)**365, (1-x)**365]

def problem2():
    temp = 1
    for i in range(365):
        for j in range(7):
            if(j < 5):
                temp = temp * 1.01
            else: temp = temp * 0.99
        i += 7
    return temp

def problem3():
    temp = (1+0.01)**365
    temp = temp/ (0.99)**104
    temp = temp**(1 / 261) -1
    return temp


if __name__ == '__main__':
    print('problerm 1')
    # print('每天进退步1‰，一年之后的水平是', '%.3f, %.3f'% problem1(0.001))
    print('每天进退步1‰，一年之后的水平是{0[0]:.3f},{0[0]:.3f}'.format(problem1(0.001)))
    print('每天进退步5‰，一年之后的水平是{0[0]:.3f},{0[0]:.3f}'.format(problem1(0.005)))
    print('每天进退步1%，一年之后的水平是{0[0]:.3f},{0[0]:.3f}'.format(problem1(0.01)))
    print('problem 2')
    print('一年365天，初始水平为1，一周5个工作日，每天进步1%，2个休息日，每天退步1%。一年后的结果是', '%3.f'%problem2())
    print('problem 3')
    print('进步系数是','%.3f'%problem3())




