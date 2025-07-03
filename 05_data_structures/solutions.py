#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据结构 - 练习题参考答案

本文件包含数据结构练习题的详细解答和说明。
"""

import time
import re
import math
from collections import Counter, defaultdict, OrderedDict, deque, namedtuple
import heapq
from typing import List, Dict, Set, Tuple, Any, Optional

# ============================================================================
# 练习1：列表操作基础 - 参考答案
# ============================================================================

def solution_1_list_basics():
    """
    练习1：列表操作基础 - 参考答案
    """
    print("练习1：列表操作基础 - 参考答案")
    
    # 1. 创建一个包含1-10的列表
    numbers = list(range(1, 11))
    print(f"1. 创建列表：{numbers}")
    
    # 2. 在列表末尾添加数字11
    numbers.append(11)
    print(f"2. 添加11后：{numbers}")
    
    # 3. 在索引2的位置插入数字99
    numbers.insert(2, 99)
    print(f"3. 插入99后：{numbers}")
    
    # 4. 删除数字5
    numbers.remove(5)
    print(f"4. 删除5后：{numbers}")
    
    # 5. 获取列表的长度
    length = len(numbers)
    print(f"5. 列表长度：{length}")
    
    # 6. 计算列表所有元素的和
    total = sum(numbers)
    print(f"6. 元素总和：{total}")
    
    # 7. 找出列表中的最大值和最小值
    max_val = max(numbers)
    min_val = min(numbers)
    print(f"7. 最大值：{max_val}，最小值：{min_val}")
    
    # 8. 将列表反转
    numbers.reverse()
    print(f"8. 反转后：{numbers}")
    
    print()

# ============================================================================
# 练习2：列表推导式 - 参考答案
# ============================================================================

def solution_2_list_comprehension():
    """
    练习2：列表推导式 - 参考答案
    """
    print("练习2：列表推导式 - 参考答案")
    
    # 1. 创建一个包含1-20中所有偶数的列表
    even_numbers = [x for x in range(1, 21) if x % 2 == 0]
    print(f"1. 1-20中的偶数：{even_numbers}")
    
    # 2. 创建一个包含1-10中每个数字平方的列表
    squares = [x**2 for x in range(1, 11)]
    print(f"2. 1-10的平方：{squares}")
    
    # 3. 从字符串"hello world"中提取所有元音字母
    vowels = [char for char in "hello world" if char in "aeiou"]
    print(f"3. 元音字母：{vowels}")
    
    # 4. 创建一个3x3的矩阵，元素为行号*列号
    matrix = [[i * j for j in range(3)] for i in range(3)]
    print(f"4. 3x3矩阵：{matrix}")
    
    # 5. 从列表[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]中筛选出大于5的偶数
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered = [x for x in numbers if x > 5 and x % 2 == 0]
    print(f"5. 大于5的偶数：{filtered}")
    
    print()

# ============================================================================
# 练习3：元组操作 - 参考答案
# ============================================================================

def solution_3_tuple_operations():
    """
    练习3：元组操作 - 参考答案
    """
    print("练习3：元组操作 - 参考答案")
    
    # 1. 创建一个包含学生信息的元组
    student = ("张三", 20, "计算机科学")
    print(f"1. 学生信息：{student}")
    
    # 2. 使用元组解包获取姓名、年龄和专业
    name, age, major = student
    print(f"2. 姓名：{name}，年龄：{age}，专业：{major}")
    
    # 3. 创建一个包含多个坐标点的元组列表
    points = [(0, 0), (1, 1), (2, 4), (3, 9)]
    print(f"3. 坐标点：{points}")
    
    # 4. 计算所有点到原点的距离
    distances = [math.sqrt(x**2 + y**2) for x, y in points]
    print(f"4. 到原点距离：{[f'{d:.2f}' for d in distances]}")
    
    # 5. 使用命名元组创建一个Point类
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    p3 = Point(1, 1)
    print(f"5. 命名元组点：{p1}, {p2}, {p3}")
    
    # 6. 计算它们之间的距离
    def distance(point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
    
    dist_p1_p2 = distance(p1, p2)
    dist_p2_p3 = distance(p2, p3)
    print(f"6. p1到p2距离：{dist_p1_p2:.2f}，p2到p3距离：{dist_p2_p3:.2f}")
    
    print()

# ============================================================================
# 练习4：字典操作基础 - 参考答案
# ============================================================================

def solution_4_dict_basics():
    """
    练习4：字典操作基础 - 参考答案
    """
    print("练习4：字典操作基础 - 参考答案")
    
    # 1. 创建一个学生成绩字典
    scores = {"数学": 85, "英语": 90, "科学": 78}
    print(f"1. 初始成绩：{scores}")
    
    # 2. 添加一门新课程"历史"，成绩为88
    scores["历史"] = 88
    print(f"2. 添加历史后：{scores}")
    
    # 3. 修改数学成绩为92
    scores["数学"] = 92
    print(f"3. 修改数学成绩后：{scores}")
    
    # 4. 删除科学这门课程
    del scores["科学"]
    print(f"4. 删除科学后：{scores}")
    
    # 5. 检查是否包含"物理"这门课程
    has_physics = "物理" in scores
    print(f"5. 是否包含物理：{has_physics}")
    
    # 6. 获取所有课程名称
    subjects = list(scores.keys())
    print(f"6. 所有课程：{subjects}")
    
    # 7. 获取所有成绩
    grades = list(scores.values())
    print(f"7. 所有成绩：{grades}")
    
    # 8. 计算平均成绩
    average = sum(scores.values()) / len(scores)
    print(f"8. 平均成绩：{average:.2f}")
    
    print()

# ============================================================================
# 练习5：字典推导式和嵌套 - 参考答案
# ============================================================================

def solution_5_dict_advanced():
    """
    练习5：字典推导式和嵌套 - 参考答案
    """
    print("练习5：字典推导式和嵌套 - 参考答案")
    
    # 1. 使用字典推导式创建一个字典，键为1-5，值为键的平方
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"1. 平方字典：{squares_dict}")
    
    # 2. 从列表创建字典，键为水果名，值为长度
    fruits = ["apple", "banana", "cherry"]
    fruit_lengths = {fruit: len(fruit) for fruit in fruits}
    print(f"2. 水果长度：{fruit_lengths}")
    
    # 3. 创建嵌套字典表示班级信息
    class_info = {
        "学生1": {"姓名": "张三", "成绩": {"数学": 85, "英语": 90}},
        "学生2": {"姓名": "李四", "成绩": {"数学": 92, "英语": 88}}
    }
    print(f"3. 班级信息：{class_info}")
    
    # 4. 计算每个学生的平均成绩
    print("4. 学生平均成绩：")
    for student_id, info in class_info.items():
        scores = info["成绩"]
        average = sum(scores.values()) / len(scores)
        print(f"   {info['姓名']}：{average:.1f}")
    
    # 5. 找出数学成绩最高的学生
    best_math_student = max(class_info.items(), 
                           key=lambda x: x[1]["成绩"]["数学"])
    print(f"5. 数学成绩最高：{best_math_student[1]['姓名']} ({best_math_student[1]['成绩']['数学']}分)")
    
    print()

# ============================================================================
# 练习6：集合操作 - 参考答案
# ============================================================================

def solution_6_set_operations():
    """
    练习6：集合操作 - 参考答案
    """
    print("练习6：集合操作 - 参考答案")
    
    # 1. 创建两个集合
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print(f"1. 集合1：{set1}，集合2：{set2}")
    
    # 2. 计算两个集合的并集
    union_set = set1 | set2
    print(f"2. 并集：{union_set}")
    
    # 3. 计算两个集合的交集
    intersection_set = set1 & set2
    print(f"3. 交集：{intersection_set}")
    
    # 4. 计算set1相对于set2的差集
    difference_set = set1 - set2
    print(f"4. 差集（set1-set2）：{difference_set}")
    
    # 5. 计算两个集合的对称差集
    symmetric_diff = set1 ^ set2
    print(f"5. 对称差集：{symmetric_diff}")
    
    # 6. 判断{1, 2}是否是set1的子集
    is_subset = {1, 2}.issubset(set1)
    print(f"6. {{1, 2}}是set1的子集：{is_subset}")
    
    # 7. 从字符串"programming"中创建一个字符集合
    char_set = set("programming")
    print(f"7. 'programming'的字符集合：{char_set}")
    
    # 8. 统计字符串"hello world"中有多少个不同的字符
    unique_chars = len(set("hello world"))
    print(f"8. 'hello world'中不同字符数：{unique_chars}")
    
    print()

# ============================================================================
# 练习7：数据结构转换 - 参考答案
# ============================================================================

def solution_7_data_conversion():
    """
    练习7：数据结构转换 - 参考答案
    """
    print("练习7：数据结构转换 - 参考答案")
    
    # 1. 将字符串"1,2,3,4,5"转换为整数列表
    str_numbers = "1,2,3,4,5"
    int_list = [int(x) for x in str_numbers.split(",")]
    print(f"1. 字符串转整数列表：{int_list}")
    
    # 2. 将列表["a", "b", "c"]转换为字典，键为索引，值为字母
    letters = ["a", "b", "c"]
    index_dict = {i: letter for i, letter in enumerate(letters)}
    print(f"2. 列表转索引字典：{index_dict}")
    
    # 3. 将字典转换为元组列表
    dict_data = {"a": 1, "b": 2, "c": 3}
    tuple_list = list(dict_data.items())
    print(f"3. 字典转元组列表：{tuple_list}")
    
    # 4. 从列表创建去重的有序列表
    numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4]
    unique_sorted = sorted(set(numbers_with_duplicates))
    print(f"4. 去重排序：{unique_sorted}")
    
    # 5. 将嵌套列表展平为一维列表
    nested_list = [[1, 2], [3, 4], [5, 6]]
    flattened = [item for sublist in nested_list for item in sublist]
    print(f"5. 展平列表：{flattened}")
    
    print()

# ============================================================================
# 练习8：文本分析 - 参考答案
# ============================================================================

def solution_8_text_analysis():
    """
    练习8：文本分析 - 参考答案
    """
    print("练习8：文本分析 - 参考答案")
    
    text = """Python is a powerful programming language. Python is easy to learn.
    Many developers choose Python for data analysis and web development."""
    
    # 清理文本并分词
    import string
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()
    
    # 1. 统计文本中每个单词的出现次数
    word_count = Counter(words)
    print(f"1. 单词计数：{dict(word_count)}")
    
    # 2. 找出出现次数最多的3个单词
    most_common = word_count.most_common(3)
    print(f"2. 最常用的3个词：{most_common}")
    
    # 3. 统计文本中不同单词的数量
    unique_words_count = len(word_count)
    print(f"3. 不同单词数量：{unique_words_count}")
    
    # 4. 找出长度大于5的所有单词
    long_words = [word for word in set(words) if len(word) > 5]
    print(f"4. 长度大于5的单词：{sorted(long_words)}")
    
    # 5. 计算文本中"Python"出现的次数
    python_count = word_count['python']
    print(f"5. 'Python'出现次数：{python_count}")
    
    # 6. 将所有单词按字母顺序排序（去重）
    sorted_unique_words = sorted(set(words))
    print(f"6. 按字母排序的唯一单词：{sorted_unique_words}")
    
    print()

# ============================================================================
# 练习9：学生管理系统 - 参考答案
# ============================================================================

def solution_9_student_management():
    """
    练习9：学生管理系统 - 参考答案
    """
    print("练习9：学生管理系统 - 参考答案")
    
    class StudentManager:
        def __init__(self):
            self.students = {}
        
        def add_student(self, student_id, name, age, major, scores):
            """添加新学生"""
            self.students[student_id] = {
                "姓名": name,
                "年龄": age,
                "专业": major,
                "成绩": scores
            }
            print(f"添加学生：{name}")
        
        def remove_student(self, student_id):
            """删除学生"""
            if student_id in self.students:
                name = self.students[student_id]["姓名"]
                del self.students[student_id]
                print(f"删除学生：{name}")
            else:
                print(f"学号{student_id}不存在")
        
        def update_student(self, student_id, **kwargs):
            """修改学生信息"""
            if student_id in self.students:
                for key, value in kwargs.items():
                    if key in self.students[student_id]:
                        self.students[student_id][key] = value
                print(f"更新学生{student_id}信息")
            else:
                print(f"学号{student_id}不存在")
        
        def find_student(self, **kwargs):
            """查找学生"""
            results = []
            for student_id, info in self.students.items():
                match = True
                for key, value in kwargs.items():
                    if key == "学号":
                        if student_id != value:
                            match = False
                            break
                    elif info.get(key) != value:
                        match = False
                        break
                if match:
                    results.append((student_id, info))
            return results
        
        def calculate_average(self, student_id):
            """计算学生平均成绩"""
            if student_id in self.students:
                scores = self.students[student_id]["成绩"]
                return sum(scores.values()) / len(scores)
            return None
        
        def sort_by_average(self):
            """按平均成绩排序"""
            student_averages = []
            for student_id, info in self.students.items():
                avg = self.calculate_average(student_id)
                student_averages.append((student_id, info["姓名"], avg))
            return sorted(student_averages, key=lambda x: x[2], reverse=True)
        
        def group_by_major(self):
            """按专业分组"""
            groups = defaultdict(list)
            for student_id, info in self.students.items():
                groups[info["专业"]].append((student_id, info["姓名"]))
            return dict(groups)
        
        def count_by_major(self):
            """统计各专业人数"""
            major_count = Counter()
            for info in self.students.values():
                major_count[info["专业"]] += 1
            return dict(major_count)
    
    # 测试学生管理系统
    sm = StudentManager()
    
    # 添加学生
    sm.add_student("001", "张三", 20, "计算机科学", {"数学": 85, "英语": 90, "编程": 95})
    sm.add_student("002", "李四", 21, "数学", {"数学": 92, "英语": 88, "统计学": 90})
    sm.add_student("003", "王五", 19, "计算机科学", {"数学": 78, "英语": 85, "编程": 88})
    
    # 查找学生
    print("\n查找计算机科学专业的学生：")
    cs_students = sm.find_student(专业="计算机科学")
    for student_id, info in cs_students:
        print(f"  {student_id}: {info['姓名']}")
    
    # 按平均成绩排序
    print("\n按平均成绩排序：")
    sorted_students = sm.sort_by_average()
    for student_id, name, avg in sorted_students:
        print(f"  {name}: {avg:.1f}")
    
    # 按专业分组
    print("\n按专业分组：")
    groups = sm.group_by_major()
    for major, students in groups.items():
        print(f"  {major}: {[name for _, name in students]}")
    
    # 统计各专业人数
    print("\n各专业人数：")
    major_counts = sm.count_by_major()
    for major, count in major_counts.items():
        print(f"  {major}: {count}人")
    
    print()

# ============================================================================
# 练习10：数据统计和分析 - 参考答案
# ============================================================================

def solution_10_data_analysis():
    """
    练习10：数据统计和分析 - 参考答案
    """
    print("练习10：数据统计和分析 - 参考答案")
    
    sales_data = [
        {"产品": "笔记本电脑", "销量": 50, "单价": 5000, "月份": "1月"},
        {"产品": "手机", "销量": 120, "单价": 3000, "月份": "1月"},
        {"产品": "平板电脑", "销量": 80, "单价": 2000, "月份": "1月"},
        {"产品": "笔记本电脑", "销量": 60, "单价": 5000, "月份": "2月"},
        {"产品": "手机", "销量": 150, "单价": 3000, "月份": "2月"},
        {"产品": "平板电脑", "销量": 90, "单价": 2000, "月份": "2月"}
    ]
    
    # 1. 计算每个产品的总销量
    product_sales = defaultdict(int)
    for item in sales_data:
        product_sales[item["产品"]] += item["销量"]
    print(f"1. 每个产品总销量：{dict(product_sales)}")
    
    # 2. 计算每个产品的总销售额
    product_revenue = defaultdict(int)
    for item in sales_data:
        product_revenue[item["产品"]] += item["销量"] * item["单价"]
    print(f"2. 每个产品总销售额：{dict(product_revenue)}")
    
    # 3. 找出销量最高的产品
    best_selling_product = max(product_sales.items(), key=lambda x: x[1])
    print(f"3. 销量最高产品：{best_selling_product[0]} ({best_selling_product[1]}台)")
    
    # 4. 计算每个月的总销售额
    monthly_revenue = defaultdict(int)
    for item in sales_data:
        monthly_revenue[item["月份"]] += item["销量"] * item["单价"]
    print(f"4. 每月总销售额：{dict(monthly_revenue)}")
    
    # 5. 找出销售额最高的月份
    best_month = max(monthly_revenue.items(), key=lambda x: x[1])
    print(f"5. 销售额最高月份：{best_month[0]} ({best_month[1]}元)")
    
    # 6. 按产品分组，显示每个产品在不同月份的销量
    print("6. 产品月度销量：")
    product_monthly = defaultdict(dict)
    for item in sales_data:
        product_monthly[item["产品"]][item["月份"]] = item["销量"]
    for product, monthly_data in product_monthly.items():
        print(f"   {product}: {monthly_data}")
    
    # 7. 计算平均单价
    unique_products = {}
    for item in sales_data:
        unique_products[item["产品"]] = item["单价"]
    average_price = sum(unique_products.values()) / len(unique_products)
    print(f"7. 平均单价：{average_price:.2f}元")
    
    # 8. 找出单价最高和最低的产品
    highest_price_product = max(unique_products.items(), key=lambda x: x[1])
    lowest_price_product = min(unique_products.items(), key=lambda x: x[1])
    print(f"8. 单价最高：{highest_price_product[0]} ({highest_price_product[1]}元)")
    print(f"   单价最低：{lowest_price_product[0]} ({lowest_price_product[1]}元)")
    
    print()

# ============================================================================
# 练习11：高级数据结构应用 - 参考答案
# ============================================================================

def solution_11_advanced_structures():
    """
    练习11：高级数据结构应用 - 参考答案
    """
    print("练习11：高级数据结构应用 - 参考答案")
    
    # 1. 使用Counter统计字符频率
    text = "hello world python programming"
    char_freq = Counter(text)
    print(f"1. 字符频率：{dict(char_freq)}")
    
    # 2. 使用defaultdict按首字母分组单词
    words = ["apple", "banana", "cherry", "apricot", "blueberry", "coconut"]
    grouped_words = defaultdict(list)
    for word in words:
        grouped_words[word[0]].append(word)
    print(f"2. 按首字母分组：{dict(grouped_words)}")
    
    # 3. 使用deque实现浏览器历史记录
    class BrowserHistory:
        def __init__(self):
            self.history = deque()
            self.current_index = -1
        
        def visit(self, url):
            # 删除当前位置之后的历史
            while len(self.history) > self.current_index + 1:
                self.history.pop()
            self.history.append(url)
            self.current_index += 1
            print(f"访问：{url}")
        
        def back(self):
            if self.current_index > 0:
                self.current_index -= 1
                print(f"后退到：{self.history[self.current_index]}")
                return self.history[self.current_index]
            else:
                print("无法后退")
                return None
        
        def forward(self):
            if self.current_index < len(self.history) - 1:
                self.current_index += 1
                print(f"前进到：{self.history[self.current_index]}")
                return self.history[self.current_index]
            else:
                print("无法前进")
                return None
    
    print("3. 浏览器历史记录：")
    browser = BrowserHistory()
    browser.visit("google.com")
    browser.visit("github.com")
    browser.visit("stackoverflow.com")
    browser.back()
    browser.back()
    browser.forward()
    
    # 4. 使用heapq找出最大和最小的数
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
    largest_5 = heapq.nlargest(5, numbers)
    smallest_5 = heapq.nsmallest(5, numbers)
    print(f"4. 最大的5个数：{largest_5}")
    print(f"   最小的5个数：{smallest_5}")
    
    # 5. 使用OrderedDict实现LRU缓存
    class LRUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()
        
        def get(self, key):
            if key in self.cache:
                # 移动到末尾（最近使用）
                self.cache.move_to_end(key)
                return self.cache[key]
            return None
        
        def put(self, key, value):
            if key in self.cache:
                # 更新并移动到末尾
                self.cache[key] = value
                self.cache.move_to_end(key)
            else:
                # 检查容量
                if len(self.cache) >= self.capacity:
                    # 删除最久未使用的（第一个）
                    self.cache.popitem(last=False)
                self.cache[key] = value
        
        def __str__(self):
            return str(dict(self.cache))
    
    print("5. LRU缓存：")
    lru = LRUCache(3)
    lru.put("a", 1)
    lru.put("b", 2)
    lru.put("c", 3)
    print(f"   添加a,b,c后：{lru}")
    lru.get("a")  # a变为最近使用
    lru.put("d", 4)  # b被淘汰
    print(f"   访问a并添加d后：{lru}")
    
    print()

# ============================================================================
# 练习12：性能优化 - 参考答案
# ============================================================================

def solution_12_performance():
    """
    练习12：性能优化 - 参考答案
    """
    print("练习12：性能优化 - 参考答案")
    
    # 1. 比较列表和集合的查找性能
    size = 10000
    test_list = list(range(size))
    test_set = set(range(size))
    target = size - 1  # 最坏情况
    
    # 列表查找
    start_time = time.time()
    result = target in test_list
    list_time = time.time() - start_time
    
    # 集合查找
    start_time = time.time()
    result = target in test_set
    set_time = time.time() - start_time
    
    print(f"1. 查找性能比较（数据量：{size}）：")
    print(f"   列表查找：{list_time:.6f}秒")
    print(f"   集合查找：{set_time:.6f}秒")
    print(f"   集合比列表快：{list_time/set_time:.1f}倍")
    
    # 2. 比较字符串拼接性能
    words = ["word"] * 1000
    
    # += 方法
    start_time = time.time()
    result1 = ""
    for word in words:
        result1 += word
    plus_time = time.time() - start_time
    
    # join 方法
    start_time = time.time()
    result2 = "".join(words)
    join_time = time.time() - start_time
    
    print(f"2. 字符串拼接性能比较（{len(words)}个单词）：")
    print(f"   += 方法：{plus_time:.6f}秒")
    print(f"   join方法：{join_time:.6f}秒")
    print(f"   join比+=快：{plus_time/join_time:.1f}倍")
    
    # 3. 比较列表推导式和传统循环
    n = 10000
    
    # 传统循环
    start_time = time.time()
    result1 = []
    for i in range(n):
        if i % 2 == 0:
            result1.append(i**2)
    loop_time = time.time() - start_time
    
    # 列表推导式
    start_time = time.time()
    result2 = [i**2 for i in range(n) if i % 2 == 0]
    comprehension_time = time.time() - start_time
    
    print(f"3. 列表创建性能比较（{n}个元素）：")
    print(f"   传统循环：{loop_time:.6f}秒")
    print(f"   列表推导式：{comprehension_time:.6f}秒")
    print(f"   推导式比循环快：{loop_time/comprehension_time:.1f}倍")
    
    # 4. 比较字典访问方法
    test_dict = {str(i): i for i in range(1000)}
    key = "999"
    iterations = 100000
    
    # get方法
    start_time = time.time()
    for _ in range(iterations):
        value = test_dict.get(key, None)
    get_time = time.time() - start_time
    
    # 直接访问（带异常处理）
    start_time = time.time()
    for _ in range(iterations):
        try:
            value = test_dict[key]
        except KeyError:
            value = None
    direct_time = time.time() - start_time
    
    print(f"4. 字典访问性能比较（{iterations}次访问）：")
    print(f"   get方法：{get_time:.6f}秒")
    print(f"   直接访问：{direct_time:.6f}秒")
    print(f"   get比直接访问快：{direct_time/get_time:.1f}倍")
    
    print()

# ============================================================================
# 练习13：数据清洗 - 参考答案
# ============================================================================

def solution_13_data_cleaning():
    """
    练习13：数据清洗 - 参考答案
    """
    print("练习13：数据清洗 - 参考答案")
    
    dirty_data = [
        {"姓名": "  张三  ", "年龄": "25", "邮箱": "zhangsan@email.com", "电话": "123-456-7890"},
        {"姓名": "李四", "年龄": "abc", "邮箱": "invalid-email", "电话": "987-654-3210"},
        {"姓名": "", "年龄": "30", "邮箱": "wangwu@email.com", "电话": "555-123-4567"},
        {"姓名": "赵六", "年龄": "22", "邮箱": "zhaoliu@email.com", "电话": "invalid-phone"},
        {"姓名": "钱七", "年龄": "-5", "邮箱": "qianqi@email.com", "电话": "111-222-3333"}
    ]
    
    def validate_email(email):
        """验证邮箱格式"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(phone):
        """验证电话号码格式"""
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        return re.match(pattern, phone) is not None
    
    def validate_age(age_str):
        """验证年龄"""
        try:
            age = int(age_str)
            return 0 < age < 150
        except ValueError:
            return False
    
    print(f"原始数据量：{len(dirty_data)}")
    
    cleaned_data = []
    errors = []
    
    for i, record in enumerate(dirty_data):
        cleaned_record = {}
        is_valid = True
        record_errors = []
        
        # 1. 清理姓名字段
        name = record["姓名"].strip()
        if not name:
            is_valid = False
            record_errors.append("姓名为空")
        else:
            cleaned_record["姓名"] = name
        
        # 2. 验证年龄字段
        if validate_age(record["年龄"]):
            cleaned_record["年龄"] = int(record["年龄"])
        else:
            is_valid = False
            record_errors.append(f"年龄无效：{record['年龄']}")
        
        # 3. 验证邮箱格式
        if validate_email(record["邮箱"]):
            cleaned_record["邮箱"] = record["邮箱"]
        else:
            is_valid = False
            record_errors.append(f"邮箱格式无效：{record['邮箱']}")
        
        # 4. 验证电话号码格式
        if validate_phone(record["电话"]):
            cleaned_record["电话"] = record["电话"]
        else:
            is_valid = False
            record_errors.append(f"电话格式无效：{record['电话']}")
        
        if is_valid:
            cleaned_data.append(cleaned_record)
        else:
            errors.append({"记录": i+1, "错误": record_errors, "原始数据": record})
    
    print(f"清洗后数据量：{len(cleaned_data)}")
    print(f"无效记录数：{len(errors)}")
    
    print("\n清洗后的有效数据：")
    for record in cleaned_data:
        print(f"  {record}")
    
    print("\n无效记录详情：")
    for error in errors:
        print(f"  记录{error['记录']}：{error['错误']}")
    
    # 6. 统计数据质量
    total_records = len(dirty_data)
    valid_records = len(cleaned_data)
    data_quality = (valid_records / total_records) * 100
    
    print(f"\n数据质量统计：")
    print(f"  总记录数：{total_records}")
    print(f"  有效记录数：{valid_records}")
    print(f"  数据质量：{data_quality:.1f}%")
    
    print()

