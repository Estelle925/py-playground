#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字符串操作 - 练习题参考答案

本文件包含字符串操作练习题的参考答案和详细解释。
"""

import re
import string
from collections import Counter

# ============================================================================
# 练习1：字符串基础操作 - 参考答案
# ============================================================================

def exercise_1_solution():
    """
    练习1：字符串基础操作 - 参考答案
    """
    print("练习1：字符串基础操作")
    print("-" * 30)
    
    # 1. 创建字符串变量
    name = "张三"
    print(f"姓名：{name}")
    
    # 2. 获取字符串长度
    length = len(name)
    print(f"长度：{length}")
    
    # 3. 转换为大写（对中文无效，这里用英文示例）
    english_name = "Zhang San"
    upper_name = english_name.upper()
    print(f"大写：{upper_name}")
    
    # 4. 转换为小写
    lower_name = english_name.lower()
    print(f"小写：{lower_name}")
    
    # 5. 获取第一个和最后一个字符
    first_char = name[0]
    last_char = name[-1]
    print(f"第一个字符：{first_char}")
    print(f"最后一个字符：{last_char}")
    print()

# ============================================================================
# 练习2：字符串切片 - 参考答案
# ============================================================================

def exercise_2_solution():
    """
    练习2：字符串切片 - 参考答案
    """
    print("练习2：字符串切片")
    print("-" * 30)
    
    text = "Python Programming Language"
    print(f"原字符串：{text}")
    
    # 1. 获取前6个字符
    first_six = text[:6]
    print(f"前6个字符：{first_six}")
    
    # 2. 获取后8个字符
    last_eight = text[-8:]
    print(f"后8个字符：{last_eight}")
    
    # 3. 获取中间的单词"Programming"
    programming = text[7:18]  # 或者使用 text.split()[1]
    print(f"中间单词：{programming}")
    
    # 4. 反转整个字符串
    reversed_text = text[::-1]
    print(f"反转字符串：{reversed_text}")
    
    # 5. 每隔一个字符取一个字符
    every_other = text[::2]
    print(f"每隔一个字符：{every_other}")
    print()

# ============================================================================
# 练习3：字符串查找和替换 - 参考答案
# ============================================================================

def exercise_3_solution():
    """
    练习3：字符串查找和替换 - 参考答案
    """
    print("练习3：字符串查找和替换")
    print("-" * 30)
    
    text = "Python is great. Python is powerful. Python is easy to learn."
    print(f"原文本：{text}")
    
    # 1. 统计"Python"出现的次数
    count = text.count("Python")
    print(f"Python出现次数：{count}")
    
    # 2. 找到第一个"Python"的位置
    first_pos = text.find("Python")
    print(f"第一个Python位置：{first_pos}")
    
    # 3. 找到最后一个"Python"的位置
    last_pos = text.rfind("Python")
    print(f"最后一个Python位置：{last_pos}")
    
    # 4. 将所有"Python"替换为"Java"
    replaced_all = text.replace("Python", "Java")
    print(f"全部替换：{replaced_all}")
    
    # 5. 只替换第一个"Python"为"JavaScript"
    replaced_first = text.replace("Python", "JavaScript", 1)
    print(f"替换第一个：{replaced_first}")
    print()

# ============================================================================
# 练习4：字符串分割和连接 - 参考答案
# ============================================================================

def exercise_4_solution():
    """
    练习4：字符串分割和连接 - 参考答案
    """
    print("练习4：字符串分割和连接")
    print("-" * 30)
    
    fruits = "apple,banana,orange,grape,watermelon"
    print(f"原字符串：{fruits}")
    
    # 1. 按逗号分割成列表
    fruit_list = fruits.split(",")
    print(f"分割后的列表：{fruit_list}")
    
    # 2. 用" | "分隔重新连接
    joined_with_pipe = " | ".join(fruit_list)
    print(f"用 | 连接：{joined_with_pipe}")
    
    # 3. 首字母大写后连接
    capitalized = [fruit.capitalize() for fruit in fruit_list]
    capitalized_joined = ", ".join(capitalized)
    print(f"首字母大写：{capitalized_joined}")
    
    # 4. 按字母顺序排序后连接
    sorted_fruits = sorted(fruit_list)
    sorted_joined = ", ".join(sorted_fruits)
    print(f"排序后连接：{sorted_joined}")
    print()

# ============================================================================
# 练习5：字符串格式化 - 参考答案
# ============================================================================

def exercise_5_solution():
    """
    练习5：字符串格式化 - 参考答案
    """
    print("练习5：字符串格式化")
    print("-" * 30)
    
    name = "张三"
    age = 25
    score = 88.5
    
    # 1. 使用%格式化
    formatted_percent = "姓名：%s，年龄：%d岁，分数：%.1f分" % (name, age, score)
    print(f"% 格式化：{formatted_percent}")
    
    # 2. 使用format()方法
    formatted_format = "姓名：{}，年龄：{}岁，分数：{}分".format(name, age, score)
    print(f"format() 方法：{formatted_format}")
    
    # 3. 使用f-string
    formatted_fstring = f"姓名：{name}，年龄：{age}岁，分数：{score}分"
    print(f"f-string：{formatted_fstring}")
    
    # 4. 格式化分数为两位小数
    formatted_decimal = f"分数（两位小数）：{score:.2f}分"
    print(f"两位小数：{formatted_decimal}")
    
    # 5. 年龄右对齐到5位宽度
    formatted_align = f"年龄（右对齐5位）：'{age:>5}'岁"
    print(f"右对齐：{formatted_align}")
    print()

# ============================================================================
# 练习6：字符串验证 - 参考答案
# ============================================================================

def exercise_6_solution():
    """
    练习6：字符串验证 - 参考答案
    """
    print("练习6：字符串验证")
    print("-" * 30)
    
    def is_digits_only(s):
        """检查是否只包含数字"""
        return s.isdigit()
    
    def is_letters_only(s):
        """检查是否只包含字母"""
        return s.isalpha()
    
    def is_alphanumeric(s):
        """检查是否只包含字母和数字"""
        return s.isalnum()
    
    def is_valid_email(s):
        """简单的邮箱验证"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, s) is not None
    
    def is_valid_phone(s):
        """检查是否为有效手机号（11位数字）"""
        return len(s) == 11 and s.isdigit() and s.startswith('1')
    
    test_strings = [
        "12345",
        "hello",
        "hello123",
        "user@example.com",
        "13812345678",
        "invalid-email",
        "1234567890"
    ]
    
    for s in test_strings:
        print(f"字符串：'{s}'")
        print(f"  只包含数字：{is_digits_only(s)}")
        print(f"  只包含字母：{is_letters_only(s)}")
        print(f"  字母和数字：{is_alphanumeric(s)}")
        print(f"  有效邮箱：{is_valid_email(s)}")
        print(f"  有效手机：{is_valid_phone(s)}")
        print()

