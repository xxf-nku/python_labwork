# 代码细节要求
# - 不要使用数据库，请使用面向对象的方式存储关联。持久化可以考虑使用文件存储。我们的目的是为了让大家熟悉面向对象的操作，所以有违实际业务逻辑，大家见谅🐱！
# - 由于系统庞大，下面只展示部分逻辑，同学们只需要能够实现下面的目的就可以了。
# - 注意抓大放小，例如电话号码的格式验证等就不用过分在意了。
# - 使用控制台交互即可，不需要设计gui。
# - 下面的所有要求只是抛砖引玉，大家可以根据自己的理解增删内容。
#
# 目的
# 利用面向对象的思想，设计一个培训机构管理系统，并设计控制台交互系统。
# 作为系统的管理员，可以实现以下操作：
# 1. 总部与分校区模块
#   1. 设立一个总部和三个分校区
#   2. 查看任意校区的员工数量，教师数量，学生数量
#   3. 查看任意校区的收入
class campus:
    pass

# 4. 课程模块
#   1. 添加新课程，输入基本信息（名称，价格，校区）
#   2. 为课程指定授课教师（一名，请展示授课教师列表让用户选择）
#   3. 查看该课程的学生列表

class Person:
    def __init__(self, name, phone, campus):
        self.name = name
        self.phone = phone
        self.campus = campus

    def get_info_base(self):
        return self.name, self.phone

    def get_info_more(self):
        return self.campus


# 2. 学生模块
#   1. 填写学生信息（姓名，电话，校区，学号），加入到班级，缴纳学费
#   2. 查看学生所在班级，所在校区，参与的课程
#   3. 学生退学
#   4. 查看学生的个人信息（姓名，电话）

class Student(Person):
    stu_list = {}

    def __init__(self, name, phone, campus, id, classid, fee):
        super.__init__(name, phone, campus)
        self.id = id
        self.list_id = len(Student.stu_list)
        self.class_id = classid
        self.lessons = []
        self.fee = fee
        Student.stu_list.update({self.list_id: self})

    def get_info_more(self):
        return self.campus, self.class_id, self.lessons

    def dropped(self):
        Student.stu_list.pop(self.list_id)

    def add_lesson(self, lesson):
        self.lessons.append(lesson)


# 3. 教师模块
#   1. 添加新教师基本信息（姓名，电话，校区，工号）
#   2. 设置教师的授课课程（可以有多门，请展示授课教师列表让用户选择）
#   3. 查看教师的基本信息
#   4. 查看教师所在的校区，教授的课程

class Teacher(Person):
    tea_list = {}

    def __init__(self, name, phone, campus, id):
        super.__init__(name, phone, campus)
        self.id = id
        self.lessons = []
        self.list_id = len(Teacher.tea_list)
        Teacher.tea_list.update({self.list_id: self})

    def get_info_base(self):
        return self.name, self.phone, self.campus, self.id

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def get_info_more(self):
        return self.campus, self.lessons


# 5. 员工模块
#   1. 员工有后勤，财务，行政三种类型
#   2. 添加新员工，在添加时就需要指定员工类型（利用继承），包含员工的个人信息（姓名，工号，校区）
#   3. 展示员工信息
class Officer(Person):
    off_list = {}

    def __init__(self, name, id, campus):
        super.__init__(name, 0, campus)
        self.id = id
        self.list_id = len(Officer.off_list)
        Officer.off_list.update({self.list_id:self})



