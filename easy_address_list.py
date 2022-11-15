import time

user_dict = {'Jack': '123456', 'Auther': '11223344', 'John': '654321', 'Steve': '666888'}
my_flag = False


def my_log(func):
    def wrapper(a):
        start = time.perf_counter()
        func(a)
        end = time.perf_counter()
        f = open('mylog.txt','a')
        # print(func.__name__)
        # print(str(end - start))
        f.write('\n'+func.__name__+'\n')
        f.write('\n'+str(end-start)+'s\n')
        f.close()
    return wrapper


def user_identify(user_dict=user_dict):
    def wrapper(func):
        def decorator(address_list):
            global my_flag
            # print(myflag)
            if my_flag:
                return func(address_list)
            print("请先登录")
            name = input("请输入用户名：")
            password = input("请输入密码：")
            if name in user_dict:
                if password == user_dict[name]:
                    print("登录成功")
                    my_flag = True
                    return func(address_list)
                else:
                    print("密码错误，请重试")
                    decorator(address_list)
                    return
            else:
                print('用户不存在，请重试')
                decorator(address_list)
                return

        return decorator

    return wrapper


@user_identify()
@my_log
def list_add(address_list):
    l_temp = []
    print("请输入姓名：", end="")
    name = input()
    l_temp.append(name)
    print("请输入QQ:", end="")
    qq = input()
    l_temp.append(qq)
    print("请输入电话号码：", end="")
    phone_num = input()
    l_temp.append(phone_num)
    print("请输入邮箱地址：", end="")
    mail_adr = input()
    l_temp.append(mail_adr)
    address_list.append(l_temp)
    print("插入成功！ 此时表为")
    list_show(address_list=address_list)
    return


@user_identify()
@my_log
def list_remove(address_list):
    print('请输入要删除的序号：', end='')
    num = int(input())
    if len(address_list) == 0:
        print('列表为空')
        return
    if num in list(range(1, len(address_list) + 1)):
        print('将要删除的信息如下')
        print(address_list.pop(num - 1))
        print('已删除,此时列表为')
        list_show(address_list=address_list)
    else:
        print('输入的序号不存在，请重新输入')
        list_remove(address_list=address_list)
        return
    return


@user_identify()
@my_log
def list_find(address_list):
    print('请输入要查找的序号：', end='')
    num = int(input())
    if len(address_list) == 0:
        print('列表为空')
        return
    if num in list(range(1, len(address_list) + 1)):
        print('查找成功，结果为')
        print('=' * 54)
        print("{:<6}{:<10}{:<10}{:<14}{:<14}".format('NO.', 'Name', 'QQ', 'Phone', 'E-mail'))
        print("{:<6}{:<10}{:<10}{:<14}{:<14}".format(
            num, address_list[num - 1][0], address_list[num - 1][1], address_list[num - 1][2],
            address_list[num - 1][3]))
        print('=' * 54)
    else:
        print('输入的序号不存在，请重新输入')
        list_find(address_list=address_list)
        return
    return


@user_identify()
@my_log
def list_change(address_list):
    print('请输入要修改的序号：', end='')
    num = int(input())
    if len(address_list) == 0:
        print('列表为空')
        return
    if num in list(range(1, len(address_list) + 1)):
        pass
    else:
        print('输入的序号不存在，请重新输入')
        list_change_1(address_list=address_list)
        return
    list_change_2(address_list=address_list, num=num)
    return


def list_change_1(address_list):
    print('请输入要修改的记录序号：', end='')
    num = int(input())
    if num in list(range(1, len(address_list) + 1)):
        pass
    else:
        print('输入的序号不存在，请重新输入')
        list_change_1(address_list=address_list)
        return
    list_change_2(address_list=address_list, num=num)
    return


def list_change_2(address_list, num):
    print('请输入要修改的子项：')
    print(' ' * 7 + 'n : 修改姓名')
    print(' ' * 7 + 'q : 修改QQ')
    print(' ' * 7 + 'p : 修改电话')
    print(' ' * 7 + 'm : 修改邮箱')
    option = input()
    if option == 'n':
        list_change_name(address_list=address_list, num=num)
    elif option == 'q':
        list_change_qq(address_list=address_list, num=num)
    elif option == 'p':
        list_change_phone_number(address_list=address_list, num=num)
    elif option == 'm':
        list_change_mail(address_list=address_list, num=num)
    else:
        print('没有对应的选项。请重新输入')
        list_change_2(address_list=address_list, num=num)
        return
    print('已完成，此时列表为')
    list_show(address_list=address_list)
    return


def list_change_name(address_list, num):
    print('请输入新的名字, 若不修改请输入空格', end='')
    name = input()
    if name == ' ':
        print('不修改')
        return
    else:
        address_list[num - 1][0] = name
    return


def list_change_qq(address_list, num):
    print('请输入新的QQ, 若不修改请输入空格', end='')
    name = input()
    if name == ' ':
        print('不修改')
        return
    else:
        address_list[num - 1][1] = name
    return


def list_change_phone_number(address_list, num):
    print('请输入新的电话, 若不修改请输入空格', end='')
    name = input()
    if name == ' ':
        print('不修改')
        return
    else:
        address_list[num - 1][2] = name
    return


def list_change_mail(address_list, num):
    print('请输入新的邮箱, 若不修改请输入空格', end='')
    name = input()
    if name == ' ':
        print('不修改')
        return
    else:
        address_list[num - 1][3] = name
    return


@user_identify()
@my_log
def list_show(address_list):
    print("=" * 54)
    print("{:<6}{:<10}{:<10}{:<14}{:<14}".format('NO.', 'Name', 'QQ', 'Phone', 'E-mail'))
    for i in range(len(address_list)):
        print("{:<6}{:<10}{:<10}{:<14}{:<14}".format(i + 1, address_list[i][0],
                                                     address_list[i][1], address_list[i][2], address_list[i][3]))
    print('=' * 54)
    return

def main():
    global my_flag
    print("#" * 15, end="")
    print("  NKCS InfoSystem V0.1  ", end="")  # 24 characters
    print("#" * 15)
    # all characters are 54
    print("=" * 13, end="")
    print("  Powered by xiaoxiongfeng  ", end="")  # 28 characters
    print("=" * 13)
    print(" " * 54)
    print(" " * 54)
    print(" " * 23, end="")
    print("a : 增加记录", end="")
    print(" " * 23)
    print(" " * 23, end="")
    print("d : 删除记录", end="")
    print(" " * 23)
    print(" " * 23, end="")
    print("c : 修改记录", end="")
    print(" " * 23)
    print(" " * 23, end="")
    print("f : 查找记录", end="")
    print(" " * 23)
    print(" " * 23, end="")
    print("s : 展示记录", end="")
    print(" " * 23)
    # information_label
    address_list = []
    while True:
        print("请输入功能对应的代号：", end="")
        x = input()
        if x == 'a':
            list_add(address_list=address_list)
            my_flag = True
            continue
        elif x == 'd':
            list_remove(address_list=address_list)
            my_flag = True
            continue
        elif x == 'c':
            list_change(address_list=address_list)
            my_flag = True
            continue
        elif x == 'f':
            list_find(address_list=address_list)
            my_flag = True
            continue
        elif x == 's':
            list_show(address_list=address_list)
            my_flag = True
            continue
        else:
            print("没有对应的代号，请重新输入")
            continue

    return


if __name__ == "__main__":
    main()
