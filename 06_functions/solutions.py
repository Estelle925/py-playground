#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第四部分：函数 - 练习题参考答案

本文件包含函数练习题的详细解答和说明
"""

import time
import functools
import re
from typing import List, Dict, Optional, Union, Callable, Any
from collections import defaultdict, Counter
from datetime import datetime

print("第四部分：函数练习题参考答案")
print("=" * 50)

# ============================================================================
# 1. 函数基础练习答案
# ============================================================================

def solution_1_1():
    """练习1.1：基本函数定义 - 参考答案"""
    print("\n解答1.1：基本函数定义")
    
    def calculate_bmi(weight: float, height: float) -> float:
        """计算BMI指数
        
        Args:
            weight: 体重(kg)
            height: 身高(m)
            
        Returns:
            BMI指数
        """
        if height <= 0 or weight <= 0:
            raise ValueError("身高和体重必须大于0")
        return weight / (height ** 2)
    
    def is_leap_year(year: int) -> bool:
        """判断是否为闰年
        
        Args:
            year: 年份
            
        Returns:
            是否为闰年
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def get_grade(score: float) -> str:
        """根据分数返回等级
        
        Args:
            score: 分数(0-100)
            
        Returns:
            等级字母
        """
        if score < 0 or score > 100:
            raise ValueError("分数必须在0-100之间")
        
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    
    def format_name(first: str, last: str) -> str:
        """格式化姓名
        
        Args:
            first: 名
            last: 姓
            
        Returns:
            格式化的姓名
        """
        return f"{last}, {first}"
    
    # 测试用例
    print(f"BMI(70, 1.75): {calculate_bmi(70, 1.75):.2f}")
    print(f"闰年2024: {is_leap_year(2024)}")
    print(f"闰年2023: {is_leap_year(2023)}")
    print(f"等级85: {get_grade(85)}")
    print(f"格式化姓名: {format_name('张', '三')}")

