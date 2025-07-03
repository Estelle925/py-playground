#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第2章：运算符 - 练习题

完成以下练习题，加深对Python运算符的理解
"""

print("第2章练习题：运算符")
print("=" * 40)

# ============================================================================
# 练习1：算术运算符
# ============================================================================
print("\n练习1：算术运算符")
print("-" * 30)

# TODO: 计算以下表达式的结果
print("计算以下表达式的结果：")

# 1. 基本算术运算
a, b = 17, 5
print(f"a = {a}, b = {b}")

# TODO: 完成以下计算
# addition = a + b
# subtraction = a - b
# multiplication = a * b
# division = a / b
# floor_division = a // b
# modulus = a % b
# power = a ** b

# TODO: 取消注释并运行
# print(f"a + b = {addition}")
# print(f"a - b = {subtraction}")
# print(f"a * b = {multiplication}")
# print(f"a / b = {division}")
# print(f"a // b = {floor_division}")
# print(f"a % b = {modulus}")
# print(f"a ** b = {power}")

# 2. 字符串和列表运算
str1 = "Python"
str2 = "编程"
list1 = [1, 2]
list2 = [3, 4, 5]

# TODO: 完成字符串和列表的运算
# string_concat = 
# string_repeat = 
# list_concat = 
# list_repeat = 

# TODO: 取消注释并运行
# print(f"\n字符串连接: '{str1}' + '{str2}' = '{string_concat}'")
# print(f"字符串重复: '{str1}' * 3 = '{string_repeat}'")
# print(f"列表连接: {list1} + {list2} = {list_concat}")
# print(f"列表重复: {list1} * 2 = {list_repeat}")

# ============================================================================
# 练习2：比较运算符
# ============================================================================
print("\n练习2：比较运算符")
print("-" * 30)

# TODO: 预测以下比较运算的结果，然后验证
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
    # TODO: 完成比较运算
    # print(f"  == : {x == y}")
    # print(f"  != : {x != y}")
    # print(f"  <  : {x < y}")
    # print(f"  >  : {x > y}")
    # print(f"  <= : {x <= y}")
    # print(f"  >= : {x >= y}")
    print()

# 链式比较练习
print("链式比较练习：")
a, b, c = 1, 5, 10
# TODO: 完成链式比较
# result1 = a < b < c
# result2 = a < b > c
# result3 = a == 1 < b == 5 < c == 10

# TODO: 取消注释并运行
# print(f"a={a}, b={b}, c={c}")
# print(f"a < b < c: {result1}")
# print(f"a < b > c: {result2}")
# print(f"a == 1 < b == 5 < c == 10: {result3}")

# ============================================================================
# 练习3：逻辑运算符
# ============================================================================
print("\n练习3：逻辑运算符")
print("-" * 30)

# TODO: 完成逻辑运算真值表
print("逻辑运算真值表：")
print("A\tB\tA and B\tA or B\tnot A\tnot B")
print("-" * 50)

logic_values = [(True, True), (True, False), (False, True), (False, False)]
for A, B in logic_values:
    # TODO: 计算逻辑运算结果
    # and_result = A and B
    # or_result = A or B
    # not_A = not A
    # not_B = not B
    
    # TODO: 取消注释并运行
    # print(f"{A}\t{B}\t{and_result}\t{or_result}\t{not_A}\t{not_B}")
    pass

# 短路求值练习
print("\n短路求值练习：")

def print_and_return_true():
    print("函数1被调用")
    return True

def print_and_return_false():
    print("函数2被调用")
    return False

# TODO: 预测哪些函数会被调用
print("测试1: False and print_and_return_true()")
# result = False and print_and_return_true()

print("\n测试2: True or print_and_return_false()")
# result = True or print_and_return_false()

print("\n测试3: print_and_return_false() and print_and_return_true()")
# result = print_and_return_false() and print_and_return_true()

# ============================================================================
# 练习4：位运算符
# ============================================================================
print("\n练习4：位运算符")
print("-" * 30)

# TODO: 完成位运算
a, b = 12, 10  # 二进制: 1100, 1010
print(f"a = {a} (二进制: {bin(a)})")
print(f"b = {b} (二进制: {bin(b)})")

# TODO: 计算位运算结果
# bitwise_and = a & b
# bitwise_or = a | b
# bitwise_xor = a ^ b
# bitwise_not_a = ~a
# left_shift = a << 2
# right_shift = a >> 2

# TODO: 取消注释并运行
# print(f"a & b = {bitwise_and} (二进制: {bin(bitwise_and)})")
# print(f"a | b = {bitwise_or} (二进制: {bin(bitwise_or)})")
# print(f"a ^ b = {bitwise_xor} (二进制: {bin(bitwise_xor)})")
# print(f"~a = {bitwise_not_a}")
# print(f"a << 2 = {left_shift} (二进制: {bin(left_shift)})")
# print(f"a >> 2 = {right_shift} (二进制: {bin(right_shift)})")

# 位运算应用练习
print("\n位运算应用：")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# TODO: 使用位运算判断奇偶数
print("奇偶数判断：")
for num in numbers:
    # TODO: 使用位运算判断奇偶
    # is_even = (num & 1) == 0
    # print(f"{num} 是 {'偶数' if is_even else '奇数'}")
    pass

# ============================================================================
# 练习5：赋值运算符
# ============================================================================
print("\n练习5：赋值运算符")
print("-" * 30)

# TODO: 使用复合赋值运算符
value = 100
print(f"初始值: {value}")

# TODO: 依次执行以下操作
# value += 50    # 加50
# value -= 20    # 减20
# value *= 2     # 乘2
# value /= 4     # 除4
# value //= 3    # 整除3
# value %= 10    # 取模10
# value **= 2    # 平方

# TODO: 每步都打印结果
# print(f"加50后: {value}")
# print(f"减20后: {value}")
# print(f"乘2后: {value}")
# print(f"除4后: {value}")
# print(f"整除3后: {value}")
# print(f"取模10后: {value}")
# print(f"平方后: {value}")

# ============================================================================
# 练习6：成员运算符
# ============================================================================
print("\n练习6：成员运算符")
print("-" * 30)

# TODO: 完成成员检查
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

# TODO: 检查成员关系
for data_type, container in data_structures.items():
    print(f"\n{data_type}: {container}")
    for item in test_items[data_type]:
        # TODO: 完成成员检查
        # in_result = item in container
        # not_in_result = item not in container
        # print(f"  {repr(item)} in container: {in_result}")
        # print(f"  {repr(item)} not in container: {not_in_result}")
        pass

# ============================================================================
# 练习7：身份运算符
# ============================================================================
print("\n练习7：身份运算符")
print("-" * 30)

# TODO: 理解 is 和 == 的区别
test_cases = [
    ([1, 2, 3], [1, 2, 3]),
    ("hello", "hello"),
    (100, 100),
    (1000, 1000),
    (None, None),
]

for case1, case2 in test_cases:
    print(f"\n比较 {repr(case1)} 和 {repr(case2)}:")
    # TODO: 比较值和身份
    # equal_value = case1 == case2
    # same_identity = case1 is case2
    # print(f"  值相等 (==): {equal_value}")
    # print(f"  身份相同 (is): {same_identity}")
    # print(f"  id(case1): {id(case1)}")
    # print(f"  id(case2): {id(case2)}")

# ============================================================================
# 练习8：运算符优先级
# ============================================================================
print("\n练习8：运算符优先级")
print("-" * 30)

# TODO: 预测以下表达式的结果，然后验证
expressions = [
    "2 + 3 * 4",
    "2 * 3 ** 2",
    "10 - 4 - 2",
    "2 ** 3 ** 2",
    "5 > 3 and 2 < 4",
    "5 > 3 or 2 > 4 and 1 < 2",
    "not 5 > 3 and 2 < 4",
    "1 < 2 < 3 < 4",
    "True or False and False",
    "3 + 4 * 2 ** 2 - 1",
]

print("表达式计算结果：")
for expr in expressions:
    # TODO: 预测结果，然后验证
    # result = eval(expr)
    # print(f"{expr:>25} = {result}")
    pass

# ============================================================================
# 练习9：综合应用
# ============================================================================
print("\n练习9：综合应用 - 简单计算器")
print("-" * 30)

# TODO: 实现一个简单的计算器函数
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
    # TODO: 实现计算器逻辑
    # if operator == '+':
    #     return num1 + num2
    # elif operator == '-':
    #     return num1 - num2
    # elif operator == '*':
    #     return num1 * num2
    # elif operator == '/':
    #     if num2 != 0:
    #         return num1 / num2
    #     else:
    #         return "错误：除零"
    # elif operator == '//':
    #     if num2 != 0:
    #         return num1 // num2
    #     else:
    #         return "错误：除零"
    # elif operator == '%':
    #     if num2 != 0:
    #         return num1 % num2
    #     else:
    #         return "错误：除零"
    # elif operator == '**':
    #     return num1 ** num2
    # else:
    #     return "错误：不支持的运算符"
    pass

# TODO: 测试计算器
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

# for num1, op, num2 in test_cases:
#     result = simple_calculator(num1, op, num2)
#     print(f"{num1} {op} {num2} = {result}")

print("\n练习完成！请查看solutions.py文件获取参考答案。")