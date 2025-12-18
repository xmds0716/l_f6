"""
该文件用于 完成学生管理系统的 具体业务的操作 即：增删改查
"""
from sympy.solvers.diophantine.diophantine import prime_as_sum_of_two_squares

from student import Student
import time

#创建管理系统
class StudntCMS(object):
    #初始化信息
    def __init__(self):
        self.stu_list = []
        #self.stu_list = [Student('小明','男',12,12334,11111),
        #                 Student('小张','女',13,5667777,122222)]

    #定义函数 实现打印 管理系统界面
    @staticmethod
    def show_view():
        print("*"*23)
        print("本管理系统操作如下")
        print("\t1.添加学员")
        print("\t2.删除学员")
        print("\t3.修改学员")
        print("\t4.查询某个学员信息")
        print("\t5.查询所有学员信息")
        print("\t6.保存信息")
        print("\t0.退出系统")
        print("*"*23)

    #添加学生信息
    def add_student(self):
        name = input("录入学生姓名：")
        gender = input("录入学生性别：")
        age = int(input("录入学生年龄："))
        phone = input("录入学生手机号：")
        desc = input("录入学生描述：")
        stu = Student(name,gender,age,phone,desc)
        self.stu_list.append(stu)
        print(f"添加{name}信息成功!")

    #删除学生信息
    def del_student(self):
        del_name = input("删除学生姓名：")
        for stu in self.stu_list:
            if stu.name == del_name:
                self.stu_list.remove(stu)
                print("删除完成\n")
                break
        else:
            print("未找到\n")

    #修改学生信息
    def update_student(self):
        upd_name = input("删除学生姓名：")
        for stu in self.stu_list:
            if stu.name == upd_name:
                stu.gender = input('请录入修改后的性别：')
                stu.age = int(input('请录入修改后的年龄：'))
                stu.phone = input('请录入修改后的手机号：')
                stu.desc = input('请录入修改后的描述信息：')
                print("修改完成\n")
                break
        else:
            print("未找到\n")

    #查询单个学生信息
    def search_one_student(self):
        search_name = input("查询学生姓名：")
        for stu in self.stu_list:
            if stu.name == search_name:
                print(stu , end = '\n')
                break
        else:
            print("未找到\n")

    #查询所有函数信息
    def search_all_student(self):
        #判断长度是否为0
        if len(self.stu_list) == 0:
            print("暂无学生信息\n")
        else:
            for stu in self.stu_list:
                print(stu)
            print()

    #保存信息
    def save_student(self):
        with open('./stu_data.txt','w',encoding='utf-8') as dest_f:
            #把[学生对象，学生对象，学生对象] -> [字典，字典，字典]
            stu_dict = [stu.__dict__ for stu in self.stu_list]
            dest_f.write(str(stu_dict))

    #加载学生信息
    def load_student(self):
        #加入日常处理
        try:
            with open('./stu_data.txt','r',encoding='utf-8') as src_f:
                stu_data = src_f.read()      #'[字典，字典。。。。。]'
                #字符串转换为列表
                stu_list = eval(stu_data)
                if len(stu_list) == 0:
                    stu_list = []
                self.stu_list = [Student(**stu_dict) for stu_dict in stu_list]
        except:
            with open('./stu_data.txt', 'w', encoding='utf-8') as src_f:
                pass

    #把上述逻辑跑通
    def start(self):
        self.load_student()
        while True:
            #添加延迟
            time.sleep(1)
            #打印提示界面
            StudntCMS.show_view()
            #提示要录入的编号 并且接收
            input_num = input('请输入你的操作编号')
            #判断编号
            if input_num == '1':
                self.add_student()
            elif input_num == '2':
                self.del_student()
            elif input_num == '3':
                self.update_student()
            elif input_num == '4':
                self.search_one_student()
            elif input_num == '5':
                self.search_all_student()
            elif input_num == '6':
                self.save_student()
                print('保存学生信息成功\n')
            elif input_num == '0':
                result = input('确定要退出吗？(Y/N) -> ')
                if result.lower() == 'y':  # 字符串lower() -> 把字母转成小写形式
                    #在退出前自动保存
                    self.save_student()
                    break
            else:
                print('输入错误\n')

if __name__ == '__main__':
    #创建管理系统对象
    cms = StudntCMS()
    #调用start函数 开始程序
    cms.start()

