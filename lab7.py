from random import randint


class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Account:
    def __init__(self):
        self.user_list = []  # 用户列表，数据格式：[User 对象, User 对象, User 对象]

    def login(self):
        """
        用户登录，用户输入用户名和密码并去 self.user_list 中检查用户是否合法
        """
        name = input("请输入用户名：")
        password = input("请输入密码：")
        user = User(name, password)
        for i in range(len(self.user_list)):
            if user == self.user_list[i]:
                print("登录成功")
                return True
            else:
                print('登录失败')
                return False

    def register(self):
        """
        用户注册，动态创建 User 对象，并添加到 self.user_list 中
        """
        name = ''
        pwd = ''
        for i in range(6):
            name += chr(randint(0, 25) + 97)
            pwd += str(randint(0, 9))
        user1 = User(name, pwd)
        self.user_list.append(user1)
        print(name, pwd)
        return

    def run(self):
        """
        主程序，先进行 2 次用户注册，再进行用户登录（3 次重试机会）
        """
        self.register()
        self.register()
        if self.login():
            return
        elif self.login():
            return
        elif self.login():
            return
        else:
            print("三次机会已用完")


class Circle:
    def __init__(self, r):
        self.r = float(r)

    def circumference(self):
        cir = round(3.1415926 * self.r * 2, 2)
        print(cir)
        return cir

    def square(self):
        squ = round(3.1415926 * self.r * self.r, 2)
        print(squ)
        return squ


class Func:
    def __init__(self, a):
        self.a = a

    def func(self):
        print(self.a)


if __name__ == "__main__":
    # obj = Account()
    # obj.run()
    # x = input("请输入半径: ")
    # obj = Circle(x)
    # obj.square()
    # obj.circumference()
    obj = Func("hello world")
    obj.func()
