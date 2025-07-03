#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第五部分：面向对象编程 - 练习题参考答案

本文件包含面向对象编程练习题的详细解答
"""

import weakref
import time
import random
import math
from abc import ABC, abstractmethod
from typing import Protocol, List, Optional, Any, Dict, Union
from datetime import datetime, timedelta
from collections import defaultdict
import re

print("第五部分：面向对象编程练习题参考答案")
print("=" * 50)

# ============================================================================
# 1. 类和对象基础练习 - 参考答案
# ============================================================================

print("\n1. 类和对象基础练习 - 参考答案")
print("-" * 30)

# 练习 1.1：创建一个简单的类
class Book:
    """书籍类"""
    
    def __init__(self, title: str, author: str, pages: int, published_year: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.published_year = published_year
    
    def __str__(self) -> str:
        return f"《{self.title}》 - {self.author} ({self.published_year}年, {self.pages}页)"
    
    def get_age(self) -> int:
        """返回书籍出版至今的年数"""
        current_year = datetime.now().year
        return current_year - self.published_year
    
    def is_long(self) -> bool:
        """如果页数超过500，返回True"""
        return self.pages > 500

# 测试Book类
print("练习 1.1 测试：")
book1 = Book("Python编程", "张三", 600, 2020)
book2 = Book("数据结构", "李四", 400, 2018)
book3 = Book("算法导论", "王五", 800, 2015)

books = [book1, book2, book3]
for book in books:
    print(f"{book}")
    print(f"  出版年数: {book.get_age()}年")
    print(f"  是否为长篇: {'是' if book.is_long() else '否'}")
    print()

# 练习 1.2：类属性和实例属性
class Student:
    """学生类"""
    
    # 类属性
    school_name = "Python大学"
    total_students = 0
    
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.courses = []  # 实例属性
        
        # 增加学生总数
        Student.total_students += 1
    
    def add_course(self, course: str) -> None:
        """添加一门课程"""
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name}添加了课程：{course}")
        else:
            print(f"{self.name}已经选择了课程：{course}")
    
    def remove_course(self, course: str) -> bool:
        """移除一门课程"""
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name}移除了课程：{course}")
            return True
        else:
            print(f"{self.name}没有选择课程：{course}")
            return False
    
    def get_courses_count(self) -> int:
        """返回所选课程数量"""
        return len(self.courses)
    
    def __str__(self) -> str:
        return f"学生：{self.name}（学号：{self.student_id}），已选课程：{self.get_courses_count()}门"

# 测试Student类
print("练习 1.2 测试：")
print(f"学校名称：{Student.school_name}")
print(f"初始学生总数：{Student.total_students}")

student1 = Student("张三", "2021001")
student2 = Student("李四", "2021002")
student3 = Student("王五", "2021003")

print(f"创建学生后总数：{Student.total_students}")

# 测试课程操作
student1.add_course("Python编程")
student1.add_course("数据结构")
student1.add_course("算法")
student1.add_course("Python编程")  # 重复添加

student2.add_course("数据库")
student2.add_course("网络编程")

print(f"\n学生信息：")
for student in [student1, student2, student3]:
    print(student)
    print(f"  课程列表：{student.courses}")

student1.remove_course("算法")
student1.remove_course("机器学习")  # 不存在的课程

# 练习 1.3：实例方法、类方法和静态方法
class MathUtils:
    """数学工具类"""
    
    def __init__(self, value: float = 0):
        self.value = value
    
    # 实例方法
    def set_value(self, value: float) -> None:
        """设置数值"""
        self.value = value
    
    def square(self) -> float:
        """返回平方"""
        return self.value ** 2
    
    def cube(self) -> float:
        """返回立方"""
        return self.value ** 3
    
    # 类方法
    @classmethod
    def from_string(cls, value_str: str) -> 'MathUtils':
        """从字符串创建实例"""
        try:
            value = float(value_str)
            return cls(value)
        except ValueError:
            raise ValueError(f"无法将'{value_str}'转换为数字")
    
    @classmethod
    def from_list(cls, value_list: List[float]) -> 'MathUtils':
        """从列表第一个元素创建实例"""
        if not value_list:
            raise ValueError("列表不能为空")
        return cls(value_list[0])
    
    # 静态方法
    @staticmethod
    def is_even(number: int) -> bool:
        """判断是否为偶数"""
        return number % 2 == 0
    
    @staticmethod
    def is_prime(number: int) -> bool:
        """判断是否为质数"""
        if number < 2:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """计算最大公约数"""
        while b:
            a, b = b, a % b
        return abs(a)
    
    def __str__(self) -> str:
        return f"MathUtils(value={self.value})"

# 测试MathUtils类
print("\n练习 1.3 测试：")

# 测试实例方法
math_util = MathUtils(5)
print(f"初始值：{math_util}")
print(f"平方：{math_util.square()}")
print(f"立方：{math_util.cube()}")

math_util.set_value(3)
print(f"设置新值后：{math_util}")
print(f"平方：{math_util.square()}")

# 测试类方法
math_util2 = MathUtils.from_string("7.5")
print(f"从字符串创建：{math_util2}")

math_util3 = MathUtils.from_list([10, 20, 30])
print(f"从列表创建：{math_util3}")

# 测试静态方法
print(f"\n静态方法测试：")
test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for num in test_numbers:
    print(f"{num}: 偶数={MathUtils.is_even(num)}, 质数={MathUtils.is_prime(num)}")

print(f"\n最大公约数测试：")
print(f"gcd(48, 18) = {MathUtils.gcd(48, 18)}")
print(f"gcd(100, 75) = {MathUtils.gcd(100, 75)}")

# ============================================================================
# 2. 继承练习 - 参考答案
# ============================================================================

print("\n\n2. 继承练习 - 参考答案")
print("-" * 30)

# 练习 2.1：基本继承
class Vehicle:
    """车辆基类"""
    
    def __init__(self, make: str, model: str, year: int, fuel_capacity: float):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
    
    def fuel_efficiency(self) -> float:
        """燃油效率（抽象方法，子类必须实现）"""
        raise NotImplementedError("子类必须实现fuel_efficiency方法")
    
    def max_distance(self) -> float:
        """最大行驶距离"""
        return self.fuel_capacity * self.fuel_efficiency()
    
    def __str__(self) -> str:
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    """汽车类"""
    
    def __init__(self, make: str, model: str, year: int, fuel_capacity: float, 
                 passengers: int, trunk_size: float):
        super().__init__(make, model, year, fuel_capacity)
        self.passengers = passengers
        self.trunk_size = trunk_size
    
    def fuel_efficiency(self) -> float:
        """汽车燃油效率"""
        return 10.0  # 10km/L
    
    def is_family_car(self) -> bool:
        """判断是否为家庭用车"""
        return self.passengers >= 5
    
    def __str__(self) -> str:
        base_info = super().__str__()
        return f"{base_info} (载客{self.passengers}人, 后备箱{self.trunk_size}L)"

class Motorcycle(Vehicle):
    """摩托车类"""
    
    def __init__(self, make: str, model: str, year: int, fuel_capacity: float, 
                 has_sidecar: bool):
        super().__init__(make, model, year, fuel_capacity)
        self.has_sidecar = has_sidecar
    
    def fuel_efficiency(self) -> float:
        """摩托车燃油效率"""
        return 20.0  # 20km/L
    
    def is_sport(self) -> bool:
        """判断是否为运动型摩托车"""
        # 简单判断：没有边车且燃油容量较小
        return not self.has_sidecar and self.fuel_capacity < 20
    
    def __str__(self) -> str:
        base_info = super().__str__()
        sidecar_info = "带边车" if self.has_sidecar else "无边车"
        return f"{base_info} ({sidecar_info})"

# 测试Vehicle继承
print("练习 2.1 测试：")
car = Car("丰田", "凯美瑞", 2022, 60, 5, 500)
motorcycle = Motorcycle("本田", "CBR600", 2021, 18, False)

vehicles = [car, motorcycle]
for vehicle in vehicles:
    print(f"车辆：{vehicle}")
    print(f"  燃油效率：{vehicle.fuel_efficiency()} km/L")
    print(f"  最大行驶距离：{vehicle.max_distance()} km")
    
    if isinstance(vehicle, Car):
        print(f"  是否为家庭用车：{'是' if vehicle.is_family_car() else '否'}")
    elif isinstance(vehicle, Motorcycle):
        print(f"  是否为运动型：{'是' if vehicle.is_sport() else '否'}")
    print()

# 练习 2.2：多重继承
class Device:
    """设备基类"""
    
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.is_on = False
    
    def power_on(self) -> None:
        """开机"""
        self.is_on = True
        print(f"{self.brand} {self.model} 已开机")
    
    def power_off(self) -> None:
        """关机"""
        self.is_on = False
        print(f"{self.brand} {self.model} 已关机")

class Portable:
    """便携设备混入类"""
    
    def __init__(self, weight: float, battery_life: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weight = weight  # kg
        self.battery_life = battery_life  # hours
    
    def is_light(self) -> bool:
        """判断是否轻便"""
        return self.weight < 1.0

class Camera(Device):
    """相机类"""
    
    def __init__(self, brand: str, model: str, megapixels: int):
        super().__init__(brand, model)
        self.megapixels = megapixels
    
    def take_photo(self) -> str:
        """拍照"""
        if not self.is_on:
            return "请先开机"
        return f"使用{self.megapixels}MP相机拍摄了一张照片"

class Phone(Device):
    """手机类"""
    
    def __init__(self, brand: str, model: str, number: str):
        super().__init__(brand, model)
        self.number = number
    
    def make_call(self, target_number: str) -> str:
        """打电话"""
        if not self.is_on:
            return "请先开机"
        return f"从{self.number}拨打{target_number}"

class SmartPhone(Phone, Portable):
    """智能手机类"""
    
    def __init__(self, brand: str, model: str, number: str, weight: float, 
                 battery_life: int, os: str):
        super().__init__(brand=brand, model=model, number=number, 
                        weight=weight, battery_life=battery_life)
        self.os = os
        self.apps = []
    
    def install_app(self, app_name: str) -> str:
        """安装应用"""
        if not self.is_on:
            return "请先开机"
        if app_name not in self.apps:
            self.apps.append(app_name)
            return f"已安装应用：{app_name}"
        return f"应用{app_name}已存在"

class DigitalCamera(Camera, Portable):
    """数码相机类"""
    
    def __init__(self, brand: str, model: str, megapixels: int, weight: float, 
                 battery_life: int, zoom: int):
        super().__init__(brand=brand, model=model, megapixels=megapixels, 
                        weight=weight, battery_life=battery_life)
        self.zoom = zoom
    
    def record_video(self) -> str:
        """录制视频"""
        if not self.is_on:
            return "请先开机"
        return f"使用{self.zoom}x变焦录制视频"

# 测试多重继承
print("练习 2.2 测试：")
smartphone = SmartPhone("苹果", "iPhone 13", "13800138000", 0.17, 20, "iOS")
digital_camera = DigitalCamera("佳能", "EOS R5", 45, 0.65, 8, 10)

devices = [smartphone, digital_camera]
for device in devices:
    print(f"设备：{device.brand} {device.model}")
    device.power_on()
    
    if isinstance(device, SmartPhone):
        print(f"  电话号码：{device.number}")
        print(f"  操作系统：{device.os}")
        print(f"  重量：{device.weight}kg")
        print(f"  电池续航：{device.battery_life}小时")
        print(f"  是否轻便：{'是' if device.is_light() else '否'}")
        print(f"  {device.make_call('10086')}")
        print(f"  {device.install_app('微信')}")
        print(f"  {device.install_app('支付宝')}")
        print(f"  已安装应用：{device.apps}")
    
    elif isinstance(device, DigitalCamera):
        print(f"  像素：{device.megapixels}MP")
        print(f"  变焦：{device.zoom}x")
        print(f"  重量：{device.weight}kg")
        print(f"  电池续航：{device.battery_life}小时")
        print(f"  是否轻便：{'是' if device.is_light() else '否'}")
        print(f"  {device.take_photo()}")
        print(f"  {device.record_video()}")
    
    device.power_off()
    print()

print(f"SmartPhone的MRO：{SmartPhone.__mro__}")
print(f"DigitalCamera的MRO：{DigitalCamera.__mro__}")

# 练习 2.3：方法重写和super()
class Shape:
    """形状基类"""
    
    def __init__(self, color: str):
        self.color = color
    
    def area(self) -> float:
        """计算面积"""
        return 0
    
    def perimeter(self) -> float:
        """计算周长"""
        return 0
    
    def describe(self) -> str:
        """描述形状"""
        return f"{self.color}的形状，面积：{self.area():.2f}，周长：{self.perimeter():.2f}"

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def diameter(self) -> float:
        """直径"""
        return 2 * self.radius

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        """判断是否为正方形"""
        return abs(self.width - self.height) < 0.001

class Square(Rectangle):
    """正方形类"""
    
    def __init__(self, color: str, side: float):
        # 使用super()调用父类的__init__
        super().__init__(color, side, side)
        self.side = side
    
    def describe(self) -> str:
        """重写描述方法"""
        base_description = super().describe()
        return f"{base_description}，边长：{self.side:.2f}"

# 测试方法重写和super()
print("\n练习 2.3 测试：")
shapes = [
    Circle("红色", 5),
    Rectangle("蓝色", 4, 6),
    Square("绿色", 3)
]

for shape in shapes:
    print(shape.describe())
    
    if isinstance(shape, Circle):
        print(f"  直径：{shape.diameter():.2f}")
    elif isinstance(shape, Rectangle) and not isinstance(shape, Square):
        print(f"  是否为正方形：{'是' if shape.is_square() else '否'}")
    
    print()

# ============================================================================
# 3. 封装练习 - 参考答案
# ============================================================================

print("\n\n3. 封装练习 - 参考答案")
print("-" * 30)

# 练习 3.1：访问控制
class BankAccount:
    """银行账户类"""
    
    def __init__(self, account_number: str, pin: str, initial_balance: float = 0):
        self.__account_number = account_number
        self.__pin = pin
        self.__balance = initial_balance
        self.__transaction_history = []
        
        if initial_balance > 0:
            self.__add_transaction("开户", initial_balance)
    
    def deposit(self, amount: float) -> bool:
        """存款"""
        if amount <= 0:
            print("存款金额必须大于0")
            return False
        
        self.__balance += amount
        self.__add_transaction("存款", amount)
        print(f"存款成功，当前余额：{self.__balance:.2f}")
        return True
    
    def withdraw(self, amount: float, pin: str) -> bool:
        """取款"""
        if not self.__verify_pin(pin):
            print("PIN码错误")
            return False
        
        if amount <= 0:
            print("取款金额必须大于0")
            return False
        
        if amount > self.__balance:
            print("余额不足")
            return False
        
        self.__balance -= amount
        self.__add_transaction("取款", -amount)
        print(f"取款成功，当前余额：{self.__balance:.2f}")
        return True
    
    def get_balance(self, pin: str) -> Optional[float]:
        """获取余额"""
        if not self.__verify_pin(pin):
            print("PIN码错误")
            return None
        return self.__balance
    
    def change_pin(self, old_pin: str, new_pin: str) -> bool:
        """修改PIN码"""
        if not self.__verify_pin(old_pin):
            print("原PIN码错误")
            return False
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("新PIN码必须是4位数字")
            return False
        
        self.__pin = new_pin
        print("PIN码修改成功")
        return True
    
    def get_account_info(self) -> str:
        """获取账户信息摘要"""
        masked_account = self.__account_number[:2] + "****" + self.__account_number[-2:]
        return f"账户：{masked_account}，交易记录：{len(self.__transaction_history)}条"
    
    def print_statement(self, pin: str) -> None:
        """打印对账单"""
        if not self.__verify_pin(pin):
            print("PIN码错误")
            return
        
        print(f"\n=== 账户对账单 ===")
        print(f"账户：{self.__account_number}")
        print(f"当前余额：{self.__balance:.2f}")
        print(f"交易历史：")
        
        for transaction in self.__transaction_history:
            print(f"  {transaction['date'].strftime('%Y-%m-%d %H:%M:%S')} - "
                  f"{transaction['type']}：{transaction['amount']:+.2f}，"
                  f"余额：{transaction['balance']:.2f}")
        print("=" * 20)
    
    def __verify_pin(self, pin: str) -> bool:
        """验证PIN码"""
        return pin == self.__pin
    
    def __add_transaction(self, transaction_type: str, amount: float) -> None:
        """添加交易记录"""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self.__balance,
            "date": datetime.now()
        }
        self.__transaction_history.append(transaction)

# 测试BankAccount类
print("练习 3.1 测试：")
account = BankAccount("1234567890", "1234", 1000)

print(account.get_account_info())
print(f"当前余额：{account.get_balance('1234')}")

account.deposit(500)
account.withdraw(200, "1234")
account.withdraw(100, "0000")  # 错误PIN
account.change_pin("1234", "5678")
account.withdraw(100, "5678")

account.print_statement("5678")

# 尝试直接访问私有属性（会失败）
try:
    print(account.__balance)
except AttributeError as e:
    print(f"\n无法直接访问私有属性：{e}")

# 练习 3.2：属性装饰器
class Person:
    """人员类"""
    
    def __init__(self, name: str, age: int, email: str = "", phone: str = ""):
        self.__name = ""
        self.__age = 0
        self.__email = ""
        self.__phone = ""
        
        # 使用属性设置器进行验证
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
    
    @property
    def name(self) -> str:
        """获取姓名"""
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        """设置姓名"""
        if not value or not value.strip():
            raise ValueError("姓名不能为空")
        
        # 检查是否只包含字母、中文和空格
        if not re.match(r'^[a-zA-Z\u4e00-\u9fa5\s]+$', value.strip()):
            raise ValueError("姓名只能包含字母、中文和空格")
        
        self.__name = value.strip()
    
    @property
    def age(self) -> int:
        """获取年龄"""
        return self.__age
    
    @age.setter
    def age(self, value: int) -> None:
        """设置年龄"""
        if not isinstance(value, int) or value < 0 or value > 120:
            raise ValueError("年龄必须是0-120之间的整数")
        self.__age = value
    
    @property
    def email(self) -> str:
        """获取邮箱"""
        return self.__email
    
    @email.setter
    def email(self, value: str) -> None:
        """设置邮箱"""
        if value and not re.match(r'^[^@]+@[^@]+\.[^@]+$', value):
            raise ValueError("邮箱格式不正确")
        self.__email = value
    
    @property
    def phone(self) -> str:
        """获取电话"""
        return self.__phone
    
    @phone.setter
    def phone(self, value: str) -> None:
        """设置电话"""
        if value and (not value.isdigit() or len(value) < 7 or len(value) > 15):
            raise ValueError("电话号码必须是7-15位数字")
        self.__phone = value
    
    @property
    def adult(self) -> bool:
        """是否成年（只读属性）"""
        return self.__age >= 18
    
    @property
    def contact_info(self) -> str:
        """联系信息（只读属性）"""
        info = f"姓名：{self.__name}，年龄：{self.__age}"
        if self.__email:
            info += f"，邮箱：{self.__email}"
        if self.__phone:
            info += f"，电话：{self.__phone}"
        return info
    
    def __str__(self) -> str:
        return self.contact_info

# 测试Person类
print("\n练习 3.2 测试：")

# 正常创建
person = Person("张三", 25, "zhangsan@example.com", "13800138000")
print(f"创建成功：{person}")
print(f"是否成年：{person.adult}")

# 测试属性修改
person.age = 30
print(f"修改年龄后：{person}")

# 测试错误处理
test_cases = [
    ("设置无效姓名", lambda: setattr(person, 'name', "")),
    ("设置无效年龄", lambda: setattr(person, 'age', -5)),
    ("设置无效邮箱", lambda: setattr(person, 'email', "invalid-email")),
    ("设置无效电话", lambda: setattr(person, 'phone', "123"))
]

for test_name, test_func in test_cases:
    try:
        test_func()
        print(f"{test_name}：未捕获到异常（可能有问题）")
    except ValueError as e:
        print(f"{test_name}：{e}")

# 练习 3.3：数据封装和验证
class Product:
    """商品类"""
    
    # 预定义类别
    VALID_CATEGORIES = ["电子产品", "服装", "食品", "图书", "家居", "运动", "美妆", "其他"]
    
    def __init__(self, product_id: Union[str, int], name: str, price: float, 
                 stock: int, category: str):
        self.__id = None
        self.__name = ""
        self.__price = 0.0
        self.__stock = 0
        self.__category = ""
        self.__ratings = []
        
        # 使用属性设置器进行验证
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
    
    @property
    def id(self) -> Union[str, int]:
        return self.__id
    
    @id.setter
    def id(self, value: Union[str, int]) -> None:
        if not value:
            raise ValueError("商品ID不能为空")
        self.__id = value
    
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        if not value or len(value.strip()) < 3 or len(value.strip()) > 100:
            raise ValueError("商品名称长度必须在3-100字符之间")
        self.__name = value.strip()
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("价格必须大于0")
        self.__price = float(value)
    
    @property
    def stock(self) -> int:
        return self.__stock
    
    @stock.setter
    def stock(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("库存必须是非负整数")
        self.__stock = value
    
    @property
    def category(self) -> str:
        return self.__category
    
    @category.setter
    def category(self, value: str) -> None:
        if value not in self.VALID_CATEGORIES:
            raise ValueError(f"类别必须是以下之一：{', '.join(self.VALID_CATEGORIES)}")
        self.__category = value
    
    @property
    def ratings(self) -> List[float]:
        return self.__ratings.copy()
    
    def add_rating(self, rating: float) -> None:
        """添加评分"""
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 5:
            raise ValueError("评分必须是0-5之间的数字")
        self.__ratings.append(float(rating))
    
    def restock(self, quantity: int) -> None:
        """增加库存"""
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("补货数量必须是正整数")
        self.__stock += quantity
    
    def discount(self, percentage: float) -> float:
        """计算折扣价格"""
        if not isinstance(percentage, (int, float)) or percentage < 0 or percentage > 100:
            raise ValueError("折扣百分比必须在0-100之间")
        return self.__price * (1 - percentage / 100)
    
    def is_available(self) -> bool:
        """检查是否有库存"""
        return self.__stock > 0
    
    def average_rating(self) -> Optional[float]:
        """计算平均评分"""
        if not self.__ratings:
            return None
        return sum(self.__ratings) / len(self.__ratings)
    
    def __str__(self) -> str:
        avg_rating = self.average_rating()
        rating_str = f"{avg_rating:.1f}" if avg_rating else "暂无评分"
        return (f"商品：{self.__name} (ID: {self.__id})\n"
                f"  价格：¥{self.__price:.2f}，库存：{self.__stock}\n"
                f"  类别：{self.__category}，评分：{rating_str}")

# 测试Product类
print("\n练习 3.3 测试：")

# 创建商品
product = Product("P001", "iPhone 13", 5999.0, 50, "电子产品")
print(f"创建商品：\n{product}")

# 添加评分
ratings = [4.5, 5.0, 4.0, 4.8, 4.2]
for rating in ratings:
    product.add_rating(rating)

print(f"\n添加评分后：\n{product}")
print(f"平均评分：{product.average_rating():.2f}")

# 测试其他方法
print(f"\n库存状态：{'有货' if product.is_available() else '缺货'}")
print(f"8折价格：¥{product.discount(20):.2f}")

product.restock(20)
print(f"补货后库存：{product.stock}")

# 测试错误处理
print("\n错误处理测试：")
error_tests = [
    ("无效价格", lambda: setattr(product, 'price', -100)),
    ("无效库存", lambda: setattr(product, 'stock', -5)),
    ("无效类别", lambda: setattr(product, 'category', "无效类别")),
    ("无效评分", lambda: product.add_rating(6)),
    ("无效折扣", lambda: product.discount(150))
]

for test_name, test_func in error_tests:
    try:
        test_func()
        print(f"{test_name}：未捕获到异常")
    except ValueError as e:
        print(f"{test_name}：{e}")

# ============================================================================
# 4. 多态练习 - 参考答案
# ============================================================================

print("\n\n4. 多态练习 - 参考答案")
print("-" * 30)

# 练习 4.1：方法重写和多态
class Employee:
    """员工基类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float):
        self.name = name
        self.id = employee_id
        self.base_salary = base_salary
    
    def calculate_salary(self) -> float:
        """计算月薪"""
        return self.base_salary
    
    def get_info(self) -> str:
        """获取员工基本信息"""
        return f"员工：{self.name} (ID: {self.id})，基本工资：¥{self.base_salary:.2f}"

