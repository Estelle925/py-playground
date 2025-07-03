# 第五部分：面向对象编程 (Object-Oriented Programming)

## 学习目标

通过本章学习，你将掌握：
- 类和对象的基本概念
- 属性和方法的定义与使用
- 构造函数和析构函数
- 继承、封装、多态三大特性
- 特殊方法（魔术方法）
- 类方法和静态方法
- 属性装饰器
- 抽象类和接口
- 设计模式基础

## 1. 类和对象基础

### 1.1 类的定义

```python
class Person:
    """人员类"""
    # 类属性
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """构造函数"""
        # 实例属性
        self.name = name
        self.age = age
    
    def introduce(self):
        """实例方法"""
        return f"我是{self.name}，今年{self.age}岁"
```

### 1.2 对象的创建和使用

```python
# 创建对象
person1 = Person("张三", 25)
person2 = Person("李四", 30)

# 访问属性
print(person1.name)  # 张三
print(Person.species)  # Homo sapiens

# 调用方法
print(person1.introduce())  # 我是张三，今年25岁
```

## 2. 属性和方法

### 2.1 实例属性 vs 类属性

```python
class Counter:
    # 类属性 - 所有实例共享
    total_count = 0
    
    def __init__(self, name):
        # 实例属性 - 每个实例独有
        self.name = name
        self.count = 0
        Counter.total_count += 1
    
    def increment(self):
        self.count += 1
```

### 2.2 方法类型

```python
class MathUtils:
    pi = 3.14159
    
    def __init__(self, precision=2):
        self.precision = precision
    
    # 实例方法
    def round_number(self, number):
        return round(number, self.precision)
    
    # 类方法
    @classmethod
    def create_default(cls):
        return cls(precision=3)
    
    # 静态方法
    @staticmethod
    def add(a, b):
        return a + b
```

## 3. 继承 (Inheritance)

### 3.1 基本继承

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "动物发出声音"
    
    def move(self):
        return f"{self.name}在移动"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "犬科")
        self.breed = breed
    
    def make_sound(self):  # 方法重写
        return "汪汪汪"
    
    def fetch(self):  # 新方法
        return f"{self.name}去捡球"
```

### 3.2 多重继承

```python
class Flyable:
    def fly(self):
        return "飞行中"

class Swimmable:
    def swim(self):
        return "游泳中"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "鸭科")
    
    def make_sound(self):
        return "嘎嘎嘎"
```

### 3.3 方法解析顺序 (MRO)

```python
# 查看方法解析顺序
print(Duck.__mro__)
# 或者
print(Duck.mro())
```

## 4. 封装 (Encapsulation)

### 4.1 访问控制

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number  # 公开属性
        self._balance = initial_balance       # 受保护属性
        self.__pin = "1234"                  # 私有属性
    
    def get_balance(self):
        """公开方法"""
        return self._balance
    
    def _validate_amount(self, amount):
        """受保护方法"""
        return amount > 0
    
    def __encrypt_pin(self, pin):
        """私有方法"""
        return f"encrypted_{pin}"
    
    def deposit(self, amount):
        if self._validate_amount(amount):
            self._balance += amount
            return True
        return False
```

### 4.2 属性装饰器

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """获取摄氏温度"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏温度"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """获取华氏温度"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """设置华氏温度"""
        self.celsius = (value - 32) * 5/9
```

## 5. 多态 (Polymorphism)

### 5.1 方法重写

```python
class Shape:
    def area(self):
        raise NotImplementedError("子类必须实现area方法")
    
    def perimeter(self):
        raise NotImplementedError("子类必须实现perimeter方法")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
```

### 5.2 多态的使用

```python
def print_shape_info(shape):
    """多态函数 - 接受任何Shape子类"""
    print(f"面积: {shape.area():.2f}")
    print(f"周长: {shape.perimeter():.2f}")

# 使用多态
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 8)
]

for shape in shapes:
    print_shape_info(shape)
```

## 6. 特殊方法（魔术方法）

### 6.1 常用特殊方法

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """开发者表示"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """加法运算"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """相等比较"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """长度"""
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        """索引访问"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("向量只有两个分量")
```

### 6.2 上下文管理器

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """进入上下文"""
        print(f"打开文件: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.file:
            self.file.close()
            print(f"关闭文件: {self.filename}")
        
        # 返回False表示不抑制异常
        return False

# 使用上下文管理器
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
```

