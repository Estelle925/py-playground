#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
控制结构 - 练习题参考答案

本文件包含控制结构练习题的参考答案和详细解释。
"""

import random
import re
from typing import List, Dict, Any, Tuple, Optional

# ============================================================================
# 练习1：条件语句基础 - 参考答案
# ============================================================================

def exercise_1_solution():
    """
    练习1：条件语句基础 - 参考答案
    """
    print("练习1：条件语句基础")
    print("-" * 30)
    
    # 1. 判断数字正负
    def check_number_sign(num):
        if num > 0:
            return "正数"
        elif num < 0:
            return "负数"
        else:
            return "零"
    
    test_numbers = [5, -3, 0, 10, -7]
    for num in test_numbers:
        result = check_number_sign(num)
        print(f"{num} 是 {result}")
    
    # 2. 分数等级判断
    def get_grade(score):
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 70:
            return "中等"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"
    
    test_scores = [95, 85, 75, 65, 55]
    print("\n分数等级：")
    for score in test_scores:
        grade = get_grade(score)
        print(f"分数{score}：{grade}")
    
    # 3. 判断闰年
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    
    test_years = [2000, 1900, 2004, 2021, 2024]
    print("\n闰年判断：")
    for year in test_years:
        is_leap = is_leap_year(year)
        print(f"{year}年：{'是' if is_leap else '不是'}闰年")
    
    # 4. BMI判断
    def get_bmi_status(height, weight):
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            status = "偏瘦"
        elif bmi < 24:
            status = "正常"
        elif bmi < 28:
            status = "偏胖"
        else:
            status = "肥胖"
        return bmi, status
    
    test_data = [(1.70, 60), (1.75, 70), (1.80, 85), (1.65, 45)]
    print("\nBMI状况：")
    for height, weight in test_data:
        bmi, status = get_bmi_status(height, weight)
        print(f"身高{height}m，体重{weight}kg：BMI={bmi:.1f}，{status}")
    
    print()

# ============================================================================
# 练习2：for循环基础 - 参考答案
# ============================================================================

def exercise_2_solution():
    """
    练习2：for循环基础 - 参考答案
    """
    print("练习2：for循环基础")
    print("-" * 30)
    
    # 1. 打印1到10
    print("1. 打印1到10：")
    for i in range(1, 11):
        print(i, end=" ")
    print()
    
    # 2. 计算1到100的和
    print("\n2. 计算1到100的和：")
    total = 0
    for i in range(1, 101):
        total += i
    print(f"1到100的和：{total}")
    # 也可以使用内置函数：sum(range(1, 101))
    
    # 3. 打印列表中所有偶数
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n3. 列表中的偶数：")
    for num in numbers:
        if num % 2 == 0:
            print(num, end=" ")
    print()
    
    # 4. 遍历字典
    student_info = {"name": "张三", "age": 20, "major": "计算机科学"}
    print("\n4. 字典键值对：")
    for key, value in student_info.items():
        print(f"{key}: {value}")
    
    # 5. 使用enumerate
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    print("\n5. 使用enumerate：")
    for index, fruit in enumerate(fruits):
        print(f"索引{index}: {fruit}")
    
    print()

# ============================================================================
# 练习3：while循环基础 - 参考答案
# ============================================================================

def exercise_3_solution():
    """
    练习3：while循环基础 - 参考答案
    """
    print("练习3：while循环基础")
    print("-" * 30)
    
    # 1. 计算2的幂次
    print("1. 2的幂次（直到大于1000）：")
    power = 1
    exponent = 0
    while power <= 1000:
        print(f"2^{exponent} = {power}")
        exponent += 1
        power = 2 ** exponent
    
    # 2. 模拟用户输入
    print("\n2. 模拟用户输入：")
    inputs = ["hello", "world", "python", "quit"]
    input_index = 0
    
    while True:
        if input_index < len(inputs):
            user_input = inputs[input_index]
            input_index += 1
        else:
            break
        
        print(f"用户输入：{user_input}")
        if user_input == "quit":
            print("程序退出")
            break
        print(f"处理：{user_input}")
    
    # 3. 倒计时
    print("\n3. 倒计时（从5开始）：")
    countdown = 5
    while countdown > 0:
        print(f"倒计时：{countdown}")
        countdown -= 1
    print("时间到！")
    
    # 4. 斐波那契数列
    print("\n4. 第一个大于100的斐波那契数：")
    a, b = 0, 1
    while b <= 100:
        print(f"斐波那契数：{b}")
        a, b = b, a + b
    print(f"第一个大于100的斐波那契数：{b}")
    
    print()

# ============================================================================
# 练习4：循环控制语句 - 参考答案
# ============================================================================

def exercise_4_solution():
    """
    练习4：循环控制语句 - 参考答案
    """
    print("练习4：循环控制语句")
    print("-" * 30)
    
    # 1. 找到第一个能被7整除的数
    print("1. 1-20中第一个能被7整除的数：")
    for i in range(1, 21):
        if i % 7 == 0:
            print(f"找到：{i}")
            break
    
    # 2. 打印不能被3整除的数
    print("\n2. 1-20中不能被3整除的数：")
    for i in range(1, 21):
        if i % 3 == 0:
            continue
        print(i, end=" ")
    print()
    
    # 3. 处理列表，跳过None值
    data = [1, 2, None, 4, 5, None, 7, 8, 9, 10]
    print("\n3. 处理列表（跳过None）：")
    for item in data:
        if item is None:
            continue
        print(f"处理：{item}")
    
    # 4. 使用for-else查找
    search_list = [10, 20, 30, 40, 50]
    target = 35
    print(f"\n4. 在列表中查找{target}：")
    for item in search_list:
        if item == target:
            print(f"找到{target}")
            break
    else:
        print(f"未找到{target}")
    
    print()

# ============================================================================
# 练习5：嵌套循环 - 参考答案
# ============================================================================

def exercise_5_solution():
    """
    练习5：嵌套循环 - 参考答案
    """
    print("练习5：嵌套循环")
    print("-" * 30)
    
    # 1. 5x5星号矩阵
    print("1. 5x5星号矩阵：")
    for i in range(5):
        for j in range(5):
            print("*", end=" ")
        print()
    
    # 2. 直角三角形
    print("\n2. 直角三角形：")
    for i in range(1, 6):
        for j in range(i):
            print("*", end=" ")
        print()
    
    # 3. 九九乘法表
    print("\n3. 九九乘法表：")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j}", end="\t")
        print()
    
    # 4. 找出二维列表最大值
    matrix = [
        [1, 5, 3],
        [9, 2, 8],
        [4, 7, 6]
    ]
    print("\n4. 二维列表最大值：")
    max_value = matrix[0][0]
    max_position = (0, 0)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)
    
    print(f"最大值：{max_value}，位置：{max_position}")
    
    print()

# ============================================================================
# 练习6：推导式 - 参考答案
# ============================================================================

def exercise_6_solution():
    """
    练习6：推导式 - 参考答案
    """
    print("练习6：推导式")
    print("-" * 30)
    
    # 1. 1-10的平方数
    squares = [x**2 for x in range(1, 11)]
    print(f"1. 1-10的平方数：{squares}")
    
    # 2. 筛选长度大于5的字符串
    words = ["python", "java", "javascript", "go", "rust", "c++"]
    long_words = [word for word in words if len(word) > 5]
    print(f"2. 长度>5的字符串：{long_words}")
    
    # 3. 创建立方字典
    cube_dict = {x: x**3 for x in range(1, 6)}
    print(f"3. 1-5的立方字典：{cube_dict}")
    
    # 4. 从嵌套列表提取偶数
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    even_numbers = [num for sublist in nested_list for num in sublist if num % 2 == 0]
    print(f"4. 嵌套列表中的偶数：{even_numbers}")
    
    # 5. 字符串长度集合
    string_lengths = {len(word) for word in words}
    print(f"5. 字符串长度集合：{string_lengths}")
    
    print()

# ============================================================================
# 练习7：数据处理 - 参考答案
# ============================================================================

def exercise_7_solution():
    """
    练习7：数据处理 - 参考答案
    """
    print("练习7：数据处理")
    print("-" * 30)
    
    students = [
        {"name": "张三", "math": 85, "english": 90, "science": 78},
        {"name": "李四", "math": 92, "english": 88, "science": 95},
        {"name": "王五", "math": 76, "english": 82, "science": 80},
        {"name": "赵六", "math": 88, "english": 85, "science": 90},
        {"name": "钱七", "math": 95, "english": 92, "science": 89}
    ]
    
    # 1. 计算每个学生的平均分
    print("1. 学生平均分：")
    for student in students:
        name = student["name"]
        scores = [student["math"], student["english"], student["science"]]
        average = sum(scores) / len(scores)
        student["average"] = average
        print(f"{name}: {average:.1f}")
    
    # 2. 找出平均分最高的学生
    print("\n2. 平均分最高的学生：")
    top_student = max(students, key=lambda s: s["average"])
    print(f"{top_student['name']}: {top_student['average']:.1f}")
    
    # 3. 统计分数段人数
    print("\n3. 分数段统计：")
    score_ranges = {"优秀(90+)": 0, "良好(80-89)": 0, "中等(70-79)": 0, "及格(60-69)": 0}
    
    for student in students:
        avg = student["average"]
        if avg >= 90:
            score_ranges["优秀(90+)"] += 1
        elif avg >= 80:
            score_ranges["良好(80-89)"] += 1
        elif avg >= 70:
            score_ranges["中等(70-79)"] += 1
        else:
            score_ranges["及格(60-69)"] += 1
    
    for range_name, count in score_ranges.items():
        print(f"{range_name}: {count}人")
    
    # 4. 找出各科最高分学生
    print("\n4. 各科最高分：")
    subjects = ["math", "english", "science"]
    subject_names = {"math": "数学", "english": "英语", "science": "科学"}
    
    for subject in subjects:
        top_student = max(students, key=lambda s: s[subject])
        print(f"{subject_names[subject]}最高分：{top_student['name']} ({top_student[subject]}分)")
    
    print()

# ============================================================================
# 练习8：文本分析 - 参考答案
# ============================================================================

def exercise_8_solution():
    """
    练习8：文本分析 - 参考答案
    """
    print("练习8：文本分析")
    print("-" * 30)
    
    text = """Python is a high-level programming language. 
    Python emphasizes code readability and simplicity. 
    Many developers choose Python for web development, 
    data analysis, and artificial intelligence projects."""
    
    # 清理文本
    import string
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()
    
    # 1. 统计单词频率
    print("1. 单词频率：")
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")
    
    # 2. 找出最长的单词
    print("\n2. 最长的单词：")
    longest_word = max(words, key=len)
    print(f"最长单词：{longest_word} (长度：{len(longest_word)})")
    
    # 3. 统计字母频率
    print("\n3. 字母频率（前10个）：")
    letter_count = {}
    for char in clean_text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letters[:10]:
        print(f"{letter}: {count}")
    
    # 4. 出现次数最多的单词
    print("\n4. 出现次数最多的单词：")
    most_common_word = max(word_count.items(), key=lambda x: x[1])
    print(f"最常用单词：{most_common_word[0]} (出现{most_common_word[1]}次)")
    
    print()

# ============================================================================
# 练习9：数学计算 - 参考答案
# ============================================================================

def exercise_9_solution():
    """
    练习9：数学计算 - 参考答案
    """
    print("练习9：数学计算")
    print("-" * 30)
    
    # 1. 计算阶乘
    def factorial(n):
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    print("1. 阶乘计算：")
    for i in range(1, 8):
        print(f"{i}! = {factorial(i)}")
    
    # 2. 判断质数
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    print("\n2. 质数判断（1-20）：")
    primes = []
    for i in range(1, 21):
        if is_prime(i):
            primes.append(i)
    print(f"质数：{primes}")
    
    # 3. 生成指定范围内的质数
    def generate_primes(start, end):
        primes = []
        for num in range(start, end + 1):
            if is_prime(num):
                primes.append(num)
        return primes
    
    print("\n3. 50-100范围内的质数：")
    primes_50_100 = generate_primes(50, 100)
    print(f"质数：{primes_50_100}")
    
    # 4. 最大公约数
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    print("\n4. 最大公约数：")
    test_pairs = [(48, 18), (56, 98), (101, 103)]
    for a, b in test_pairs:
        result = gcd(a, b)
        print(f"gcd({a}, {b}) = {result}")
    
    # 5. 帕斯卡三角形
    def pascal_triangle(n):
        triangle = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle
    
    print("\n5. 帕斯卡三角形（前6行）：")
    triangle = pascal_triangle(6)
    for i, row in enumerate(triangle):
        spaces = " " * (6 - i)
        print(spaces + " ".join(map(str, row)))
    
    print()

# ============================================================================
# 练习10：模式匹配和查找 - 参考答案
# ============================================================================

def exercise_10_solution():
    """
    练习10：模式匹配和查找 - 参考答案
    """
    print("练习10：模式匹配和查找")
    print("-" * 30)
    
    numbers = [1, 5, 3, 8, 2, 9, 4, 7, 6, 10, 15, 12]
    text = "hello world, hello python, hello programming"
    pattern = "hello"
    
    # 1. 查找满足条件的元素
    print("1. 查找大于5的数字：")
    greater_than_5 = [num for num in numbers if num > 5]
    print(f"大于5的数字：{greater_than_5}")
    
    # 2. 查找子字符串位置
    print("\n2. 查找'hello'的所有位置：")
    positions = []
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    print(f"'hello'的位置：{positions}")
    
    # 3. 简单模式匹配
    def simple_match(text, pattern):
        """简单的通配符匹配（支持*和?）"""
        # 这里实现一个简化版本
        if '*' not in pattern and '?' not in pattern:
            return text == pattern
        
        # 转换为正则表达式
        regex_pattern = pattern.replace('*', '.*').replace('?', '.')
        return re.match(f'^{regex_pattern}$', text) is not None
    
    print("\n3. 模式匹配测试：")
    test_cases = [
        ("hello", "hello"),
        ("hello", "h*o"),
        ("hello", "h?llo"),
        ("world", "w*d"),
        ("python", "p*n")
    ]
    
    for text_test, pattern_test in test_cases:
        match = simple_match(text_test, pattern_test)
        print(f"'{text_test}' 匹配 '{pattern_test}': {match}")
    
    # 4. 在二维列表中查找坐标
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    target_value = 7
    
    print(f"\n4. 在二维列表中查找{target_value}：")
    found_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == target_value:
                found_positions.append((i, j))
    
    if found_positions:
        print(f"找到{target_value}，位置：{found_positions}")
    else:
        print(f"未找到{target_value}")
    
    print()

if __name__ == "__main__":
    print("控制结构练习题 - 参考答案")
    print("=" * 50)
    
    # 运行前10个练习的参考答案
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
    
    print("\n学习要点总结：")
    print("- 条件语句：if-elif-else，三元运算符")
    print("- 循环语句：for循环遍历，while循环条件")
    print("- 控制语句：break跳出，continue跳过，pass占位")
    print("- 嵌套结构：循环嵌套，条件嵌套")
    print("- 推导式：列表、字典、集合推导式")
    print("- 实际应用：数据处理、文本分析、算法实现")
    
    print("\n编程技巧：")
    print("- 使用enumerate()获取索引和值")
    print("- 使用zip()同时遍历多个序列")
    print("- 利用for-else和while-else处理特殊情况")
    print("- 推导式比循环更简洁高效")
    print("- 合理使用内置函数如max()、min()、sum()")