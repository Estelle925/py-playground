#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第四部分：函数 - 示例代码

本文件包含函数相关的各种示例，包括：
1. 函数基础
2. 参数类型
3. 返回值
4. 作用域
5. 高级特性
6. 函数式编程
7. 装饰器
8. 实际应用
"""

import time
import functools
from typing import List, Dict, Optional, Union, Callable, Any

print("第四部分：函数示例")
print("=" * 50)

# ============================================================================
# 1. 函数基础
# ============================================================================

print("\n1. 函数基础")
print("-" * 30)

# 1.1 基本函数定义和调用
def greet(name):
    """简单的问候函数"""
    return f"Hello, {name}!"

def calculate_area(length, width):
    """计算矩形面积"""
    return length * width

def get_user_info():
    """获取用户信息（无参数函数）"""
    return {
        "name": "张三",
        "age": 25,
        "city": "北京"
    }

# 函数调用示例
print(f"问候: {greet('Alice')}")
print(f"矩形面积: {calculate_area(5, 3)}")
print(f"用户信息: {get_user_info()}")

# 1.2 函数作为对象
print("\n函数作为对象:")
my_function = greet  # 函数赋值给变量
print(f"通过变量调用: {my_function('Bob')}")
print(f"函数名: {greet.__name__}")
print(f"函数文档: {greet.__doc__}")

# ============================================================================
# 2. 参数类型
# ============================================================================

print("\n\n2. 参数类型")
print("-" * 30)

# 2.1 位置参数
def subtract(a, b):
    """减法运算"""
    return a - b

print(f"位置参数: subtract(10, 3) = {subtract(10, 3)}")

# 2.2 关键字参数
def introduce(name, age, city):
    """自我介绍"""
    return f"我是{name}，{age}岁，来自{city}"

print(f"关键字参数: {introduce(city='上海', name='李四', age=28)}")
print(f"混合参数: {introduce('王五', city='广州', age=30)}")

# 2.3 默认参数
def power(base, exponent=2):
    """幂运算，默认计算平方"""
    return base ** exponent

print(f"默认参数: power(5) = {power(5)}")
print(f"指定参数: power(5, 3) = {power(5, 3)}")

# 2.4 默认参数的陷阱和正确用法
def bad_append(item, target_list=[]):  # 危险的默认参数
    """错误的默认参数示例"""
    target_list.append(item)
    return target_list

def good_append(item, target_list=None):  # 正确的默认参数
    """正确的默认参数示例"""
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

print("\n默认参数陷阱演示:")
print(f"第一次调用bad_append: {bad_append(1)}")
print(f"第二次调用bad_append: {bad_append(2)}")
print(f"第一次调用good_append: {good_append(1)}")
print(f"第二次调用good_append: {good_append(2)}")

# 2.5 可变位置参数 (*args)
def sum_all(*args):
    """计算所有参数的和"""
    return sum(args)

def print_args(*args):
    """打印所有位置参数"""
    print(f"接收到 {len(args)} 个参数:")
    for i, arg in enumerate(args):
        print(f"  参数{i+1}: {arg}")

print("\n可变位置参数:")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print_args("hello", 42, [1, 2, 3], {"key": "value"})

# 2.6 可变关键字参数 (**kwargs)
def print_kwargs(**kwargs):
    """打印所有关键字参数"""
    print(f"接收到 {len(kwargs)} 个关键字参数:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

def create_person(**kwargs):
    """创建人员信息"""
    person = {
        "name": kwargs.get("name", "未知"),
        "age": kwargs.get("age", 0),
        "city": kwargs.get("city", "未知")
    }
    # 添加额外信息
    for key, value in kwargs.items():
        if key not in person:
            person[key] = value
    return person

print("\n可变关键字参数:")
print_kwargs(name="张三", age=25, city="北京", job="工程师")
person = create_person(name="李四", age=30, city="上海", hobby="读书", skill="Python")
print(f"创建的人员信息: {person}")

# 2.7 混合参数类型
def flexible_function(required, *args, default="default", **kwargs):
    """演示混合参数类型"""
    print(f"必需参数: {required}")
    print(f"位置参数: {args}")
    print(f"默认参数: {default}")
    print(f"关键字参数: {kwargs}")

print("\n混合参数类型:")
flexible_function("必需值", 1, 2, 3, default="自定义", extra="额外", info="信息")

# ============================================================================
# 3. 返回值
# ============================================================================

print("\n\n3. 返回值")
print("-" * 30)

# 3.1 单个返回值
def get_square(x):
    """返回平方值"""
    return x ** 2

def get_absolute(x):
    """返回绝对值"""
    if x >= 0:
        return x
    else:
        return -x

print(f"平方值: get_square(5) = {get_square(5)}")
print(f"绝对值: get_absolute(-10) = {get_absolute(-10)}")

# 3.2 多个返回值
def divide_with_remainder(dividend, divisor):
    """除法运算，返回商和余数"""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

def get_name_parts(full_name):
    """分割姓名"""
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], " ".join(parts[1:])
    else:
        return parts[0], ""

print("\n多个返回值:")
q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} 余 {r}")

first_name, last_name = get_name_parts("张 三 丰")
print(f"姓: {first_name}, 名: {last_name}")

# 3.3 返回不同类型的值
def analyze_number(num):
    """分析数字，返回不同类型的信息"""
    if not isinstance(num, (int, float)):
        return None, "输入不是数字"
    
    info = {
        "value": num,
        "type": type(num).__name__,
        "is_positive": num > 0,
        "is_even": num % 2 == 0 if isinstance(num, int) else None,
        "square": num ** 2
    }
    return info, "分析成功"

print("\n返回不同类型:")
result, message = analyze_number(42)
print(f"分析结果: {result}")
print(f"消息: {message}")

# 3.4 无返回值（返回None）
def log_message(message):
    """记录消息（无返回值）"""
    print(f"[LOG] {message}")

def update_global_counter():
    """更新全局计数器"""
    global counter
    counter += 1
    print(f"计数器更新为: {counter}")

counter = 0
result = log_message("这是一条日志")
print(f"log_message返回值: {result}")
update_global_counter()

# ============================================================================
# 4. 作用域
# ============================================================================

print("\n\n4. 作用域")
print("-" * 30)

# 4.1 局部作用域和全局作用域
global_var = "我是全局变量"

def scope_demo():
    """作用域演示"""
    local_var = "我是局部变量"
    print(f"函数内访问全局变量: {global_var}")
    print(f"函数内访问局部变量: {local_var}")
    
    # 局部变量会遮蔽同名的全局变量
    global_var = "我是局部的global_var"
    print(f"局部遮蔽后: {global_var}")

print("作用域演示:")
print(f"函数外的全局变量: {global_var}")
scope_demo()
print(f"函数调用后的全局变量: {global_var}")

# 4.2 global关键字
global_counter = 0

def increment_global():
    """使用global修改全局变量"""
    global global_counter
    global_counter += 1
    print(f"全局计数器: {global_counter}")

def try_increment_without_global():
    """不使用global尝试修改（会出错）"""
    try:
        global_counter += 1  # 这会引发UnboundLocalError
    except UnboundLocalError as e:
        print(f"错误: {e}")

print("\nglobal关键字:")
print(f"初始计数器: {global_counter}")
increment_global()
increment_global()
try_increment_without_global()

# 4.3 nonlocal关键字和闭包
def make_counter(start=0):
    """创建计数器闭包"""
    count = start
    
    def increment(step=1):
        nonlocal count
        count += step
        return count
    
    def decrement(step=1):
        nonlocal count
        count -= step
        return count
    
    def get_count():
        return count
    
    # 返回函数字典
    return {
        "increment": increment,
        "decrement": decrement,
        "get_count": get_count
    }

print("\nnonlocal和闭包:")
counter1 = make_counter(10)
counter2 = make_counter(100)

print(f"counter1初始值: {counter1['get_count']()}")
print(f"counter1递增: {counter1['increment']()}")
print(f"counter1递增5: {counter1['increment'](5)}")
print(f"counter1递减: {counter1['decrement']()}")

print(f"counter2初始值: {counter2['get_count']()}")
print(f"counter2递增: {counter2['increment']()}")

# 4.4 闭包的实际应用
def make_multiplier(factor):
    """创建乘法器"""
    def multiplier(number):
        return number * factor
    return multiplier

def make_validator(min_val, max_val):
    """创建验证器"""
    def validate(value):
        return min_val <= value <= max_val
    return validate

print("\n闭包应用:")
double = make_multiplier(2)
triple = make_multiplier(3)
print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")

age_validator = make_validator(0, 120)
score_validator = make_validator(0, 100)
print(f"年龄25有效: {age_validator(25)}")
print(f"年龄150有效: {age_validator(150)}")
print(f"分数85有效: {score_validator(85)}")
print(f"分数105有效: {score_validator(105)}")

# ============================================================================
# 5. 高级特性
# ============================================================================

print("\n\n5. 高级特性")
print("-" * 30)

# 5.1 Lambda函数
print("Lambda函数:")

# 基本lambda
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0

print(f"square(6) = {square(6)}")
print(f"add(3, 4) = {add(3, 4)}")
print(f"is_even(7) = {is_even(7)}")

# lambda在数据处理中的应用
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 96}
]

# 按分数排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"按分数排序: {[s['name'] for s in sorted_students]}")

# 过滤高分学生
high_score_students = list(filter(lambda s: s["score"] >= 90, students))
print(f"高分学生: {[s['name'] for s in high_score_students]}")

# 5.2 递归函数
print("\n递归函数:")

def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """斐波那契数列"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n, memo={}):
    """带记忆化的斐波那契"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print(f"factorial(5) = {factorial(5)}")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci_memo(30) = {fibonacci_memo(30)}")

# 递归遍历目录结构（模拟）
def print_tree(node, level=0):
    """打印树形结构"""
    indent = "  " * level
    if isinstance(node, dict):
        for key, value in node.items():
            print(f"{indent}{key}/")
            print_tree(value, level + 1)
    elif isinstance(node, list):
        for item in node:
            print_tree(item, level)
    else:
        print(f"{indent}{node}")

file_tree = {
    "project": {
        "src": ["main.py", "utils.py"],
        "tests": ["test_main.py"],
        "docs": {"api": ["index.md"], "guide": ["tutorial.md"]}
    }
}

print("\n目录树结构:")
print_tree(file_tree)

# ============================================================================
# 6. 函数式编程
# ============================================================================

print("\n\n6. 函数式编程")
print("-" * 30)

# 6.1 map函数
numbers = [1, 2, 3, 4, 5]
print(f"原始数据: {numbers}")

# 使用map
squared = list(map(lambda x: x ** 2, numbers))
print(f"平方: {squared}")

# 多个序列的map
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(f"对应相加: {sums}")

# 6.2 filter函数
all_numbers = list(range(1, 21))
print(f"\n所有数字: {all_numbers}")

# 过滤偶数
even_numbers = list(filter(lambda x: x % 2 == 0, all_numbers))
print(f"偶数: {even_numbers}")

# 过滤质数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = list(filter(is_prime, all_numbers))
print(f"质数: {primes}")

# 6.3 reduce函数
from functools import reduce

print("\nreduce函数:")
# 计算乘积
product = reduce(lambda x, y: x * y, numbers)
print(f"乘积: {product}")

# 找最大值
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"最大值: {max_value}")

# 字符串连接
words = ["Hello", "World", "Python", "Programming"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"连接字符串: {sentence}")

# 6.4 高阶函数组合
def compose(*functions):
    """函数组合"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

