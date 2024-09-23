# 为了更好地理解self的用法，创建一个简单的类，该类表示一个学生对象，具有姓名和年龄属性以及一些方法来操作这些属性。

#示例：一个简单的类

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if 18 <= age <=60:
            self.age = age
        
        else:
            print("年龄不合法")
            
    def greet(self):
        return f"你好，我是{self.name}，今年{self.age}岁。
    
"

# 创建一个Student实例
student = Student("Alice", 25)

# 使用实例方法
print(student.get_name())  # 输出：Alice
print(student.get_age())   # 输出：25

student.set_age(30)        # 设置合法年龄
print(student.get_age())   # 输出：30

student.set_age(10)        # 设置不合法年龄
# 输出：年龄不合法

print(student.greet())      # 输出：你好，我是Alice，今年30岁。