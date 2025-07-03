#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第1章：变量与数据类型 - 示例代码

本文件包含Python基本数据类型和变量操作的示例
"""

# ============================================================================
# 1. 基本数据类型示例
# ============================================================================

print("=" * 50)
print("1. 基本数据类型示例")
print("=" * 50)

# 1.1 整数类型 (int)
age = 25
temperature = -10
big_number = 1000000

print(f"年龄: {age}, 类型: {type(age)}")
print(f"温度: {temperature}, 类型: {type(temperature)}")
print(f"大数字: {big_number}, 类型: {type(big_number)}")

# 1.2 浮点数类型 (float)
height = 175.5
pi = 3.14159
scientific = 1.23e-4  # 科学计数法

print(f"\n身高: {height}, 类型: {type(height)}")
print(f"圆周率: {pi}, 类型: {type(pi)}")
print(f"科学计数法: {scientific}, 类型: {type(scientific)}")

# 1.3 字符串类型 (str)
name = "张三"
message = '你好，世界！'
multiline = """这是一个
多行字符串
示例"""

print(f"\n姓名: {name}, 类型: {type(name)}")
print(f"消息: {message}, 类型: {type(message)}")
print(f"多行字符串: {multiline}, 类型: {type(multiline)}")

# 1.4 布尔类型 (bool)
is_student = True
is_working = False

print(f"\n是学生: {is_student}, 类型: {type(is_student)}")
print(f"在工作: {is_working}, 类型: {type(is_working)}")

# 1.5 空值类型 (None)
data = None
print(f"\n数据: {data}, 类型: {type(data)}")

# 1.6 复数类型 (complex)
complex_num = 3 + 4j
print(f"\n复数: {complex_num}, 类型: {type(complex_num)}")
print(f"实部: {complex_num.real}, 虚部: {complex_num.imag}")

# ============================================================================
# 2. 变量赋值和命名
# ============================================================================

print("\n" + "=" * 50)
print("2. 变量赋值和命名")
print("=" * 50)

# 2.1 基本赋值
x = 10
y = 20
z = x + y
print(f"x = {x}, y = {y}, z = x + y = {z}")

# 2.2 多重赋值
a, b, c = 1, 2, 3
print(f"\n多重赋值: a = {a}, b = {b}, c = {c}")

# 2.3 链式赋值
m = n = o = 100
print(f"链式赋值: m = {m}, n = {n}, o = {o}")

# 2.4 变量交换
num1, num2 = 5, 10
print(f"\n交换前: num1 = {num1}, num2 = {num2}")
num1, num2 = num2, num1
print(f"交换后: num1 = {num1}, num2 = {num2}")

# 2.5 命名规范示例
user_name = "李四"  # 推荐：小写+下划线
MAX_SIZE = 1000    # 推荐：常量用大写
_private_var = "私有变量"  # 约定：下划线开头表示私有

print(f"\n用户名: {user_name}")
print(f"最大尺寸: {MAX_SIZE}")
print(f"私有变量: {_private_var}")

# ============================================================================
# 3. 类型检查和转换
# ============================================================================

print("\n" + "=" * 50)
print("3. 类型检查和转换")
print("=" * 50)

# 3.1 类型检查
value = 42
print(f"值: {value}")
print(f"类型: {type(value)}")
print(f"是否为整数: {isinstance(value, int)}")
print(f"是否为字符串: {isinstance(value, str)}")

# 3.2 显式类型转换
str_num = "123"
float_num = "45.67"
bool_str = "True"

print(f"\n字符串转整数: '{str_num}' -> {int(str_num)}")
print(f"字符串转浮点数: '{float_num}' -> {float(float_num)}")
print(f"整数转字符串: {value} -> '{str(value)}'")
print(f"整数转浮点数: {value} -> {float(value)}")

# 3.3 布尔值转换
print(f"\n布尔值转换示例:")
values = [0, 1, -1, "", "hello", [], [1, 2], None]
for val in values:
    print(f"{repr(val):>10} -> {bool(val)}")

# ============================================================================
# 4. 变量的内存管理
# ============================================================================

print("\n" + "=" * 50)
print("4. 变量的内存管理")
print("=" * 50)

# 4.1 变量引用
list1 = [1, 2, 3]
list2 = list1  # list2引用同一个对象
list3 = list1.copy()  # list3是新对象

print(f"list1 id: {id(list1)}")
print(f"list2 id: {id(list2)}")
print(f"list3 id: {id(list3)}")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")

# 4.2 小整数缓存
a = 100
b = 100
print(f"\n小整数缓存:")
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")
print(f"id(a): {id(a)}, id(b): {id(b)}")

# 大整数不缓存
c = 1000
d = 1000
print(f"\n大整数:")
print(f"c = {c}, d = {d}")
print(f"c is d: {c is d}")
print(f"id(c): {id(c)}, id(d): {id(d)}")

# ============================================================================
# 5. 常见错误和注意事项
# ============================================================================

print("\n" + "=" * 50)
print("5. 常见错误和注意事项")
print("=" * 50)

# 5.1 类型转换错误处理
try:
    invalid_int = int("abc")
except ValueError as e:
    print(f"类型转换错误: {e}")

# 5.2 除零错误
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"除零错误: {e}")

# 5.3 浮点数精度问题
print(f"\n浮点数精度问题:")
print(f"0.1 + 0.2 = {0.1 + 0.2}")
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")

# 解决方案：使用decimal模块
from decimal import Decimal
dec1 = Decimal('0.1')
dec2 = Decimal('0.2')
print(f"使用Decimal: {dec1} + {dec2} = {dec1 + dec2}")

print("\n" + "=" * 50)
print("示例代码运行完成！")
print("=" * 50)