class Manager(Employee):
    """经理类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float, 
                 bonus: float, team_size: int):
        super().__init__(name, employee_id, base_salary)
        self.bonus = bonus
        self.team_size = team_size
    
    def calculate_salary(self) -> float:
        """经理工资计算"""
        return self.base_salary + self.bonus + (self.team_size * 100)
    
    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}，奖金：¥{self.bonus:.2f}，团队规模：{self.team_size}人"

class Developer(Employee):
    """开发者类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float, 
                 programming_languages: List[str], overtime_hours: int):
        super().__init__(name, employee_id, base_salary)
        self.programming_languages = programming_languages
        self.overtime_hours = overtime_hours
    
    def calculate_salary(self) -> float:
        """开发者工资计算"""
        language_bonus = len(self.programming_languages) * 500
        overtime_pay = self.overtime_hours * 150
        return self.base_salary + language_bonus + overtime_pay
    
    def get_info(self) -> str:
        base_info = super().get_info()
        languages = ", ".join(self.programming_languages)
        return (f"{base_info}，编程语言：{languages}，"
                f"加班时间：{self.overtime_hours}小时")

class SalesPerson(Employee):
    """销售人员类"""
    
    def __init__(self, name: str, employee_id: str, base_salary: float, 
                 sales_volume: float, commission_rate: float):
        super().__init__(name, employee_id, base_salary)
        self.sales_volume = sales_volume
        self.commission_rate = commission_rate
    
    def calculate_salary(self) -> float:
        """销售人员工资计算"""
        commission = self.sales_volume * self.commission_rate
        return self.base_salary + commission
    
    def get_info(self) -> str:
        base_info = super().get_info()
        return (f"{base_info}，销售额：¥{self.sales_volume:.2f}，"
                f"佣金比例：{self.commission_rate*100:.1f}%")