# 创建组合函数
add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2
square_func = lambda x: x ** 2

# 组合函数：先加1，再乘2，最后平方
composed = compose(square_func, multiply_by_two, add_one)
print(f"\n函数组合 compose(square, *2, +1)(3) = {composed(3)}")

# ============================================================================
# 7. 装饰器
# ============================================================================

print("\n\n7. 装饰器")
print("-" * 30)

# 7.1 基本装饰器
def timer_decorator(func):
    """计时装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f}秒")
        return result
    return wrapper

def log_decorator(func):
    """日志装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    return wrapper

# 使用装饰器
@timer_decorator
def slow_function():
    """模拟耗时操作"""
    time.sleep(0.1)
    return "完成"

@log_decorator
def add_numbers(a, b):
    """加法函数"""
    return a + b

print("装饰器示例:")
result = slow_function()
print(f"结果: {result}")

result = add_numbers(5, 3)

# 7.2 带参数的装饰器
def repeat(times):
    """重复执行装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
                print(f"第{i+1}次执行: {result}")
            return results
        return wrapper
    return decorator

def validate_types(**expected_types):
    """类型验证装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 验证参数类型
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            
            for param_name, expected_type in expected_types.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(f"参数 {param_name} 期望类型 {expected_type.__name__}, 实际类型 {type(value).__name__}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    return f"Hello, {name}!"

@validate_types(x=int, y=int)
def multiply(x, y):
    return x * y

print("\n带参数的装饰器:")
say_hello("Alice")

try:
    result = multiply(5, 3)
    print(f"multiply(5, 3) = {result}")
    multiply(5, "3")  # 这会引发类型错误
except TypeError as e:
    print(f"类型错误: {e}")

# 7.3 类装饰器
class CountCalls:
    """计数装饰器类"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def greet_user(name):
    return f"你好, {name}!"

print("\n类装饰器:")
greet_user("张三")
greet_user("李四")
greet_user("王五")

# 7.4 functools.wraps保持元数据
def better_log_decorator(func):
    """改进的日志装饰器，保持原函数元数据"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@better_log_decorator
def documented_function(x, y):
    """这是一个有文档的函数"""
    return x + y

print("\n保持元数据的装饰器:")
print(f"函数名: {documented_function.__name__}")
print(f"函数文档: {documented_function.__doc__}")
result = documented_function(2, 3)
print(f"结果: {result}")

# ============================================================================
# 8. 实际应用示例
# ============================================================================

print("\n\n8. 实际应用示例")
print("-" * 30)

# 8.1 缓存装饰器
def memoize(func):
    """记忆化装饰器"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"缓存命中: {func.__name__}{args}")
            return cache[key]
        
        print(f"计算中: {func.__name__}{args}")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    wrapper.cache = cache  # 暴露缓存以便检查
    return wrapper

@memoize
def expensive_fibonacci(n):
    """昂贵的斐波那契计算"""
    if n <= 1:
        return n
    return expensive_fibonacci(n - 1) + expensive_fibonacci(n - 2)

print("缓存装饰器示例:")
print(f"fibonacci(10) = {expensive_fibonacci(10)}")
print(f"fibonacci(10) = {expensive_fibonacci(10)}")
print(f"缓存大小: {len(expensive_fibonacci.cache)}")

# 8.2 重试装饰器
def retry(max_attempts=3, delay=1):
    """重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"第{attempt + 1}次尝试失败: {e}")
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
            
            print(f"所有尝试都失败了，抛出最后一个异常")
            raise last_exception
        
        return wrapper
    return decorator

