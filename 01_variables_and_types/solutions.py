#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第1章：变量与数据类型 - 练习题答案

这里提供了exercises.py中所有练习题的参考答案
"""

print("第1章练习题答案：变量与数据类型")
print("=" * 40)

# ============================================================================
# 练习1：基本数据类型识别 - 答案
# ============================================================================
print("\n练习1答案：识别下列变量的数据类型")
print("-" * 30)

variables = [
    42,           # 类型：int
    3.14,         # 类型：float
    "Hello",      # 类型：str
    True,         # 类型：bool
    None,         # 类型：NoneType
    [1, 2, 3],    # 类型：list
    (1, 2, 3),    # 类型：tuple
    {"a": 1},     # 类型：dict
    {1, 2, 3},    # 类型：set
]

for i, var in enumerate(variables, 1):
    print(f"{i}. {repr(var):>15} -> 类型: {type(var).__name__}")

# ============================================================================
# 练习2：变量赋值和命名 - 答案
# ============================================================================
print("\n练习2答案：变量赋值和命名")
print("-" * 30)

# 1. 创建一个变量存储你的姓名
your_name = "张三"

# 2. 创建一个变量存储你的年龄
your_age = 25

# 3. 创建一个变量存储你的身高（浮点数）
your_height = 175.5

# 4. 创建一个变量表示你是否是学生（布尔值）
is_student = True

# 5. 使用多重赋值创建三个变量 x, y, z，分别赋值为 10, 20, 30
x, y, z = 10, 20, 30

print(f"姓名: {your_name}")
print(f"年龄: {your_age}")
print(f"身高: {your_height}")
print(f"是学生: {is_student}")
print(f"x={x}, y={y}, z={z}")

# ============================================================================
# 练习3：类型转换 - 答案
# ============================================================================
print("\n练习3答案：类型转换")
print("-" * 30)

str_number = "123"
str_float = "45.67"
int_number = 100
float_number = 3.14

# 1. 将字符串 "123" 转换为整数
converted_int = int(str_number)

# 2. 将字符串 "45.67" 转换为浮点数
converted_float = float(str_float)

# 3. 将整数 100 转换为字符串
converted_str = str(int_number)

# 4. 将浮点数 3.14 转换为整数（注意：会丢失小数部分）
converted_int_from_float = int(float_number)

print(f"'{str_number}' -> {converted_int} (类型: {type(converted_int)})")
print(f"'{str_float}' -> {converted_float} (类型: {type(converted_float)})")
print(f"{int_number} -> '{converted_str}' (类型: {type(converted_str)})")
print(f"{float_number} -> {converted_int_from_float} (类型: {type(converted_int_from_float)})")

# ============================================================================
# 练习4：布尔值转换 - 答案
# ============================================================================
print("\n练习4答案：布尔值转换")
print("-" * 30)

test_values = [
    0,              # False - 数字0
    1,              # True - 非零数字
    -1,             # True - 非零数字
    "",             # False - 空字符串
    " ",            # True - 非空字符串（包含空格）
    "0",            # True - 非空字符串
    "False",        # True - 非空字符串
    [],             # False - 空列表
    [0],            # True - 非空列表
    {},             # False - 空字典
    {"key": None},  # True - 非空字典
    None            # False - None值
]

print("布尔值转换结果：")
for value in test_values:
    result = bool(value)
    explanation = {
        0: "数字0为False",
        1: "非零数字为True",
        -1: "非零数字为True",
        "": "空字符串为False",
        " ": "非空字符串为True",
        "0": "非空字符串为True",
        "False": "非空字符串为True",
        tuple([]): "空容器为False",
        tuple([0]): "非空容器为True",
        None: "None为False"
    }
    
    print(f"{repr(value):>15} -> {result}")

# ============================================================================
# 练习5：变量交换 - 答案
# ============================================================================
print("\n练习5答案：变量交换")
print("-" * 30)

a, b = 10, 20
print(f"交换前: a = {a}, b = {b}")

# 方法1：使用Python的多重赋值（推荐）
a, b = b, a
print(f"方法1交换后: a = {a}, b = {b}")

# 重置变量
a, b = 10, 20

# 方法2：使用临时变量
temp = a
a = b
b = temp
print(f"方法2交换后: a = {a}, b = {b}")

# 重置变量
a, b = 10, 20

# 方法3：使用算术运算（仅适用于数字）
a = a + b  # a = 30
b = a - b  # b = 30 - 20 = 10
a = a - b  # a = 30 - 10 = 20
print(f"方法3交换后: a = {a}, b = {b}")

# ============================================================================
# 练习6：变量作用域 - 答案
# ============================================================================
print("\n练习6答案：变量作用域")
print("-" * 30)

global_var = "我是全局变量"

def scope_test():
    local_var = "我是局部变量"
    global global_var
    print(f"函数内部 - 全局变量: {global_var}")
    print(f"函数内部 - 局部变量: {local_var}")
    
    # 修改全局变量的值
    global_var = "全局变量已被修改"

# 调用函数
scope_test()
print(f"函数外部 - 全局变量: {global_var}")

# 尝试访问局部变量（这会产生错误）
try:
    print(f"函数外部 - 局部变量: {local_var}")
except NameError as e:
    print(f"错误：{e}")
    print("说明：局部变量只能在定义它的函数内部访问")

# ============================================================================
# 练习7：综合应用 - 答案
# ============================================================================
print("\n练习7答案：综合应用 - 个人信息管理")
print("-" * 30)

# 个人信息变量
name = "李四"
age = 28
height_cm = 170
weight_kg = 65
is_married = False

# BMI计算
height_m = height_cm / 100  # 转换为米
bmi = weight_kg / (height_m ** 2)

# BMI状态判断
if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
elif bmi < 28:
    status = "偏胖"
else:
    status = "肥胖"

# 输出报告
print(f"""
===== 个人信息报告 =====
姓名: {name}
年龄: {age}岁
身高: {height_cm}cm
体重: {weight_kg}kg
婚姻状况: {'已婚' if is_married else '未婚'}
BMI指数: {bmi:.2f}
体重状态: {status}
=====================
""")

# ============================================================================
# 额外知识点：高级类型转换技巧
# ============================================================================
print("\n额外知识点：高级类型转换技巧")
print("-" * 30)

# 1. 安全的类型转换
def safe_int_convert(value, default=0):
    """安全地将值转换为整数"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

test_values = ["123", "abc", None, 45.67, ""]
for val in test_values:
    result = safe_int_convert(val)
    print(f"safe_int_convert({repr(val)}) = {result}")

# 2. 批量类型转换
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(f"\n批量转换: {str_numbers} -> {int_numbers}")

# 3. 使用eval进行动态类型转换（注意：eval有安全风险，实际项目中慎用）
expressions = ["1 + 2", "3 * 4", "'hello' + ' world'"]
for expr in expressions:
    try:
        result = eval(expr)
        print(f"eval('{expr}') = {result} (类型: {type(result).__name__})")
    except Exception as e:
        print(f"eval('{expr}') 出错: {e}")

print("\n所有练习题答案展示完成！")
print("\n学习建议：")
print("1. 对比你的答案和标准答案，找出差异")
print("2. 理解每种数据类型的特点和用途")
print("3. 掌握类型转换的方法和注意事项")
print("4. 练习变量命名的最佳实践")
print("5. 理解变量作用域的概念")