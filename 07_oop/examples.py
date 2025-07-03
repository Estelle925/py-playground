#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第五部分：面向对象编程 - 示例代码

本文件包含面向对象编程的各种示例，展示类、对象、继承、封装、多态等概念
"""

import weakref
import time
from abc import ABC, abstractmethod
from typing import Protocol, List, Optional, Any
from datetime import datetime
from collections import defaultdict

print("第五部分：面向对象编程示例")
print("=" * 50)

# ============================================================================
# 1. 类和对象基础
# ============================================================================

print("\n1. 类和对象基础")
print("-" * 30)

class Person:
    """人员类 - 展示基本的类定义"""
    
    # 类属性 - 所有实例共享
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name: str, age: int, email: str = ""):
        """构造函数
        
        Args:
            name: 姓名
            age: 年龄
            email: 邮箱地址
        """
        # 实例属性 - 每个实例独有
        self.name = name
        self.age = age
        self.email = email
        self.created_at = datetime.now()
        
        # 更新类属性
        Person.population += 1
    
    def introduce(self) -> str:
        """自我介绍"""
        return f"我是{self.name}，今年{self.age}岁"
    
    def celebrate_birthday(self) -> None:
        """庆祝生日"""
        self.age += 1
        print(f"{self.name}过生日了！现在{self.age}岁")
    
    def send_email(self, subject: str, content: str) -> bool:
        """发送邮件（模拟）"""
        if not self.email:
            print(f"{self.name}没有邮箱地址")
            return False
        
        print(f"发送邮件给{self.name}({self.email})")
        print(f"主题: {subject}")
        print(f"内容: {content}")
        return True
    
    @classmethod
    def get_population(cls) -> int:
        """获取总人口数"""
        return cls.population
    
    @staticmethod
    def is_adult(age: int) -> bool:
        """判断是否成年"""
        return age >= 18
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self) -> str:
        """开发者表示"""
        return f"Person('{self.name}', {self.age}, '{self.email}')"

# 创建和使用对象
print("创建Person对象:")
person1 = Person("张三", 25, "zhangsan@example.com")
person2 = Person("李四", 30)
person3 = Person("王五", 17)

print(f"person1: {person1}")
print(f"person2: {person2}")
print(f"总人口: {Person.get_population()}")

print("\n调用方法:")
print(person1.introduce())
person1.celebrate_birthday()
person1.send_email("问候", "你好，最近怎么样？")

print(f"\n静态方法测试:")
print(f"{person1.name}是否成年: {Person.is_adult(person1.age)}")
print(f"{person3.name}是否成年: {Person.is_adult(person3.age)}")

# ============================================================================
# 2. 继承示例
# ============================================================================

print("\n\n2. 继承示例")
print("-" * 30)

class Animal:
    """动物基类"""
    
    def __init__(self, name: str, species: str, age: int = 0):
        self.name = name
        self.species = species
        self.age = age
        self.energy = 100
    
    def eat(self, food: str) -> None:
        """吃东西"""
        print(f"{self.name}正在吃{food}")
        self.energy = min(100, self.energy + 20)
    
    def sleep(self, hours: int) -> None:
        """睡觉"""
        print(f"{self.name}睡了{hours}小时")
        self.energy = min(100, self.energy + hours * 10)
    
    def make_sound(self) -> str:
        """发出声音 - 基类提供默认实现"""
        return f"{self.name}发出了声音"
    
    def move(self) -> str:
        """移动"""
        if self.energy < 10:
            return f"{self.name}太累了，无法移动"
        self.energy -= 10
        return f"{self.name}移动了一段距离"
    
    def get_info(self) -> str:
        """获取动物信息"""
        return f"{self.name}({self.species})，{self.age}岁，能量:{self.energy}"

class Dog(Animal):
    """狗类 - 继承自Animal"""
    
    def __init__(self, name: str, breed: str, age: int = 0):
        # 调用父类构造函数
        super().__init__(name, "犬科", age)
        self.breed = breed  # 狗特有的属性
        self.loyalty = 100
    
    def make_sound(self) -> str:
        """重写父类方法"""
        return f"{self.name}汪汪汪！"
    
    def fetch(self, item: str) -> str:
        """狗特有的方法"""
        if self.energy < 15:
            return f"{self.name}太累了，不想捡{item}"
        self.energy -= 15
        self.loyalty = min(100, self.loyalty + 5)
        return f"{self.name}兴奋地去捡{item}！"
    
    def wag_tail(self) -> str:
        """摇尾巴"""
        return f"{self.name}开心地摇着尾巴"
    
    def get_info(self) -> str:
        """重写获取信息方法"""
        base_info = super().get_info()
        return f"{base_info}，品种:{self.breed}，忠诚度:{self.loyalty}"

class Cat(Animal):
    """猫类 - 继承自Animal"""
    
    def __init__(self, name: str, color: str, age: int = 0):
        super().__init__(name, "猫科", age)
        self.color = color
        self.independence = 80
    
    def make_sound(self) -> str:
        """重写父类方法"""
        return f"{self.name}喵喵喵~"
    
    def climb(self, target: str) -> str:
        """爬高"""
        if self.energy < 20:
            return f"{self.name}没力气爬{target}"
        self.energy -= 20
        return f"{self.name}敏捷地爬上了{target}"
    
    def purr(self) -> str:
        """呼噜声"""
        return f"{self.name}满足地发出呼噜声"
    
    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}，颜色:{self.color}，独立性:{self.independence}"

# 多重继承示例
class Flyable:
    """可飞行的混入类"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.altitude = 0
    
    def fly(self, height: int) -> str:
        """飞行"""
        if hasattr(self, 'energy') and self.energy < 30:
            return f"{self.name}太累了，无法飞行"
        
        if hasattr(self, 'energy'):
            self.energy -= 30
        
        self.altitude = height
        return f"{self.name}飞到了{height}米高空"
    
    def land(self) -> str:
        """降落"""
        self.altitude = 0
        return f"{self.name}安全降落"

