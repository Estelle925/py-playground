#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第2章：运算符 - 示例代码

本文件包含Python各种运算符的详细示例
"""

# ============================================================================
# 1. 算术运算符
# ============================================================================

print("=" * 50)
print("1. 算术运算符")
print("=" * 50)

# 基本算术运算
a, b = 10, 3

print(f"a = {a}, b = {b}")
print(f"加法: {a} + {b} = {a + b}")
print(f"减法: {a} - {b} = {a - b}")
print(f"乘法: {a} * {b} = {a * b}")
print(f"除法: {a} / {b} = {a / b}")
print(f"整除: {a} // {b} = {a // b}")
print(f"取模: {a} % {b} = {a % b}")
print(f"幂运算: {a} ** {b} = {a ** b}")

# 字符串和列表的特殊运算
print("\n字符串和列表的特殊运算:")
str1, str2 = "Hello", "World"
list1, list2 = [1, 2], [3, 4]

print(f"字符串连接: '{str1}' + ' ' + '{str2}' = '{str1 + ' ' + str2}'")
print(f"字符串重复: '{str1}' * 3 = '{str1 * 3}'")
print(f"列表连接: {list1} + {list2} = {list1 + list2}")
print(f"列表重复: {list1} * 3 = {list1 * 3}")

# 除法的特殊情况
print("\n除法的特殊情况:")
print(f"正数整除: 7 // 3 = {7 // 3}")
print(f"负数整除: -7 // 3 = {-7 // 3}")
print(f"浮点数整除: 7.5 // 2.5 = {7.5 // 2.5}")

# ============================================================================
# 2. 比较运算符
# ============================================================================

print("\n" + "=" * 50)
print("2. 比较运算符")
print("=" * 50)

x, y = 5, 10
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# 链式比较
print("\n链式比较:")
a, b, c = 1, 5, 10
print(f"a = {a}, b = {b}, c = {c}")
print(f"a < b < c: {a < b < c}")
print(f"a < b > c: {a < b > c}")
print(f"等价于: (a < b) and (b < c): {(a < b) and (b < c)}")

# 字符串比较（字典序）
print("\n字符串比较（字典序）:")
str_a, str_b = "apple", "banana"
print(f"'{str_a}' < '{str_b}': {str_a < str_b}")
print(f"'{str_a}' > '{str_b}': {str_a > str_b}")

# ============================================================================
# 3. 逻辑运算符
# ============================================================================

print("\n" + "=" * 50)
print("3. 逻辑运算符")
print("=" * 50)

# 基本逻辑运算
p, q = True, False
print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")
print(f"p or q: {p or q}")
print(f"not p: {not p}")
print(f"not q: {not q}")

# 逻辑运算的真值表
print("\n逻辑运算真值表:")
values = [(True, True), (True, False), (False, True), (False, False)]
print("p\tq\tp and q\tp or q\tnot p")
print("-" * 40)
for p, q in values:
    print(f"{p}\t{q}\t{p and q}\t{p or q}\t{not p}")

# 短路求值
print("\n短路求值示例:")
def func_true():
    print("func_true() 被调用")
    return True

def func_false():
    print("func_false() 被调用")
    return False

print("测试 and 短路:")
result = func_false() and func_true()  # func_true() 不会被调用
print(f"结果: {result}")

print("\n测试 or 短路:")
result = func_true() or func_false()  # func_false() 不会被调用
print(f"结果: {result}")

# ============================================================================
# 4. 位运算符
# ============================================================================

print("\n" + "=" * 50)
print("4. 位运算符")
print("=" * 50)

# 位运算示例
a, b = 12, 10  # 二进制: 1100, 1010
print(f"a = {a} (二进制: {bin(a)})")
print(f"b = {b} (二进制: {bin(b)})")
print(f"按位与 a & b = {a & b} (二进制: {bin(a & b)})")
print(f"按位或 a | b = {a | b} (二进制: {bin(a | b)})")
print(f"按位异或 a ^ b = {a ^ b} (二进制: {bin(a ^ b)})")
print(f"按位取反 ~a = {~a} (二进制: {bin(~a & 0xFFFF)})")
print(f"左移 a << 2 = {a << 2} (二进制: {bin(a << 2)})")
print(f"右移 a >> 2 = {a >> 2} (二进制: {bin(a >> 2)})")

# 位运算的实际应用
print("\n位运算的实际应用:")
# 判断奇偶数
num = 15
print(f"{num} 是{'奇数' if num & 1 else '偶数'}")

# 交换两个数（不使用临时变量）
x, y = 5, 10
print(f"交换前: x = {x}, y = {y}")
x = x ^ y
y = x ^ y
x = x ^ y
print(f"交换后: x = {x}, y = {y}")

# ============================================================================
# 5. 赋值运算符
# ============================================================================

print("\n" + "=" * 50)
print("5. 赋值运算符")
print("=" * 50)

# 基本赋值
value = 10
print(f"初始值: {value}")

# 复合赋值运算符
value += 5  # 等价于 value = value + 5
print(f"value += 5: {value}")

value -= 3  # 等价于 value = value - 3
print(f"value -= 3: {value}")

value *= 2  # 等价于 value = value * 2
print(f"value *= 2: {value}")

value /= 4  # 等价于 value = value / 4
print(f"value /= 4: {value}")

value //= 2  # 等价于 value = value // 2
print(f"value //= 2: {value}")

value %= 3  # 等价于 value = value % 3
print(f"value %= 3: {value}")

value **= 3  # 等价于 value = value ** 3
print(f"value **= 3: {value}")

# 字符串的复合赋值
text = "Hello"
print(f"\n初始字符串: '{text}'")
text += " World"  # 字符串连接
print(f"text += ' World': '{text}'")
text *= 2  # 字符串重复
print(f"text *= 2: '{text}'")

# ============================================================================
# 6. 成员运算符
# ============================================================================

print("\n" + "=" * 50)
print("6. 成员运算符")
print("=" * 50)

# 列表中的成员检查
fruits = ["apple", "banana", "orange"]
print(f"水果列表: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# 字符串中的成员检查
text = "Hello World"
print(f"\n文本: '{text}'")
print(f"'Hello' in text: {'Hello' in text}")
print(f"'hello' in text: {'hello' in text}")
print(f"'xyz' not in text: {'xyz' not in text}")

# 字典中的成员检查（检查键）
student = {"name": "张三", "age": 20, "grade": "A"}
print(f"\n学生信息: {student}")
print(f"'name' in student: {'name' in student}")
print(f"'score' in student: {'score' in student}")
print(f"'张三' in student: {'张三' in student}")  # 检查值需要用 in student.values()
print(f"'张三' in student.values(): {'张三' in student.values()}")

# ============================================================================
# 7. 身份运算符
# ============================================================================

print("\n" + "=" * 50)
print("7. 身份运算符")
print("=" * 50)

# is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"c = a, id(c) = {id(c)}")

print(f"\na == b: {a == b}  # 值相等")
print(f"a is b: {a is b}  # 不是同一个对象")
print(f"a is c: {a is c}  # 是同一个对象")

# 小整数和字符串的缓存
print("\n小整数缓存:")
x = 100
y = 100
print(f"x = {x}, y = {y}")
print(f"x is y: {x is y}  # 小整数被缓存")

x = 1000
y = 1000
print(f"\nx = {x}, y = {y}")
print(f"x is y: {x is y}  # 大整数不缓存")

# None的比较
value = None
print(f"\nvalue = {value}")
print(f"value is None: {value is None}  # 推荐")
print(f"value == None: {value == None}  # 不推荐")

# ============================================================================
# 8. 运算符优先级
# ============================================================================

print("\n" + "=" * 50)
print("8. 运算符优先级")
print("=" * 50)

# 算术运算符优先级
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
print(f"2 + 3 * 4 = {result1}  # 乘法优先")
print(f"(2 + 3) * 4 = {result2}  # 括号改变优先级")

# 幂运算的右结合性
result3 = 2 ** 3 ** 2
result4 = (2 ** 3) ** 2
print(f"\n2 ** 3 ** 2 = {result3}  # 右结合: 2 ** (3 ** 2)")
print(f"(2 ** 3) ** 2 = {result4}  # 左结合")

# 比较和逻辑运算符
result5 = 5 > 3 and 2 < 4
result6 = 5 > 3 or 2 > 4 and 1 < 2
print(f"\n5 > 3 and 2 < 4 = {result5}")
print(f"5 > 3 or 2 > 4 and 1 < 2 = {result6}  # and 优先级高于 or")

# 复杂表达式
complex_expr = not 5 > 3 and 2 < 4 or 1 == 1
print(f"not 5 > 3 and 2 < 4 or 1 == 1 = {complex_expr}")
print("解析: (not (5 > 3)) and (2 < 4) or (1 == 1)")
print(f"     = (not True) and True or True")
print(f"     = False and True or True")
print(f"     = False or True")
print(f"     = True")

# ============================================================================
# 9. 运算符重载示例
# ============================================================================

print("\n" + "=" * 50)
print("9. 运算符重载示例")
print("=" * 50)

class Vector:
    """简单的二维向量类，演示运算符重载"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """重载 + 运算符"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """重载 - 运算符"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """重载 * 运算符（标量乘法）"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """重载 == 运算符"""
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        """重载 != 运算符"""
        return not self.__eq__(other)

# 使用重载的运算符
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")

print(f"\nv1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")
print(f"v1 == v2 = {v1 == v2}")
print(f"v1 == v3 = {v1 == v3}")
print(f"v1 != v2 = {v1 != v2}")

print("\n" + "=" * 50)
print("运算符示例代码运行完成！")
print("=" * 50)