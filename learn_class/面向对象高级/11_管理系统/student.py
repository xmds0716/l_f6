"""
该文件用于记录 学生类  学生的属性信息为：姓名 性别 年龄 手机号 描述信息
"""
class Student:
    def __init__(self,name,gender,age,phone,desc):
        """
        初始化学生信息
        :param name:    姓名
        :param gender:  性别
        :param age:     年龄
        :param phone:   手机号
        :param desc:    描述信息
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        """
        描述信息
        :return:
        """
        return f"{self.name} {self.gender} {self.age} {self.phone} {self.desc}"


if __name__ == '__main__':
    s = Student("小明","男",38,1234567,"帮主")
    print(s)
