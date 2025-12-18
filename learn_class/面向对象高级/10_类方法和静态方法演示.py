"""
类方法：
    属于类的方法 可以通过  类名. 或者 对象名. 的方式来调用
    定义类方法的时候 必须使用 装饰器 @classmethod 且第一个参数必须表示 类对象

静态方法：
    属于该类下所有对象所共享的方法 可以通过 类名. 或者 对象名. 的方式来调用
    定义静态方法的时候 必须使用装饰器 @staticmethod 且参数传不传都可以

区别：
    1.类方法的第一个参数必须是 类对象  静态方法无参数的特殊要求
    2.可以理解为： 如果函数中要使用 类对象 就定义成类方法   否则定义成 静态方法    除此之外 并无任何去别
"""
class Student:
    #定义类对象
    school = "黑马"

    #定义类方法
    @classmethod
    def show1(cls):
        print(cls.school)
        print("类方法")

    #定义静态方法
    @staticmethod
    def show2():
        print(Student.school)
        print("静态方法")

if __name__ == '__main__':
    s1 = Student()
    s1.show1()
    s1.show2()