# ============================================================================
# 练习7：文本处理 - 参考答案
# ============================================================================

def exercise_7_solution():
    """
    练习7：文本处理 - 参考答案
    """
    print("练习7：文本处理")
    print("-" * 30)
    
    text = """Python is a high-level, interpreted programming language. 
    Python's design philosophy emphasizes code readability. 
    Python is widely used in web development, data analysis, and artificial intelligence."""
    
    print(f"原文本：{text}")
    print()
    
    # 1. 统计单词数量
    words = text.split()
    word_count = len(words)
    print(f"单词数量：{word_count}")
    
    # 2. 统计每个单词出现的次数
    # 移除标点符号后统计
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    clean_words = clean_text.lower().split()
    word_freq = Counter(clean_words)
    print(f"单词频率：{dict(word_freq)}")
    
    # 3. 找出最长的单词
    longest_word = max(clean_words, key=len)
    print(f"最长单词：{longest_word} (长度：{len(longest_word)})")
    
    # 4. 移除所有标点符号
    no_punctuation = clean_text
    print(f"移除标点：{no_punctuation}")
    
    # 5. 转换为标题格式
    title_case = text.title()
    print(f"标题格式：{title_case}")
    print()

# ============================================================================
# 练习8：密码强度检查 - 参考答案
# ============================================================================

def exercise_8_solution():
    """
    练习8：密码强度检查 - 参考答案
    """
    print("练习8：密码强度检查")
    print("-" * 30)
    
    def check_password_strength(password):
        """
        检查密码强度
        返回：(强度等级, 满足条件数, 详细信息)
        """
        conditions = {
            '长度至少8位': len(password) >= 8,
            '包含大写字母': any(c.isupper() for c in password),
            '包含小写字母': any(c.islower() for c in password),
            '包含数字': any(c.isdigit() for c in password),
            '包含特殊字符': any(c in string.punctuation for c in password)
        }
        
        satisfied_count = sum(conditions.values())
        
        if satisfied_count == 5:
            strength = "强"
        elif satisfied_count == 4:
            strength = "中等"
        elif satisfied_count == 3:
            strength = "弱"
        else:
            strength = "很弱"
        
        return strength, satisfied_count, conditions
    
    passwords = [
        "password",
        "Password123",
        "P@ssw0rd",
        "MySecureP@ssw0rd123",
        "123456",
        "Aa1!"
    ]
    
    for pwd in passwords:
        strength, count, conditions = check_password_strength(pwd)
        print(f"密码：'{pwd}'")
        print(f"强度：{strength} (满足{count}/5个条件)")
        for condition, satisfied in conditions.items():
            status = "✓" if satisfied else "✗"
            print(f"  {status} {condition}")
        print()

# ============================================================================
# 练习9：字符串编码解码 - 参考答案
# ============================================================================