## 7. 抽象类和接口

### 7.1 抽象基类

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    """可绘制接口"""
    
    @abstractmethod
    def draw(self):
        """绘制方法"""
        pass
    
    @abstractmethod
    def get_area(self):
        """获取面积"""
        pass
    
    # 具体方法
    def description(self):
        return f"这是一个可绘制对象，面积为{self.get_area()}"

class Square(Drawable):
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        return f"绘制边长为{self.side}的正方形"
    
    def get_area(self):
        return self.side ** 2
```

### 7.2 协议和类型提示

```python
from typing import Protocol

class Comparable(Protocol):
    """可比较协议"""
    def __lt__(self, other):
        ...

def sort_items(items: list[Comparable]) -> list[Comparable]:
    """排序函数，接受任何实现了Comparable协议的对象"""
    return sorted(items)
```

## 8. 设计模式基础

### 8.1 单例模式

```python
class Singleton:
    _instance = None
    _initialized = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._initialized:
            self.value = 0
            self._initialized = True
```

### 8.2 工厂模式

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "dog":
            return Dog(name, "混种")
        elif animal_type == "duck":
            return Duck(name)
        else:
            raise ValueError(f"未知的动物类型: {animal_type}")
```

### 8.3 观察者模式

```python
class Observable:
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class Observer:
    def update(self, observable, *args, **kwargs):
        raise NotImplementedError
```

## 9. 最佳实践

### 9.1 设计原则

1. **单一职责原则 (SRP)**：一个类应该只有一个改变的理由
2. **开闭原则 (OCP)**：对扩展开放，对修改关闭
3. **里氏替换原则 (LSP)**：子类应该能够替换父类
4. **接口隔离原则 (ISP)**：不应该强迫类依赖它们不使用的方法
5. **依赖倒置原则 (DIP)**：依赖抽象而不是具体实现

### 9.2 命名约定

- 类名使用 PascalCase：`MyClass`
- 方法和属性使用 snake_case：`my_method`
- 常量使用 UPPER_CASE：`MAX_SIZE`
- 私有属性以双下划线开头：`__private_attr`
- 受保护属性以单下划线开头：`_protected_attr`

### 9.3 文档字符串

```python
class Calculator:
    """简单计算器类
    
    这个类提供基本的数学运算功能。
    
    Attributes:
        precision (int): 计算精度
    
    Example:
        >>> calc = Calculator(precision=2)
        >>> calc.add(1.5, 2.3)
        3.8
    """
    
    def __init__(self, precision=2):
        """初始化计算器
        
        Args:
            precision (int): 小数点后保留位数
        """
        self.precision = precision
    
    def add(self, a, b):
        """加法运算
        
        Args:
            a (float): 第一个数
            b (float): 第二个数
        
        Returns:
            float: 两数之和
        
        Raises:
            TypeError: 当参数不是数字时
        """
        return round(a + b, self.precision)
```

## 10. 常见陷阱和注意事项

### 10.1 可变默认参数

```python
# 错误示例
class BadList:
    def __init__(self, items=[]):  # 危险！
        self.items = items

# 正确示例
class GoodList:
    def __init__(self, items=None):
        self.items = items if items is not None else []
```

### 10.2 循环引用

```python
class Parent:
    def __init__(self):
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # 可能造成循环引用

# 使用弱引用避免循环引用
import weakref

class Child:
    def __init__(self):
        self._parent = None
    
    @property
    def parent(self):
        return self._parent() if self._parent else None
    
    @parent.setter
    def parent(self, value):
        self._parent = weakref.ref(value) if value else None
```

## 练习建议

1. **基础练习**：创建简单的类和对象
2. **继承练习**：设计类层次结构
3. **多态练习**：实现通用接口
4. **封装练习**：使用属性装饰器
5. **特殊方法练习**：实现运算符重载
6. **设计模式练习**：实现常见设计模式
7. **项目练习**：设计完整的面向对象系统

通过这些练习，你将深入理解面向对象编程的核心概念，并能够设计出结构清晰、易于维护的代码。