class Swimmable:
    """可游泳的混入类"""
    
    def swim(self, distance: int) -> str:
        """游泳"""
        if hasattr(self, 'energy') and self.energy < 25:
            return f"{self.name}太累了，无法游泳"
        
        if hasattr(self, 'energy'):
            self.energy -= 25
        
        return f"{self.name}游了{distance}米"

class Duck(Animal, Flyable, Swimmable):
    """鸭子类 - 多重继承"""
    
    def __init__(self, name: str, age: int = 0):
        # 注意多重继承时的super()调用
        super().__init__(name, "鸭科", age)
    
    def make_sound(self) -> str:
        return f"{self.name}嘎嘎嘎！"
    
    def dive(self, depth: int) -> str:
        """潜水"""
        if self.energy < 20:
            return f"{self.name}太累了，无法潜水"
        self.energy -= 20
        return f"{self.name}潜到了{depth}米深的水中"

# 测试继承
print("创建动物对象:")
dog = Dog("旺财", "金毛", 3)
cat = Cat("咪咪", "橘色", 2)
duck = Duck("唐老鸭", 1)

print(f"狗: {dog.get_info()}")
print(f"猫: {cat.get_info()}")
print(f"鸭: {duck.get_info()}")

print("\n动物行为:")
print(dog.make_sound())
print(cat.make_sound())
print(duck.make_sound())

print("\n特有行为:")
print(dog.fetch("球"))
print(dog.wag_tail())
print(cat.climb("树"))
print(cat.purr())
print(duck.fly(50))
print(duck.swim(100))
print(duck.dive(5))
print(duck.land())

# 查看方法解析顺序
print(f"\nDuck的MRO: {Duck.__mro__}")

# ============================================================================
# 3. 封装示例
# ============================================================================

print("\n\n3. 封装示例")
print("-" * 30)