def exercise_9_solution():
    """
    练习9：字符串编码解码 - 参考答案
    """
    print("练习9：字符串编码解码")
    print("-" * 30)
    
    chinese_text = "你好，世界！Python编程"
    print(f"原始文本：{chinese_text}")
    
    # 1. UTF-8编码
    utf8_bytes = chinese_text.encode('utf-8')
    print(f"UTF-8编码：{utf8_bytes}")
    
    # 2. 解码回字符串
    decoded_text = utf8_bytes.decode('utf-8')
    print(f"UTF-8解码：{decoded_text}")
    
    # 3. 尝试不同编码格式
    try:
        gbk_bytes = chinese_text.encode('gbk')
        print(f"GBK编码：{gbk_bytes}")
        gbk_decoded = gbk_bytes.decode('gbk')
        print(f"GBK解码：{gbk_decoded}")
    except UnicodeEncodeError as e:
        print(f"GBK编码错误：{e}")
    
    # 4. 处理编码错误
    try:
        ascii_bytes = chinese_text.encode('ascii')
    except UnicodeEncodeError as e:
        print(f"ASCII编码错误：{e}")
        # 使用错误处理策略
        ascii_bytes = chinese_text.encode('ascii', errors='ignore')
        print(f"ASCII编码（忽略错误）：{ascii_bytes}")
        ascii_bytes = chinese_text.encode('ascii', errors='replace')
        print(f"ASCII编码（替换错误）：{ascii_bytes}")
    
    print()

# ============================================================================
# 练习10：综合应用 - 简单文本分析器 - 参考答案
# ============================================================================

def exercise_10_solution():
    """
    练习10：综合应用 - 简单文本分析器 - 参考答案
    """
    print("练习10：综合应用 - 简单文本分析器")
    print("-" * 30)
    
    text = """Python is a powerful programming language. It is easy to learn and use.
    
    Python supports multiple programming paradigms. Object-oriented programming is one of them.
    Functional programming is another paradigm that Python supports.
    
    Python has a rich ecosystem of libraries and frameworks. This makes Python very popular
    among developers worldwide."""
    
    print("文本分析结果：")
    print("=" * 40)
    
    # 1. 字符总数（包括空格）
    total_chars_with_spaces = len(text)
    print(f"字符总数（含空格）：{total_chars_with_spaces}")
    
    # 2. 字符总数（不包括空格）
    total_chars_no_spaces = len(text.replace(' ', '').replace('\n', ''))
    print(f"字符总数（不含空格）：{total_chars_no_spaces}")
    
    # 3. 单词总数
    words = text.split()
    total_words = len(words)
    print(f"单词总数：{total_words}")
    
    # 4. 句子总数
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    total_sentences = len(sentences)
    print(f"句子总数：{total_sentences}")
    
    # 5. 段落总数
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    total_paragraphs = len(paragraphs)
    print(f"段落总数：{total_paragraphs}")
    
    # 6. 平均单词长度
    clean_words = [word.strip(string.punctuation) for word in words]
    avg_word_length = sum(len(word) for word in clean_words) / len(clean_words)
    print(f"平均单词长度：{avg_word_length:.2f}")
    
    # 7. 最常用的5个单词
    word_freq = Counter(word.lower().strip(string.punctuation) for word in words)
    most_common = word_freq.most_common(5)
    print(f"最常用的5个单词：{most_common}")
    
    # 8. 最长的句子
    longest_sentence = max(sentences, key=len)
    print(f"最长的句子：{longest_sentence.strip()}")
    print(f"最长句子长度：{len(longest_sentence.strip())}个字符")
    
    print()

# ============================================================================
# 额外知识点：高级字符串操作
# ============================================================================

def advanced_string_operations():
    """
    额外知识点：高级字符串操作
    """
    print("额外知识点：高级字符串操作")
    print("-" * 30)
    
    # 1. 字符串模板
    from string import Template
    template = Template('Hello $name, you have $count new messages.')
    result = template.substitute(name='Alice', count=5)
    print(f"字符串模板：{result}")
    
    # 2. 正则表达式替换
    text = "Phone: 123-456-7890, Mobile: 098-765-4321"
    # 将电话号码格式化
    formatted = re.sub(r'(\d{3})-(\d{3})-(\d{4})', r'(\1) \2-\3', text)
    print(f"正则替换：{formatted}")
    
    # 3. 字符串对齐和填充
    text = "Python"
    print(f"左对齐：'{text:<10}'")
    print(f"右对齐：'{text:>10}'")
    print(f"居中：'{text:^10}'")
    print(f"用*填充：'{text:*^10}'")
    
    # 4. 多行字符串处理
    multiline = """line1
    line2
    line3"""
    # 移除每行前导空格
    import textwrap
    dedented = textwrap.dedent(multiline)
    print(f"去除缩进：\n{dedented}")
    
    print()

if __name__ == "__main__":
    print("字符串操作练习题 - 参考答案")
    print("=" * 50)
    
    # 运行所有练习的参考答案
    exercise_1_solution()
    exercise_2_solution()
    exercise_3_solution()
    exercise_4_solution()
    exercise_5_solution()
    exercise_6_solution()
    exercise_7_solution()
    exercise_8_solution()
    exercise_9_solution()
    exercise_10_solution()
    advanced_string_operations()
    
    print("\n学习建议：")
    print("- 字符串是不可变对象，每次操作都会创建新字符串")
    print("- 大量字符串拼接时使用join()而不是+操作符")
    print("- 使用f-string进行字符串格式化（Python 3.6+）")
    print("- 正则表达式适合复杂的字符串匹配和替换")
    print("- 注意字符串编码问题，特别是处理中文时")