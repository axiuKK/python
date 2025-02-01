class Student():
    def __init__(self,name,number,grade):
        self.name=name
        self.number=number
        self.grade=grade
#定义一个空列表，存放学生信息
class_info=[]
def menu():
    print("-----学生成绩管理系统-----")
    print("1:添加学生信息")
    print("2:查询学生信息")
    print("3:修改学生信息")
    print("4:删除学生信息")
    print("5:显示所有学生信息")
    print("6:统计功能")
    print("7:文件操作")
    print("8:退出系统")

def add_student():
    global class_info  # 声明全局变量，保存学生信息的列表
    while True:  # 使用循环确保用户输入不重复的学号
        name = input("请输入学生姓名：")
        number = input("请输入学生学号：")
        grade = int(input("请输入学生成绩："))

        # 检查学号是否重复
        a=0
        for student in class_info:
            if student.number == number:
                print("您输入的学号已存在，请重新输入")
                a=1
                break  # 如果学号重复，退出当前循环，重新输入
         # 如果没有重复
        if a==0:
            new_student = Student(name, number, grade)
            class_info.append(new_student)
            print("学生信息添加成功！")
            break  # 添加成功后退出循环

def search_student():
    global class_info
    number=input("请输入要查找学生的学号：")
    for student in class_info:
        if(student.number==number):
            #输出学生信息
            print(f"姓名：{student.name},学号：{student.number},成绩：{student.grade}")
            return 0
    
    print("未查找到该学生")

def modify_student():
    global class_info
    number=input("请输入要修改学生的学号：")
    for student in class_info:
        if(student.number==number):
            student.name=input("请输入修改后的学生姓名：")
            student.grade=int(input("请输入修改后的学生成绩："))
            print("修改成功")
            return 0
    
    print("输入的学生不存在")

def delete_student():
    global class_info
    number=input("请输入要删除的学生学号：")
    for student in class_info:
        if(student.number==number):
            #删除学生
            class_info.remove(student)
            print("删除成功")
            return 0
    
    print("学生不存在")

def show_student():
    global class_info
    #按学号升序排序
    sorted(class_info,key=lambda student:student.number)
    for student in class_info:
        print(f"学号：{student.number},姓名：{student.name},成绩：{student.grade}")

def statistic_student():
    global class_info
    total_grade=0
    low_grade=class_info[0].grade
    high_grade=low_grade
    n=0

    for student in class_info:
        total_grade+=student.grade
        n=n+1
        if student.grade<low_grade:
            low_grade=student.grade
        if student.grade>high_grade:
            high_grade=student.grade
    
    average_grade=total_grade/n
    print(f"平均成绩：{average_grade}")
    print(f"最低分：{low_grade}")
    print(f"最高分：{high_grade}")

def file_student():
    global class_info
    #保存信息到文件
    with open('students.txt','w',encoding='utf-8') as file:
        for student in class_info:
            file.write(f"{student.number},{student.name},{student.grade}\n")
    print("保存完成")
    #读取文件信息
    class_info.clear()
    with open('students.txt','r',encoding='utf-8') as file:
        lines=file.readlines()
        for line in lines:
            class_info.append(line)
    print("读取完成")

def main():
    while True:
        menu()
        choose=int(input("请输入您需要的功能："))
        if choose==1:
            add_student()
        elif choose==2:
            search_student()
        elif choose==3:
            modify_student()
        elif choose==4:
            delete_student()
        elif choose==5:
            show_student()
        elif choose==6:
            statistic_student()
        elif choose==7:
            file_student()
        else:
            print("退出系统中")
            break
    return 0

main()