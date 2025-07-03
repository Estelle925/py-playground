#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第2章：运算符 - 练习题答案

这里提供了exercises.py中所有练习题的参考答案
"""

print("第2章练习题答案：运算符")
print("=" * 40)

# ============================================================================
# 练习1：算术运算符 - 答案
# ============================================================================
print("\n练习1答案：算术运算符")
print("-" * 30)

# 1. 基本算术运算
a, b = 17, 5
print(f"a = {a}, b = {b}")

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
power = a ** b

print(f"a + b = {addition}")
print(f"a - b = {subtraction}")
print(f"a * b = {multiplication}")
print(f"a / b = {division}")
print(f"a // b = {floor_division}")
print(f"a % b = {modulus}")
print(f"a ** b = {power}")

# 2. 字符串和列表运算
str1 = "Python"
str2 = "编程"
list1 = [1, 2]
list2 = [3, 4, 5]

string_concat = str1 + str2
string_repeat = str1 * 3
list_concat = list1 + list2
list_repeat = list1 * 2

print(f"\n字符串连接: '{str1}' + '{str2}' = '{string_concat}'")
print(f"字符串重复: '{str1}' * 3 = '{string_repeat}'")
print(f"列表连接: {list1} + {list2} = {list_concat}")
print(f"列表重复: {list1} * 2 = {list_repeat}")

# ============================================================================
# 练习2：比较运算符 - 答案
# ============================================================================
print("\n练习2答案：比较运算符")
print("-" * 30)

comparisons = [
    (10, 5),
    (3.14, 3.14),
    ("apple", "banana"),
    ("Apple", "apple"),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2], [1, 2, 3]),
]

print("比较运算结果：")
for x, y in comparisons:
    print(f"{repr(x)} vs {repr(y)}:")
    print(f"  == : {x == y}")
    print(f"  != : {x != y}")
    try:
        print(f"  <  : {x < y}")
        print(f"  >  : {x > y}")
        print(f"  <= : {x <= y}")
        print(f"  >= : {x >= y}")
    except TypeError:
        print(f"  <, >, <=, >= : 不支持此类型的比较")
    print()

# 链式比较练习
print("链式比较练习：")
a, b, c = 1, 5, 10
result1 = a < b < c
result2 = a < b > c
result3 = a == 1 < b == 5 < c == 10

print(f"a={a}, b={b}, c={c}")
print(f"a < b < c: {result1}")
print(f"a < b > c: {result2}")
print(f"a == 1 < b == 5 < c == 10: {result3}")

# ============================================================================
# 练习3：逻辑运算符 - 答案
# ============================================================================
print("\n练习3答案：逻辑运算符")
print("-" * 30)

# 逻辑运算真值表
print("逻辑运算真值表：")
print("A\tB\tA and B\tA or B\tnot A\tnot B")
print("-" * 50)

logic_values = [(True, True), (True, False), (False, True), (False, False)]
for A, B in logic_values:
    and_result = A and B
    or_result = A or B
    not_A = not A
    not_B = not B
    print(f"{A}\t{B}\t{and_result}\t{or_result}\t{not_A}\t{not_B}")

# 短路求值练习
print("\n短路求值练习：")

def print_and_return_true():
    print("函数1被调用")
    return True

def print_and_return_false():
    print("函数2被调用")
    return False

print("测试1: False and print_and_return_true()")
result = False and print_and_return_true()  # 函数1不会被调用
print(f"结果: {result}")

print("\n测试2: True or print_and_return_false()")
result = True or print_and_return_false()  # 函数2不会被调用
print(f"结果: {result}")

print("\n测试3: print_and_return_false() and print_and_return_true()")
result = print_and_return_false() and print_and_return_true()  # 函数1不会被调用
print(f"结果: {result}")

# ============================================================================
# 练习4：位运算符 - 答案
# ============================================================================
print("\n练习4答案：位运算符")
print("-" * 30)

a, b = 12, 10  # 二进制: 1100, 1010
print(f"a = {a} (二进制: {bin(a)})")
print(f"b = {b} (二进制: {bin(b)})")

bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not_a = ~a
left_shift = a << 2
right_shift = a >> 2

print(f"a & b = {bitwise_and} (二进制: {bin(bitwise_and)})")
print(f"a | b = {bitwise_or} (二进制: {bin(bitwise_or)})")
print(f"a ^ b = {bitwise_xor} (二进制: {bin(bitwise_xor)})")
print(f"~a = {bitwise_not_a}")
print(f"a << 2 = {left_shift} (二进制: {bin(left_shift)})")
print(f"a >> 2 = {right_shift} (二进制: {bin(right_shift)})")

# 位运算应用练习
print("\n位运算应用：")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("奇偶数判断：")
for num in numbers:
    is_even = (num & 1) == 0
    print(f"{num} 是 {'偶数' if is_even else '奇数'}")

# ============================================================================
# 练习5：赋值运算符 - 答案
# ============================================================================
print("\n练习5答案：赋值运算符")
print("-" * 30)

value = 100
print(f"初始值: {value}")

value += 50    # 加50
print(f"加50后: {value}")

value -= 20    # 减20
print(f"减20后: {value}")

value *= 2     # 乘2
print(f"乘2后: {value}")

value /= 4     # 除4
print(f"除4后: {value}")

value //= 3    # 整除3
print(f"整除3后: {value}")

value %= 10    # 取模10
print(f"取模10后: {value}")

value **= 2    # 平方
print(f"平方后: {value}")

# ============================================================================
# 练习6：成员运算符 - 答案
# ============================================================================
print("\n练习6答案：成员运算符")
print("-" * 30)

data_structures = {
    "列表": [1, 2, 3, 4, 5],
    "字符串": "Hello Python",
    "元组": (10, 20, 30),
    "字典": {"name": "张三", "age": 25},
    "集合": {"a", "b", "c"}
}

test_items = {
    "列表": [3, 6],
    "字符串": ["Hello", "hello", "Python"],
    "元组": [20, 40],
    "字典": ["name", "score"],  # 检查键
    "集合": ["a", "d"]
}

for data_type, container in data_structures.items():
    print(f"\n{data_type}: {container}")
    for item in test_items[data_type]:
        in_result = item in container
        not_in_result = item not in container
        print(f"  {repr(item)} in container: {in_result}")
        print(f"  {repr(item)} not in container: {not_in_result}")

# ============================================================================
# 练习7：身份运算符 - 答案
# ============================================================================
print("\n练习7答案：身份运算符")
print("-" * 30)

test_cases = [
    ([1, 2, 3], [1, 2, 3]),
    ("hello", "hello"),
    (100, 100),
    (1000, 1000),
    (None, None),
]

for case1, case2 in test_cases:
    print(f"\n比较 {repr(case1)} 和 {repr(case2)}:")
    equal_value = case1 == case2
    same_identity = case1 is case2
    print(f"  值相等 (==): {equal_value}")
    print(f"  身份相同 (is): {same_identity}")
    print(f"  id(case1): {id(case1)}")
    print(f"  id(case2): {id(case2)}")

# ============================================================================
# 练习8：运算符优先级 - 答案
# ============================================================================
print("\n练习8答案：运算符优先级")
print("-" * 30)

expressions = [
    "2 + 3 * 4",           # 14 (乘法优先)
    "2 * 3 ** 2",          # 18 (幂运算优先)
    "10 - 4 - 2",          # 4 (左结合)
    "2 ** 3 ** 2",         # 512 (右结合: 2**(3**2))
    "5 > 3 and 2 < 4",     # True
    "5 > 3 or 2 > 4 and 1 < 2",  # True (and优先级高于or)
    "not 5 > 3 and 2 < 4", # False
    "1 < 2 < 3 < 4",       # True
    "True or False and False",  # True (and优先级高于or)
    "3 + 4 * 2 ** 2 - 1",  # 18
]

print("表达式计算结果：")
for expr in expressions:
    result = eval(expr)
    print(f"{expr:>25} = {result}")

# 详细解析几个复杂表达式
print("\n详细解析：")
print("2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = 512")
print("5 > 3 or 2 > 4 and 1 < 2 = True or (False and True) = True or False = True")
print("3 + 4 * 2 ** 2 - 1 = 3 + 4 * 4 - 1 = 3 + 16 - 1 = 18")

# ============================================================================
# 练习9：综合应用 - 答案
# ============================================================================
print("\n练习9答案：综合应用 - 简单计算器")
print("-" * 30)

def simple_calculator(num1, operator, num2):
    """
    简单计算器函数
    
    参数:
        num1: 第一个数字
        operator: 运算符 (+, -, *, /, //, %, **)
        num2: 第二个数字
    
    返回:
        计算结果
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "错误：除零"
    elif operator == '//':
        if num2 != 0:
            return num1 // num2
        else:
            return "错误：除零"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "错误：除零"
    elif operator == '**':
        return num1 ** num2
    else:
        return "错误：不支持的运算符"

# 测试计算器
test_cases = [
    (10, '+', 5),
    (10, '-', 3),
    (6, '*', 7),
    (15, '/', 3),
    (17, '//', 5),
    (17, '%', 5),
    (2, '**', 8),
    (10, '/', 0),  # 除零测试
    (5, '&', 3),   # 不支持的运算符
]

print("计算器测试结果：")
for num1, op, num2 in test_cases:
    result = simple_calculator(num1, op, num2)
    print(f"{num1} {op} {num2} = {result}")

# ============================================================================
# 额外知识点：运算符的高级用法
# ============================================================================
print("\n额外知识点：运算符的高级用法")
print("-" * 30)

# 1. 链式赋值的注意事项
print("1. 链式赋值的注意事项：")
a = b = [1, 2, 3]  # 两个变量指向同一个列表
c = [1, 2, 3]      # 独立的列表

print(f"初始状态: a={a}, b={b}, c={c}")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")

a.append(4)  # 修改a也会影响b
print(f"a.append(4)后: a={a}, b={b}, c={c}")

# 2. 布尔运算的返回值
print("\n2. 布尔运算的返回值：")
print(f"'hello' and 'world': {'hello' and 'world'}")
print(f"'' or 'default': {'' or 'default'}")
print(f"0 or 42: {0 or 42}")
print(f"None or 'value': {None or 'value'}")

# 3. 比较运算符的链式使用
print("\n3. 比较运算符的链式使用：")
age = 25
print(f"年龄: {age}")
print(f"18 <= age < 60: {18 <= age < 60}")
print(f"等价于: (18 <= age) and (age < 60): {(18 <= age) and (age < 60)}")

# 4. 位运算的实际应用
print("\n4. 位运算的实际应用：")
# 权限系统示例
READ = 1    # 001
WRITE = 2   # 010
EXECUTE = 4 # 100

user_permission = READ_write = READ | WRITE  # 011
print(f"用户权限: {user_permission} (二进制: {bin(user_permission)})")
print(f"有读权限: {bool(user_permission & READ)}")
print(f"有写权限: {bool(user_permission & WRITE)}")
print(f"有执行权限: {bool(user_permission & EXECUTE)}")

# 添加执行权限
user_permission |= EXECUTE
print(f"添加执行权限后: {user_permission} (二进制: {bin(user_permission)})")

# 移除写权限
user_permission &= ~WRITE
print(f"移除写权限后: {user_permission} (二进制: {bin(user_permission)})")

print("\n所有练习题答案展示完成！")
print("\n学习建议：")
print("1. 熟练掌握各种运算符的使用方法")
print("2. 理解运算符优先级，必要时使用括号")
print("3. 区分 == 和 is 的使用场景")
print("4. 掌握逻辑运算符的短路求值特性")
print("5. 了解位运算在实际编程中的应用")
print("6. 练习复合赋值运算符的使用")