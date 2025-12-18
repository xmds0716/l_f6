"""
__dict__属性：
    它是Python内置的属性 可以把对象转为字典形式
"""
from sympy.stats import StudentT
from student import Student

#把 学生对象 -> 字典形式   属性名做建 属性值做值
s1 = Student("小明","男",38,1234567,"帮主")
print(s1)

my_dict = s1.__dict__
print(my_dict)
print("-"*23)

#把[学生对象，学生对象。学生对象] -> [字典，字典，字典]
s1 = Student("小明","男",38,1234567,"帮主")
s2 = Student('小明','男',12,12334,11111)
s3 = Student('小张','女',13,5667777,122222)
stu_list = [s1,s2,s3]

#列表推导式
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)
print("-"*23)

#把{'name': '小明', 'gender': '男', 'age': 38, 'phone': 1234567, 'desc': '帮主'} -> 学生对象
my_dict = {'name': '小明', 'gender': '男', 'age': 38, 'phone': 1234567, 'desc': '帮主'}
s5 = Student(**my_dict)
print(s5)