# ============================================================================
# 练习14：图数据结构 - 参考答案
# ============================================================================

def solution_14_graph_structure():
    """
    练习14：图数据结构 - 参考答案
    """
    print("练习14：图数据结构 - 参考答案")
    
    class Graph:
        def __init__(self):
            self.graph = defaultdict(list)
        
        def add_edge(self, u, v):
            """添加边（无向图）"""
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        def add_node(self, node):
            """添加节点"""
            if node not in self.graph:
                self.graph[node] = []
        
        def dfs(self, start, visited=None):
            """深度优先搜索"""
            if visited is None:
                visited = set()
            
            visited.add(start)
            result = [start]
            
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    result.extend(self.dfs(neighbor, visited))
            
            return result
        
        def bfs(self, start):
            """广度优先搜索"""
            visited = set()
            queue = deque([start])
            result = []
            
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    result.append(node)
                    
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            
            return result
        
        def find_connected_components(self):
            """找出所有连通分量"""
            visited = set()
            components = []
            
            for node in self.graph:
                if node not in visited:
                    component = self.dfs(node, visited)
                    components.append(component)
            
            return components
        
        def shortest_path(self, start, end):
            """找出两个节点之间的最短路径"""
            if start == end:
                return [start]
            
            visited = set()
            queue = deque([(start, [start])])
            
            while queue:
                node, path = queue.popleft()
                
                if node not in visited:
                    visited.add(node)
                    
                    for neighbor in self.graph[node]:
                        new_path = path + [neighbor]
                        
                        if neighbor == end:
                            return new_path
                        
                        if neighbor not in visited:
                            queue.append((neighbor, new_path))
            
            return None  # 没有路径
    
    # 创建示例图
    g = Graph()
    
    # 添加边
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('D', 'F')]
    for u, v in edges:
        g.add_edge(u, v)
    
    print(f"图的邻接表：{dict(g.graph)}")
    
    # 深度优先搜索
    dfs_result = g.dfs('A')
    print(f"从A开始的DFS：{dfs_result}")
    
    # 广度优先搜索
    bfs_result = g.bfs('A')
    print(f"从A开始的BFS：{bfs_result}")
    
    # 连通分量
    components = g.find_connected_components()
    print(f"连通分量：{components}")
    
    # 最短路径
    path = g.shortest_path('A', 'F')
    print(f"A到F的最短路径：{path}")
    
    path = g.shortest_path('C', 'E')
    print(f"C到E的最短路径：{path}")
    
    print()