def solution_1_2():
    """练习1.2：函数文档和类型提示 - 参考答案"""
    print("\n解答1.2：函数文档和类型提示")
    
    def calculate_compound_interest(
        principal: float, 
        rate: float, 
        time: float, 
        compound_frequency: int = 1
    ) -> float:
        """
        计算复利
        
        使用公式：A = P(1 + r/n)^(nt)
        
        Args:
            principal: 本金
            rate: 年利率（小数形式，如0.05表示5%）
            time: 时间（年）
            compound_frequency: 复利频率（每年复利次数），默认为1
            
        Returns:
            最终金额
            
        Raises:
            ValueError: 当参数为负数时
            
        Examples:
            >>> calculate_compound_interest(1000, 0.05, 2, 4)
            1104.49
        """
        if principal < 0 or rate < 0 or time < 0 or compound_frequency <= 0:
            raise ValueError("所有参数必须为非负数，复利频率必须大于0")
        
        return principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    
    def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
        """
        找出两个列表的共同元素
        
        Args:
            list1: 第一个列表
            list2: 第二个列表
            
        Returns:
            包含共同元素的列表（去重且保持顺序）
            
        Examples:
            >>> find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])
            [3, 4]
        """
        seen = set(list2)
        result = []
        for item in list1:
            if item in seen and item not in result:
                result.append(item)
        return result
    
    def validate_email(email: str) -> bool:
        """
        简单的邮箱验证
        
        Args:
            email: 邮箱地址字符串
            
        Returns:
            是否为有效邮箱格式
            
        Examples:
            >>> validate_email("user@example.com")
            True
            >>> validate_email("invalid-email")
            False
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    # 测试用例
    print(f"复利计算: {calculate_compound_interest(1000, 0.05, 2, 4):.2f}")
    print(f"共同元素: {find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])}")
    print(f"邮箱验证: {validate_email('user@example.com')}")
    print(f"邮箱验证: {validate_email('invalid-email')}")

# ============================================================================
# 2. 参数类型练习答案
# ============================================================================

def solution_2_1():
    """练习2.1：默认参数和关键字参数 - 参考答案"""
    print("\n解答2.1：灵活的日志函数")
    
    def log_message(
        message: str, 
        level: str = "INFO", 
        timestamp: bool = True,
        time_format: str = "%Y-%m-%d %H:%M:%S", 
        file_path: Optional[str] = None
    ) -> None:
        """
        记录日志消息
        
        Args:
            message: 日志消息
            level: 日志级别
            timestamp: 是否包含时间戳
            time_format: 时间格式
            file_path: 可选的文件输出路径
        """
        log_entry = f"[{level}]"
        
        if timestamp:
            current_time = datetime.now().strftime(time_format)
            log_entry += f" {current_time}"
        
        log_entry += f" {message}"
        
        print(log_entry)
        
        if file_path:
            try:
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(log_entry + '\n')
            except IOError as e:
                print(f"写入文件失败: {e}")
    
    # 测试用例
    log_message("这是一条信息")
    log_message("这是警告", level="WARNING")
    log_message("这是错误", level="ERROR", timestamp=False)
    log_message("带自定义时间格式", time_format="%H:%M:%S")

def solution_2_2():
    """练习2.2：可变参数 - 参考答案"""
    print("\n解答2.2：可变参数")
    
    def calculate_stats(*numbers: Union[int, float]) -> Dict[str, float]:
        """
        计算数字的统计信息
        
        Args:
            *numbers: 可变数量的数字
            
        Returns:
            包含统计信息的字典
        """
        if not numbers:
            return {"count": 0, "sum": 0, "average": 0, "min": 0, "max": 0}
        
        return {
            "count": len(numbers),
            "sum": sum(numbers),
            "average": sum(numbers) / len(numbers),
            "min": min(numbers),
            "max": max(numbers)
        }
    
    def create_report(**data: Any) -> str:
        """
        创建格式化报告
        
        Args:
            **data: 任意关键字参数
            
        Returns:
            格式化的报告字符串
        """
        if not data:
            return "空报告"
        
        report_lines = ["=== 报告 ==="]
        for key, value in data.items():
            formatted_key = key.replace('_', ' ').title()
            report_lines.append(f"{formatted_key}: {value}")
        report_lines.append("=" * 15)
        
        return "\n".join(report_lines)
    
    def flexible_join(separator: str, *items: Any, **options: Any) -> str:
        """
        灵活的字符串连接函数
        
        Args:
            separator: 分隔符
            *items: 要连接的项目
            **options: 连接选项
            
        Returns:
            连接后的字符串
        """
        # 转换为字符串
        str_items = [str(item) for item in items]
        
        # 应用选项
        if options.get('uppercase'):
            str_items = [item.upper() for item in str_items]
        elif options.get('lowercase'):
            str_items = [item.lower() for item in str_items]
        
        # 连接
        result = separator.join(str_items)
        
        # 添加前缀和后缀
        if 'prefix' in options:
            result = str(options['prefix']) + result
        if 'suffix' in options:
            result = result + str(options['suffix'])
        
        return result
    
    # 测试用例
    stats = calculate_stats(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"统计结果: {stats}")
    
    report = create_report(name="张三", age=25, city="北京", job="工程师")
    print(f"报告:\n{report}")
    
    result = flexible_join("-", "hello", "world", "python", 
                          uppercase=True, prefix=">>")
    print(f"连接结果: {result}")

def solution_2_3():
    """练习2.3：参数解包 - 参考答案"""
    print("\n解答2.3：参数解包")
    
    def process_order(customer_name: str, *items: str, **details: Any) -> int:
        """处理订单"""
        print(f"客户: {customer_name}")
        print(f"商品: {items}")
        print(f"详情: {details}")
        return len(items)
    
    # 测试数据
    customer = "李四"
    item_list = ["苹果", "香蕉", "橙子"]
    order_details = {"address": "北京市", "phone": "13800138000", "urgent": True}
    
    print("1. 直接传参:")
    count1 = process_order("张三", "苹果", "香蕉", address="上海市", phone="13900139000")
    print(f"商品数量: {count1}\n")
    
    print("2. 使用列表解包:")
    count2 = process_order(customer, *item_list, **order_details)
    print(f"商品数量: {count2}\n")
    
    print("3. 使用字典解包:")
    order_info = {
        "customer_name": "王五",
        "address": "广州市",
        "phone": "13700137000"
    }
    # 注意：这里需要分离位置参数和关键字参数
    count3 = process_order(order_info["customer_name"], "葡萄", "西瓜", 
                          address=order_info["address"], 
                          phone=order_info["phone"])
    print(f"商品数量: {count3}\n")
    
    print("4. 混合使用:")
    extra_items = ["草莓", "蓝莓"]
    extra_details = {"delivery_time": "明天", "gift_wrap": True}
    count4 = process_order(customer, "芒果", *extra_items, 
                          **order_details, **extra_details)
    print(f"商品数量: {count4}")

# ============================================================================
# 3. 返回值处理练习答案
# ============================================================================

def solution_3_1():
    """练习3.1：多返回值 - 参考答案"""
    print("\n解答3.1：多返回值")
    
    def parse_name(full_name: str) -> tuple[str, str]:
        """
        解析全名，返回姓和名
        
        Args:
            full_name: 完整姓名
            
        Returns:
            (姓, 名) 元组
        """
        full_name = full_name.strip()
        if not full_name:
            return "", ""
        
        # 处理不同格式的姓名
        if len(full_name) == 1:
            return full_name, ""
        elif len(full_name) == 2:
            return full_name[0], full_name[1]
        else:
            # 对于复姓或多字名，假设第一个字是姓
            return full_name[0], full_name[1:]
    
    def analyze_text(text: str) -> tuple[int, int, int, int]:
        """
        分析文本，返回字符数、单词数、句子数、段落数
        
        Args:
            text: 要分析的文本
            
        Returns:
            (字符数, 单词数, 句子数, 段落数)
        """
        if not text:
            return 0, 0, 0, 0
        
        # 字符数（不包括空格）
        char_count = len(text.replace(' ', ''))
        
        # 单词数
        words = text.split()
        word_count = len(words)
        
        # 句子数（简单计算，基于句号、问号、感叹号）
        sentence_endings = '.!?'
        sentence_count = sum(1 for char in text if char in sentence_endings)
        if sentence_count == 0 and text.strip():
            sentence_count = 1  # 如果没有句号但有内容，算作一句
        
        # 段落数（基于换行符）
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        paragraph_count = len(paragraphs)
        if paragraph_count == 0 and text.strip():
            paragraph_count = 1
        
        return char_count, word_count, sentence_count, paragraph_count
    
    def divide_safe(a: float, b: float) -> tuple[Optional[float], bool, str]:
        """
        安全除法运算
        
        Args:
            a: 被除数
            b: 除数
            
        Returns:
            (结果, 是否成功, 错误信息)
        """
        try:
            if b == 0:
                return None, False, "除数不能为0"
            result = a / b
            return result, True, "计算成功"
        except TypeError:
            return None, False, "参数类型错误"
        except Exception as e:
            return None, False, f"未知错误: {e}"
    
    # 测试用例
    first, last = parse_name("张三丰")
    print(f"姓: {first}, 名: {last}")
    
    first2, last2 = parse_name("欧阳修")
    print(f"姓: {first2}, 名: {last2}")
    
    chars, words, sentences, paragraphs = analyze_text("Hello world. This is Python!")
    print(f"字符: {chars}, 单词: {words}, 句子: {sentences}, 段落: {paragraphs}")
    
    result, success, error = divide_safe(10, 0)
    print(f"结果: {result}, 成功: {success}, 错误: {error}")
    
    result2, success2, error2 = divide_safe(10, 2)
    print(f"结果: {result2}, 成功: {success2}, 错误: {error2}")

def solution_3_2():
    """练习3.2：条件返回 - 参考答案"""
    print("\n解答3.2：条件返回")
    
    def smart_search(query: str, search_type: str = "auto") -> Union[List[str], Dict[str, Any], str]:
        """
        智能搜索函数
        
        Args:
            query: 搜索查询
            search_type: 搜索类型
            
        Returns:
            根据搜索类型返回不同格式的结果
        """
        # 模拟数据
        data = [
            "Python编程", "Java开发", "JavaScript前端", 
            "数据科学", "机器学习", "人工智能"
        ]
        
        query_lower = query.lower()
        
        if search_type == "exact":
            # 精确匹配，返回列表
            results = [item for item in data if query in item]
            return results
        
        elif search_type == "fuzzy":
            # 模糊匹配，返回带分数的字典
            results = {}
            for item in data:
                if query_lower in item.lower():
                    # 简单的相似度计算
                    score = len(query) / len(item) if item else 0
                    results[item] = score
            return results
        
        elif search_type == "regex":
            # 正则匹配，返回匹配信息
            try:
                pattern = re.compile(query, re.IGNORECASE)
                matches = []
                for item in data:
                    match = pattern.search(item)
                    if match:
                        matches.append({
                            "text": item,
                            "match": match.group(),
                            "start": match.start(),
                            "end": match.end()
                        })
                return matches
            except re.error:
                return "正则表达式错误"
        
        else:  # auto
            # 自动选择最佳匹配，返回简单列表
            results = []
            for item in data:
                if query_lower in item.lower():
                    results.append(item)
            return results if results else ["未找到匹配项"]
    
    # 测试不同搜索类型
    print("精确搜索 'Python':")
    result1 = smart_search("Python", "exact")
    print(f"结果: {result1}")
    
    print("\n模糊搜索 'script':")
    result2 = smart_search("script", "fuzzy")
    print(f"结果: {result2}")
    
    print("\n正则搜索 '.*学.*':")
    result3 = smart_search(".*学.*", "regex")
    print(f"结果: {result3}")
    
    print("\n自动搜索 '数据':")
    result4 = smart_search("数据", "auto")
    print(f"结果: {result4}")

# ============================================================================
# 4. 作用域和闭包练习答案
# ============================================================================

def solution_4_1():
    """练习4.1：闭包应用 - 参考答案"""
    print("\n解答4.1：闭包应用")
    
    def make_accumulator(initial: float = 0) -> Callable[[float], float]:
        """
        创建累加器闭包
        
        Args:
            initial: 初始值
            
        Returns:
            累加器函数
        """
        total = initial
        
        def accumulator(value: float) -> float:
            nonlocal total
            total += value
            return total
        
        return accumulator
    
    def make_password_validator(**rules: Any) -> Callable[[str], tuple[bool, List[str]]]:
        """
        创建密码验证器
        
        Args:
            **rules: 验证规则
            
        Returns:
            验证函数
        """
        def validator(password: str) -> tuple[bool, List[str]]:
            errors = []
            
            # 检查最小长度
            min_length = rules.get('min_length', 0)
            if len(password) < min_length:
                errors.append(f"密码长度至少需要{min_length}个字符")
            
            # 检查是否需要大写字母
            if rules.get('require_uppercase', False):
                if not any(c.isupper() for c in password):
                    errors.append("密码必须包含大写字母")
            
            # 检查是否需要数字
            if rules.get('require_digits', False):
                if not any(c.isdigit() for c in password):
                    errors.append("密码必须包含数字")
            
            # 检查是否需要特殊字符
            if rules.get('require_special', False):
                special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
                if not any(c in special_chars for c in password):
                    errors.append("密码必须包含特殊字符")
            
            return len(errors) == 0, errors
        
        return validator
    
    def make_rate_limiter(max_calls: int, time_window: float) -> Callable:
        """
        创建限流器装饰器
        
        Args:
            max_calls: 最大调用次数
            time_window: 时间窗口（秒）
            
        Returns:
            限流装饰器
        """
        def decorator(func: Callable) -> Callable:
            calls = []
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                now = time.time()
                
                # 清理过期的调用记录
                calls[:] = [call_time for call_time in calls 
                           if now - call_time < time_window]
                
                # 检查是否超过限制
                if len(calls) >= max_calls:
                    raise Exception(f"调用频率超限：{time_window}秒内最多{max_calls}次")
                
                # 记录本次调用
                calls.append(now)
                return func(*args, **kwargs)
            
            return wrapper
        return decorator
    
    # 测试累加器
    print("累加器测试:")
    acc1 = make_accumulator()
    acc2 = make_accumulator(100)
    print(f"acc1(5): {acc1(5)}")
    print(f"acc1(3): {acc1(3)}")
    print(f"acc2(10): {acc2(10)}")
    print(f"acc1(2): {acc1(2)}")
    
    # 测试密码验证器
    print("\n密码验证器测试:")
    validator = make_password_validator(
        min_length=8, 
        require_uppercase=True, 
        require_digits=True
    )
    
    valid1, errors1 = validator('abc123')
    print(f"密码'abc123': 有效={valid1}, 错误={errors1}")
    
    valid2, errors2 = validator('Abc12345')
    print(f"密码'Abc12345': 有效={valid2}, 错误={errors2}")
    
    # 测试限流器
    print("\n限流器测试:")
    @make_rate_limiter(max_calls=2, time_window=1.0)
    def test_function():
        return "调用成功"
    
    try:
        print(test_function())
        print(test_function())
        print(test_function())  # 这次应该失败
    except Exception as e:
        print(f"限流错误: {e}")

def solution_4_2():
    """练习4.2：作用域陷阱 - 参考答案"""
    print("\n解答4.2：作用域陷阱")
    
    # 问题1：修复闭包问题
    print("闭包问题修复:")
    
    # 错误的实现
    functions = []
    for i in range(5):
        functions.append(lambda: i)  # 所有lambda都引用同一个i
    
    print("修复前的结果:")
    for func in functions:
        print(func(), end=" ")
    print()
    
    # 修复方法1：使用默认参数
    fixed_functions1 = []
    for i in range(5):
        fixed_functions1.append(lambda x=i: x)
    
    print("修复方法1（默认参数）:")
    for func in fixed_functions1:
        print(func(), end=" ")
    print()
    
    # 修复方法2：使用闭包工厂
    def make_function(value):
        return lambda: value
    
    fixed_functions2 = []
    for i in range(5):
        fixed_functions2.append(make_function(i))
    
    print("修复方法2（闭包工厂）:")
    for func in fixed_functions2:
        print(func(), end=" ")
    print()
    
    # 修复方法3：使用列表推导式
    fixed_functions3 = [lambda x=i: x for i in range(5)]
    
    print("修复方法3（列表推导式）:")
    for func in fixed_functions3:
        print(func(), end=" ")
    print()
    
    # 问题2：计数器类
    class Counter:
        def __init__(self):
            self._count = 0
        
        def increment(self):
            self._count += 1
            return self._count
        
        def get_count(self):
            return self._count
        
        def make_incrementer(self):
            """返回一个递增函数，正确使用作用域"""
            def incrementer(step=1):
                self._count += step
                return self._count
            return incrementer
    
    print("\n计数器类测试:")
    counter = Counter()
    print(f"初始计数: {counter.get_count()}")
    print(f"递增: {counter.increment()}")
    print(f"递增: {counter.increment()}")
    
    incrementer = counter.make_incrementer()
    print(f"使用递增器: {incrementer()}")
    print(f"使用递增器(步长3): {incrementer(3)}")
    print(f"最终计数: {counter.get_count()}")

# ============================================================================
# 5. 装饰器练习答案
# ============================================================================

def solution_5_1():
    """练习5.1：基础装饰器 - 参考答案"""
    print("\n解答5.1：基础装饰器")
    
    def timing(func: Callable) -> Callable:
        """计时装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} 执行时间: {end_time - start_time:.4f}秒")
            return result
        return wrapper
    
    def cache(func: Callable) -> Callable:
        """缓存装饰器"""
        cache_dict = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 创建缓存键
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in cache_dict:
                print(f"缓存命中: {func.__name__}{args}")
                return cache_dict[key]
            
            print(f"计算中: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result
        
        wrapper.cache = cache_dict  # 暴露缓存
        return wrapper
    
    def validate(*types: type) -> Callable:
        """参数验证装饰器"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 验证位置参数类型
                for i, (arg, expected_type) in enumerate(zip(args, types)):
                    if not isinstance(arg, expected_type):
                        raise TypeError(
                            f"参数{i+1}期望类型{expected_type.__name__}, "
                            f"实际类型{type(arg).__name__}"
                        )
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable:
        """重试装饰器"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                
                for attempt in range(max_attempts):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        print(f"第{attempt + 1}次尝试失败: {e}")
                        if attempt < max_attempts - 1:
                            time.sleep(delay)
                
                print(f"所有{max_attempts}次尝试都失败了")
                raise last_exception
            return wrapper
        return decorator
    
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
    
    @retry(max_attempts=3, delay=0.1)
    def unreliable_function():
        import random
        if random.random() < 0.7:
            raise Exception("随机失败")
        return "成功"
    
    # 测试用例
    print("斐波那契测试:")
    print(f"fibonacci(10): {fibonacci(10)}")
    print(f"fibonacci(10): {fibonacci(10)}")
    
    print("\n参数验证测试:")
    print(f"add(3, 5): {add(3, 5)}")
    try:
        add(3, "5")
    except TypeError as e:
        print(f"类型错误: {e}")
    
    print("\n重试测试:")
    try:
        result = unreliable_function()
        print(f"最终结果: {result}")
    except Exception as e:
        print(f"最终失败: {e}")

def solution_5_2():
    """练习5.2：高级装饰器 - 参考答案"""
    print("\n解答5.2：高级装饰器")
    
    class RateLimiter:
        """限流器类装饰器"""
        def __init__(self, max_calls: int, time_window: float):
            self.max_calls = max_calls
            self.time_window = time_window
            self.calls = defaultdict(list)
        
        def __call__(self, func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                now = time.time()
                func_calls = self.calls[func.__name__]
                
                # 清理过期调用
                func_calls[:] = [call_time for call_time in func_calls 
                               if now - call_time < self.time_window]
                
                # 检查限制
                if len(func_calls) >= self.max_calls:
                    raise Exception(
                        f"函数{func.__name__}调用频率超限："
                        f"{self.time_window}秒内最多{self.max_calls}次"
                    )
                
                # 记录调用
                func_calls.append(now)
                return func(*args, **kwargs)
            
            return wrapper
    
    def require_permission(permission: str) -> Callable:
        """权限检查装饰器工厂"""
        def decorator(func: Callable) -> Callable:
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 模拟权限检查
                current_user_permissions = ["user", "admin"]  # 模拟当前用户权限
                
                if permission not in current_user_permissions:
                    raise PermissionError(f"需要{permission}权限才能执行{func.__name__}")
                
                print(f"权限验证通过: {permission}")
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    def log_calls(func: Callable) -> Callable:
        """日志装饰器，保持元数据"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] 调用函数: {func.__name__}")
            print(f"[LOG] 参数: args={args}, kwargs={kwargs}")
            
            try:
                result = func(*args, **kwargs)
                print(f"[LOG] 返回值: {result}")
                return result
            except Exception as e:
                print(f"[LOG] 异常: {e}")
                raise
        return wrapper
    
    # 测试高级装饰器
    @RateLimiter(max_calls=2, time_window=2.0)
    @require_permission("admin")
    @log_calls
    def sensitive_operation(data: str) -> str:
        """敏感操作"""
        return f"处理数据: {data}"
    
    print("高级装饰器测试:")
    try:
        result1 = sensitive_operation("测试数据1")
        print(f"结果1: {result1}")
        
        result2 = sensitive_operation("测试数据2")
        print(f"结果2: {result2}")
        
        # 这次应该触发限流
        result3 = sensitive_operation("测试数据3")
        print(f"结果3: {result3}")
        
    except Exception as e:
        print(f"操作失败: {e}")
    
    # 验证函数元数据保持
    print(f"\n函数名: {sensitive_operation.__name__}")
    print(f"函数文档: {sensitive_operation.__doc__}")

# ============================================================================
# 6. 递归练习答案
# ============================================================================

def solution_6_1():
    """练习6.1：经典递归问题 - 参考答案"""
    print("\n解答6.1：经典递归问题")
    
    def hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
        """汉诺塔解法"""
        if n == 1:
            print(f"移动盘子从 {source} 到 {target}")
        else:
            # 将n-1个盘子从源柱移到辅助柱
            hanoi(n-1, source, auxiliary, target)
            # 将最大的盘子从源柱移到目标柱
            print(f"移动盘子从 {source} 到 {target}")
            # 将n-1个盘子从辅助柱移到目标柱
            hanoi(n-1, auxiliary, target, source)
    
    def quicksort(arr: List[int]) -> List[int]:
        """快速排序"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)
    
    class TreeNode:
        """二叉树节点"""
        def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
            self.val = val
            self.left = left
            self.right = right
    
    def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
        """中序遍历"""
        if not root:
            return []
        return (inorder_traversal(root.left) + 
                [root.val] + 
                inorder_traversal(root.right))
    
    def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
        """前序遍历"""
        if not root:
            return []
        return ([root.val] + 
                preorder_traversal(root.left) + 
                preorder_traversal(root.right))
    
    def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
        """后序遍历"""
        if not root:
            return []
        return (postorder_traversal(root.left) + 
                postorder_traversal(root.right) + 
                [root.val])
    
    def traverse_directory(directory_dict: Dict[str, Any], level: int = 0) -> None:
        """递归遍历目录结构"""
        indent = "  " * level
        
        if isinstance(directory_dict, dict):
            for name, content in directory_dict.items():
                print(f"{indent}{name}/")
                traverse_directory(content, level + 1)
        elif isinstance(directory_dict, list):
            for item in directory_dict:
                if isinstance(item, str):
                    print(f"{indent}{item}")
                else:
                    traverse_directory(item, level)
        else:
            print(f"{indent}{directory_dict}")
    
    # 测试用例
    print("汉诺塔(3层):")
    hanoi(3, 'A', 'C', 'B')
    
    print("\n快速排序:")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"排序前: {arr}")
    sorted_arr = quicksort(arr.copy())
    print(f"排序后: {sorted_arr}")
    
    print("\n二叉树遍历:")
    # 构建测试树:     1
    #               /   \
    #              2     3
    #             / \
    #            4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"中序遍历: {inorder_traversal(root)}")
    print(f"前序遍历: {preorder_traversal(root)}")
    print(f"后序遍历: {postorder_traversal(root)}")
    
    print("\n目录遍历:")
    directory = {
        "project": {
            "src": ["main.py", "utils.py"],
            "tests": ["test_main.py"],
            "docs": {
                "api": ["index.md"],
                "guide": ["tutorial.md"]
            }
        }
    }
    traverse_directory(directory)

def solution_6_2():
    """练习6.2：递归优化 - 参考答案"""
    print("\n解答6.2：递归优化")
    
    def fibonacci_memo(n: int, memo: Optional[Dict[int, int]] = None) -> int:
        """记忆化斐波那契"""
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return n
        
        memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        return memo[n]
    
    def factorial_tail(n: int, acc: int = 1) -> int:
        """尾递归阶乘"""
        if n <= 1:
            return acc
        return factorial_tail(n-1, acc * n)
    
    def fibonacci_iterative(n: int) -> int:
        """迭代版斐波那契"""
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    def deep_sum(nested_list: List[Any], max_depth: int = 10, current_depth: int = 0) -> int:
        """深度限制的递归求和"""
        if current_depth >= max_depth:
            raise RecursionError(f"递归深度超过限制: {max_depth}")
        
        total = 0
        for item in nested_list:
            if isinstance(item, list):
                total += deep_sum(item, max_depth, current_depth + 1)
            elif isinstance(item, (int, float)):
                total += item
        return total
    
    # 性能比较函数
    def time_function(func: Callable, *args) -> tuple[Any, float]:
        start = time.time()
        result = func(*args)
        end = time.time()
        return result, end - start
    
    # 性能测试
    print("性能比较:")
    n = 35
    
    result1, time1 = time_function(fibonacci_memo, n)
    print(f"记忆化递归 fibonacci({n}): {result1}, 时间: {time1:.4f}s")
    
    result2, time2 = time_function(fibonacci_iterative, n)
    print(f"迭代版本 fibonacci({n}): {result2}, 时间: {time2:.4f}s")
    
    print(f"\n性能提升: {time1/time2:.2f}倍" if time2 > 0 else "")
    
    # 测试尾递归
    print(f"\n尾递归阶乘 factorial(10): {factorial_tail(10)}")
    
    # 测试深度限制
    print("\n深度限制测试:")
    nested = [1, [2, [3, [4, [5]]]]]
    try:
        result = deep_sum(nested, max_depth=5)
        print(f"嵌套列表求和: {result}")
    except RecursionError as e:
        print(f"递归错误: {e}")
    
    # 测试过深的嵌套
    very_nested = [1]
    for i in range(15):
        very_nested = [very_nested, i]
    
    try:
        result = deep_sum(very_nested, max_depth=10)
        print(f"过深嵌套求和: {result}")
    except RecursionError as e:
        print(f"递归深度限制生效: {e}")

# ============================================================================
# 7. 函数式编程练习答案
# ============================================================================

def solution_7_1():
    """练习7.1：高阶函数 - 参考答案"""
    print("\n解答7.1：高阶函数")
    
    # 数据准备
    students = [
        {"name": "Alice", "age": 20, "scores": [85, 92, 78]},
        {"name": "Bob", "age": 22, "scores": [90, 88, 94]},
        {"name": "Charlie", "age": 19, "scores": [76, 85, 89]},
        {"name": "Diana", "age": 21, "scores": [95, 91, 87]}
    ]
    
    def calculate_averages(students: List[Dict]) -> List[Dict]:
        """使用map计算每个学生的平均分"""
        def add_average(student):
            avg = sum(student["scores"]) / len(student["scores"])
            return {**student, "average": avg}
        
        return list(map(add_average, students))
    
    def find_excellent_students(students: List[Dict]) -> List[Dict]:
        """使用filter找出优秀学生（平均分>=90）"""
        students_with_avg = calculate_averages(students)
        return list(filter(lambda s: s["average"] >= 90, students_with_avg))
    
    def calculate_overall_average(students: List[Dict]) -> float:
        """使用reduce计算所有学生的总平均分"""
        from functools import reduce
        
        students_with_avg = calculate_averages(students)
        total_avg = reduce(
            lambda acc, student: acc + student["average"], 
            students_with_avg, 
            0
        )
        return total_avg / len(students_with_avg)
    
    def my_map(func: Callable, iterable) -> List:
        """自定义map函数"""
        result = []
        for item in iterable:
            result.append(func(item))
        return result
    
    def compose(*functions: Callable) -> Callable:
        """函数组合"""
        from functools import reduce
        return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)
    
    def curry(func: Callable) -> Callable:
        """柯里化函数"""
        import inspect
        sig = inspect.signature(func)
        param_count = len(sig.parameters)
        
        def curried(*args):
            if len(args) >= param_count:
                return func(*args[:param_count])
            else:
                return lambda *more_args: curried(*(args + more_args))
        
        return curried
    
    # 测试用例
    print("学生数据处理:")
    averages = calculate_averages(students)
    for student in averages:
        print(f"{student['name']}: {student['average']:.2f}")
    
    print("\n优秀学生:")
    excellent = find_excellent_students(students)
    for student in excellent:
        print(f"{student['name']}: {student['average']:.2f}")
    
    overall = calculate_overall_average(students)
    print(f"\n总平均分: {overall:.2f}")
    
    print("\n自定义map测试:")
    numbers = [1, 2, 3, 4, 5]
    squared = my_map(lambda x: x ** 2, numbers)
    print(f"平方: {squared}")
    
    print("\n函数组合测试:")
    add_one = lambda x: x + 1
    multiply_two = lambda x: x * 2
    square = lambda x: x ** 2
    
    composed = compose(square, multiply_two, add_one)
    print(f"compose(square, *2, +1)(3) = {composed(3)}")
    
    print("\n柯里化测试:")
    def add_three(a, b, c):
        return a + b + c
    
    curried_add = curry(add_three)
    print(f"curried_add(1)(2)(3) = {curried_add(1)(2)(3)}")
    print(f"curried_add(1, 2)(3) = {curried_add(1, 2)(3)}")