# 模拟不稳定的网络请求
import random

@retry(max_attempts=3, delay=0.1)
def unstable_network_request():
    """模拟不稳定的网络请求"""
    if random.random() < 0.7:  # 70%的失败率
        raise ConnectionError("网络连接失败")
    return "请求成功"

print("\n重试装饰器示例:")
try:
    result = unstable_network_request()
    print(f"最终结果: {result}")
except ConnectionError as e:
    print(f"最终失败: {e}")

# 8.3 数据处理管道
def create_pipeline(*functions):
    """创建数据处理管道"""
    def pipeline(data):
        result = data
        for func in functions:
            result = func(result)
        return result
    return pipeline

# 数据处理函数
def clean_text(text):
    """清理文本"""
    return text.strip().lower()

def remove_punctuation(text):
    """移除标点符号"""
    import string
    return text.translate(str.maketrans('', '', string.punctuation))

def split_words(text):
    """分割单词"""
    return text.split()

def count_words(words):
    """统计单词"""
    from collections import Counter
    return Counter(words)

# 创建文本处理管道
text_pipeline = create_pipeline(
    clean_text,
    remove_punctuation,
    split_words,
    count_words
)

print("\n数据处理管道示例:")
sample_text = "  Hello, World! Hello Python Programming.  "
result = text_pipeline(sample_text)
print(f"原文: {sample_text!r}")
print(f"处理结果: {dict(result)}")