# ============================================================================
# 练习15：综合应用 - 简单数据库 - 参考答案
# ============================================================================

def solution_15_simple_database():
    """
    练习15：综合应用 - 简单数据库 - 参考答案
    """
    print("练习15：综合应用 - 简单数据库 - 参考答案")
    
    class SimpleDatabase:
        def __init__(self):
            self.tables = {}  # 表结构：{table_name: {"columns": [...], "data": [...], "indexes": {...}}}
            self.next_id = 1
        
        def create_table(self, table_name, columns):
            """创建表"""
            self.tables[table_name] = {
                "columns": columns,
                "data": [],
                "indexes": {}
            }
            print(f"创建表 {table_name}，字段：{columns}")
        
        def insert(self, table_name, record):
            """插入记录"""
            if table_name not in self.tables:
                raise ValueError(f"表 {table_name} 不存在")
            
            # 添加自动ID
            if "id" not in record:
                record["id"] = self.next_id
                self.next_id += 1
            
            self.tables[table_name]["data"].append(record)
            
            # 更新索引
            for column, index in self.tables[table_name]["indexes"].items():
                if column in record:
                    if record[column] not in index:
                        index[record[column]] = []
                    index[record[column]].append(len(self.tables[table_name]["data"]) - 1)
            
            print(f"插入记录到 {table_name}：{record}")
        
        def create_index(self, table_name, column):
            """创建索引"""
            if table_name not in self.tables:
                raise ValueError(f"表 {table_name} 不存在")
            
            index = {}
            for i, record in enumerate(self.tables[table_name]["data"]):
                if column in record:
                    value = record[column]
                    if value not in index:
                        index[value] = []
                    index[value].append(i)
            
            self.tables[table_name]["indexes"][column] = index
            print(f"为 {table_name}.{column} 创建索引")
        
        def select(self, table_name, where=None, order_by=None, limit=None):
            """查询记录"""
            if table_name not in self.tables:
                raise ValueError(f"表 {table_name} 不存在")
            
            data = self.tables[table_name]["data"]
            
            # 应用WHERE条件
            if where:
                filtered_data = []
                for record in data:
                    match = True
                    for key, condition in where.items():
                        if key not in record:
                            match = False
                            break
                        
                        if callable(condition):
                            if not condition(record[key]):
                                match = False
                                break
                        else:
                            if record[key] != condition:
                                match = False
                                break
                    
                    if match:
                        filtered_data.append(record)
                
                data = filtered_data
            
            # 排序
            if order_by:
                if isinstance(order_by, str):
                    data = sorted(data, key=lambda x: x.get(order_by, 0))
                elif isinstance(order_by, dict):
                    column = list(order_by.keys())[0]
                    reverse = order_by[column] == "DESC"
                    data = sorted(data, key=lambda x: x.get(column, 0), reverse=reverse)
            
            # 限制结果数量
            if limit:
                data = data[:limit]
            
            return data
        
        def update(self, table_name, updates, where=None):
            """更新记录"""
            if table_name not in self.tables:
                raise ValueError(f"表 {table_name} 不存在")
            
            updated_count = 0
            for record in self.tables[table_name]["data"]:
                # 检查WHERE条件
                if where:
                    match = True
                    for key, condition in where.items():
                        if key not in record:
                            match = False
                            break
                        
                        if callable(condition):
                            if not condition(record[key]):
                                match = False
                                break
                        else:
                            if record[key] != condition:
                                match = False
                                break
                    
                    if not match:
                        continue
                
                # 更新记录
                for key, value in updates.items():
                    record[key] = value
                updated_count += 1
            
            print(f"更新了 {updated_count} 条记录")
            return updated_count
        
        def delete(self, table_name, where=None):
            """删除记录"""
            if table_name not in self.tables:
                raise ValueError(f"表 {table_name} 不存在")
            
            if where is None:
                # 删除所有记录
                deleted_count = len(self.tables[table_name]["data"])
                self.tables[table_name]["data"] = []
            else:
                # 按条件删除
                original_data = self.tables[table_name]["data"]
                filtered_data = []
                deleted_count = 0
                
                for record in original_data:
                    match = True
                    for key, condition in where.items():
                        if key not in record:
                            match = False
                            break
                        
                        if callable(condition):
                            if not condition(record[key]):
                                match = False
                                break
                        else:
                            if record[key] != condition:
                                match = False
                                break
                    
                    if match:
                        deleted_count += 1
                    else:
                        filtered_data.append(record)
                
                self.tables[table_name]["data"] = filtered_data
            
            print(f"删除了 {deleted_count} 条记录")
            return deleted_count
        
        def aggregate(self, table_name, operation, column, where=None):
            """聚合查询"""
            data = self.select(table_name, where)
            
            if not data:
                return None
            
            values = [record[column] for record in data if column in record]
            
            if operation.upper() == "COUNT":
                return len(values)
            elif operation.upper() == "SUM":
                return sum(values)
            elif operation.upper() == "AVG":
                return sum(values) / len(values) if values else 0
            elif operation.upper() == "MAX":
                return max(values) if values else None
            elif operation.upper() == "MIN":
                return min(values) if values else None
            else:
                raise ValueError(f"不支持的聚合操作：{operation}")
        
        def group_by(self, table_name, group_column, aggregate_column=None, operation="COUNT"):
            """分组查询"""
            data = self.tables[table_name]["data"]
            groups = defaultdict(list)
            
            # 分组
            for record in data:
                if group_column in record:
                    groups[record[group_column]].append(record)
            
            # 聚合
            result = {}
            for group_value, group_data in groups.items():
                if aggregate_column:
                    values = [record[aggregate_column] for record in group_data if aggregate_column in record]
                    if operation.upper() == "COUNT":
                        result[group_value] = len(values)
                    elif operation.upper() == "SUM":
                        result[group_value] = sum(values)
                    elif operation.upper() == "AVG":
                        result[group_value] = sum(values) / len(values) if values else 0
                    elif operation.upper() == "MAX":
                        result[group_value] = max(values) if values else None
                    elif operation.upper() == "MIN":
                        result[group_value] = min(values) if values else None
                else:
                    result[group_value] = len(group_data)
            
            return result
    
    # 测试数据库
    db = SimpleDatabase()
    
    # 创建用户表
    db.create_table("users", ["id", "name", "age", "email", "city"])
    
    # 插入数据
    users_data = [
        {"name": "张三", "age": 25, "email": "zhangsan@email.com", "city": "北京"},
        {"name": "李四", "age": 30, "email": "lisi@email.com", "city": "上海"},
        {"name": "王五", "age": 28, "email": "wangwu@email.com", "city": "北京"},
        {"name": "赵六", "age": 35, "email": "zhaoliu@email.com", "city": "广州"},
        {"name": "钱七", "age": 22, "email": "qianqi@email.com", "city": "上海"}
    ]
    
    for user in users_data:
        db.insert("users", user)
    
    # 创建索引
    db.create_index("users", "age")
    db.create_index("users", "city")
    
    print("\n查询所有用户：")
    all_users = db.select("users")
    for user in all_users:
        print(f"  {user}")
    
    print("\n查询年龄大于25的用户：")
    young_users = db.select("users", where={"age": lambda x: x > 25})
    for user in young_users:
        print(f"  {user}")
    
    print("\n查询北京的用户：")
    beijing_users = db.select("users", where={"city": "北京"})
    for user in beijing_users:
        print(f"  {user}")
    
    print("\n按年龄排序（降序）：")
    sorted_users = db.select("users", order_by={"age": "DESC"})
    for user in sorted_users:
        print(f"  {user['name']}: {user['age']}岁")
    
    print("\n聚合查询：")
    print(f"  用户总数：{db.aggregate('users', 'COUNT', 'id')}")
    print(f"  平均年龄：{db.aggregate('users', 'AVG', 'age'):.1f}岁")
    print(f"  最大年龄：{db.aggregate('users', 'MAX', 'age')}岁")
    print(f"  最小年龄：{db.aggregate('users', 'MIN', 'age')}岁")
    
    print("\n按城市分组统计：")
    city_groups = db.group_by("users", "city")
    for city, count in city_groups.items():
        print(f"  {city}: {count}人")
    
    print("\n按城市分组计算平均年龄：")
    city_avg_age = db.group_by("users", "city", "age", "AVG")
    for city, avg_age in city_avg_age.items():
        print(f"  {city}: {avg_age:.1f}岁")
    
    # 更新数据
    print("\n更新张三的年龄为26：")
    db.update("users", {"age": 26}, where={"name": "张三"})
    
    # 删除数据
    print("\n删除年龄小于25的用户：")
    db.delete("users", where={"age": lambda x: x < 25})
    
    print("\n删除后的用户列表：")
    remaining_users = db.select("users")
    for user in remaining_users:
        print(f"  {user}")
    
    print()

