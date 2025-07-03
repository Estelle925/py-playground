#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
控制结构 - 示例代码

本文件演示Python中各种控制结构的使用方法，包括条件语句、循环语句和控制流语句。
"""

import time
import random
from typing import List, Any

# ============================================================================
# 1. 条件语句示例
# ============================================================================

def conditional_statements_examples():
    """
    条件语句示例
    """
    print("1. 条件语句示例")
    print("=" * 40)
    
    # 1.1 基本if语句
    print("1.1 基本if语句")
    age = 18
    if age >= 18:
        print(f"年龄{age}岁，已成年")
    
    # 1.2 if-else语句
    print("\n1.2 if-else语句")
    score = 85
    if score >= 60:
        print(f"分数{score}，及格了")
    else:
        print(f"分数{score}，不及格")
    
    # 1.3 if-elif-else语句
    print("\n1.3 if-elif-else语句")
    grade = 92
    if grade >= 90:
        level = "优秀"
    elif grade >= 80:
        level = "良好"
    elif grade >= 70:
        level = "中等"
    elif grade >= 60:
        level = "及格"
    else:
        level = "不及格"
    print(f"分数{grade}，等级：{level}")
    
    # 1.4 条件表达式（三元运算符）
    print("\n1.4 条件表达式")
    x = 10
    result = "正数" if x > 0 else "非正数"
    print(f"{x} 是 {result}")
    
    # 复杂条件表达式
    status = "优秀" if grade >= 90 else "良好" if grade >= 80 else "一般"
    print(f"简化等级判断：{status}")
    
    # 1.5 复合条件
    print("\n1.5 复合条件")
    temperature = 25
    humidity = 60
    if temperature > 20 and humidity < 70:
        print("天气舒适")
    elif temperature > 30 or humidity > 80:
        print("天气不适")
    else:
        print("天气一般")
    
    print()

# ============================================================================
# 2. for循环示例
# ============================================================================

def for_loop_examples():
    """
    for循环示例
    """
    print("2. for循环示例")
    print("=" * 40)
    
    # 2.1 遍历列表
    print("2.1 遍历列表")
    fruits = ["苹果", "香蕉", "橙子", "葡萄"]
    for fruit in fruits:
        print(f"我喜欢吃{fruit}")
    
    # 2.2 遍历字符串
    print("\n2.2 遍历字符串")
    word = "Python"
    for char in word:
        print(f"字符：{char}")
    
    # 2.3 使用range()
    print("\n2.3 使用range()")
    print("range(5):")
    for i in range(5):
        print(f"  {i}")
    
    print("range(2, 8):")
    for i in range(2, 8):
        print(f"  {i}")
    
    print("range(0, 10, 2):")
    for i in range(0, 10, 2):
        print(f"  {i}")
    
    # 2.4 使用enumerate()
    print("\n2.4 使用enumerate()")
    colors = ["红色", "绿色", "蓝色"]
    for index, color in enumerate(colors):
        print(f"索引{index}: {color}")
    
    # 从指定数字开始编号
    for index, color in enumerate(colors, start=1):
        print(f"第{index}种颜色: {color}")
    
    # 2.5 使用zip()
    print("\n2.5 使用zip()")
    names = ["张三", "李四", "王五"]
    ages = [25, 30, 35]
    cities = ["北京", "上海", "广州"]
    
    for name, age, city in zip(names, ages, cities):
        print(f"{name}，{age}岁，住在{city}")
    
    # 2.6 遍历字典
    print("\n2.6 遍历字典")
    student = {"姓名": "小明", "年龄": 20, "专业": "计算机"}
    
    print("遍历键：")
    for key in student:
        print(f"  {key}")
    
    print("遍历值：")
    for value in student.values():
        print(f"  {value}")
    
    print("遍历键值对：")
    for key, value in student.items():
        print(f"  {key}: {value}")
    
    print()

# ============================================================================
# 3. while循环示例
# ============================================================================

def while_loop_examples():
    """
    while循环示例
    """
    print("3. while循环示例")
    print("=" * 40)
    
    # 3.1 基本while循环
    print("3.1 基本while循环")
    count = 0
    while count < 5:
        print(f"计数：{count}")
        count += 1
    
    # 3.2 用户输入循环
    print("\n3.2 模拟用户输入循环")
    # 模拟用户输入，实际使用时可以用input()
    inputs = ["hello", "world", "quit"]
    input_index = 0
    
    while True:
        if input_index < len(inputs):
            user_input = inputs[input_index]
            input_index += 1
        else:
            break
        
        print(f"用户输入：{user_input}")
        if user_input == "quit":
            print("退出程序")
            break
        print(f"处理输入：{user_input}")
    
    # 3.3 条件累加
    print("\n3.3 条件累加")
    total = 0
    num = 1
    while total < 100:
        total += num
        print(f"加上{num}，总和：{total}")
        num += 1
    
    # 3.4 查找循环
    print("\n3.4 查找循环")
    numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
    target = 7
    index = 0
    found = False
    
    while index < len(numbers) and not found:
        if numbers[index] == target:
            found = True
            print(f"找到{target}，位置：{index}")
        else:
            index += 1
    
    if not found:
        print(f"未找到{target}")
    
    print()

# ============================================================================
# 4. 循环控制语句示例
# ============================================================================

def loop_control_examples():
    """
    循环控制语句示例
    """
    print("4. 循环控制语句示例")
    print("=" * 40)
    
    # 4.1 break语句
    print("4.1 break语句")
    for i in range(10):
        if i == 5:
            print(f"遇到{i}，跳出循环")
            break
        print(f"当前数字：{i}")
    
    # 4.2 continue语句
    print("\n4.2 continue语句")
    for i in range(10):
        if i % 2 == 0:
            continue  # 跳过偶数
        print(f"奇数：{i}")
    
    # 4.3 pass语句
    print("\n4.3 pass语句")
    for i in range(5):
        if i == 2:
            pass  # 什么都不做，占位符
        print(f"处理：{i}")
    
    # 4.4 else子句
    print("\n4.4 for-else语句")
    numbers = [1, 3, 5, 7, 9]
    target = 4
    
    for num in numbers:
        if num == target:
            print(f"找到{target}")
            break
    else:
        print(f"没有找到{target}")
    
    print("\n4.5 while-else语句")
    count = 0
    while count < 3:
        print(f"计数：{count}")
        count += 1
    else:
        print("while循环正常结束")
    
    print()

# ============================================================================
# 5. 嵌套控制结构示例
# ============================================================================

def nested_structures_examples():
    """
    嵌套控制结构示例
    """
    print("5. 嵌套控制结构示例")
    print("=" * 40)
    
    # 5.1 嵌套循环 - 乘法表
    print("5.1 九九乘法表")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j}", end="\t")
        print()  # 换行
    
    # 5.2 二维列表遍历
    print("\n5.2 二维列表遍历")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            print(f"matrix[{i}][{j}] = {value}")
    
    # 5.3 条件嵌套循环
    print("\n5.3 条件嵌套循环")
    students = [
        {"name": "张三", "scores": [85, 90, 78]},
        {"name": "李四", "scores": [92, 88, 95]},
        {"name": "王五", "scores": [76, 82, 80]}
    ]
    
    for student in students:
        name = student["name"]
        scores = student["scores"]
        total = sum(scores)
        average = total / len(scores)
        
        print(f"{name}的成绩：")
        for i, score in enumerate(scores, 1):
            if score >= 90:
                grade = "优秀"
            elif score >= 80:
                grade = "良好"
            else:
                grade = "一般"
            print(f"  科目{i}: {score}分 ({grade})")
        print(f"  平均分: {average:.1f}分")
        print()

# ============================================================================
# 6. 推导式示例
# ============================================================================

def comprehension_examples():
    """
    推导式示例
    """
    print("6. 推导式示例")
    print("=" * 40)
    
    # 6.1 列表推导式
    print("6.1 列表推导式")
    
    # 基本列表推导式
    squares = [x**2 for x in range(10)]
    print(f"平方数：{squares}")
    
    # 带条件的列表推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"偶数的平方：{even_squares}")
    
    # 复杂表达式
    words = ["hello", "world", "python", "programming"]
    capitalized = [word.capitalize() for word in words if len(word) > 5]
    print(f"长单词首字母大写：{capitalized}")
    
    # 6.2 字典推导式
    print("\n6.2 字典推导式")
    
    # 基本字典推导式
    square_dict = {x: x**2 for x in range(5)}
    print(f"数字及其平方：{square_dict}")
    
    # 从列表创建字典
    fruits = ["apple", "banana", "orange"]
    fruit_lengths = {fruit: len(fruit) for fruit in fruits}
    print(f"水果名长度：{fruit_lengths}")
    
    # 6.3 集合推导式
    print("\n6.3 集合推导式")
    
    # 基本集合推导式
    unique_lengths = {len(word) for word in words}
    print(f"单词长度集合：{unique_lengths}")
    
    # 6.4 生成器表达式
    print("\n6.4 生成器表达式")
    
    # 生成器表达式（惰性求值）
    squares_gen = (x**2 for x in range(10))
    print(f"生成器对象：{squares_gen}")
    print(f"生成器内容：{list(squares_gen)}")
    
    # 内存效率对比
    print("\n内存效率对比：")
    # 列表推导式 - 立即创建所有元素
    list_comp = [x**2 for x in range(1000000)]
    print(f"列表推导式创建完成，长度：{len(list_comp)}")
    
    # 生成器表达式 - 按需生成
    gen_exp = (x**2 for x in range(1000000))
    print(f"生成器表达式创建完成：{gen_exp}")
    
    print()

# ============================================================================
# 7. 实际应用示例
# ============================================================================

def practical_examples():
    """
    实际应用示例
    """
    print("7. 实际应用示例")
    print("=" * 40)
    
    # 7.1 数据处理
    print("7.1 数据处理 - 学生成绩统计")
    students_data = [
        {"name": "张三", "math": 85, "english": 90, "science": 78},
        {"name": "李四", "math": 92, "english": 88, "science": 95},
        {"name": "王五", "math": 76, "english": 82, "science": 80},
        {"name": "赵六", "math": 88, "english": 85, "science": 90}
    ]
    
    # 计算每个学生的总分和平均分
    for student in students_data:
        name = student["name"]
        math = student["math"]
        english = student["english"]
        science = student["science"]
        
        total = math + english + science
        average = total / 3
        
        print(f"{name}: 总分{total}, 平均分{average:.1f}")
    
    # 找出各科最高分
    subjects = ["math", "english", "science"]
    for subject in subjects:
        max_score = max(student[subject] for student in students_data)
        top_students = [s["name"] for s in students_data if s[subject] == max_score]
        print(f"{subject}最高分：{max_score}，学生：{', '.join(top_students)}")
    
    # 7.2 文本分析
    print("\n7.2 文本分析")
    text = "Python is a powerful programming language. Python is easy to learn."
    
    # 统计单词频率
    words = text.lower().replace('.', '').split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    print("单词频率：")
    for word, count in word_count.items():
        print(f"  {word}: {count}")
    
    # 7.3 数值计算
    print("\n7.3 数值计算 - 斐波那契数列")
    def fibonacci(n):
        """生成斐波那契数列的前n项"""
        fib_sequence = []
        a, b = 0, 1
        
        for _ in range(n):
            fib_sequence.append(a)
            a, b = b, a + b
        
        return fib_sequence
    
    fib_10 = fibonacci(10)
    print(f"斐波那契数列前10项：{fib_10}")
    
    # 7.4 模拟和游戏
    print("\n7.4 简单猜数字游戏模拟")
    def guess_number_simulation():
        """模拟猜数字游戏"""
        target = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print(f"目标数字：{target}（实际游戏中不显示）")
        
        # 模拟智能猜测策略（二分查找）
        low, high = 1, 100
        
        while attempts < max_attempts:
            attempts += 1
            guess = (low + high) // 2
            print(f"第{attempts}次猜测：{guess}")
            
            if guess == target:
                print(f"恭喜！用{attempts}次猜中了！")
                return True
            elif guess < target:
                print("太小了")
                low = guess + 1
            else:
                print("太大了")
                high = guess - 1
        
        print(f"游戏结束！目标数字是{target}")
        return False
    
    guess_number_simulation()
    
    print()

# ============================================================================
# 8. 性能优化示例
# ============================================================================

def performance_examples():
    """
    性能优化示例
    """
    print("8. 性能优化示例")
    print("=" * 40)
    
    # 8.1 避免重复计算
    print("8.1 避免重复计算")
    
    # 低效的方式
    def inefficient_way():
        data = list(range(1000))
        result = []
        for i in range(len(data)):
            if len(data) > 500:  # 重复计算len(data)
                result.append(data[i] * 2)
        return result
    
    # 高效的方式
    def efficient_way():
        data = list(range(1000))
        result = []
        data_length = len(data)  # 缓存长度
        for item in data:  # 直接遍历元素
            if data_length > 500:
                result.append(item * 2)
        return result
    
    # 最高效的方式（使用推导式）
    def most_efficient_way():
        data = list(range(1000))
        return [item * 2 for item in data] if len(data) > 500 else []
    
    # 简单性能测试
    import time
    
    start = time.time()
    result1 = inefficient_way()
    time1 = time.time() - start
    
    start = time.time()
    result2 = efficient_way()
    time2 = time.time() - start
    
    start = time.time()
    result3 = most_efficient_way()
    time3 = time.time() - start
    
    print(f"低效方式耗时：{time1:.6f}秒")
    print(f"高效方式耗时：{time2:.6f}秒")
    print(f"最高效方式耗时：{time3:.6f}秒")
    
    # 8.2 使用内置函数
    print("\n8.2 使用内置函数")
    
    numbers = list(range(1, 101))
    
    # 使用循环求和
    start = time.time()
    total1 = 0
    for num in numbers:
        total1 += num
    time1 = time.time() - start
    
    # 使用内置sum函数
    start = time.time()
    total2 = sum(numbers)
    time2 = time.time() - start
    
    print(f"循环求和：{total1}，耗时：{time1:.6f}秒")
    print(f"sum函数：{total2}，耗时：{time2:.6f}秒")
    
    # 8.3 使用any()和all()
    print("\n8.3 使用any()和all()")
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 检查是否有偶数
    has_even = any(x % 2 == 0 for x in data)
    print(f"是否有偶数：{has_even}")
    
    # 检查是否都是正数
    all_positive = all(x > 0 for x in data)
    print(f"是否都是正数：{all_positive}")
    
    print()

if __name__ == "__main__":
    print("Python控制结构示例")
    print("=" * 50)
    
    # 运行所有示例
    conditional_statements_examples()
    for_loop_examples()
    while_loop_examples()
    loop_control_examples()
    nested_structures_examples()
    comprehension_examples()
    practical_examples()
    performance_examples()
    
    print("\n学习要点总结：")
    print("- 条件语句用于根据条件执行不同的代码分支")
    print("- for循环适合遍历已知序列，while循环适合条件循环")
    print("- break和continue用于控制循环流程")
    print("- 推导式提供了简洁高效的数据处理方式")
    print("- 合理使用内置函数可以提高代码性能")
    print("- 避免不必要的重复计算和深层嵌套")