#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第四部分：函数 - 练习题

本文件包含函数相关的练习题，涵盖：
1. 函数基础
2. 参数类型
3. 返回值处理
4. 作用域和闭包
5. 装饰器
6. 递归
7. 函数式编程
8. 高级应用

每个练习都有明确的要求和测试用例
"""

print("第四部分：函数练习题")
print("=" * 50)

# ============================================================================
# 1. 函数基础练习
# ============================================================================

print("\n1. 函数基础练习")
print("-" * 30)

# 练习1.1：基本函数定义
def exercise_1_1():
    """
    练习1.1：编写以下函数
    
    1. calculate_bmi(weight, height) - 计算BMI指数
    2. is_leap_year(year) - 判断是否为闰年
    3. get_grade(score) - 根据分数返回等级（A/B/C/D/F）
    4. format_name(first, last) - 格式化姓名
    """
    print("练习1.1：基本函数定义")
    
    # TODO: 实现calculate_bmi函数
    # BMI = weight(kg) / height(m)^2
    def calculate_bmi(weight, height):
        pass
    
    # TODO: 实现is_leap_year函数
    # 闰年规则：能被4整除但不能被100整除，或者能被400整除
    def is_leap_year(year):
        pass
    
    # TODO: 实现get_grade函数
    # A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59
    def get_grade(score):
        pass
    
    # TODO: 实现format_name函数
    # 返回"Last, First"格式
    def format_name(first, last):
        pass
    
    # 测试用例
    print(f"BMI(70, 1.75): {calculate_bmi(70, 1.75)}")
    print(f"闰年2024: {is_leap_year(2024)}")
    print(f"闰年2023: {is_leap_year(2023)}")
    print(f"等级85: {get_grade(85)}")
    print(f"格式化姓名: {format_name('张', '三')}")

# 练习1.2：函数文档和类型提示
def exercise_1_2():
    """
    练习1.2：为函数添加完整的文档字符串和类型提示
    
    要求：
    1. 添加详细的docstring
    2. 添加类型提示
    3. 包含参数说明、返回值说明、异常说明
    4. 添加使用示例
    """
    print("\n练习1.2：函数文档和类型提示")
    
    # TODO: 为以下函数添加完整的文档和类型提示
    def calculate_compound_interest(principal, rate, time, compound_frequency):
        # 复利计算：A = P(1 + r/n)^(nt)
        # P: 本金, r: 年利率, t: 时间(年), n: 复利频率
        pass
    
    def find_common_elements(list1, list2):
        # 找出两个列表的共同元素
        pass
    
    def validate_email(email):
        # 简单的邮箱验证
        pass

# ============================================================================
# 2. 参数类型练习
# ============================================================================

print("\n2. 参数类型练习")
print("-" * 30)

# 练习2.1：默认参数和关键字参数
def exercise_2_1():
    """
    练习2.1：实现一个灵活的日志函数
    
    要求：
    1. 支持不同的日志级别（INFO, WARNING, ERROR）
    2. 支持自定义时间格式
    3. 支持可选的文件输出
    4. 使用默认参数简化调用
    """
    print("练习2.1：灵活的日志函数")
    
    # TODO: 实现log_message函数
    def log_message(message, level="INFO", timestamp=True, 
                   time_format="%Y-%m-%d %H:%M:%S", file_path=None):
        pass
    
    # 测试用例
    log_message("这是一条信息")
    log_message("这是警告", level="WARNING")
    log_message("这是错误", level="ERROR", timestamp=False)

# 练习2.2：可变参数
def exercise_2_2():
    """
    练习2.2：实现统计函数
    
    要求：
    1. calculate_stats(*numbers) - 计算多个数字的统计信息
    2. create_report(**data) - 创建报告
    3. flexible_join(separator, *items, **options) - 灵活的连接函数
    """
    print("\n练习2.2：可变参数")
    
    # TODO: 实现calculate_stats函数
    # 返回字典包含：count, sum, average, min, max
    def calculate_stats(*numbers):
        pass
    
    # TODO: 实现create_report函数
    # 根据传入的关键字参数创建格式化报告
    def create_report(**data):
        pass
    
    # TODO: 实现flexible_join函数
    # 支持选项：uppercase, lowercase, prefix, suffix
    def flexible_join(separator, *items, **options):
        pass
    
    # 测试用例
    stats = calculate_stats(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"统计结果: {stats}")
    
    report = create_report(name="张三", age=25, city="北京", job="工程师")
    print(f"报告: {report}")
    
    result = flexible_join("-", "hello", "world", "python", 
                          uppercase=True, prefix=">>")
    print(f"连接结果: {result}")

# 练习2.3：参数解包
def exercise_2_3():
    """
    练习2.3：参数解包练习
    
    要求：
    1. 使用*和**解包参数
    2. 实现函数调用的动态参数传递
    3. 处理嵌套数据结构
    """
    print("\n练习2.3：参数解包")
    
    def process_order(customer_name, *items, **details):
        """处理订单"""
        print(f"客户: {customer_name}")
        print(f"商品: {items}")
        print(f"详情: {details}")
        return len(items)
    
    # TODO: 使用不同方式调用process_order函数
    # 1. 直接传参
    # 2. 使用列表解包
    # 3. 使用字典解包
    # 4. 混合使用
    
    # 测试数据
    customer = "李四"
    item_list = ["苹果", "香蕉", "橙子"]
    order_details = {"address": "北京市", "phone": "13800138000", "urgent": True}
    
    # TODO: 实现不同的调用方式
    pass

# ============================================================================
# 3. 返回值处理练习
# ============================================================================

print("\n3. 返回值处理练习")
print("-" * 30)

# 练习3.1：多返回值
def exercise_3_1():
    """
    练习3.1：实现返回多个值的函数
    
    要求：
    1. parse_name(full_name) - 解析全名，返回姓和名
    2. analyze_text(text) - 分析文本，返回多个统计信息
    3. divide_safe(a, b) - 安全除法，返回结果和状态
    """
    print("练习3.1：多返回值")
    
    # TODO: 实现parse_name函数
    # 处理"张三"、"李小明"、"欧阳修"等不同格式
    def parse_name(full_name):
        pass
    
    # TODO: 实现analyze_text函数
    # 返回：字符数、单词数、句子数、段落数
    def analyze_text(text):
        pass
    
    # TODO: 实现divide_safe函数
    # 返回：(结果, 是否成功, 错误信息)
    def divide_safe(a, b):
        pass
    
    # 测试用例
    first, last = parse_name("张三丰")
    print(f"姓: {first}, 名: {last}")
    
    chars, words, sentences, paragraphs = analyze_text("Hello world. This is Python.")
    print(f"字符: {chars}, 单词: {words}, 句子: {sentences}, 段落: {paragraphs}")
    
    result, success, error = divide_safe(10, 0)
    print(f"结果: {result}, 成功: {success}, 错误: {error}")

# 练习3.2：条件返回
def exercise_3_2():
    """
    练习3.2：根据条件返回不同类型的值
    
    要求：
    1. 实现智能搜索函数
    2. 根据不同条件返回不同格式的结果
    3. 处理异常情况
    """
    print("\n练习3.2：条件返回")
    
    # TODO: 实现smart_search函数
    # 根据查询类型返回不同格式的结果
    def smart_search(query, search_type="auto"):
        # search_type: "auto", "exact", "fuzzy", "regex"
        # 返回格式根据类型而定
        pass
    
    # 模拟数据
    data = [
        "Python编程", "Java开发", "JavaScript前端", 
        "数据科学", "机器学习", "人工智能"
    ]
    
    # 测试不同搜索类型
    pass

# ============================================================================
# 4. 作用域和闭包练习
# ============================================================================

print("\n4. 作用域和闭包练习")
print("-" * 30)

# 练习4.1：闭包应用
def exercise_4_1():
    """
    练习4.1：使用闭包实现实用功能
    
    要求：
    1. make_accumulator() - 创建累加器
    2. make_password_validator(rules) - 创建密码验证器
    3. make_rate_limiter(max_calls, time_window) - 创建限流器
    """
    print("练习4.1：闭包应用")
    
    # TODO: 实现make_accumulator函数
    def make_accumulator(initial=0):
        # 返回一个函数，每次调用都累加传入的值
        pass
    
    # TODO: 实现make_password_validator函数
    def make_password_validator(**rules):
        # rules可能包含：min_length, require_uppercase, require_digits等
        # 返回验证函数
        pass
    
    # TODO: 实现make_rate_limiter函数
    def make_rate_limiter(max_calls, time_window):
        # 返回一个装饰器，限制函数调用频率
        pass
    
    # 测试累加器
    acc1 = make_accumulator()
    acc2 = make_accumulator(100)
    print(f"acc1(5): {acc1(5)}")
    print(f"acc1(3): {acc1(3)}")
    print(f"acc2(10): {acc2(10)}")
    
    # 测试密码验证器
    validator = make_password_validator(
        min_length=8, 
        require_uppercase=True, 
        require_digits=True
    )
    print(f"密码'abc123': {validator('abc123')}")
    print(f"密码'Abc12345': {validator('Abc12345')}")

# 练习4.2：作用域陷阱
def exercise_4_2():
    """
    练习4.2：理解和解决作用域相关的问题
    
    要求：
    1. 修复循环中的闭包问题
    2. 正确使用global和nonlocal
    3. 避免常见的作用域陷阱
    """
    print("\n练习4.2：作用域陷阱")
    
    # 问题1：修复以下代码的闭包问题
    functions = []
    for i in range(5):
        # TODO: 修复这个闭包问题
        functions.append(lambda: i)
    
    print("修复前的结果:")
    for func in functions:
        print(func(), end=" ")
    print()
    
    # TODO: 提供正确的实现
    fixed_functions = []
    # 在这里实现修复版本
    
    # 问题2：实现一个计数器类，正确使用作用域
    class Counter:
        def __init__(self):
            # TODO: 实现计数器
            pass
        
        def increment(self):
            # TODO: 实现递增
            pass
        
        def get_count(self):
            # TODO: 返回当前计数
            pass
        
        def make_incrementer(self):
            # TODO: 返回一个递增函数
            pass

# ============================================================================
# 5. 装饰器练习
# ============================================================================

print("\n5. 装饰器练习")
print("-" * 30)

# 练习5.1：基础装饰器
def exercise_5_1():
    """
    练习5.1：实现常用装饰器
    
    要求：
    1. @timing - 计时装饰器
    2. @cache - 缓存装饰器
    3. @validate - 参数验证装饰器
    4. @retry - 重试装饰器
    """
    print("练习5.1：基础装饰器")
    
    # TODO: 实现timing装饰器
    def timing(func):
        pass
    
    # TODO: 实现cache装饰器
    def cache(func):
        pass
    
    # TODO: 实现validate装饰器
    def validate(*types):
        pass
    
    # TODO: 实现retry装饰器
    def retry(max_attempts=3):
        pass
    
    # 测试装饰器
    @timing
    @cache
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    @validate(int, int)
    def add(a, b):
        return a + b
    
    # 测试用例
    print(f"fibonacci(10): {fibonacci(10)}")
    print(f"fibonacci(10): {fibonacci(10)}")
    print(f"add(3, 5): {add(3, 5)}")

# 练习5.2：高级装饰器
def exercise_5_2():
    """
    练习5.2：实现高级装饰器
    
    要求：
    1. 类装饰器
    2. 装饰器工厂
    3. 装饰器链
    4. 保持函数元数据
    """
    print("\n练习5.2：高级装饰器")
    
    # TODO: 实现RateLimiter类装饰器
    class RateLimiter:
        def __init__(self, max_calls, time_window):
            pass
        
        def __call__(self, func):
            pass
    
    # TODO: 实现权限检查装饰器工厂
    def require_permission(permission):
        pass
    
    # TODO: 实现日志装饰器，保持元数据
    def log_calls(func):
        pass
    
    # 测试高级装饰器
    @RateLimiter(max_calls=3, time_window=60)
    @require_permission("admin")
    @log_calls
    def sensitive_operation(data):
        """敏感操作"""
        return f"处理数据: {data}"

# ============================================================================
# 6. 递归练习
# ============================================================================

print("\n6. 递归练习")
print("-" * 30)

# 练习6.1：经典递归问题
def exercise_6_1():
    """
    练习6.1：实现经典递归算法
    
    要求：
    1. 汉诺塔问题
    2. 快速排序
    3. 二叉树遍历
    4. 目录遍历
    """
    print("练习6.1：经典递归问题")
    
    # TODO: 实现汉诺塔解法
    def hanoi(n, source, target, auxiliary):
        # 打印移动步骤
        pass
    
    # TODO: 实现快速排序
    def quicksort(arr):
        pass
    
    # TODO: 实现二叉树节点类和遍历
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            pass
    
    def inorder_traversal(root):
        # 中序遍历
        pass
    
    def preorder_traversal(root):
        # 前序遍历
        pass
    
    def postorder_traversal(root):
        # 后序遍历
        pass
    
    # TODO: 实现目录遍历（模拟）
    def traverse_directory(directory_dict, level=0):
        # 递归遍历目录结构
        pass
    
    # 测试用例
    print("汉诺塔(3层):")
    hanoi(3, 'A', 'C', 'B')
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"排序前: {arr}")
    sorted_arr = quicksort(arr.copy())
    print(f"排序后: {sorted_arr}")

# 练习6.2：递归优化
def exercise_6_2():
    """
    练习6.2：递归优化技术
    
    要求：
    1. 记忆化递归
    2. 尾递归优化
    3. 递归转迭代
    4. 递归深度控制
    """
    print("\n练习6.2：递归优化")
    
    # TODO: 实现记忆化斐波那契
    def fibonacci_memo(n, memo=None):
        pass
    
    # TODO: 实现尾递归阶乘
    def factorial_tail(n, acc=1):
        pass
    
    # TODO: 将递归转换为迭代
    def fibonacci_iterative(n):
        pass
    
    # TODO: 实现深度限制的递归
    def deep_sum(nested_list, max_depth=10, current_depth=0):
        # 计算嵌套列表的和，限制递归深度
        pass
    
    # 性能比较
    import time
    
    def time_function(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        return result, end - start
    
    # 比较不同实现的性能
    n = 30
    result1, time1 = time_function(fibonacci_memo, n)
    result2, time2 = time_function(fibonacci_iterative, n)
    
    print(f"记忆化递归 fibonacci({n}): {result1}, 时间: {time1:.4f}s")
    print(f"迭代版本 fibonacci({n}): {result2}, 时间: {time2:.4f}s")

# ============================================================================
# 7. 函数式编程练习
# ============================================================================

print("\n7. 函数式编程练习")
print("-" * 30)

# 练习7.1：高阶函数
def exercise_7_1():
    """
    练习7.1：使用和实现高阶函数
    
    要求：
    1. 使用map, filter, reduce解决问题
    2. 实现自定义高阶函数
    3. 函数组合
    4. 柯里化
    """
    print("练习7.1：高阶函数")
    
    # 数据准备
    students = [
        {"name": "Alice", "age": 20, "scores": [85, 92, 78]},
        {"name": "Bob", "age": 22, "scores": [90, 88, 94]},
        {"name": "Charlie", "age": 19, "scores": [76, 85, 89]},
        {"name": "Diana", "age": 21, "scores": [95, 91, 87]}
    ]
    
    # TODO: 使用map计算每个学生的平均分
    def calculate_averages(students):
        pass
    
    # TODO: 使用filter找出优秀学生（平均分>=90）
    def find_excellent_students(students):
        pass
    
    # TODO: 使用reduce计算所有学生的总平均分
    def calculate_overall_average(students):
        pass
    
    # TODO: 实现自定义的map函数
    def my_map(func, iterable):
        pass
    
    # TODO: 实现函数组合
    def compose(*functions):
        pass
    
    # TODO: 实现柯里化
    def curry(func):
        pass
    
    # 测试用例
    averages = calculate_averages(students)
    print(f"平均分: {averages}")
    
    excellent = find_excellent_students(students)
    print(f"优秀学生: {excellent}")
    
    overall = calculate_overall_average(students)
    print(f"总平均分: {overall}")

# 练习7.2：函数式数据处理
def exercise_7_2():
    """
    练习7.2：函数式数据处理管道
    
    要求：
    1. 构建数据处理管道
    2. 使用纯函数
    3. 避免副作用
    4. 函数式错误处理
    """
    print("\n练习7.2：函数式数据处理")
    
    # TODO: 实现数据处理管道
    class Pipeline:
        def __init__(self, data):
            pass
        
        def map(self, func):
            pass
        
        def filter(self, predicate):
            pass
        
        def reduce(self, func, initial=None):
            pass
        
        def collect(self):
            pass
    
    # TODO: 实现Maybe单子用于错误处理
    class Maybe:
        def __init__(self, value):
            pass
        
        def map(self, func):
            pass
        
        def flat_map(self, func):
            pass
        
        @property
        def value(self):
            pass
        
        @property
        def is_nothing(self):
            pass
    
    # 测试数据处理管道
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = (Pipeline(data)
              .filter(lambda x: x % 2 == 0)
              .map(lambda x: x ** 2)
              .reduce(lambda acc, x: acc + x, 0)
              .collect())
    
    print(f"管道处理结果: {result}")

# ============================================================================
# 8. 综合应用练习
# ============================================================================

print("\n8. 综合应用练习")
print("-" * 30)

# 练习8.1：函数式计算器
def exercise_8_1():
    """
    练习8.1：实现函数式计算器
    
    要求：
    1. 支持基本运算
    2. 支持函数链式调用
    3. 支持历史记录
    4. 支持撤销操作
    """
    print("练习8.1：函数式计算器")
    
    # TODO: 实现Calculator类
    class Calculator:
        def __init__(self, initial_value=0):
            pass
        
        def add(self, value):
            pass
        
        def subtract(self, value):
            pass
        
        def multiply(self, value):
            pass
        
        def divide(self, value):
            pass
        
        def power(self, value):
            pass
        
        def sqrt(self):
            pass
        
        def undo(self):
            pass
        
        def reset(self):
            pass
        
        def get_value(self):
            pass
        
        def get_history(self):
            pass
    
    # 测试计算器
    calc = Calculator(10)
    result = (calc.add(5)
                  .multiply(2)
                  .subtract(3)
                  .divide(3)
                  .get_value())
    
    print(f"计算结果: {result}")
    print(f"历史记录: {calc.get_history()}")

# 练习8.2：事件处理系统
def exercise_8_2():
    """
    练习8.2：实现基于函数的事件处理系统
    
    要求：
    1. 事件注册和触发
    2. 事件过滤
    3. 异步事件处理
    4. 事件链和中间件
    """
    print("\n练习8.2：事件处理系统")
    
    # TODO: 实现EventEmitter类
    class EventEmitter:
        def __init__(self):
            pass
        
        def on(self, event_name, handler):
            # 注册事件处理器
            pass
        
        def off(self, event_name, handler=None):
            # 移除事件处理器
            pass
        
        def emit(self, event_name, *args, **kwargs):
            # 触发事件
            pass
        
        def once(self, event_name, handler):
            # 一次性事件处理器
            pass
        
        def filter(self, predicate):
            # 事件过滤
            pass
        
        def middleware(self, middleware_func):
            # 添加中间件
            pass
    
    # TODO: 实现事件装饰器
    def event_handler(event_name):
        pass
    
    # 测试事件系统
    emitter = EventEmitter()
    
    @event_handler("user_login")
    def handle_login(user_id, timestamp):
        print(f"用户 {user_id} 在 {timestamp} 登录")
    
    @event_handler("user_logout")
    def handle_logout(user_id, timestamp):
        print(f"用户 {user_id} 在 {timestamp} 登出")
    
    # 触发事件
    emitter.emit("user_login", "user123", "2024-01-01 10:00:00")
    emitter.emit("user_logout", "user123", "2024-01-01 11:00:00")

# 练习8.3：函数式配置管理
def exercise_8_3():
    """
    练习8.3：实现函数式配置管理系统
    
    要求：
    1. 不可变配置对象
    2. 配置合并和覆盖
    3. 配置验证
    4. 环境特定配置
    """
    print("\n练习8.3：函数式配置管理")
    
    # TODO: 实现Config类
    class Config:
        def __init__(self, data=None):
            pass
        
        def get(self, key, default=None):
            pass
        
        def set(self, key, value):
            # 返回新的Config实例
            pass
        
        def merge(self, other_config):
            # 合并配置
            pass
        
        def validate(self, schema):
            # 验证配置
            pass
        
        def for_environment(self, env):
            # 获取环境特定配置
            pass
        
        def to_dict(self):
            pass
    
    # TODO: 实现配置装饰器
    def with_config(config_key):
        pass
    
    # 测试配置管理
    base_config = Config({
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "myapp"
        },
        "debug": False
    })
    
    dev_config = base_config.merge(Config({
        "debug": True,
        "database": {"name": "myapp_dev"}
    }))
    
    print(f"开发环境配置: {dev_config.to_dict()}")

if __name__ == "__main__":
    print("\n开始函数练习...")
    print("请逐个完成每个练习，并运行测试用例验证结果。")
    print("\n练习提示：")
    print("1. 仔细阅读每个练习的要求")
    print("2. 先实现基本功能，再考虑边界情况")
    print("3. 注意函数的文档字符串和类型提示")
    print("4. 测试不同的输入情况")
    print("5. 考虑性能和可维护性")
    
    # 运行练习（取消注释来运行）
    # exercise_1_1()
    # exercise_1_2()
    # exercise_2_1()
    # exercise_2_2()
    # exercise_2_3()
    # exercise_3_1()
    # exercise_3_2()
    # exercise_4_1()
    # exercise_4_2()
    # exercise_5_1()
    # exercise_5_2()
    # exercise_6_1()
    # exercise_6_2()
    # exercise_7_1()
    # exercise_7_2()
    # exercise_8_1()
    # exercise_8_2()
    # exercise_8_3()