def solution_7_2():
    """练习7.2：函数式数据处理 - 参考答案"""
    print("\n解答7.2：函数式数据处理")
    
    class Pipeline:
        """数据处理管道"""
        def __init__(self, data):
            self._data = data
        
        def map(self, func: Callable) -> 'Pipeline':
            """映射操作"""
            return Pipeline([func(item) for item in self._data])
        
        def filter(self, predicate: Callable) -> 'Pipeline':
            """过滤操作"""
            return Pipeline([item for item in self._data if predicate(item)])
        
        def reduce(self, func: Callable, initial=None) -> 'Pipeline':
            """归约操作"""
            from functools import reduce as func_reduce
            if initial is None:
                result = func_reduce(func, self._data)
            else:
                result = func_reduce(func, self._data, initial)
            return Pipeline(result)
        
        def collect(self):
            """收集结果"""
            return self._data
    
    class Maybe:
        """Maybe单子用于错误处理"""
        def __init__(self, value):
            self._value = value
        
        def map(self, func: Callable) -> 'Maybe':
            """映射操作"""
            if self.is_nothing:
                return self
            try:
                return Maybe(func(self._value))
            except Exception:
                return Maybe(None)
        
        def flat_map(self, func: Callable) -> 'Maybe':
            """平坦映射"""
            if self.is_nothing:
                return self
            try:
                result = func(self._value)
                return result if isinstance(result, Maybe) else Maybe(result)
            except Exception:
                return Maybe(None)
        
        @property
        def value(self):
            """获取值"""
            return self._value
        
        @property
        def is_nothing(self) -> bool:
            """是否为空值"""
            return self._value is None
        
        def __repr__(self):
            return f"Maybe({self._value})"
    
    # 测试数据处理管道
    print("数据处理管道测试:")
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    result = (Pipeline(data)
              .filter(lambda x: x % 2 == 0)  # 过滤偶数
              .map(lambda x: x ** 2)         # 平方
              .reduce(lambda acc, x: acc + x, 0)  # 求和
              .collect())
    
    print(f"管道处理结果: {result}")
    
    # 更复杂的管道
    words = ["hello", "world", "python", "programming", "functional"]
    word_stats = (Pipeline(words)
                  .filter(lambda w: len(w) > 5)  # 长度大于5
                  .map(lambda w: w.upper())       # 转大写
                  .map(lambda w: (w, len(w)))     # 添加长度信息
                  .collect())
    
    print(f"单词统计: {word_stats}")
    
    # 测试Maybe单子
    print("\nMaybe单子测试:")
    
    def safe_divide(x, y):
        return Maybe(x / y if y != 0 else None)
    
    def safe_sqrt(x):
        import math
        return Maybe(math.sqrt(x) if x >= 0 else None)
    
    # 安全的链式计算
    result1 = (Maybe(16)
               .flat_map(lambda x: safe_sqrt(x))  # 开方
               .map(lambda x: x * 2)              # 乘2
               .flat_map(lambda x: safe_divide(x, 2)))  # 除2
    
    print(f"安全计算结果: {result1}")
    
    # 处理错误情况
    result2 = (Maybe(-16)
               .flat_map(lambda x: safe_sqrt(x))  # 负数开方失败
               .map(lambda x: x * 2))
    
    print(f"错误处理结果: {result2}")
    
    # 链式处理列表
    numbers = [1, 4, 9, 16, 25]
    safe_results = []
    
    for num in numbers:
        result = (Maybe(num)
                  .flat_map(lambda x: safe_sqrt(x))
                  .map(lambda x: round(x, 2)))
        safe_results.append(result.value if not result.is_nothing else "错误")
    
    print(f"批量安全处理: {safe_results}")

