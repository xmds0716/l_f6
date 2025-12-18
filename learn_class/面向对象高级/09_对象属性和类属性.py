"""
属性介绍：
    他是一个名词 用来描述事物的外在特征
分类：
    对象属性：属于每个对象的 即： 每个对象的属性值可能都不同 修改A对象的属性 不影响对象B
    类属性 ：属于类的 即：能被该类下所有的类对象所共享 A对象修改类的属性 B对象访问的是修改后的

对象属性：
    定义到init魔法方法中的属性 每个对象都有自己的内容
    只能通过 对象名. 的方式调用
类属性：
    定义到类中 函数外的属性（变量） 能被该类下所有的对象共享
    既能通过 类名. 还能通过 对象名. 的方式来调用 推荐使用 类名. 的方式
"""
class Student:
    #定义类属性
    teach_name = "王老师"
    #定义对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名：%s 年龄：%d" %(self.name, self.age)

if __name__ == '__main__':
    #对象属性
    s1 = Student("小明",18)
    s2 = Student("小美",19)
    #修改s1的属性
    s1.name = "小张"
    s1.age = 20
    print(s1)
    print(s2)

    print("-"*23)
    #类属性
    #类属性可以通过 类名. 和 对象名. 的方式调用
    print(s1.teach_name)
    print(s2.teach_name)
    print(Student.teach_name)

    #s1.teach_name = "刘老师"  只能给s1的对象赋值
    #如果要修改类变量的值 只能通过 类名. 的方式来实现
    Student.teach_name = "刘老师"
    print(s1.teach_name)
    print(s2.teach_name)
    print(Student.teach_name)