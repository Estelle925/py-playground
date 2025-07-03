#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第3章：字符串操作 - 示例代码

本文件包含Python字符串操作的详细示例
"""

import re
import string

# ============================================================================
# 1. 字符串创建和基本特性
# ============================================================================

print("=" * 50)
print("1. 字符串创建和基本特性")
print("=" * 50)

# 1.1 不同方式创建字符串
single_quote = 'Hello World'
double_quote = "Hello World"
triple_quote = '''这是一个
多行字符串
示例'''
raw_string = r'C:\Users\name\Documents'  # 原始字符串，不转义
byte_string = b'Hello'  # 字节字符串

print(f"单引号字符串: {single_quote}")
print(f"双引号字符串: {double_quote}")
print(f"三引号字符串: {repr(triple_quote)}")
print(f"原始字符串: {raw_string}")
print(f"字节字符串: {byte_string}")

# 1.2 字符串的不可变性
original = "Hello"
print(f"\n原始字符串: {original}")
print(f"字符串ID: {id(original)}")

# 字符串操作会创建新的字符串对象
modified = original + " World"
print(f"修改后字符串: {modified}")
print(f"新字符串ID: {id(modified)}")
print(f"原字符串是否改变: {original}")

# 1.3 字符串长度和字符访问
text = "Python编程"
print(f"\n字符串: {text}")
print(f"长度: {len(text)}")
print(f"第一个字符: {text[0]}")
print(f"最后一个字符: {text[-1]}")
print(f"第三个字符: {text[2]}")

# ============================================================================
# 2. 字符串切片操作
# ============================================================================

print("\n" + "=" * 50)
print("2. 字符串切片操作")
print("=" * 50)

text = "Python Programming"
print(f"原字符串: '{text}'")
print(f"长度: {len(text)}")

# 基本切片
print(f"\n基本切片:")
print(f"text[0:6]: '{text[0:6]}'")
print(f"text[7:18]: '{text[7:18]}'")
print(f"text[:6]: '{text[:6]}'")
print(f"text[7:]: '{text[7:]}'")
print(f"text[:]: '{text[:]}'")

# 负索引切片
print(f"\n负索引切片:")
print(f"text[-11:-1]: '{text[-11:-1]}'")
print(f"text[:-1]: '{text[:-1]}'")
print(f"text[-11:]: '{text[-11:]}'")

# 带步长的切片
print(f"\n带步长的切片:")
print(f"text[::2]: '{text[::2]}'")
print(f"text[1::2]: '{text[1::2]}'")
print(f"text[::-1]: '{text[::-1]}'")
print(f"text[6:0:-1]: '{text[6:0:-1]}'")

# ============================================================================
# 3. 字符串方法 - 大小写转换
# ============================================================================

print("\n" + "=" * 50)
print("3. 字符串方法 - 大小写转换")
print("=" * 50)

text = "Hello World Python"
print(f"原字符串: '{text}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"capitalize(): '{text.capitalize()}'")
print(f"title(): '{text.title()}'")
print(f"swapcase(): '{text.swapcase()}'")

# 特殊情况
special_text = "hello WORLD"
print(f"\n特殊情况: '{special_text}'")
print(f"swapcase(): '{special_text.swapcase()}'")

# ============================================================================
# 4. 字符串方法 - 查找和替换
# ============================================================================

print("\n" + "=" * 50)
print("4. 字符串方法 - 查找和替换")
print("=" * 50)

text = "Python is great, Python is powerful"
print(f"原字符串: '{text}'")

# 查找方法
print(f"\n查找方法:")
print(f"find('Python'): {text.find('Python')}")
print(f"find('Java'): {text.find('Java')}")
print(f"rfind('Python'): {text.rfind('Python')}")
print(f"count('Python'): {text.count('Python')}")
print(f"count('is'): {text.count('is')}")

# index方法（找不到会抛异常）
try:
    print(f"index('Python'): {text.index('Python')}")
    print(f"index('Java'): {text.index('Java')}")
except ValueError as e:
    print(f"index('Java') 抛出异常: {e}")

# 替换方法
print(f"\n替换方法:")
print(f"replace('Python', 'Java'): '{text.replace('Python', 'Java')}'")
print(f"replace('Python', 'Java', 1): '{text.replace('Python', 'Java', 1)}'")
print(f"replace('is', 'was'): '{text.replace('is', 'was')}'")

# ============================================================================
# 5. 字符串方法 - 判断方法
# ============================================================================

print("\n" + "=" * 50)
print("5. 字符串方法 - 判断方法")
print("=" * 50)

test_strings = [
    "Hello",
    "hello world",
    "123",
    "abc123",
    "   ",
    "",
    "Hello World",
    "HELLO",
    "123.45",
    "\t\n"
]

print("字符串判断方法测试:")
print(f"{'字符串':<12} {'isalpha':<8} {'isdigit':<8} {'isalnum':<8} {'isspace':<8} {'isupper':<8} {'islower':<8}")
print("-" * 70)

for s in test_strings:
    print(f"{repr(s):<12} {str(s.isalpha()):<8} {str(s.isdigit()):<8} {str(s.isalnum()):<8} {str(s.isspace()):<8} {str(s.isupper()):<8} {str(s.islower()):<8}")

# 开头和结尾判断
print(f"\n开头和结尾判断:")
filename = "document.pdf"
url = "https://www.example.com"

print(f"'{filename}' endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"'{filename}' endswith('.txt'): {filename.endswith('.txt')}")
print(f"'{url}' startswith('https'): {url.startswith('https')}")
print(f"'{url}' startswith('http'): {url.startswith('http')}")

# 多个后缀/前缀判断
print(f"'{filename}' endswith(('.pdf', '.doc', '.txt')): {filename.endswith(('.pdf', '.doc', '.txt'))}")

# ============================================================================
# 6. 字符串方法 - 分割和连接
# ============================================================================

print("\n" + "=" * 50)
print("6. 字符串方法 - 分割和连接")
print("=" * 50)

# 分割方法
text = "apple,banana,orange,grape"
print(f"原字符串: '{text}'")
print(f"split(','): {text.split(',')}")
print(f"split(',', 2): {text.split(',', 2)}")

# 默认分割（按空白字符）
text2 = "  hello   world  python  "
print(f"\n原字符串: '{text2}'")
print(f"split(): {text2.split()}")
print(f"split(' '): {text2.split(' ')}")

# 从右开始分割
path = "/home/user/documents/file.txt"
print(f"\n路径: '{path}'")
print(f"rsplit('/', 1): {path.rsplit('/', 1)}")
print(f"split('/'): {path.split('/')}")

# 按行分割
multiline = "第一行\n第二行\r\n第三行\r第四行"
print(f"\n多行文本: {repr(multiline)}")
print(f"splitlines(): {multiline.splitlines()}")
print(f"splitlines(True): {multiline.splitlines(True)}")

# 连接方法
words = ['Python', 'is', 'awesome']
print(f"\n单词列表: {words}")
print(f"' '.join(words): '{' '.join(words)}'")
print(f"'-'.join(words): '{'-'.join(words)}'")
print(f"''.join(words): '{' '.join(words)}'")

# 连接数字（需要转换为字符串）
numbers = [1, 2, 3, 4, 5]
print(f"\n数字列表: {numbers}")
print(f"','.join(map(str, numbers)): '{','.join(map(str, numbers))}'")

# ============================================================================
# 7. 字符串方法 - 去除空白和对齐
# ============================================================================

print("\n" + "=" * 50)
print("7. 字符串方法 - 去除空白和对齐")
print("=" * 50)

# 去除空白
text = "   Hello World   "
print(f"原字符串: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")
print(f"rstrip(): '{text.rstrip()}'")

# 去除指定字符
text2 = "...Hello World..."
print(f"\n原字符串: '{text2}'")
print(f"strip('.'): '{text2.strip('.')}'")
print(f"strip('.H'): '{text2.strip('.H')}'")

# 对齐和填充
text3 = "Python"
width = 20
print(f"\n原字符串: '{text3}'")
print(f"center({width}): '{text3.center(width)}'")
print(f"center({width}, '*'): '{text3.center(width, '*')}'")
print(f"ljust({width}): '{text3.ljust(width)}'")
print(f"ljust({width}, '-'): '{text3.ljust(width, '-')}'")
print(f"rjust({width}): '{text3.rjust(width)}'")
print(f"rjust({width}, '='): '{text3.rjust(width, '=')}'")

# 数字填充
number = "42"
print(f"\n数字: '{number}'")
print(f"zfill(5): '{number.zfill(5)}'")
print(f"zfill(10): '{number.zfill(10)}'")

# ============================================================================
# 8. 字符串格式化
# ============================================================================

print("\n" + "=" * 50)
print("8. 字符串格式化")
print("=" * 50)

name = "张三"
age = 25
score = 95.5

# 8.1 % 格式化（旧式）
print("8.1 % 格式化（旧式）:")
print("姓名: %s, 年龄: %d, 分数: %.2f" % (name, age, score))
print("姓名: %s, 年龄: %d" % (name, age))

# 8.2 str.format() 方法
print("\n8.2 str.format() 方法:")
print("姓名: {}, 年龄: {}, 分数: {:.2f}".format(name, age, score))
print("姓名: {0}, 年龄: {1}, 分数: {2:.2f}".format(name, age, score))
print("姓名: {name}, 年龄: {age}, 分数: {score:.2f}".format(name=name, age=age, score=score))

# 8.3 f-string（推荐）
print("\n8.3 f-string（推荐）:")
print(f"姓名: {name}, 年龄: {age}, 分数: {score:.2f}")
print(f"姓名: {name}, 年龄: {age}")

# 8.4 格式化选项
print("\n8.4 格式化选项:")
number = 1234567.89
percentage = 0.856

print(f"数字格式化:")
print(f"原数字: {number}")
print(f"保留2位小数: {number:.2f}")
print(f"千分位分隔符: {number:,.2f}")
print(f"科学计数法: {number:.2e}")

print(f"\n百分比格式化:")
print(f"原数字: {percentage}")
print(f"百分比: {percentage:.2%}")
print(f"百分比（1位小数）: {percentage:.1%}")

print(f"\n进制转换:")
num = 255
print(f"十进制: {num}")
print(f"二进制: {num:b}")
print(f"八进制: {num:o}")
print(f"十六进制（小写）: {num:x}")
print(f"十六进制（大写）: {num:X}")

print(f"\n对齐格式化:")
text = "Python"
print(f"左对齐: '{text:<15}'")
print(f"右对齐: '{text:>15}'")
print(f"居中对齐: '{text:^15}'")
print(f"用*填充居中: '{text:*^15}'")

# ============================================================================
# 9. 字符串编码和解码
# ============================================================================

print("\n" + "=" * 50)
print("9. 字符串编码和解码")
print("=" * 50)

# 字符串编码
text = "Hello 世界"
print(f"原字符串: {text}")
print(f"字符串类型: {type(text)}")

# 编码为字节
utf8_bytes = text.encode('utf-8')
ascii_bytes = "Hello".encode('ascii')
gbk_bytes = "世界".encode('gbk')

print(f"\nUTF-8编码: {utf8_bytes}")
print(f"ASCII编码: {ascii_bytes}")
print(f"GBK编码: {gbk_bytes}")

# 解码为字符串
decoded_utf8 = utf8_bytes.decode('utf-8')
decoded_ascii = ascii_bytes.decode('ascii')
decoded_gbk = gbk_bytes.decode('gbk')

print(f"\nUTF-8解码: {decoded_utf8}")
print(f"ASCII解码: {decoded_ascii}")
print(f"GBK解码: {decoded_gbk}")

# 编码错误处理
print(f"\n编码错误处理:")
try:
    "世界".encode('ascii')
except UnicodeEncodeError as e:
    print(f"编码错误: {e}")
    # 使用错误处理策略
    result = "世界".encode('ascii', errors='ignore')
    print(f"忽略错误: {result}")
    result = "世界".encode('ascii', errors='replace')
    print(f"替换错误: {result}")

# ============================================================================
# 10. 正则表达式基础
# ============================================================================

print("\n" + "=" * 50)
print("10. 正则表达式基础")
print("=" * 50)

# 基本匹配
text = "我的电话是 138-1234-5678，邮箱是 user@example.com"
print(f"原文本: {text}")

# 查找电话号码
phone_pattern = r'\d{3}-\d{4}-\d{4}'
phone_match = re.search(phone_pattern, text)
if phone_match:
    print(f"找到电话号码: {phone_match.group()}")

# 查找邮箱
email_pattern = r'\w+@\w+\.\w+'
email_match = re.search(email_pattern, text)
if email_match:
    print(f"找到邮箱: {email_match.group()}")

# 查找所有数字
digits = re.findall(r'\d+', text)
print(f"所有数字: {digits}")

# 替换操作
print(f"\n替换操作:")
text2 = "今天是2024年1月1日"
print(f"原文本: {text2}")

# 替换所有数字为*
hidden = re.sub(r'\d', '*', text2)
print(f"隐藏数字: {hidden}")

# 替换年份
new_text = re.sub(r'\d{4}', '2025', text2)
print(f"替换年份: {new_text}")

# 分组匹配
print(f"\n分组匹配:")
date_text = "今天是2024-01-01，明天是2024-01-02"
date_pattern = r'(\d{4})-(\d{2})-(\d{2})'

for match in re.finditer(date_pattern, date_text):
    year, month, day = match.groups()
    print(f"日期: {match.group()}, 年: {year}, 月: {month}, 日: {day}")

# ============================================================================
# 11. 字符串性能优化
# ============================================================================

print("\n" + "=" * 50)
print("11. 字符串性能优化")
print("=" * 50)

import time

# 字符串连接性能比较
print("字符串连接性能比较:")

# 方法1：使用 + 连接（效率低）
start_time = time.time()
result1 = ""
for i in range(1000):
    result1 += str(i)
time1 = time.time() - start_time
print(f"使用 + 连接耗时: {time1:.4f}秒")

# 方法2：使用 join 连接（效率高）
start_time = time.time()
parts = []
for i in range(1000):
    parts.append(str(i))
result2 = ''.join(parts)
time2 = time.time() - start_time
print(f"使用 join 连接耗时: {time2:.4f}秒")

# 方法3：使用列表推导式 + join（最高效）
start_time = time.time()
result3 = ''.join(str(i) for i in range(1000))
time3 = time.time() - start_time
print(f"使用列表推导式 + join 耗时: {time3:.4f}秒")

print(f"\n性能提升: join比+快 {time1/time2:.1f} 倍")

# 字符串常量池
print(f"\n字符串常量池:")
a = "hello"
b = "hello"
c = "hel" + "lo"
d = "hello" * 1

print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a is d: {a is d}")

print("\n" + "=" * 50)
print("字符串操作示例代码运行完成！")
print("=" * 50)