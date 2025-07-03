#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据结构 - 示例代码

本文件演示Python中各种数据结构的使用方法，包括列表、元组、字典、集合等。
"""

import time
import copy
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
import heapq
from typing import List, Dict, Set, Tuple, Any

# ============================================================================
# 1. 列表（List）示例
# ============================================================================

def list_examples():
    """
    列表示例
    """
    print("1. 列表（List）示例")
    print("=" * 40)
    
    # 1.1 创建列表
    print("1.1 创建列表")
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
    empty_list = []
    range_list = list(range(10))
    
    print(f"数字列表：{numbers}")
    print(f"混合列表：{mixed_list}")
    print(f"空列表：{empty_list}")
    print(f"范围列表：{range_list}")
    
    # 1.2 访问和切片
    print("\n1.2 访问和切片")
    print(f"第一个元素：{numbers[0]}")
    print(f"最后一个元素：{numbers[-1]}")
    print(f"切片[1:4]：{numbers[1:4]}")
    print(f"步长切片[::2]：{numbers[::2]}")
    print(f"反转[-1::-1]：{numbers[::-1]}")
    
    # 1.3 修改列表
    print("\n1.3 修改列表")
    fruits = ["苹果", "香蕉", "橙子"]
    print(f"原始列表：{fruits}")
    
    # 添加元素
    fruits.append("葡萄")  # 末尾添加
    print(f"append后：{fruits}")
    
    fruits.insert(1, "草莓")  # 指定位置插入
    print(f"insert后：{fruits}")
    
    fruits.extend(["芒果", "菠萝"])  # 扩展列表
    print(f"extend后：{fruits}")
    
    # 删除元素
    fruits.remove("香蕉")  # 删除指定值
    print(f"remove后：{fruits}")
    
    popped = fruits.pop()  # 删除并返回最后一个
    print(f"pop后：{fruits}，弹出的元素：{popped}")
    
    del fruits[0]  # 删除指定位置
    print(f"del后：{fruits}")
    
    # 1.4 列表方法
    print("\n1.4 列表方法")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"原始列表：{numbers}")
    print(f"长度：{len(numbers)}")
    print(f"最大值：{max(numbers)}")
    print(f"最小值：{min(numbers)}")
    print(f"求和：{sum(numbers)}")
    print(f"计数1的个数：{numbers.count(1)}")
    print(f"查找5的索引：{numbers.index(5)}")
    
    # 排序和反转
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    print(f"排序后：{numbers_copy}")
    
    numbers_copy.reverse()
    print(f"反转后：{numbers_copy}")
    
    # 1.5 列表推导式
    print("\n1.5 列表推导式")
    squares = [x**2 for x in range(10)]
    print(f"平方数：{squares}")
    
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"偶数平方：{even_squares}")
    
    matrix = [[i*j for j in range(3)] for i in range(3)]
    print(f"矩阵：{matrix}")
    
    print()

# ============================================================================
# 2. 元组（Tuple）示例
# ============================================================================

def tuple_examples():
    """
    元组示例
    """
    print("2. 元组（Tuple）示例")
    print("=" * 40)
    
    # 2.1 创建元组
    print("2.1 创建元组")
    coordinates = (3, 4)
    colors = ("红", "绿", "蓝")
    mixed_tuple = (1, "hello", 3.14, True)
    empty_tuple = ()
    single_tuple = (42,)  # 单元素元组需要逗号
    
    print(f"坐标：{coordinates}")
    print(f"颜色：{colors}")
    print(f"混合元组：{mixed_tuple}")
    print(f"空元组：{empty_tuple}")
    print(f"单元素元组：{single_tuple}")
    
    # 2.2 访问元组
    print("\n2.2 访问元组")
    print(f"第一个坐标：{coordinates[0]}")
    print(f"第二个坐标：{coordinates[1]}")
    print(f"颜色切片[1:]：{colors[1:]}")
    
    # 2.3 元组解包
    print("\n2.3 元组解包")
    x, y = coordinates
    print(f"x = {x}, y = {y}")
    
    # 多重赋值
    a, b, c = colors
    print(f"a = {a}, b = {b}, c = {c}")
    
    # 交换变量
    a, b = b, a
    print(f"交换后：a = {a}, b = {b}")
    
    # 2.4 命名元组
    print("\n2.4 命名元组")
    Point = namedtuple('Point', ['x', 'y'])
    Student = namedtuple('Student', ['name', 'age', 'grade'])
    
    p1 = Point(1, 2)
    p2 = Point(x=3, y=4)
    student = Student("张三", 20, "A")
    
    print(f"点1：{p1}")
    print(f"点2：{p2}")
    print(f"学生：{student}")
    print(f"学生姓名：{student.name}")
    print(f"点1的x坐标：{p1.x}")
    
    # 2.5 元组的不可变性
    print("\n2.5 元组的不可变性")
    try:
        coordinates[0] = 5  # 这会引发错误
    except TypeError as e:
        print(f"错误：{e}")
    
    # 但包含可变对象的元组，其可变对象可以修改
    tuple_with_list = ([1, 2, 3], "hello")
    print(f"包含列表的元组：{tuple_with_list}")
    tuple_with_list[0].append(4)
    print(f"修改列表后：{tuple_with_list}")
    
    print()

# ============================================================================
# 3. 字典（Dictionary）示例
# ============================================================================

def dictionary_examples():
    """
    字典示例
    """
    print("3. 字典（Dictionary）示例")
    print("=" * 40)
    
    # 3.1 创建字典
    print("3.1 创建字典")
    student = {"name": "张三", "age": 20, "major": "计算机科学"}
    empty_dict = {}
    dict_from_tuples = dict([("a", 1), ("b", 2), ("c", 3)])
    dict_comprehension = {x: x**2 for x in range(5)}
    
    print(f"学生信息：{student}")
    print(f"空字典：{empty_dict}")
    print(f"从元组创建：{dict_from_tuples}")
    print(f"字典推导式：{dict_comprehension}")
    
    # 3.2 访问和修改
    print("\n3.2 访问和修改")
    print(f"学生姓名：{student['name']}")
    print(f"学生年龄：{student.get('age', '未知')}")
    print(f"学生邮箱：{student.get('email', '未提供')}")
    
    # 修改和添加
    student["age"] = 21
    student["email"] = "zhangsan@example.com"
    print(f"修改后：{student}")
    
    # 3.3 字典方法
    print("\n3.3 字典方法")
    print(f"所有键：{list(student.keys())}")
    print(f"所有值：{list(student.values())}")
    print(f"所有项：{list(student.items())}")
    
    # setdefault方法
    student.setdefault("grade", "A")
    print(f"setdefault后：{student}")
    
    # update方法
    additional_info = {"phone": "123-456-7890", "city": "北京"}
    student.update(additional_info)
    print(f"update后：{student}")
    
    # 3.4 遍历字典
    print("\n3.4 遍历字典")
    print("遍历键：")
    for key in student:
        print(f"  {key}")
    
    print("遍历值：")
    for value in student.values():
        print(f"  {value}")
    
    print("遍历键值对：")
    for key, value in student.items():
        print(f"  {key}: {value}")
    
    # 3.5 字典推导式
    print("\n3.5 字典推导式")
    word_lengths = {word: len(word) for word in ["python", "java", "go"]}
    print(f"单词长度：{word_lengths}")
    
    # 过滤字典
    long_words = {k: v for k, v in word_lengths.items() if v > 3}
    print(f"长单词：{long_words}")
    
    # 3.6 嵌套字典
    print("\n3.6 嵌套字典")
    students = {
        "001": {"name": "张三", "scores": {"math": 85, "english": 90}},
        "002": {"name": "李四", "scores": {"math": 92, "english": 88}}
    }
    
    print(f"学生数据：{students}")
    print(f"张三的数学成绩：{students['001']['scores']['math']}")
    
    print()

# ============================================================================
# 4. 集合（Set）示例
# ============================================================================

def set_examples():
    """
    集合示例
    """
    print("4. 集合（Set）示例")
    print("=" * 40)
    
    # 4.1 创建集合
    print("4.1 创建集合")
    numbers = {1, 2, 3, 4, 5}
    empty_set = set()
    from_list = set([1, 2, 2, 3, 3, 4])  # 自动去重
    from_string = set("hello")  # 字符集合
    
    print(f"数字集合：{numbers}")
    print(f"空集合：{empty_set}")
    print(f"从列表创建（去重）：{from_list}")
    print(f"从字符串创建：{from_string}")
    
    # 4.2 集合操作
    print("\n4.2 集合操作")
    fruits = {"苹果", "香蕉", "橙子"}
    print(f"原始集合：{fruits}")
    
    # 添加元素
    fruits.add("葡萄")
    print(f"add后：{fruits}")
    
    fruits.update(["芒果", "菠萝"])
    print(f"update后：{fruits}")
    
    # 删除元素
    fruits.remove("香蕉")  # 元素不存在会报错
    print(f"remove后：{fruits}")
    
    fruits.discard("不存在的水果")  # 元素不存在不报错
    print(f"discard后：{fruits}")
    
    # 4.3 集合运算
    print("\n4.3 集合运算")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"集合1：{set1}")
    print(f"集合2：{set2}")
    
    # 并集
    union = set1 | set2
    union_method = set1.union(set2)
    print(f"并集（|）：{union}")
    print(f"并集（union）：{union_method}")
    
    # 交集
    intersection = set1 & set2
    intersection_method = set1.intersection(set2)
    print(f"交集（&）：{intersection}")
    print(f"交集（intersection）：{intersection_method}")
    
    # 差集
    difference = set1 - set2
    difference_method = set1.difference(set2)
    print(f"差集（-）：{difference}")
    print(f"差集（difference）：{difference_method}")
    
    # 对称差集
    sym_diff = set1 ^ set2
    sym_diff_method = set1.symmetric_difference(set2)
    print(f"对称差集（^）：{sym_diff}")
    print(f"对称差集（symmetric_difference）：{sym_diff_method}")
    
    # 4.4 集合关系
    print("\n4.4 集合关系")
    small_set = {1, 2}
    large_set = {1, 2, 3, 4, 5}
    
    print(f"小集合：{small_set}")
    print(f"大集合：{large_set}")
    print(f"小集合是大集合的子集：{small_set.issubset(large_set)}")
    print(f"大集合是小集合的超集：{large_set.issuperset(small_set)}")
    print(f"两集合不相交：{small_set.isdisjoint({6, 7, 8})}")
    
    # 4.5 集合推导式
    print("\n4.5 集合推导式")
    squares = {x**2 for x in range(10)}
    print(f"平方数集合：{squares}")
    
    vowels = {char for char in "hello world" if char in "aeiou"}
    print(f"元音字母：{vowels}")
    
    print()

# ============================================================================
# 5. 字符串（String）高级操作示例
# ============================================================================

def string_advanced_examples():
    """
    字符串高级操作示例
    """
    print("5. 字符串高级操作示例")
    print("=" * 40)
    
    # 5.1 字符串作为序列
    print("5.1 字符串作为序列")
    text = "Python编程"
    print(f"字符串：{text}")
    print(f"长度：{len(text)}")
    print(f"第一个字符：{text[0]}")
    print(f"最后一个字符：{text[-1]}")
    print(f"切片[0:6]：{text[0:6]}")
    
    # 5.2 字符串方法链
    print("\n5.2 字符串方法链")
    messy_text = "  Hello, World!  "
    cleaned = messy_text.strip().lower().replace(",", "")
    print(f"原始：'{messy_text}'")
    print(f"清理后：'{cleaned}'")
    
    # 5.3 字符串格式化高级用法
    print("\n5.3 字符串格式化高级用法")
    name = "张三"
    age = 25
    score = 88.567
    
    # f-string高级格式化
    formatted = f"姓名：{name:>10}，年龄：{age:0>3}，分数：{score:.2f}"
    print(f"格式化：{formatted}")
    
    # 格式化表格
    print("\n学生成绩表：")
    students = [("张三", 85), ("李四", 92), ("王五", 78)]
    print(f"{'姓名':^6} {'成绩':^6}")
    print("-" * 15)
    for name, score in students:
        print(f"{name:^6} {score:^6}")
    
    # 5.4 字符串与其他数据结构
    print("\n5.4 字符串与其他数据结构")
    
    # 字符串转列表
    char_list = list("hello")
    print(f"字符列表：{char_list}")
    
    # 字符串转集合（去重）
    char_set = set("hello")
    print(f"字符集合：{char_set}")
    
    # 统计字符频率
    char_count = {char: "hello".count(char) for char in set("hello")}
    print(f"字符频率：{char_count}")
    
    print()

# ============================================================================
# 6. 高级数据结构示例
# ============================================================================

def advanced_data_structures():
    """
    高级数据结构示例
    """
    print("6. 高级数据结构示例")
    print("=" * 40)
    
    # 6.1 Counter（计数器）
    print("6.1 Counter（计数器）")
    from collections import Counter
    
    # 统计字符频率
    text = "hello world"
    char_counter = Counter(text)
    print(f"字符计数：{char_counter}")
    print(f"最常见的3个字符：{char_counter.most_common(3)}")
    
    # 统计单词频率
    words = ["python", "java", "python", "go", "python", "java"]
    word_counter = Counter(words)
    print(f"单词计数：{word_counter}")
    
    # Counter运算
    counter1 = Counter([1, 2, 3, 1, 2])
    counter2 = Counter([1, 2, 2, 3, 4])
    print(f"计数器1：{counter1}")
    print(f"计数器2：{counter2}")
    print(f"相加：{counter1 + counter2}")
    print(f"相减：{counter1 - counter2}")
    print(f"交集：{counter1 & counter2}")
    print(f"并集：{counter1 | counter2}")
    
    # 6.2 defaultdict（默认字典）
    print("\n6.2 defaultdict（默认字典）")
    from collections import defaultdict
    
    # 分组
    dd = defaultdict(list)
    students = [("张三", "计算机"), ("李四", "数学"), ("王五", "计算机"), ("赵六", "数学")]
    
    for name, major in students:
        dd[major].append(name)
    
    print(f"按专业分组：{dict(dd)}")
    
    # 计数
    count_dd = defaultdict(int)
    for char in "hello world":
        count_dd[char] += 1
    print(f"字符计数：{dict(count_dd)}")
    
    # 6.3 OrderedDict（有序字典）
    print("\n6.3 OrderedDict（有序字典）")
    from collections import OrderedDict
    
    # 注意：Python 3.7+普通字典也保持插入顺序
    od = OrderedDict()
    od['first'] = 1
    od['second'] = 2
    od['third'] = 3
    
    print(f"有序字典：{od}")
    
    # 移动到末尾
    od.move_to_end('first')
    print(f"移动first到末尾：{od}")
    
    # 6.4 deque（双端队列）
    print("\n6.4 deque（双端队列）")
    from collections import deque
    
    dq = deque([1, 2, 3])
    print(f"初始队列：{dq}")
    
    # 两端操作
    dq.appendleft(0)
    dq.append(4)
    print(f"两端添加后：{dq}")
    
    left = dq.popleft()
    right = dq.pop()
    print(f"两端删除后：{dq}，左：{left}，右：{right}")
    
    # 旋转
    dq.rotate(1)  # 向右旋转
    print(f"向右旋转1位：{dq}")
    
    dq.rotate(-2)  # 向左旋转
    print(f"向左旋转2位：{dq}")
    
    # 6.5 heapq（堆）
    print("\n6.5 heapq（堆）")
    import heapq
    
    # 创建堆
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    heapq.heapify(numbers)
    print(f"堆化后：{numbers}")
    
    # 堆操作
    heapq.heappush(numbers, 0)
    print(f"推入0后：{numbers}")
    
    smallest = heapq.heappop(numbers)
    print(f"弹出最小值{smallest}后：{numbers}")
    
    # 获取最大/最小的n个元素
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    largest_3 = heapq.nlargest(3, data)
    smallest_3 = heapq.nsmallest(3, data)
    print(f"原数据：{data}")
    print(f"最大的3个：{largest_3}")
    print(f"最小的3个：{smallest_3}")
    
    print()

# ============================================================================
# 7. 性能比较示例
# ============================================================================

def performance_comparison():
    """
    性能比较示例
    """
    print("7. 性能比较示例")
    print("=" * 40)
    
    # 7.1 成员测试性能
    print("7.1 成员测试性能")
    
    # 准备数据
    size = 10000
    test_list = list(range(size))
    test_set = set(range(size))
    test_dict = {i: i for i in range(size)}
    target = size - 1  # 最坏情况
    
    # 列表成员测试
    start_time = time.time()
    result = target in test_list
    list_time = time.time() - start_time
    
    # 集合成员测试
    start_time = time.time()
    result = target in test_set
    set_time = time.time() - start_time
    
    # 字典键测试
    start_time = time.time()
    result = target in test_dict
    dict_time = time.time() - start_time
    
    print(f"数据规模：{size}")
    print(f"列表成员测试：{list_time:.6f}秒")
    print(f"集合成员测试：{set_time:.6f}秒")
    print(f"字典键测试：{dict_time:.6f}秒")
    print(f"集合比列表快：{list_time/set_time:.1f}倍")
    
    # 7.2 字符串拼接性能
    print("\n7.2 字符串拼接性能")
    
    words = ["word"] * 1000
    
    # 使用+操作符（低效）
    start_time = time.time()
    result1 = ""
    for word in words:
        result1 += word
    plus_time = time.time() - start_time
    
    # 使用join方法（高效）
    start_time = time.time()
    result2 = "".join(words)
    join_time = time.time() - start_time
    
    print(f"单词数量：{len(words)}")
    print(f"+操作符拼接：{plus_time:.6f}秒")
    print(f"join方法拼接：{join_time:.6f}秒")
    print(f"join比+快：{plus_time/join_time:.1f}倍")
    
    # 7.3 列表vs元组创建性能
    print("\n7.3 列表vs元组创建性能")
    
    n = 100000
    
    # 列表创建
    start_time = time.time()
    for _ in range(n):
        lst = [1, 2, 3, 4, 5]
    list_create_time = time.time() - start_time
    
    # 元组创建
    start_time = time.time()
    for _ in range(n):
        tpl = (1, 2, 3, 4, 5)
    tuple_create_time = time.time() - start_time
    
    print(f"创建次数：{n}")
    print(f"列表创建：{list_create_time:.6f}秒")
    print(f"元组创建：{tuple_create_time:.6f}秒")
    print(f"元组比列表快：{list_create_time/tuple_create_time:.1f}倍")
    
    print()

# ============================================================================
# 8. 实际应用示例
# ============================================================================

def practical_applications():
    """
    实际应用示例
    """
    print("8. 实际应用示例")
    print("=" * 40)
    
    # 8.1 数据分析
    print("8.1 数据分析 - 学生成绩统计")
    
    # 学生成绩数据
    students_scores = [
        {"name": "张三", "math": 85, "english": 90, "science": 78},
        {"name": "李四", "math": 92, "english": 88, "science": 95},
        {"name": "王五", "math": 76, "english": 82, "science": 80},
        {"name": "赵六", "math": 88, "english": 85, "science": 90},
        {"name": "钱七", "math": 95, "english": 92, "science": 89}
    ]
    
    # 使用不同数据结构进行分析
    
    # 计算平均分（使用列表推导式）
    averages = [(s["name"], (s["math"] + s["english"] + s["science"]) / 3) 
                for s in students_scores]
    print("学生平均分：")
    for name, avg in averages:
        print(f"  {name}: {avg:.1f}")
    
    # 找出各科最高分（使用字典）
    subjects = ["math", "english", "science"]
    subject_names = {"math": "数学", "english": "英语", "science": "科学"}
    
    print("\n各科最高分：")
    for subject in subjects:
        scores = [(s["name"], s[subject]) for s in students_scores]
        top_student = max(scores, key=lambda x: x[1])
        print(f"  {subject_names[subject]}：{top_student[0]} ({top_student[1]}分)")
    
    # 统计分数分布（使用Counter）
    all_scores = []
    for student in students_scores:
        all_scores.extend([student["math"], student["english"], student["science"]])
    
    score_ranges = Counter()
    for score in all_scores:
        if score >= 90:
            score_ranges["优秀"] += 1
        elif score >= 80:
            score_ranges["良好"] += 1
        elif score >= 70:
            score_ranges["中等"] += 1
        else:
            score_ranges["需要提高"] += 1
    
    print(f"\n分数分布：{dict(score_ranges)}")
    
    # 8.2 文本处理
    print("\n8.2 文本处理 - 词频分析")
    
    text = """Python is a powerful programming language. 
    Python is easy to learn and use. Many developers 
    choose Python for web development, data analysis, 
    and artificial intelligence."""
    
    # 清理文本并分词
    import string
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()
    
    # 使用Counter统计词频
    word_freq = Counter(words)
    print(f"总词数：{len(words)}")
    print(f"唯一词数：{len(word_freq)}")
    print(f"最常用的5个词：{word_freq.most_common(5)}")
    
    # 使用集合找出唯一词
    unique_words = set(words)
    print(f"唯一词汇：{sorted(unique_words)}")
    
    # 8.3 数据去重和合并
    print("\n8.3 数据去重和合并")
    
    # 多个数据源
    source1 = ["apple", "banana", "orange", "apple"]
    source2 = ["banana", "grape", "kiwi", "orange"]
    source3 = ["mango", "apple", "grape", "pear"]
    
    # 使用集合去重和合并
    all_fruits = set(source1) | set(source2) | set(source3)
    print(f"所有水果（去重）：{sorted(all_fruits)}")
    
    # 找出共同的水果
    common_fruits = set(source1) & set(source2) & set(source3)
    print(f"共同水果：{common_fruits}")
    
    # 使用字典统计来源
    fruit_sources = defaultdict(set)
    for i, source in enumerate([source1, source2, source3], 1):
        for fruit in source:
            fruit_sources[fruit].add(f"源{i}")
    
    print("水果来源：")
    for fruit, sources in sorted(fruit_sources.items()):
        print(f"  {fruit}: {', '.join(sorted(sources))}")
    
    print()

if __name__ == "__main__":
    print("Python数据结构示例")
    print("=" * 50)
    
    # 运行所有示例
    list_examples()
    tuple_examples()
    dictionary_examples()
    set_examples()
    string_advanced_examples()
    advanced_data_structures()
    performance_comparison()
    practical_applications()
    
    print("\n学习要点总结：")
    print("- 列表：有序、可变，适合需要索引和修改的场景")
    print("- 元组：有序、不可变，适合固定数据和函数返回值")
    print("- 字典：键值对存储，适合快速查找和数据关联")
    print("- 集合：无序、唯一，适合去重和集合运算")
    print("- 字符串：不可变序列，丰富的文本处理方法")
    print("- 高级数据结构：Counter、defaultdict、deque等解决特定问题")
    print("- 性能考虑：根据使用场景选择合适的数据结构")
    print("- 实际应用：数据分析、文本处理、数据去重等")