if __name__ == "__main__":
    print("数据结构练习题参考答案")
    print("=" * 50)
    
    solutions = [
        solution_1_list_basics,
        solution_2_list_comprehension,
        solution_3_tuple_operations,
        solution_4_dict_basics,
        solution_5_dict_advanced,
        solution_6_set_operations,
        solution_7_data_conversion,
        solution_8_text_analysis,
        solution_9_student_management,
        solution_10_data_analysis,
        solution_11_advanced_structures,
        solution_12_performance,
        solution_13_data_cleaning,
        solution_14_graph_structure,
        solution_15_simple_database
    ]
    
    # 运行所有解答
    for i, solution in enumerate(solutions, 1):
        print(f"\n{'='*20} 解答 {i} {'='*20}")
        try:
            solution()
        except Exception as e:
            print(f"运行解答{i}时出错：{e}")
    
    print("\n学习要点总结：")
    print("1. 列表（List）：")
    print("   - 有序、可变的序列")
    print("   - 支持索引、切片、增删改查")
    print("   - 列表推导式提高代码简洁性")
    print("   - 适用场景：需要保持顺序、频繁修改的数据")
    
    print("\n2. 元组（Tuple）：")
    print("   - 有序、不可变的序列")
    print("   - 支持解包、命名元组")
    print("   - 内存效率高，创建速度快")
    print("   - 适用场景：固定数据、函数返回多值、字典键")
    
    print("\n3. 字典（Dictionary）：")
    print("   - 键值对存储，无序（Python 3.7+保持插入顺序）")
    print("   - O(1)平均时间复杂度的查找")
    print("   - 支持嵌套、推导式")
    print("   - 适用场景：快速查找、数据映射、配置存储")
    
    print("\n4. 集合（Set）：")
    print("   - 无序、唯一元素的集合")
    print("   - 支持数学集合运算（并、交、差、对称差）")
    print("   - O(1)平均时间复杂度的成员测试")
    print("   - 适用场景：去重、成员测试、集合运算")
    
    print("\n5. 高级数据结构：")
    print("   - Counter：计数器，统计频率")
    print("   - defaultdict：带默认值的字典")
    print("   - OrderedDict：有序字典（Python 3.7+普通字典也有序）")
    print("   - deque：双端队列，高效的两端操作")
    print("   - heapq：堆，优先队列实现")
    
    print("\n6. 性能优化建议：")
    print("   - 成员测试：集合 > 字典 > 列表")
    print("   - 字符串拼接：join() > +=操作符")
    print("   - 列表创建：推导式 > 传统循环")
    print("   - 字典访问：get()方法处理不存在的键")
    print("   - 根据使用场景选择合适的数据结构")
    
    print("\n7. 实际应用技巧：")
    print("   - 数据清洗：验证、转换、过滤")
    print("   - 文本分析：分词、计数、统计")
    print("   - 数据分组：defaultdict、groupby")
    print("   - 图算法：邻接表表示、DFS/BFS遍历")
    print("   - 缓存实现：OrderedDict实现LRU")
    
    print("\n编程最佳实践：")
    print("1. 选择合适的数据结构解决特定问题")
    print("2. 理解时间和空间复杂度")
    print("3. 使用推导式提高代码可读性")
    print("4. 善用collections模块的高级数据结构")
    print("5. 注意数据结构的可变性和不可变性")
    print("6. 在性能关键的地方进行基准测试")
    print("7. 编写清晰的文档和注释")
    print("8. 处理边界情况和异常")