# 8.4 配置管理
class ConfigManager:
    """配置管理器"""
    def __init__(self):
        self._config = {}
        self._validators = {}
    
    def register_validator(self, key, validator_func):
        """注册验证器"""
        self._validators[key] = validator_func
    
    def set(self, key, value):
        """设置配置值"""
        if key in self._validators:
            if not self._validators[key](value):
                raise ValueError(f"配置值 {key}={value} 验证失败")
        self._config[key] = value
    
    def get(self, key, default=None):
        """获取配置值"""
        return self._config.get(key, default)
    
    def configure(self, **kwargs):
        """批量配置"""
        for key, value in kwargs.items():
            self.set(key, value)

# 使用配置管理器
config = ConfigManager()

# 注册验证器
config.register_validator('port', lambda x: isinstance(x, int) and 1 <= x <= 65535)
config.register_validator('debug', lambda x: isinstance(x, bool))
config.register_validator('max_connections', lambda x: isinstance(x, int) and x > 0)

print("\n配置管理示例:")
try:
    config.configure(
        host="localhost",
        port=8080,
        debug=True,
        max_connections=100
    )
    print(f"主机: {config.get('host')}")
    print(f"端口: {config.get('port')}")
    print(f"调试模式: {config.get('debug')}")
    print(f"最大连接数: {config.get('max_connections')}")
    
    # 尝试设置无效值
    config.set('port', 70000)  # 这会失败
except ValueError as e:
    print(f"配置错误: {e}")

print("\n函数示例演示完成！")
print("\n学习要点:")
print("1. 函数是代码复用和模块化的基础")
print("2. 理解不同类型的参数和返回值")
print("3. 掌握作用域和闭包的概念")
print("4. 学会使用装饰器增强函数功能")
print("5. 运用函数式编程思想")
print("6. 在实际项目中合理设计函数")