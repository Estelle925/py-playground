# 第四部分：函数

## 学习目标

通过本章学习，你将掌握：

1. **函数基础**：定义、调用、参数传递
2. **参数类型**：位置参数、关键字参数、默认参数、可变参数
3. **返回值**：单个返回值、多个返回值、生成器
4. **作用域**：局部作用域、全局作用域、闭包
5. **高级特性**：装饰器、lambda函数、递归
6. **函数式编程**：map、filter、reduce等
7. **最佳实践**：函数设计原则、文档字符串、类型提示

## 1. 函数基础

### 1.1 函数定义和调用

```python
# 基本函数定义
def greet(name):
    """问候函数"""
    return f"Hello, {name}!"

# 函数调用
result = greet("Alice")
print(result)  # Hello, Alice!
```

### 1.2 函数的组成部分

- **def关键字**：定义函数
- **函数名**：遵循标识符命名规则
- **参数列表**：函数接收的输入
- **文档字符串**：函数说明（可选但推荐）
- **函数体**：实现功能的代码
- **返回值**：函数的输出（可选）

## 2. 参数类型

### 2.1 位置参数

```python
def add(a, b):
    return a + b

result = add(3, 5)  # a=3, b=5
```

### 2.2 关键字参数

```python
def introduce(name, age, city):
    return f"我是{name}，{age}岁，来自{city}"

# 关键字参数调用
result = introduce(age=25, city="北京", name="张三")
```

### 2.3 默认参数

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
```

**注意事项**：
- 默认参数必须在非默认参数之后
- 避免使用可变对象作为默认参数

```python
# 错误示例
def bad_function(items=[]):  # 危险！
    items.append("new")
    return items

# 正确示例
def good_function(items=None):
    if items is None:
        items = []
    items.append("new")
    return items
```

### 2.4 可变参数

#### *args（可变位置参数）

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(10, 20))         # 30
```

#### **kwargs（可变关键字参数）

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="上海")
```

#### 混合使用

```python
def flexible_function(required, *args, default="default", **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

flexible_function("必需参数", 1, 2, 3, default="自定义", extra="额外")
```

## 3. 返回值

### 3.1 单个返回值

```python
def square(x):
    return x ** 2

def get_absolute(x):
    if x >= 0:
        return x
    else:
        return -x
```

### 3.2 多个返回值

```python
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder  # 返回元组

q, r = divide_with_remainder(17, 5)  # 解包
print(f"商: {q}, 余数: {r}")  # 商: 3, 余数: 2
```

### 3.3 无返回值

```python
def print_message(message):
    print(message)
    # 隐式返回None

result = print_message("Hello")
print(result)  # None
```

## 4. 作用域

### 4.1 局部作用域和全局作用域

```python
global_var = "全局变量"

def my_function():
    local_var = "局部变量"
    print(global_var)  # 可以访问全局变量
    print(local_var)   # 访问局部变量

my_function()
# print(local_var)  # 错误！局部变量在函数外不可访问
```

### 4.2 global关键字

```python
counter = 0

def increment():
    global counter
    counter += 1

print(counter)  # 0
increment()
print(counter)  # 1
```

### 4.3 nonlocal关键字

```python
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 1
        return x
    
    return inner_function

func = outer_function()
print(func())  # 11
print(func())  # 12
```

### 4.4 闭包

```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

## 5. 高级特性

### 5.1 Lambda函数

```python
# 基本lambda
square = lambda x: x ** 2
print(square(5))  # 25

# 多个参数
add = lambda x, y: x + y
print(add(3, 4))  # 7

# 在高阶函数中使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### 5.2 装饰器基础

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("函数执行前")
        result = func(*args, **kwargs)
        print("函数执行后")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# 输出：
# 函数执行前
# Hello, Alice!
# 函数执行后
```

### 5.3 递归

```python
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

def fibonacci(n):
    """斐波那契数列"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 6. 函数式编程

### 6.1 map函数

```python
numbers = [1, 2, 3, 4, 5]

# 使用map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 等价的列表推导式
squared2 = [x ** 2 for x in numbers]
```

### 6.2 filter函数

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 过滤偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# 等价的列表推导式
even_numbers2 = [x for x in numbers if x % 2 == 0]
```

### 6.3 reduce函数

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 计算乘积
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# 等价的循环
product2 = 1
for num in numbers:
    product2 *= num
```

## 7. 文档字符串和类型提示

### 7.1 文档字符串

```python
def calculate_area(length, width):
    """
    计算矩形面积
    
    Args:
        length (float): 矩形长度
        width (float): 矩形宽度
    
    Returns:
        float: 矩形面积
    
    Raises:
        ValueError: 当长度或宽度为负数时
    
    Examples:
        >>> calculate_area(5, 3)
        15.0
        >>> calculate_area(2.5, 4)
        10.0
    """
    if length < 0 or width < 0:
        raise ValueError("长度和宽度必须为非负数")
    return length * width
```

### 7.2 类型提示

```python
from typing import List, Dict, Optional, Union

def process_numbers(numbers: List[int]) -> Dict[str, float]:
    """
    处理数字列表，返回统计信息
    
    Args:
        numbers: 整数列表
    
    Returns:
        包含统计信息的字典
    """
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers) if numbers else 0,
        "max": max(numbers) if numbers else 0,
        "min": min(numbers) if numbers else 0
    }