class BankAccount:
    """银行账户类 - 展示封装概念"""
    
    # 类属性
    bank_name = "Python银行"
    interest_rate = 0.02
    
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0):
        # 公开属性
        self.account_number = account_number
        self.owner = owner
        self.created_at = datetime.now()
        
        # 受保护属性（约定：以单下划线开头）
        self._balance = initial_balance
        self._transaction_history = []
        
        # 私有属性（名称改写：以双下划线开头）
        self.__pin = "1234"
        self.__is_frozen = False
        
        # 记录初始交易
        if initial_balance > 0:
            self._add_transaction("开户", initial_balance)
    
    # 公开方法
    def get_balance(self) -> float:
        """获取余额"""
        return self._balance
    
    def deposit(self, amount: float) -> bool:
        """存款"""
        if not self._validate_amount(amount):
            print("存款金额必须大于0")
            return False
        
        if self.__is_frozen:
            print("账户已冻结，无法存款")
            return False
        
        self._balance += amount
        self._add_transaction("存款", amount)
        print(f"存款成功，当前余额: {self._balance:.2f}")
        return True
    
    def withdraw(self, amount: float, pin: str) -> bool:
        """取款"""
        if not self._validate_pin(pin):
            print("PIN码错误")
            return False
        
        if not self._validate_amount(amount):
            print("取款金额必须大于0")
            return False
        
        if self.__is_frozen:
            print("账户已冻结，无法取款")
            return False
        
        if amount > self._balance:
            print("余额不足")
            return False
        
        self._balance -= amount
        self._add_transaction("取款", -amount)
        print(f"取款成功，当前余额: {self._balance:.2f}")
        return True
    
    def transfer(self, target_account: 'BankAccount', amount: float, pin: str) -> bool:
        """转账"""
        if self.withdraw(amount, pin):
            if target_account.deposit(amount):
                print(f"转账成功：{amount:.2f}元已转至{target_account.owner}的账户")
                return True
            else:
                # 如果目标账户存款失败，需要回滚
                self.deposit(amount)
                print("转账失败：目标账户存款失败")
                return False
        return False
    
    def get_transaction_history(self) -> List[dict]:
        """获取交易历史"""
        return self._transaction_history.copy()
    
    def change_pin(self, old_pin: str, new_pin: str) -> bool:
        """修改PIN码"""
        if not self._validate_pin(old_pin):
            print("原PIN码错误")
            return False
        
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("新PIN码必须是4位数字")
            return False
        
        self.__pin = new_pin
        print("PIN码修改成功")
        return True
    
    # 受保护方法（约定：以单下划线开头）
    def _validate_amount(self, amount: float) -> bool:
        """验证金额"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def _validate_pin(self, pin: str) -> bool:
        """验证PIN码"""
        return pin == self.__pin
    
    def _add_transaction(self, transaction_type: str, amount: float) -> None:
        """添加交易记录"""
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "balance": self._balance,
            "timestamp": datetime.now()
        }
        self._transaction_history.append(transaction)
    
    # 私有方法（名称改写：以双下划线开头）
    def __freeze_account(self) -> None:
        """冻结账户"""
        self.__is_frozen = True
    
    def __unfreeze_account(self) -> None:
        """解冻账户"""
        self.__is_frozen = False
    
    # 管理员方法（演示访问私有方法）
    def admin_freeze(self, admin_code: str) -> bool:
        """管理员冻结账户"""
        if admin_code == "ADMIN123":
            self.__freeze_account()
            print(f"账户{self.account_number}已被冻结")
            return True
        print("管理员代码错误")
        return False
    
    def admin_unfreeze(self, admin_code: str) -> bool:
        """管理员解冻账户"""
        if admin_code == "ADMIN123":
            self.__unfreeze_account()
            print(f"账户{self.account_number}已解冻")
            return True
        print("管理员代码错误")
        return False
    
    def __str__(self) -> str:
        return f"BankAccount({self.account_number}, {self.owner}, {self._balance:.2f})"

# 属性装饰器示例
class Temperature:
    """温度类 - 展示属性装饰器"""
    
    def __init__(self, celsius: float = 0):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """获取摄氏温度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        """设置摄氏温度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度(-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """获取华氏温度"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """设置华氏温度"""
        celsius_value = (value - 32) * 5/9
        if celsius_value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = celsius_value
    
    @property
    def kelvin(self) -> float:
        """获取开尔文温度"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value: float) -> None:
        """设置开尔文温度"""
        if value < 0:
            raise ValueError("开尔文温度不能为负数")
        self._celsius = value - 273.15
    
    def __str__(self) -> str:
        return f"{self._celsius:.2f}°C ({self.fahrenheit:.2f}°F, {self.kelvin:.2f}K)"

# 测试封装
print("银行账户测试:")
account1 = BankAccount("001", "张三", 1000)
account2 = BankAccount("002", "李四", 500)

print(f"账户1: {account1}")
print(f"账户2: {account2}")

print("\n存取款测试:")
account1.deposit(200)
account1.withdraw(150, "1234")
account1.withdraw(150, "0000")  # 错误PIN

print("\n转账测试:")
account1.transfer(account2, 300, "1234")