# ============================================================================
# 8. 综合应用练习答案
# ============================================================================

def solution_8_1():
    """练习8.1：函数式计算器 - 参考答案"""
    print("\n解答8.1：函数式计算器")
    
    class Calculator:
        """函数式计算器"""
        def __init__(self, initial_value: float = 0):
            self._value = initial_value
            self._history = [initial_value]
        
        def add(self, value: float) -> 'Calculator':
            """加法"""
            self._value += value
            self._history.append(self._value)
            return self
        
        def subtract(self, value: float) -> 'Calculator':
            """减法"""
            self._value -= value
            self._history.append(self._value)
            return self
        
        def multiply(self, value: float) -> 'Calculator':
            """乘法"""
            self._value *= value
            self._history.append(self._value)
            return self
        
        def divide(self, value: float) -> 'Calculator':
            """除法"""
            if value == 0:
                raise ValueError("除数不能为0")
            self._value /= value
            self._history.append(self._value)
            return self
        
        def power(self, exponent: float) -> 'Calculator':
            """幂运算"""
            self._value **= exponent
            self._history.append(self._value)
            return self
        
        def sqrt(self) -> 'Calculator':
            """开方"""
            import math
            if self._value < 0:
                raise ValueError("负数不能开方")
            self._value = math.sqrt(self._value)
            self._history.append(self._value)
            return self
        
        def apply(self, func: Callable[[float], float]) -> 'Calculator':
            """应用自定义函数"""
            self._value = func(self._value)
            self._history.append(self._value)
            return self
        
        def result(self) -> float:
            """获取结果"""
            return self._value
        
        def history(self) -> List[float]:
            """获取历史记录"""
            return self._history.copy()
        
        def reset(self, value: float = 0) -> 'Calculator':
            """重置"""
            self._value = value
            self._history = [value]
            return self
        
        def undo(self) -> 'Calculator':
            """撤销上一步操作"""
            if len(self._history) > 1:
                self._history.pop()
                self._value = self._history[-1]
            return self
    
    # 测试计算器
    print("函数式计算器测试:")
    calc = Calculator(10)
    
    result = (calc
              .add(5)        # 10 + 5 = 15
              .multiply(2)   # 15 * 2 = 30
              .subtract(10)  # 30 - 10 = 20
              .divide(4)     # 20 / 4 = 5
              .power(2)      # 5^2 = 25
              .sqrt()        # √25 = 5
              .result())
    
    print(f"链式计算结果: {result}")
    print(f"计算历史: {calc.history()}")
    
    # 使用自定义函数
    calc2 = Calculator(3)
    result2 = (calc2
               .apply(lambda x: x * 3)  # 自定义乘3
               .apply(lambda x: x + 1)  # 自定义加1
               .result())
    
    print(f"自定义函数结果: {result2}")
    
    # 撤销操作
    calc3 = Calculator(100)
    calc3.add(50).multiply(2)  # 100 + 50 = 150, 150 * 2 = 300
    print(f"撤销前: {calc3.result()}")
    calc3.undo()  # 撤销乘法
    print(f"撤销后: {calc3.result()}")