def process_payroll(employees: List[Employee]) -> None:
    """处理工资单 - 多态函数"""
    print("\n=== 工资单处理 ===")
    total_payroll = 0
    
    for employee in employees:
        salary = employee.calculate_salary()
        total_payroll += salary
        
        print(f"\n{employee.get_info()}")
        print(f"月薪：¥{salary:.2f}")
        
        # 根据类型显示额外信息
        if isinstance(employee, Manager):
            print(f"  管理奖金：¥{employee.bonus:.2f}")
            print(f"  团队奖金：¥{employee.team_size * 100:.2f}")
        elif isinstance(employee, Developer):
            print(f"  技能奖金：¥{len(employee.programming_languages) * 500:.2f}")
            print(f"  加班费：¥{employee.overtime_hours * 150:.2f}")
        elif isinstance(employee, SalesPerson):
            print(f"  销售佣金：¥{employee.sales_volume * employee.commission_rate:.2f}")
    
    print(f"\n总工资支出：¥{total_payroll:.2f}")
    print("=" * 20)

# 测试多态
print("练习 4.1 测试：")
employees = [
    Manager("张经理", "M001", 15000, 5000, 8),
    Developer("李开发", "D001", 12000, ["Python", "Java", "JavaScript"], 20),
    Developer("王程序员", "D002", 10000, ["Python", "Go"], 15),
    SalesPerson("赵销售", "S001", 8000, 100000, 0.05),
    SalesPerson("钱业务", "S002", 8000, 150000, 0.04)
]