print("\n交易历史:")
for transaction in account1.get_transaction_history():
    print(f"{transaction['timestamp'].strftime('%H:%M:%S')} - "
          f"{transaction['type']}: {transaction['amount']:.2f}, "
          f"余额: {transaction['balance']:.2f}")

print("\n管理员操作:")
account1.admin_freeze("ADMIN123")
account1.deposit(100)  # 应该失败
account1.admin_unfreeze("ADMIN123")
account1.deposit(100)  # 应该成功

print("\n温度转换测试:")
temp = Temperature(25)
print(f"初始温度: {temp}")

temp.fahrenheit = 100
print(f"设置华氏100度后: {temp}")

temp.kelvin = 300
print(f"设置开尔文300度后: {temp}")

try:
    temp.celsius = -300  # 应该抛出异常
except ValueError as e:
    print(f"温度设置错误: {e}")

# ============================================================================
# 4. 多态示例
# ============================================================================

print("\n\n4. 多态示例")
print("-" * 30)

class Shape(ABC):
    """形状抽象基类"""
    
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def area(self) -> float:
        """计算面积"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """计算周长"""
        pass
    
    def description(self) -> str:
        """描述形状"""
        return f"{self.name}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"

class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width: float, height: float):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        """判断是否为正方形"""
        return abs(self.width - self.height) < 0.001

class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius: float):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self) -> float:
        return 3.14159 * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * 3.14159 * self.radius
    
    def diameter(self) -> float:
        """直径"""
        return 2 * self.radius

class Triangle(Shape):
    """三角形类"""
    
    def __init__(self, a: float, b: float, c: float):
        super().__init__("三角形")
        self.a = a
        self.b = b
        self.c = c
        
        # 验证三角形的有效性
        if not self._is_valid_triangle():
            raise ValueError("无效的三角形边长")
    
    def _is_valid_triangle(self) -> bool:
        """验证三角形是否有效"""
        return (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a)
    
    def area(self) -> float:
        """使用海伦公式计算面积"""
        s = self.perimeter() / 2  # 半周长
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def triangle_type(self) -> str:
        """判断三角形类型"""
        sides = sorted([self.a, self.b, self.c])
        
        if abs(sides[0] - sides[1]) < 0.001 and abs(sides[1] - sides[2]) < 0.001:
            return "等边三角形"
        elif (abs(sides[0] - sides[1]) < 0.001 or 
              abs(sides[1] - sides[2]) < 0.001 or 
              abs(sides[0] - sides[2]) < 0.001):
            return "等腰三角形"
        else:
            return "普通三角形"

# 多态函数
def print_shape_info(shape: Shape) -> None:
    """打印形状信息 - 多态函数"""
    print(f"  {shape.description()}")
    
    # 根据具体类型调用特有方法
    if isinstance(shape, Rectangle):
        if shape.is_square():
            print(f"    这是一个正方形")
    elif isinstance(shape, Circle):
        print(f"    直径: {shape.diameter():.2f}")
    elif isinstance(shape, Triangle):
        print(f"    类型: {shape.triangle_type()}")

def calculate_total_area(shapes: List[Shape]) -> float:
    """计算总面积 - 多态应用"""
    return sum(shape.area() for shape in shapes)

def find_largest_shape(shapes: List[Shape]) -> Shape:
    """找到面积最大的形状"""
    return max(shapes, key=lambda shape: shape.area())

# 测试多态
print("创建各种形状:")
shapes = [
    Rectangle(5, 3),
    Rectangle(4, 4),  # 正方形
    Circle(3),
    Triangle(3, 4, 5),  # 直角三角形
    Triangle(5, 5, 5),  # 等边三角形
    Circle(2)
]

print("\n形状信息:")
for shape in shapes:
    print_shape_info(shape)

print(f"\n总面积: {calculate_total_area(shapes):.2f}")
largest = find_largest_shape(shapes)
print(f"最大形状: {largest.description()}")

# ============================================================================
# 5. 特殊方法示例
# ============================================================================

print("\n\n5. 特殊方法示例")
print("-" * 30)

class Vector:
    """二维向量类 - 展示特殊方法"""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """用户友好的字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """开发者字符串表示"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """向量加法"""
        if not isinstance(other, Vector):
            raise TypeError("只能与另一个Vector相加")
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        """向量减法"""
        if not isinstance(other, Vector):
            raise TypeError("只能与另一个Vector相减")
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        """标量乘法"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("只能与数字相乘")
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar: float) -> 'Vector':
        """右乘法（支持 3 * vector）"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector':
        """标量除法"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("只能除以数字")
        if scalar == 0:
            raise ValueError("不能除以零")
        return Vector(self.x / scalar, self.y / scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        """相等比较"""
        if not isinstance(other, Vector):
            return False
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9
    
    def __lt__(self, other: 'Vector') -> bool:
        """小于比较（按模长）"""
        if not isinstance(other, Vector):
            raise TypeError("只能与另一个Vector比较")
        return self.magnitude() < other.magnitude()
    
    def __le__(self, other: 'Vector') -> bool:
        """小于等于比较"""
        return self < other or self == other
    
    def __abs__(self) -> float:
        """向量的模长"""
        return self.magnitude()
    
    def __len__(self) -> int:
        """向量的维度"""
        return 2
    
    def __getitem__(self, index: int) -> float:
        """索引访问"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("向量索引超出范围")
    
    def __setitem__(self, index: int, value: float) -> None:
        """索引设置"""
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("向量索引超出范围")
    
    def __iter__(self):
        """迭代器"""
        yield self.x
        yield self.y
    
    def __hash__(self) -> int:
        """哈希值（使向量可以作为字典键）"""
        return hash((self.x, self.y))
    
    def magnitude(self) -> float:
        """计算向量模长"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def normalize(self) -> 'Vector':
        """归一化向量"""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("零向量无法归一化")
        return Vector(self.x / mag, self.y / mag)
    
    def dot(self, other: 'Vector') -> float:
        """点积"""
        if not isinstance(other, Vector):
            raise TypeError("只能与另一个Vector计算点积")
        return self.x * other.x + self.y * other.y
    
    def angle_with(self, other: 'Vector') -> float:
        """与另一个向量的夹角（弧度）"""
        import math
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        if magnitudes == 0:
            raise ValueError("零向量无法计算夹角")
        cos_angle = dot_product / magnitudes
        # 处理浮点数精度问题
        cos_angle = max(-1, min(1, cos_angle))
        return math.acos(cos_angle)

# 上下文管理器示例
class Timer:
    """计时器上下文管理器"""
    
    def __init__(self, name: str = "操作"):
        self.name = name
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        """进入上下文"""
        print(f"开始{self.name}...")
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        self.end_time = time.time()
        duration = self.end_time - self.start_time
        
        if exc_type is None:
            print(f"{self.name}完成，耗时: {duration:.4f}秒")
        else:
            print(f"{self.name}失败，耗时: {duration:.4f}秒")
            print(f"异常类型: {exc_type.__name__}")
            print(f"异常信息: {exc_val}")
        
        # 返回False表示不抑制异常
        return False
    
    def elapsed_time(self) -> float:
        """获取已用时间"""
        if self.start_time is None:
            return 0
        current_time = self.end_time if self.end_time else time.time()
        return current_time - self.start_time

# 测试特殊方法
print("向量运算测试:")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"3 * v1 = {3 * v1}")
print(f"v1 / 2 = {v1 / 2}")

print(f"\n向量比较:")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 < v2: {v1 < v2}")
print(f"|v1| = {abs(v1):.2f}")
print(f"|v2| = {abs(v2):.2f}")

print(f"\n向量访问:")
print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")
print(f"len(v1) = {len(v1)}")
print(f"list(v1) = {list(v1)}")

print(f"\n向量运算:")
print(f"v1 · v2 = {v1.dot(v2)}")
import math
angle = v1.angle_with(v2)
print(f"v1与v2夹角: {angle:.4f}弧度 ({math.degrees(angle):.2f}度)")

# 向量作为字典键
vector_dict = {v1: "第一个向量", v2: "第二个向量"}
print(f"\n向量字典: {vector_dict}")

print("\n计时器测试:")
with Timer("向量计算") as timer:
    # 模拟一些计算
    result = Vector(0, 0)
    for i in range(1000):
        result = result + Vector(i, i)
    time.sleep(0.1)  # 模拟耗时操作

print(f"计算结果: {result}")

# 测试异常情况
print("\n异常处理测试:")
try:
    with Timer("错误操作"):
        raise ValueError("模拟错误")
except ValueError:
    print("捕获到异常")

print("\n" + "=" * 50)
print("面向对象编程示例完成！")
print("=" * 50)