def solution_8_2():
    """练习8.2：配置管理系统 - 参考答案"""
    print("\n解答8.2：配置管理系统")
    
    class ConfigManager:
        """配置管理器"""
        def __init__(self):
            self._config = {}
            self._validators = {}
            self._transformers = {}
            self._defaults = {}
        
        def set_default(self, key: str, value: Any) -> 'ConfigManager':
            """设置默认值"""
            self._defaults[key] = value
            return self
        
        def add_validator(self, key: str, validator: Callable[[Any], bool]) -> 'ConfigManager':
            """添加验证器"""
            self._validators[key] = validator
            return self
        
        def add_transformer(self, key: str, transformer: Callable[[Any], Any]) -> 'ConfigManager':
            """添加转换器"""
            self._transformers[key] = transformer
            return self
        
        def set(self, key: str, value: Any) -> 'ConfigManager':
            """设置配置值"""
            # 应用转换器
            if key in self._transformers:
                value = self._transformers[key](value)
            
            # 验证值
            if key in self._validators:
                if not self._validators[key](value):
                    raise ValueError(f"配置项 {key} 的值 {value} 验证失败")
            
            self._config[key] = value
            return self
        
        def get(self, key: str, default: Any = None) -> Any:
            """获取配置值"""
            if key in self._config:
                return self._config[key]
            elif key in self._defaults:
                return self._defaults[key]
            else:
                return default
        
        def load_from_dict(self, config_dict: Dict[str, Any]) -> 'ConfigManager':
            """从字典加载配置"""
            for key, value in config_dict.items():
                self.set(key, value)
            return self
        
        def to_dict(self) -> Dict[str, Any]:
            """转换为字典"""
            result = self._defaults.copy()
            result.update(self._config)
            return result
        
        def validate_all(self) -> List[str]:
            """验证所有配置"""
            errors = []
            all_config = self.to_dict()
            
            for key, validator in self._validators.items():
                if key in all_config:
                    if not validator(all_config[key]):
                        errors.append(f"配置项 {key} 验证失败")
                else:
                    errors.append(f"必需的配置项 {key} 缺失")
            
            return errors
    
    # 创建配置管理器实例
    config = ConfigManager()
    
    # 设置默认值
    config.set_default("host", "localhost")
    config.set_default("port", 8080)
    config.set_default("debug", False)
    
    # 添加验证器
    config.add_validator("port", lambda x: isinstance(x, int) and 1 <= x <= 65535)
    config.add_validator("host", lambda x: isinstance(x, str) and len(x) > 0)
    config.add_validator("debug", lambda x: isinstance(x, bool))
    
    # 添加转换器
    config.add_transformer("port", lambda x: int(x) if isinstance(x, str) else x)
    config.add_transformer("debug", lambda x: str(x).lower() in ['true', '1', 'yes'] if isinstance(x, str) else x)
    
    # 测试配置管理
    print("配置管理测试:")
    
    # 设置配置
    config.set("host", "0.0.0.0")
    config.set("port", "9000")  # 字符串会被转换为整数
    config.set("debug", "true")  # 字符串会被转换为布尔值
    
    print(f"主机: {config.get('host')}")
    print(f"端口: {config.get('port')}")
    print(f"调试: {config.get('debug')}")
    print(f"数据库: {config.get('database', 'sqlite')}")
    
    # 批量加载配置
    new_config = {
        "host": "127.0.0.1",
        "port": 3000,
        "timeout": 30
    }
    config.load_from_dict(new_config)
    
    print(f"\n更新后的配置: {config.to_dict()}")
    
    # 验证配置
    errors = config.validate_all()
    if errors:
        print(f"配置错误: {errors}")
    else:
        print("所有配置验证通过")
    
    # 测试验证失败
    try:
        config.set("port", 70000)  # 超出端口范围
    except ValueError as e:
        print(f"验证错误: {e}")