process_payroll(employees)

# 练习 4.2：抽象基类
class PaymentMethod(ABC):
    """支付方式抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """处理支付"""
        pass
    
    @abstractmethod
    def refund(self, amount: float) -> bool:
        """处理退款"""
        pass
    
    @abstractmethod
    def get_transaction_fee(self, amount: float) -> float:
        """获取交易费用"""
        pass
    
    @abstractmethod
    def is_international(self) -> bool:
        """检查是否支持国际支付"""
        pass

class CreditCard(PaymentMethod):
    """信用卡支付"""
    
    def __init__(self, card_number: str, holder_name: str):
        super().__init__("信用卡")
        self.card_number = card_number
        self.holder_name = holder_name
    
    def process_payment(self, amount: float) -> bool:
        print(f"使用信用卡({self.card_number[-4:]})支付¥{amount:.2f}")
        # 模拟支付处理
        if amount > 0:
            print("信用卡支付成功")
            return True
        return False
    
    def refund(self, amount: float) -> bool:
        print(f"信用卡退款¥{amount:.2f}")
        print("退款将在3-5个工作日内到账")
        return True
    
    def get_transaction_fee(self, amount: float) -> float:
        return amount * 0.025  # 2.5%手续费
    
    def is_international(self) -> bool:
        return True

class PayPal(PaymentMethod):
    """PayPal支付"""
    
    def __init__(self, email: str):
        super().__init__("PayPal")
        self.email = email
    
    def process_payment(self, amount: float) -> bool:
        print(f"使用PayPal({self.email})支付¥{amount:.2f}")
        if amount > 0:
            print("PayPal支付成功")
            return True
        return False
    
    def refund(self, amount: float) -> bool:
        print(f"PayPal退款¥{amount:.2f}")
        print("退款将立即处理")
        return True
    
    def get_transaction_fee(self, amount: float) -> float:
        return amount * 0.035  # 3.5%手续费
    
    def is_international(self) -> bool:
        return True

class BankTransfer(PaymentMethod):
    """银行转账"""
    
    def __init__(self, bank_name: str, account_number: str):
        super().__init__("银行转账")
        self.bank_name = bank_name
        self.account_number = account_number
    
    def process_payment(self, amount: float) -> bool:
        print(f"使用{self.bank_name}银行转账支付¥{amount:.2f}")
        if amount > 0:
            print("银行转账支付成功")
            return True
        return False
    
    def refund(self, amount: float) -> bool:
        print(f"银行转账退款¥{amount:.2f}")
        print("退款将在1-2个工作日内到账")
        return True
    
    def get_transaction_fee(self, amount: float) -> float:
        return 5.0  # 固定5元手续费
    
    def is_international(self) -> bool:
        return False

class Cryptocurrency(PaymentMethod):
    """加密货币支付"""
    
    def __init__(self, currency_type: str, wallet_address: str):
        super().__init__(f"{currency_type}支付")
        self.currency_type = currency_type
        self.wallet_address = wallet_address
    
    def process_payment(self, amount: float) -> bool:
        print(f"使用{self.currency_type}支付¥{amount:.2f}")
        if amount > 0:
            print(f"{self.currency_type}支付成功")
            return True
        return False
    
    def refund(self, amount: float) -> bool:
        print(f"{self.currency_type}退款¥{amount:.2f}")
        print("加密货币退款需要手动处理")
        return True
    
    def get_transaction_fee(self, amount: float) -> float:
        return amount * 0.01  # 1%网络费用
    
    def is_international(self) -> bool:
        return True

def process_order(amount: float, payment_method: PaymentMethod) -> bool:
    """处理订单 - 多态函数"""
    print(f"\n=== 处理订单 ===")
    print(f"订单金额：¥{amount:.2f}")
    print(f"支付方式：{payment_method.name}")
    
    # 计算手续费
    fee = payment_method.get_transaction_fee(amount)
    total_amount = amount + fee
    
    print(f"手续费：¥{fee:.2f}")
    print(f"总金额：¥{total_amount:.2f}")
    print(f"支持国际支付：{'是' if payment_method.is_international() else '否'}")
    
    # 处理支付
    success = payment_method.process_payment(total_amount)
    
    if success:
        print("订单处理成功！")
    else:
        print("订单处理失败！")
    
    print("=" * 15)
    return success

# 测试抽象基类和多态
print("\n练习 4.2 测试：")
payment_methods = [
    CreditCard("1234567890123456", "张三"),
    PayPal("user@example.com"),
    BankTransfer("中国银行", "6217000000000000"),
    Cryptocurrency("Bitcoin", "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
]

order_amount = 1000.0
for payment_method in payment_methods:
    process_order(order_amount, payment_method)

# 练习 4.3：接口和协议
class Drawable(Protocol):
    """可绘制协议"""
    def draw(self) -> None: ...

class Resizable(Protocol):
    """可调整大小协议"""
    def resize(self, width: int, height: int) -> None: ...

class Interactive(Protocol):
    """可交互协议"""
    def handle_click(self, x: int, y: int) -> None: ...
    def handle_hover(self, x: int, y: int) -> None: ...

class Button:
    """按钮类 - 实现Drawable和Interactive"""
    
    def __init__(self, text: str, x: int, y: int, width: int, height: int):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.clicked = False
    
    def draw(self) -> None:
        print(f"绘制按钮：'{self.text}' 位置({self.x}, {self.y}) 大小{self.width}x{self.height}")
    
    def handle_click(self, x: int, y: int) -> None:
        if (self.x <= x <= self.x + self.width and 
            self.y <= y <= self.y + self.height):
            self.clicked = True
            print(f"按钮'{self.text}'被点击了！")
        else:
            print(f"点击位置({x}, {y})不在按钮'{self.text}'范围内")
    
    def handle_hover(self, x: int, y: int) -> None:
        if (self.x <= x <= self.x + self.width and 
            self.y <= y <= self.y + self.height):
            print(f"鼠标悬停在按钮'{self.text}'上")
        else:
            print(f"鼠标不在按钮'{self.text}'范围内")

class Image:
    """图片类 - 实现Drawable和Resizable"""
    
    def __init__(self, filename: str, x: int, y: int, width: int, height: int):
        self.filename = filename
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self) -> None:
        print(f"绘制图片：{self.filename} 位置({self.x}, {self.y}) 大小{self.width}x{self.height}")
    
    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        print(f"图片{self.filename}调整大小为{width}x{height}")

class Canvas:
    """画布类 - 实现Drawable、Resizable和Interactive"""
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.elements = []
    
    def draw(self) -> None:
        print(f"绘制画布：大小{self.width}x{self.height}，包含{len(self.elements)}个元素")
        for element in self.elements:
            print(f"  - {element}")
    
    def resize(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        print(f"画布调整大小为{width}x{height}")
    
    def handle_click(self, x: int, y: int) -> None:
        print(f"画布在位置({x}, {y})被点击")
        self.elements.append(f"点击标记({x}, {y})")
    
    def handle_hover(self, x: int, y: int) -> None:
        print(f"鼠标在画布位置({x}, {y})悬停")

class Text:
    """文本类 - 实现Drawable"""
    
    def __init__(self, content: str, x: int, y: int, font_size: int):
        self.content = content
        self.x = x
        self.y = y
        self.font_size = font_size
    
    def draw(self) -> None:
        print(f"绘制文本：'{self.content}' 位置({self.x}, {self.y}) 字体大小{self.font_size}")

def render(drawables: List[Drawable]) -> None:
    """渲染可绘制对象"""
    print("\n=== 渲染元素 ===")
    for drawable in drawables:
        drawable.draw()
    print("=" * 15)

def resize_elements(resizables: List[Resizable], width: int, height: int) -> None:
    """调整可调整大小的元素"""
    print(f"\n=== 调整元素大小为{width}x{height} ===")
    for resizable in resizables:
        resizable.resize(width, height)
    print("=" * 15)

def handle_user_click(interactives: List[Interactive], x: int, y: int) -> None:
    """处理用户点击"""
    print(f"\n=== 处理点击事件({x}, {y}) ===")
    for interactive in interactives:
        interactive.handle_click(x, y)
    print("=" * 15)

# 测试协议和多态
print("\n练习 4.3 测试：")

# 创建各种元素
button = Button("确定", 10, 10, 80, 30)
image = Image("logo.png", 100, 10, 200, 100)
canvas = Canvas(800, 600)
text = Text("Hello World", 50, 50, 16)

# 测试渲染
all_drawables = [button, image, canvas, text]
render(all_drawables)

# 测试调整大小
resizable_elements = [image, canvas]
resize_elements(resizable_elements, 300, 200)

# 测试交互
interactive_elements = [button, canvas]
handle_user_click(interactive_elements, 50, 25)  # 点击按钮
handle_user_click(interactive_elements, 400, 300)  # 点击画布

# ============================================================================
# 5. 特殊方法练习 - 参考答案
# ============================================================================

print("\n\n5. 特殊方法练习 - 参考答案")
print("-" * 30)

# 练习 5.1：运算符重载
class Fraction:
    """分数类"""
    
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("分母不能为零")
        
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def simplify(self) -> None:
        """化简分数"""
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return abs(a)
        
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        
        # 确保分母为正
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def __eq__(self, other: 'Fraction') -> bool:
        if not isinstance(other, Fraction):
            return False
        return (self.numerator == other.numerator and 
                self.denominator == other.denominator)
    
    def __ne__(self, other: 'Fraction') -> bool:
        return not self.__eq__(other)
    
    def __lt__(self, other: 'Fraction') -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("只能与另一个Fraction比较")
        return (self.numerator * other.denominator < 
                other.numerator * self.denominator)
    
    def __le__(self, other: 'Fraction') -> bool:
        return self < other or self == other
    
    def __gt__(self, other: 'Fraction') -> bool:
        return not self <= other
    
    def __ge__(self, other: 'Fraction') -> bool:
        return not self < other
    
    def __add__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            raise TypeError("只能与另一个Fraction相加")
        
        new_numerator = (self.numerator * other.denominator + 
                        other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            raise TypeError("只能与另一个Fraction相减")
        
        new_numerator = (self.numerator * other.denominator - 
                        other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            raise TypeError("只能与另一个Fraction相乘")
        
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        if not isinstance(other, Fraction):
            raise TypeError("只能除以另一个Fraction")
        if other.numerator == 0:
            raise ValueError("不能除以零")
        
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def __neg__(self) -> 'Fraction':
        return Fraction(-self.numerator, self.denominator)
    
    def __abs__(self) -> 'Fraction':
        return Fraction(abs(self.numerator), self.denominator)
    
    def to_decimal(self) -> float:
        """转换为小数"""
        return self.numerator / self.denominator

# 测试Fraction类
print("练习 5.1 测试：")
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f3 = Fraction(2, 4)  # 应该化简为1/2

print(f"f1 = {f1}")
print(f"f2 = {f2}")
print(f"f3 = {f3}")
print(f"f1 == f3: {f1 == f3}")

print(f"\n运算测试：")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")
print(f"-f1 = {-f1}")
print(f"|f1| = {abs(f1)}")

print(f"\n比较测试：")
print(f"f1 < f2: {f1 < f2}")
print(f"f1 > f2: {f1 > f2}")
print(f"f1 <= f3: {f1 <= f3}")

print(f"\n小数转换：")
print(f"f1 = {f1.to_decimal():.4f}")
print(f"f2 = {f2.to_decimal():.4f}")

# 练习 5.2：容器和迭代
class Playlist:
    """音乐播放列表"""
    
    def __init__(self, name: str):
        self.name = name
        self.songs = []
        self.current_position = 0
    
    def add_song(self, song: str) -> None:
        """添加歌曲"""
        self.songs.append(song)
        print(f"已添加歌曲：{song}")
    
    def remove_song(self, song: str) -> bool:
        """移除歌曲"""
        if song in self.songs:
            self.songs.remove(song)
            print(f"已移除歌曲：{song}")
            # 调整当前位置
            if self.current_position >= len(self.songs):
                self.current_position = 0
            return True
        print(f"歌曲不存在：{song}")
        return False
    
    def __len__(self) -> int:
        """返回歌曲数量"""
        return len(self.songs)
    
    def __getitem__(self, index: int) -> str:
        """通过索引获取歌曲"""
        return self.songs[index]
    
    def __setitem__(self, index: int, song: str) -> None:
        """通过索引设置歌曲"""
        self.songs[index] = song
    
    def __delitem__(self, index: int) -> None:
        """通过索引删除歌曲"""
        del self.songs[index]
        if self.current_position >= len(self.songs):
            self.current_position = 0
    
    def __iter__(self):
        """返回迭代器"""
        self.current_position = 0
        return self
    
    def __next__(self) -> str:
        """实现迭代器协议"""
        if self.current_position >= len(self.songs):
            raise StopIteration
        
        song = self.songs[self.current_position]
        self.current_position += 1
        return song
    
    def __contains__(self, song: str) -> bool:
        """检查歌曲是否在播放列表中"""
        return song in self.songs
    
    def shuffle(self) -> None:
        """随机打乱歌曲顺序"""
        random.shuffle(self.songs)
        self.current_position = 0
        print("播放列表已打乱")
    
    def sort(self, key=None, reverse=False) -> None:
        """排序歌曲"""
        self.songs.sort(key=key, reverse=reverse)
        self.current_position = 0
        print("播放列表已排序")
    
    def __str__(self) -> str:
        return f"播放列表'{self.name}'：{len(self.songs)}首歌曲"

# 测试Playlist类
print("\n练习 5.2 测试：")
playlist = Playlist("我的最爱")

# 添加歌曲
songs = ["歌曲A", "歌曲B", "歌曲C", "歌曲D", "歌曲E"]
for song in songs:
    playlist.add_song(song)

print(f"\n{playlist}")
print(f"播放列表长度：{len(playlist)}")

# 测试索引访问
print(f"\n索引访问测试：")
print(f"第一首歌：{playlist[0]}")
print(f"最后一首歌：{playlist[-1]}")

# 修改歌曲
playlist[1] = "新歌曲B"
print(f"修改后第二首歌：{playlist[1]}")

# 测试成员检查
print(f"\n成员检查：")
print(f"'歌曲A' 在播放列表中：{'歌曲A' in playlist}")
print(f"'不存在的歌' 在播放列表中：{'不存在的歌' in playlist}")

# 测试迭代
print(f"\n迭代播放列表：")
for i, song in enumerate(playlist, 1):
    print(f"{i}. {song}")

# 测试删除
print(f"\n删除第三首歌：")
del playlist[2]
print(f"删除后播放列表：{list(playlist)}")

# 测试排序和打乱
print(f"\n排序测试：")
playlist.sort()
print(f"排序后：{list(playlist)}")

playlist.shuffle()
print(f"打乱后：{list(playlist)}")

# 练习 5.3：上下文管理器
class FileManager:
    """文件管理器上下文管理器"""
    
    def __init__(self, file_path: str, mode: str = 'r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入上下文"""
        try:
            self.file = open(self.file_path, self.mode)
            print(f"文件 {self.file_path} 已打开（模式：{self.mode}）")
            return self.file
        except Exception as e:
            print(f"打开文件失败：{e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.file:
            self.file.close()
            print(f"文件 {self.file_path} 已关闭")
        
        if exc_type:
            print(f"文件操作出现异常：{exc_type.__name__}: {exc_val}")
        
        return False  # 不抑制异常

class DatabaseConnection:
    """数据库连接上下文管理器（模拟）"""
    
    def __init__(self, host: str, database: str, user: str):
        self.host = host
        self.database = database
        self.user = user
        self.connection = None
        self.transaction_started = False
    
    def __enter__(self):
        """建立连接"""
        print(f"连接到数据库：{self.host}/{self.database} (用户：{self.user})")
        self.connection = f"Connection-{random.randint(1000, 9999)}"
        self.transaction_started = True
        print(f"数据库连接已建立：{self.connection}")
        print("事务已开始")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """关闭连接"""
        if self.transaction_started:
            if exc_type:
                print("检测到异常，回滚事务")
                self.rollback()
            else:
                print("提交事务")
                self.commit()
        
        if self.connection:
            print(f"关闭数据库连接：{self.connection}")
            self.connection = None
        
        return False
    
    def execute(self, sql: str) -> str:
        """执行SQL（模拟）"""
        if not self.connection:
            raise RuntimeError("数据库未连接")
        print(f"执行SQL：{sql}")
        return f"Result-{random.randint(100, 999)}"
    
    def commit(self) -> None:
        """提交事务"""
        print("事务已提交")
        self.transaction_started = False
    
    def rollback(self) -> None:
        """回滚事务"""
        print("事务已回滚")
        self.transaction_started = False

class Timer:
    """计时器上下文管理器"""
    
    def __init__(self, name: str = "操作"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        """开始计时"""
        self.start_time = time.time()
        print(f"开始{self.name}...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """结束计时"""
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        
        if exc_type:
            print(f"{self.name}失败，耗时：{duration:.4f}秒")
            print(f"异常：{exc_type.__name__}: {exc_val}")
        else:
            print(f"{self.name}完成，耗时：{duration:.4f}秒")
        
        return False
    
    def elapsed(self) -> float:
        """返回当前经过的时间"""
        if self.start_time is None:
            return 0
        current_time = self.end_time if self.end_time else time.time()
        return current_time - self.start_time

# 测试上下文管理器
print("\n练习 5.3 测试：")

# 测试Timer
print("计时器测试：")
with Timer("数学计算") as timer:
    # 模拟一些计算
    result = sum(i**2 for i in range(1000))
    time.sleep(0.1)  # 模拟耗时操作
    print(f"计算结果：{result}")

# 测试DatabaseConnection
print("\n数据库连接测试：")
with DatabaseConnection("localhost", "testdb", "admin") as db:
    db.execute("SELECT * FROM users")
    db.execute("UPDATE users SET status = 'active'")
    # 正常完成，会自动提交

# 测试异常情况
print("\n异常处理测试：")
try:
    with DatabaseConnection("localhost", "testdb", "admin") as db:
        db.execute("SELECT * FROM users")
        raise ValueError("模拟数据库操作错误")
except ValueError:
    print("捕获到异常，事务已回滚")

# 测试FileManager（创建临时文件）
print("\n文件管理器测试：")
temp_file = "/tmp/test_file.txt"
try:
    with FileManager(temp_file, 'w') as f:
        f.write("Hello, World!\n")
        f.write("这是一个测试文件。\n")
    
    with FileManager(temp_file, 'r') as f:
        content = f.read()
        print(f"文件内容：\n{content}")
except Exception as e:
    print(f"文件操作失败：{e}")

# ============================================================================
# 6. 设计模式练习 - 参考答案
# ============================================================================

print("\n\n6. 设计模式练习 - 参考答案")
print("-" * 30)

# 练习 6.1：单例模式
class Singleton:
    """单例模式基类"""
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

class DatabaseManager(Singleton):
    """数据库管理器 - 单例模式"""
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.connections = {}
            self.connection_count = 0
            self.initialized = True
            print("数据库管理器初始化")
    
    def get_connection(self, database_name: str) -> str:
        """获取数据库连接"""
        if database_name not in self.connections:
            self.connection_count += 1
            connection_id = f"conn_{self.connection_count}"
            self.connections[database_name] = connection_id
            print(f"创建新连接：{database_name} -> {connection_id}")
        else:
            print(f"复用现有连接：{database_name} -> {self.connections[database_name]}")
        
        return self.connections[database_name]
    
    def close_connection(self, database_name: str) -> None:
        """关闭数据库连接"""
        if database_name in self.connections:
            connection_id = self.connections.pop(database_name)
            print(f"关闭连接：{database_name} -> {connection_id}")
        else:
            print(f"连接不存在：{database_name}")
    
    def get_status(self) -> Dict[str, Any]:
        """获取管理器状态"""
        return {
            'active_connections': len(self.connections),
            'total_created': self.connection_count,
            'databases': list(self.connections.keys())
        }

class ConfigManager(Singleton):
    """配置管理器 - 单例模式"""
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.config = {}
            self.initialized = True
            print("配置管理器初始化")
    
    def set(self, key: str, value: Any) -> None:
        """设置配置项"""
        self.config[key] = value
        print(f"设置配置：{key} = {value}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项"""
        return self.config.get(key, default)
    
    def load_from_dict(self, config_dict: Dict[str, Any]) -> None:
        """从字典加载配置"""
        self.config.update(config_dict)
        print(f"加载配置：{len(config_dict)}项")
    
    def get_all(self) -> Dict[str, Any]:
        """获取所有配置"""
        return self.config.copy()

# 测试单例模式
print("练习 6.1 测试：")

# 测试DatabaseManager单例
print("数据库管理器测试：")
db1 = DatabaseManager()
db2 = DatabaseManager()
print(f"db1 is db2: {db1 is db2}")

db1.get_connection("users_db")
db2.get_connection("products_db")
db1.get_connection("users_db")  # 复用连接

print(f"状态：{db1.get_status()}")

# 测试ConfigManager单例
print("\n配置管理器测试：")
config1 = ConfigManager()
config2 = ConfigManager()
print(f"config1 is config2: {config1 is config2}")

config1.set("debug", True)
config1.set("max_connections", 100)
print(f"从config2获取debug：{config2.get('debug')}")

# 练习 6.2：工厂模式
class Animal(ABC):
    """动物抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        pass
    
    def __str__(self) -> str:
        return f"{self.get_type()}：{self.name}"

class Dog(Animal):
    """狗类"""
    
    def make_sound(self) -> str:
        return "汪汪！"
    
    def get_type(self) -> str:
        return "狗"
    
    def fetch(self) -> str:
        return f"{self.name}去捡球了！"

class Cat(Animal):
    """猫类"""
    
    def make_sound(self) -> str:
        return "喵喵！"
    
    def get_type(self) -> str:
        return "猫"
    
    def climb(self) -> str:
        return f"{self.name}爬到了树上！"

class Bird(Animal):
    """鸟类"""
    
    def make_sound(self) -> str:
        return "啾啾！"
    
    def get_type(self) -> str:
        return "鸟"
    
    def fly(self) -> str:
        return f"{self.name}飞起来了！"

class Fish(Animal):
    """鱼类"""
    
    def make_sound(self) -> str:
        return "咕噜咕噜..."
    
    def get_type(self) -> str:
        return "鱼"
    
    def swim(self) -> str:
        return f"{self.name}在水中游泳！"

class AnimalFactory:
    """动物工厂"""
    
    _animal_types = {
        'dog': Dog,
        'cat': Cat,
        'bird': Bird,
        'fish': Fish
    }
    
    @classmethod
    def create_animal(cls, animal_type: str, name: str) -> Animal:
        """创建动物"""
        animal_type = animal_type.lower()
        if animal_type not in cls._animal_types:
            available_types = ', '.join(cls._animal_types.keys())
            raise ValueError(f"不支持的动物类型：{animal_type}。支持的类型：{available_types}")
        
        animal_class = cls._animal_types[animal_type]
        return animal_class(name)
    
    @classmethod
    def get_supported_types(cls) -> List[str]:
        """获取支持的动物类型"""
        return list(cls._animal_types.keys())
    
    @classmethod
    def register_animal_type(cls, animal_type: str, animal_class: type) -> None:
        """注册新的动物类型"""
        if not issubclass(animal_class, Animal):
            raise TypeError("动物类必须继承自Animal")
        cls._animal_types[animal_type.lower()] = animal_class
        print(f"注册新动物类型：{animal_type}")

class Zoo:
    """动物园类"""
    
    def __init__(self, name: str):
        self.name = name
        self.animals = []
    
    def add_animal(self, animal_type: str, name: str) -> None:
        """添加动物"""
        try:
            animal = AnimalFactory.create_animal(animal_type, name)
            self.animals.append(animal)
            print(f"添加动物：{animal}")
        except ValueError as e:
            print(f"添加动物失败：{e}")
    
    def feed_all(self) -> None:
        """喂养所有动物"""
        print(f"\n=== {self.name}喂养时间 ===")
        for animal in self.animals:
            print(f"喂养{animal}，它说：{animal.make_sound()}")
        print("=" * 20)
    
    def animal_show(self) -> None:
        """动物表演"""
        print(f"\n=== {self.name}动物表演 ===")
        for animal in self.animals:
            print(f"{animal}的表演：")
            if isinstance(animal, Dog):
                print(f"  - {animal.fetch()}")
            elif isinstance(animal, Cat):
                print(f"  - {animal.climb()}")
            elif isinstance(animal, Bird):
                print(f"  - {animal.fly()}")
            elif isinstance(animal, Fish):
                print(f"  - {animal.swim()}")
        print("=" * 20)
    
    def get_statistics(self) -> Dict[str, int]:
        """获取动物统计"""
        stats = {}
        for animal in self.animals:
            animal_type = animal.get_type()
            stats[animal_type] = stats.get(animal_type, 0) + 1
        return stats

# 测试工厂模式
print("\n练习 6.2 测试：")

# 创建动物园
zoo = Zoo("快乐动物园")

# 添加各种动物
animals_to_add = [
    ('dog', '旺财'),
    ('cat', '咪咪'),
    ('bird', '小黄'),
    ('fish', '金鱼'),
    ('dog', '大黄'),
    ('cat', '小白')
]

for animal_type, name in animals_to_add:
    zoo.add_animal(animal_type, name)

# 尝试添加不支持的动物类型
zoo.add_animal('elephant', '大象')

# 动物园活动
zoo.feed_all()
zoo.animal_show()

# 统计信息
print(f"\n动物统计：{zoo.get_statistics()}")
print(f"支持的动物类型：{AnimalFactory.get_supported_types()}")

# 练习 6.3：观察者模式
class Observer(ABC):
    """观察者抽象基类"""
    
    @abstractmethod
    def update(self, subject: 'Subject', event: str, data: Any = None) -> None:
        pass

class Subject:
    """被观察者（主题）"""
    
    def __init__(self):
        self._observers = []
    
    def attach(self, observer: Observer) -> None:
        """添加观察者"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"观察者 {observer.__class__.__name__} 已添加")
    
    def detach(self, observer: Observer) -> None:
        """移除观察者"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"观察者 {observer.__class__.__name__} 已移除")
    
    def notify(self, event: str, data: Any = None) -> None:
        """通知所有观察者"""
        print(f"\n=== 通知事件：{event} ===")
        for observer in self._observers:
            observer.update(self, event, data)
        print("=" * 20)

class NewsAgency(Subject):
    """新闻机构"""
    
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.latest_news = None
    
    def publish_news(self, news: str) -> None:
        """发布新闻"""
        self.latest_news = news
        print(f"{self.name} 发布新闻：{news}")
        self.notify("news_published", news)
    
    def breaking_news(self, news: str) -> None:
        """发布突发新闻"""
        self.latest_news = news
        print(f"{self.name} 发布突发新闻：{news}")
        self.notify("breaking_news", news)

class NewsChannel(Observer):
    """新闻频道"""
    
    def __init__(self, name: str):
        self.name = name
        self.news_count = 0
    
    def update(self, subject: Subject, event: str, data: Any = None) -> None:
        """接收新闻更新"""
        self.news_count += 1
        if event == "breaking_news":
            print(f"📺 {self.name}：紧急插播！{data}")
        else:
            print(f"📺 {self.name}：播报新闻 - {data}")

class Newspaper(Observer):
    """报纸"""
    
    def __init__(self, name: str):
        self.name = name
        self.articles = []
    
    def update(self, subject: Subject, event: str, data: Any = None) -> None:
        """接收新闻更新"""
        self.articles.append(data)
        if event == "breaking_news":
            print(f"📰 {self.name}：加印特刊！{data}")
        else:
            print(f"📰 {self.name}：刊登文章 - {data}")

class OnlinePortal(Observer):
    """在线门户"""
    
    def __init__(self, name: str):
        self.name = name
        self.online_articles = []
        self.push_notifications = []
    
    def update(self, subject: Subject, event: str, data: Any = None) -> None:
        """接收新闻更新"""
        self.online_articles.append(data)
        if event == "breaking_news":
            self.push_notifications.append(data)
            print(f"💻 {self.name}：推送通知！{data}")
        else:
            print(f"💻 {self.name}：发布在线文章 - {data}")

class MobileApp(Observer):
    """手机应用"""
    
    def __init__(self, name: str):
        self.name = name
        self.notifications = []
    
    def update(self, subject: Subject, event: str, data: Any = None) -> None:
        """接收新闻更新"""
        self.notifications.append(data)
        if event == "breaking_news":
            print(f"📱 {self.name}：弹窗提醒！{data}")
        else:
            print(f"📱 {self.name}：推送消息 - {data}")

# 测试观察者模式
print("\n练习 6.3 测试：")

# 创建新闻机构
news_agency = NewsAgency("环球新闻社")

# 创建各种媒体观察者
channel1 = NewsChannel("新闻频道1")
channel2 = NewsChannel("财经频道")
newspaper1 = Newspaper("日报")
newspaper2 = Newspaper("晚报")
portal = OnlinePortal("新闻门户")
app = MobileApp("新闻APP")

# 注册观察者
print("注册观察者：")
news_agency.attach(channel1)
news_agency.attach(channel2)
news_agency.attach(newspaper1)
news_agency.attach(newspaper2)
news_agency.attach(portal)
news_agency.attach(app)

# 发布普通新闻
news_agency.publish_news("科技公司发布新产品")
news_agency.publish_news("股市今日上涨2%")

# 发布突发新闻
news_agency.breaking_news("重大科学发现！")

# 移除一些观察者
print("\n移除部分观察者：")
news_agency.detach(newspaper2)
news_agency.detach(channel2)

# 再次发布新闻
news_agency.publish_news("新政策即将实施")

# ============================================================================
# 7. 综合应用练习 - 参考答案
# ============================================================================

print("\n\n7. 综合应用练习 - 参考答案")
print("-" * 30)

# 练习 7.1：图书管理系统
class Book:
    """图书类"""
    
    def __init__(self, isbn: str, title: str, author: str, 
                 publisher: str, year: int, price: float):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.price = price
        self.is_borrowed = False
        self.borrower = None
        self.borrow_date = None
    
    def borrow(self, borrower: 'Member') -> bool:
        """借书"""
        if self.is_borrowed:
            return False
        
        self.is_borrowed = True
        self.borrower = borrower
        self.borrow_date = datetime.now()
        return True
    
    def return_book(self) -> bool:
        """还书"""
        if not self.is_borrowed:
            return False
        
        self.is_borrowed = False
        self.borrower = None
        self.borrow_date = None
        return True
    
    def __str__(self) -> str:
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"《{self.title}》- {self.author} ({status})"
    
    def __repr__(self) -> str:
        return f"Book('{self.isbn}', '{self.title}', '{self.author}')"

class Member:
    """会员类"""
    
    def __init__(self, member_id: str, name: str, email: str, phone: str):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []
        self.borrow_history = []
        self.join_date = datetime.now()
    
    def can_borrow(self, max_books: int = 5) -> bool:
        """检查是否可以借书"""
        return len(self.borrowed_books) < max_books
    
    def borrow_book(self, book: Book) -> bool:
        """借书"""
        if not self.can_borrow():
            return False
        
        if book.borrow(self):
            self.borrowed_books.append(book)
            self.borrow_history.append({
                'book': book,
                'action': 'borrow',
                'date': datetime.now()
            })
            return True
        return False
    
    def return_book(self, book: Book) -> bool:
        """还书"""
        if book not in self.borrowed_books:
            return False
        
        if book.return_book():
            self.borrowed_books.remove(book)
            self.borrow_history.append({
                'book': book,
                'action': 'return',
                'date': datetime.now()
            })
            return True
        return False
    
    def __str__(self) -> str:
        return f"会员：{self.name} (ID: {self.member_id})，已借：{len(self.borrowed_books)}本"

class Library:
    """图书馆类"""
    
    def __init__(self, name: str):
        self.name = name
        self.books = {}  # ISBN -> Book
        self.members = {}  # member_id -> Member
        self.max_borrow_books = 5
        self.max_borrow_days = 30
    
    def add_book(self, book: Book) -> bool:
        """添加图书"""
        if book.isbn in self.books:
            print(f"图书已存在：{book.isbn}")
            return False
        
        self.books[book.isbn] = book
        print(f"添加图书：{book}")
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """移除图书"""
        if isbn not in self.books:
            print(f"图书不存在：{isbn}")
            return False
        
        book = self.books[isbn]
        if book.is_borrowed:
            print(f"图书已借出，无法移除：{book}")
            return False
        
        del self.books[isbn]
        print(f"移除图书：{book}")
        return True
    
    def register_member(self, member: Member) -> bool:
        """注册会员"""
        if member.member_id in self.members:
            print(f"会员已存在：{member.member_id}")
            return False
        
        self.members[member.member_id] = member
        print(f"注册会员：{member}")
        return True
    
    def borrow_book(self, member_id: str, isbn: str) -> bool:
        """借书"""
        if member_id not in self.members:
            print(f"会员不存在：{member_id}")
            return False
        
        if isbn not in self.books:
            print(f"图书不存在：{isbn}")
            return False
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if not member.can_borrow(self.max_borrow_books):
            print(f"会员{member.name}已达到最大借书数量")
            return False
        
        if book.is_borrowed:
            print(f"图书已被借出：{book}")
            return False
        
        if member.borrow_book(book):
            print(f"借书成功：{member.name} 借阅 {book.title}")
            return True
        
        return False
    
    def return_book(self, member_id: str, isbn: str) -> bool:
        """还书"""
        if member_id not in self.members:
            print(f"会员不存在：{member_id}")
            return False
        
        if isbn not in self.books:
            print(f"图书不存在：{isbn}")
            return False
        
        member = self.members[member_id]
        book = self.books[isbn]
        
        if member.return_book(book):
            print(f"还书成功：{member.name} 归还 {book.title}")
            return True
        
        print(f"还书失败：{member.name} 未借阅 {book.title}")
        return False
    
    def search_books(self, keyword: str) -> List[Book]:
        """搜索图书"""
        results = []
        keyword = keyword.lower()
        
        for book in self.books.values():
            if (keyword in book.title.lower() or 
                keyword in book.author.lower() or 
                keyword in book.publisher.lower()):
                results.append(book)
        
        return results
    
    def get_overdue_books(self) -> List[Dict[str, Any]]:
        """获取逾期图书"""
        overdue = []
        current_time = datetime.now()
        
        for book in self.books.values():
            if book.is_borrowed and book.borrow_date:
                days_borrowed = (current_time - book.borrow_date).days
                if days_borrowed > self.max_borrow_days:
                    overdue.append({
                        'book': book,
                        'member': book.borrower,
                        'days_overdue': days_borrowed - self.max_borrow_days
                    })
        
        return overdue
    
    def get_statistics(self) -> Dict[str, Any]:
        """获取统计信息"""
        total_books = len(self.books)
        borrowed_books = sum(1 for book in self.books.values() if book.is_borrowed)
        available_books = total_books - borrowed_books
        
        return {
            'total_books': total_books,
            'borrowed_books': borrowed_books,
            'available_books': available_books,
            'total_members': len(self.members),
            'borrow_rate': borrowed_books / total_books if total_books > 0 else 0
        }

# 测试图书管理系统
print("练习 7.1 测试：")

# 创建图书馆
library = Library("市立图书馆")

# 添加图书
books_data = [
    ("978-0-123456-78-9", "Python编程", "张三", "科技出版社", 2023, 89.0),
    ("978-0-123456-79-6", "数据结构与算法", "李四", "教育出版社", 2022, 76.5),
    ("978-0-123456-80-2", "机器学习实战", "王五", "科技出版社", 2023, 95.0),
    ("978-0-123456-81-9", "Web开发指南", "赵六", "网络出版社", 2023, 82.0)
]

for isbn, title, author, publisher, year, price in books_data:
    book = Book(isbn, title, author, publisher, year, price)
    library.add_book(book)

# 注册会员
members_data = [
    ("M001", "小明", "xiaoming@email.com", "13800138001"),
    ("M002", "小红", "xiaohong@email.com", "13800138002"),
    ("M003", "小刚", "xiaogang@email.com", "13800138003")
]

for member_id, name, email, phone in members_data:
    member = Member(member_id, name, email, phone)
    library.register_member(member)

# 借书操作
print("\n=== 借书操作 ===")
library.borrow_book("M001", "978-0-123456-78-9")
library.borrow_book("M001", "978-0-123456-79-6")
library.borrow_book("M002", "978-0-123456-80-2")
library.borrow_book("M001", "978-0-123456-78-9")  # 重复借阅

# 搜索图书
print("\n=== 搜索图书 ===")
search_results = library.search_books("Python")
print(f"搜索'Python'的结果：")
for book in search_results:
    print(f"  - {book}")

# 还书操作
print("\n=== 还书操作 ===")
library.return_book("M001", "978-0-123456-78-9")
library.return_book("M002", "978-0-123456-79-6")  # 错误的还书

# 统计信息
print("\n=== 统计信息 ===")
stats = library.get_statistics()
for key, value in stats.items():
    if key == 'borrow_rate':
        print(f"{key}: {value:.2%}")
    else:
        print(f"{key}: {value}")

print("\n" + "=" * 50)
print("面向对象编程练习题参考答案完成！")
print("=" * 50)

# ============================================================================
# 学习要点总结
# ============================================================================

print("\n\n=== 面向对象编程学习要点总结 ===")
print("""
1. 类和对象基础
   - 类是对象的模板，对象是类的实例
   - 实例属性vs类属性，实例方法vs类方法vs静态方法
   - 构造函数__init__和字符串表示__str__、__repr__

2. 继承
   - 单继承：子类继承父类的属性和方法
   - 多重继承：MRO（方法解析顺序）
   - 方法重写：子类重新定义父类方法
   - super()：调用父类方法

3. 封装
   - 访问控制：公开、受保护(_)、私有(__)
   - 属性装饰器：@property、@setter、@deleter
   - 数据验证和业务逻辑封装

4. 多态
   - 方法重写实现多态
   - 抽象基类ABC和@abstractmethod
   - 协议Protocol（结构化子类型）
   - 鸭子类型："如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子"

5. 特殊方法（魔术方法）
   - 运算符重载：__add__、__sub__、__mul__等
   - 比较操作：__eq__、__lt__、__gt__等
   - 容器操作：__len__、__getitem__、__setitem__等
   - 迭代器：__iter__、__next__
   - 上下文管理器：__enter__、__exit__

6. 设计模式
   - 单例模式：确保类只有一个实例
   - 工厂模式：创建对象的接口
   - 观察者模式：一对多的依赖关系

7. 最佳实践
   - 单一职责原则：一个类只负责一个功能
   - 开闭原则：对扩展开放，对修改关闭
   - 里氏替换原则：子类可以替换父类
   - 依赖倒置原则：依赖抽象而不是具体实现
   - 组合优于继承：优先使用组合而不是继承
""")

print("\n=== 编程最佳实践 ===")
print("""
1. 命名约定
   - 类名：PascalCase（如：StudentManager）
   - 方法和属性：snake_case（如：get_student_info）
   - 常量：UPPER_CASE（如：MAX_STUDENTS）
   - 私有属性：以下划线开头（如：_private_var）

2. 文档字符串
   - 为类和方法编写清晰的文档字符串
   - 说明参数、返回值和异常
   - 提供使用示例

3. 类型提示
   - 使用类型提示提高代码可读性
   - from typing import List, Dict, Optional等
   - 有助于IDE提供更好的代码补全

4. 异常处理
   - 在适当的地方抛出和捕获异常
   - 使用具体的异常类型
   - 提供有意义的错误信息

5. 测试
   - 为类和方法编写单元测试
   - 测试正常情况和边界情况
   - 使用断言验证预期行为
""")