def find_user(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    """
    查找用户信息
    
    Args:
        user_id: 用户ID
    
    Returns:
        用户信息字典，如果未找到则返回None
    """
    # 模拟数据库查询
    users = {
        1: {"name": "Alice", "age": 30},
        2: {"name": "Bob", "age": 25}
    }
    return users.get(user_id)
```

## 8. 最佳实践

### 8.1 函数设计原则

1. **单一职责原则**：一个函数只做一件事
2. **函数名要有意义**：清楚表达函数的功能
3. **参数数量适中**：通常不超过3-4个参数
4. **避免副作用**：尽量使用纯函数
5. **适当的抽象层次**：函数内的操作应在同一抽象层次

### 8.2 代码示例

```python
# 好的函数设计
def calculate_discount_price(original_price: float, discount_rate: float) -> float:
    """
    计算折扣后的价格
    
    Args:
        original_price: 原价
        discount_rate: 折扣率（0-1之间）
    
    Returns:
        折扣后的价格
    """
    if not 0 <= discount_rate <= 1:
        raise ValueError("折扣率必须在0-1之间")
    
    return original_price * (1 - discount_rate)

# 避免的函数设计
def bad_function(a, b, c, d, e):  # 参数太多
    # 做了太多不相关的事情
    result1 = a + b
    result2 = c * d
    print(f"结果: {result1}, {result2}")  # 副作用
    global some_global_var  # 修改全局状态
    some_global_var = e
    return result1, result2
```

### 8.3 错误处理

```python
def safe_divide(dividend: float, divisor: float) -> float:
    """
    安全的除法运算
    
    Args:
        dividend: 被除数
        divisor: 除数
    
    Returns:
        除法结果
    
    Raises:
        ZeroDivisionError: 当除数为0时
        TypeError: 当参数类型不正确时
    """
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("参数必须是数字类型")
    
    if divisor == 0:
        raise ZeroDivisionError("除数不能为0")
    
    return dividend / divisor
```

## 9. 常见陷阱

### 9.1 可变默认参数

```python
# 错误
def append_to_list(item, target_list=[]):
    target_list.append(item)
    return target_list

# 正确
def append_to_list(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

### 9.2 闭包中的变量绑定

```python
# 错误
functions = []
for i in range(3):
    functions.append(lambda: i)  # 所有lambda都引用同一个i

for func in functions:
    print(func())  # 输出: 2, 2, 2

# 正确
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # 使用默认参数捕获当前值

for func in functions:
    print(func())  # 输出: 0, 1, 2
```

## 10. 练习建议

1. **基础练习**：编写各种类型的函数，熟悉参数传递
2. **递归练习**：实现经典递归算法（阶乘、斐波那契、汉诺塔）
3. **装饰器练习**：编写计时装饰器、缓存装饰器
4. **函数式编程**：使用map、filter、reduce解决问题
5. **实际项目**：将重复代码抽象成函数
6. **代码重构**：改进现有代码的函数设计
7. **性能优化**：比较不同实现方式的性能
8. **错误处理**：为函数添加适当的错误处理

通过本章的学习和练习，你将能够编写出结构清晰、功能明确、易于维护的函数，这是成为优秀Python程序员的重要基础。