# ============================================================================
# 运行所有解答
# ============================================================================

if __name__ == "__main__":
    # 运行所有练习解答
    solution_1_1()
    solution_1_2()
    solution_2_1()
    solution_2_2()
    solution_2_3()
    solution_3_1()
    solution_3_2()
    solution_4_1()
    solution_4_2()
    solution_5_1()
    solution_5_2()
    solution_6_1()
    solution_6_2()
    solution_7_1()
    solution_7_2()
    solution_8_1()
    solution_8_2()
    
    print("\n" + "=" * 50)
    print("函数练习题解答完成！")
    print("=" * 50)
    
    print("\n学习要点总结:")
    print("1. 函数设计原则：单一职责、参数验证、错误处理")
    print("2. 参数类型：位置参数、关键字参数、默认参数、可变参数")
    print("3. 作用域管理：局部作用域、全局作用域、闭包")
    print("4. 装饰器应用：功能增强、代码复用、关注点分离")
    print("5. 递归优化：记忆化、尾递归、迭代替代")
    print("6. 函数式编程：高阶函数、纯函数、不可变性")
    print("7. 实际应用：配置管理、数据处理、错误处理")
    
    print("\n编程最佳实践:")
    print("• 编写清晰的函数文档和类型提示")
    print("• 保持函数简洁，避免过长的函数")
    print("• 使用有意义的函数名和参数名")
    print("• 合理使用默认参数，避免可变默认参数")
    print("• 优先使用纯函数，减少副作用")
    print("• 适当使用装饰器增强功能")
    print("• 注意递归深度，考虑性能优化")
    print("• 利用函数式编程提高代码可读性");
