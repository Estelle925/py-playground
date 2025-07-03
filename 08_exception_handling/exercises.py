#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理练习题

本文件包含了Python异常处理的各种练习题，涵盖：
1. 基本异常处理
2. 自定义异常
3. 异常处理最佳实践
4. 高级异常处理技术
5. 实际应用场景

每个练习都有详细的要求说明，请按照要求完成相应的代码。
"""

print("=" * 60)
print("异常处理练习题")
print("=" * 60)

# ============================================================================
# 练习1：基本异常处理
# ============================================================================

print("\n练习1：基本异常处理")
print("-" * 30)

# 练习1.1：安全的数学计算器
def exercise_1_1():
    """
    练习1.1：实现一个安全的数学计算器
    
    要求：
    1. 实现一个Calculator类，包含add、subtract、multiply、divide方法
    2. divide方法需要处理除零错误
    3. 所有方法都需要处理类型错误（非数字输入）
    4. 使用适当的异常处理，并返回有意义的错误信息
    5. 实现一个safe_calculate方法，接受操作符和两个操作数
    
    示例：
    calc = Calculator()
    result = calc.safe_calculate('+', 10, 5)  # 返回15
    result = calc.safe_calculate('/', 10, 0)  # 返回错误信息
    """
    print("\n练习1.1：安全的数学计算器")
    
    # TODO: 在这里实现Calculator类
    class Calculator:
        pass
    
    # 测试代码
    calc = Calculator()
    test_cases = [
        ('+', 10, 5),
        ('-', 10, 5),
        ('*', 10, 5),
        ('/', 10, 5),
        ('/', 10, 0),  # 除零错误
        ('+', '10', 5),  # 类型错误
        ('%', 10, 5),  # 不支持的操作
    ]
    
    for op, a, b in test_cases:
        try:
            result = calc.safe_calculate(op, a, b)
            print(f"{a} {op} {b} = {result}")
        except Exception as e:
            print(f"计算 {a} {op} {b} 时发生错误：{e}")

# 练习1.2：文件读取器
def exercise_1_2():
    """
    练习1.2：实现一个安全的文件读取器
    
    要求：
    1. 实现一个FileReader类
    2. 包含read_file方法，能够安全地读取文件内容
    3. 处理文件不存在、权限不足、编码错误等异常
    4. 提供默认值选项
    5. 使用上下文管理器确保文件正确关闭
    6. 实现read_json方法，专门处理JSON文件
    
    示例：
    reader = FileReader()
    content = reader.read_file('test.txt', default='文件不存在')
    data = reader.read_json('config.json', default={})
    """
    print("\n练习1.2：文件读取器")
    
    # TODO: 在这里实现FileReader类
    class FileReader:
        pass
    
    # 测试代码
    reader = FileReader()
    
    # 创建测试文件
    test_files = {
        'test.txt': '这是测试文件内容',
        'config.json': '{"name": "test", "version": "1.0"}',
        'invalid.json': '{"name": "test", "version":}',  # 无效JSON
    }
    
    for filename, content in test_files.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"创建测试文件失败：{e}")
    
    # 测试文件读取
    test_cases = [
        ('test.txt', None),
        ('nonexistent.txt', '默认内容'),
        ('config.json', None),
        ('invalid.json', {}),
        ('nonexistent.json', {'default': True}),
    ]
    
    for filename, default in test_cases:
        if filename.endswith('.json'):
            result = reader.read_json(filename, default=default)
            print(f"读取JSON {filename}：{result}")
        else:
            result = reader.read_file(filename, default=default)
            print(f"读取文件 {filename}：{result}")
    
    # 清理测试文件
    import os
    for filename in test_files.keys():
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

# ============================================================================
# 练习2：自定义异常
# ============================================================================

print("\n练习2：自定义异常")
print("-" * 30)

# 练习2.1：银行账户系统
def exercise_2_1():
    """
    练习2.1：实现一个银行账户系统的异常处理
    
    要求：
    1. 定义以下自定义异常：
       - InsufficientFundsError：余额不足
       - InvalidAmountError：无效金额（负数或零）
       - AccountNotFoundError：账户不存在
       - AccountFrozenError：账户被冻结
    2. 实现BankAccount类，包含：
       - 账户号、余额、状态（正常/冻结）
       - deposit（存款）、withdraw（取款）方法
       - freeze（冻结）、unfreeze（解冻）方法
    3. 实现Bank类，管理多个账户：
       - 创建账户、查找账户
       - 转账功能（从一个账户转到另一个账户）
    4. 所有操作都要有适当的异常处理
    
    示例：
    bank = Bank()
    account1 = bank.create_account('123456', 1000)
    account2 = bank.create_account('789012', 500)
    bank.transfer('123456', '789012', 200)  # 转账
    """
    print("\n练习2.1：银行账户系统")
    
    # TODO: 在这里定义自定义异常
    class BankError(Exception):
        """银行系统异常基类"""
        pass
    
    class InsufficientFundsError(BankError):
        pass
    
    # TODO: 定义其他异常类
    
    # TODO: 在这里实现BankAccount类
    class BankAccount:
        pass
    
    # TODO: 在这里实现Bank类
    class Bank:
        pass
    
    # 测试代码
    try:
        bank = Bank()
        
        # 创建账户
        account1 = bank.create_account('123456', 1000)
        account2 = bank.create_account('789012', 500)
        
        print(f"账户1余额：{account1.balance}")
        print(f"账户2余额：{account2.balance}")
        
        # 测试存款
        account1.deposit(200)
        print(f"存款后账户1余额：{account1.balance}")
        
        # 测试取款
        account1.withdraw(300)
        print(f"取款后账户1余额：{account1.balance}")
        
        # 测试转账
        bank.transfer('123456', '789012', 400)
        print(f"转账后账户1余额：{account1.balance}")
        print(f"转账后账户2余额：{account2.balance}")
        
        # 测试异常情况
        try:
            account1.withdraw(2000)  # 余额不足
        except InsufficientFundsError as e:
            print(f"取款失败：{e}")
        
        try:
            account1.deposit(-100)  # 无效金额
        except Exception as e:
            print(f"存款失败：{e}")
        
        # 测试冻结账户
        account1.freeze()
        try:
            account1.withdraw(100)  # 账户被冻结
        except Exception as e:
            print(f"冻结账户取款失败：{e}")
        
    except Exception as e:
        print(f"银行系统错误：{e}")

# 练习2.2：用户认证系统
def exercise_2_2():
    """
    练习2.2：实现一个用户认证系统
    
    要求：
    1. 定义以下自定义异常：
       - AuthenticationError：认证失败基类
       - InvalidCredentialsError：用户名或密码错误
       - AccountLockedError：账户被锁定
       - PasswordExpiredError：密码已过期
       - TooManyAttemptsError：尝试次数过多
    2. 实现User类，包含：
       - 用户名、密码哈希、锁定状态、失败尝试次数
       - 密码过期时间
    3. 实现AuthenticationSystem类：
       - 用户注册、登录
       - 密码验证、账户锁定逻辑
       - 失败尝试计数（3次失败后锁定）
    4. 实现密码强度验证
    
    示例：
    auth = AuthenticationSystem()
    auth.register('user1', 'StrongPass123!')
    auth.login('user1', 'StrongPass123!')  # 成功
    auth.login('user1', 'wrongpass')  # 失败
    """
    print("\n练习2.2：用户认证系统")
    
    # TODO: 在这里定义认证相关的异常
    class AuthenticationError(Exception):
        pass
    
    # TODO: 定义其他异常类
    
    # TODO: 在这里实现User类
    class User:
        pass
    
    # TODO: 在这里实现AuthenticationSystem类
    class AuthenticationSystem:
        pass
    
    # 测试代码
    try:
        auth = AuthenticationSystem()
        
        # 测试用户注册
        print("注册用户...")
        auth.register('alice', 'StrongPass123!')
        auth.register('bob', 'AnotherPass456@')
        
        # 测试成功登录
        print("\n测试成功登录...")
        result = auth.login('alice', 'StrongPass123!')
        print(f"登录结果：{result}")
        
        # 测试失败登录
        print("\n测试失败登录...")
        for i in range(4):  # 尝试4次错误密码
            try:
                auth.login('alice', 'wrongpassword')
            except AuthenticationError as e:
                print(f"登录尝试{i+1}失败：{e}")
        
        # 测试弱密码注册
        print("\n测试弱密码注册...")
        try:
            auth.register('charlie', '123')  # 弱密码
        except Exception as e:
            print(f"注册失败：{e}")
        
    except Exception as e:
        print(f"认证系统错误：{e}")

# ============================================================================
# 练习3：高级异常处理
# ============================================================================

print("\n练习3：高级异常处理")
print("-" * 30)

# 练习3.1：重试装饰器
def exercise_3_1():
    """
    练习3.1：实现一个通用的重试装饰器
    
    要求：
    1. 实现retry装饰器，支持以下参数：
       - max_attempts：最大重试次数
       - delay：重试间隔（秒）
       - backoff：退避策略（linear/exponential）
       - exceptions：需要重试的异常类型
       - on_retry：重试时的回调函数
    2. 支持指数退避和线性退避
    3. 记录重试日志
    4. 在最后一次失败后抛出原始异常
    
    示例：
    @retry(max_attempts=3, delay=1, backoff='exponential')
    def unreliable_function():
        # 可能失败的函数
        pass
    """
    print("\n练习3.1：重试装饰器")
    
    import time
    import random
    from functools import wraps
    
    # TODO: 在这里实现retry装饰器
    def retry(max_attempts=3, delay=1, backoff='linear', 
              exceptions=(Exception,), on_retry=None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # TODO: 实现重试逻辑
                pass
            return wrapper
        return decorator
    
    # 测试函数
    @retry(max_attempts=3, delay=0.5, backoff='exponential', 
           exceptions=(ConnectionError, TimeoutError))
    def unreliable_network_call(success_rate=0.3):
        """模拟不可靠的网络调用"""
        if random.random() < success_rate:
            return "网络调用成功"
        else:
            error_type = random.choice([ConnectionError, TimeoutError])
            raise error_type("网络调用失败")
    
    @retry(max_attempts=2, delay=0.2)
    def flaky_database_operation():
        """模拟不稳定的数据库操作"""
        if random.random() < 0.6:
            return "数据库操作成功"
        else:
            raise RuntimeError("数据库连接失败")
    
    # 测试重试装饰器
    print("测试网络调用重试：")
    try:
        result = unreliable_network_call(success_rate=0.7)
        print(f"结果：{result}")
    except Exception as e:
        print(f"最终失败：{e}")
    
    print("\n测试数据库操作重试：")
    try:
        result = flaky_database_operation()
        print(f"结果：{result}")
    except Exception as e:
        print(f"最终失败：{e}")

# 练习3.2：异常聚合器
def exercise_3_2():
    """
    练习3.2：实现一个异常聚合器
    
    要求：
    1. 实现ExceptionAggregator类，能够：
       - 收集多个操作中的异常
       - 在所有操作完成后统一处理异常
       - 支持继续执行模式和快速失败模式
    2. 实现上下文管理器接口
    3. 提供异常统计和报告功能
    4. 支持异常过滤和分类
    
    示例：
    with ExceptionAggregator(fail_fast=False) as agg:
        agg.execute(lambda: risky_operation1())
        agg.execute(lambda: risky_operation2())
        agg.execute(lambda: risky_operation3())
    # 在这里处理所有收集到的异常
    """
    print("\n练习3.2：异常聚合器")
    
    # TODO: 在这里实现ExceptionAggregator类
    class ExceptionAggregator:
        def __init__(self, fail_fast=True):
            pass
        
        def execute(self, func, *args, **kwargs):
            """执行函数并收集异常"""
            pass
        
        def __enter__(self):
            pass
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        
        def get_exceptions(self):
            """获取收集到的异常"""
            pass
        
        def get_statistics(self):
            """获取异常统计"""
            pass
    
    # 测试函数
    def operation1():
        raise ValueError("操作1失败")
    
    def operation2():
        return "操作2成功"
    
    def operation3():
        raise ConnectionError("操作3网络错误")
    
    def operation4():
        raise ValueError("操作4验证失败")
    
    # 测试快速失败模式
    print("测试快速失败模式：")
    try:
        with ExceptionAggregator(fail_fast=True) as agg:
            agg.execute(operation2)
            agg.execute(operation1)  # 这里应该立即失败
            agg.execute(operation3)  # 不应该执行到这里
    except Exception as e:
        print(f"快速失败：{e}")
    
    # 测试继续执行模式
    print("\n测试继续执行模式：")
    try:
        with ExceptionAggregator(fail_fast=False) as agg:
            agg.execute(operation1)
            agg.execute(operation2)
            agg.execute(operation3)
            agg.execute(operation4)
        
        # 这里不应该到达，因为有异常
        print("所有操作完成")
    except Exception as e:
        print(f"聚合异常：{e}")
        # TODO: 显示异常统计

# ============================================================================
# 练习4：实际应用场景
# ============================================================================

print("\n练习4：实际应用场景")
print("-" * 30)

# 练习4.1：Web API客户端
def exercise_4_1():
    """
    练习4.1：实现一个健壮的Web API客户端
    
    要求：
    1. 实现APIClient类，支持：
       - GET、POST、PUT、DELETE请求
       - 自动重试机制
       - 超时处理
       - 错误状态码处理
    2. 定义API相关的异常：
       - APIError：API错误基类
       - HTTPError：HTTP错误
       - TimeoutError：超时错误
       - RateLimitError：限流错误
    3. 实现请求日志记录
    4. 支持认证（API Key）
    5. 实现响应缓存（简单的内存缓存）
    
    示例：
    client = APIClient('https://api.example.com', api_key='secret')
    data = client.get('/users/123')
    result = client.post('/users', {'name': 'John', 'email': 'john@example.com'})
    """
    print("\n练习4.1：Web API客户端")
    
    import json
    import time
    from urllib.parse import urljoin
    
    # TODO: 定义API相关异常
    class APIError(Exception):
        pass
    
    # TODO: 定义其他异常类
    
    # TODO: 实现APIClient类
    class APIClient:
        def __init__(self, base_url, api_key=None, timeout=30, max_retries=3):
            pass
        
        def get(self, endpoint, params=None):
            """GET请求"""
            pass
        
        def post(self, endpoint, data=None):
            """POST请求"""
            pass
        
        def put(self, endpoint, data=None):
            """PUT请求"""
            pass
        
        def delete(self, endpoint):
            """DELETE请求"""
            pass
        
        def _make_request(self, method, endpoint, data=None, params=None):
            """发起HTTP请求"""
            pass
    
    # 测试代码
    try:
        # 创建API客户端
        client = APIClient('https://jsonplaceholder.typicode.com', timeout=10)
        
        # 测试GET请求
        print("测试GET请求：")
        try:
            users = client.get('/users')
            print(f"获取到{len(users)}个用户")
        except APIError as e:
            print(f"GET请求失败：{e}")
        
        # 测试POST请求
        print("\n测试POST请求：")
        try:
            new_user = {
                'name': 'Test User',
                'email': 'test@example.com',
                'username': 'testuser'
            }
            result = client.post('/users', new_user)
            print(f"创建用户成功：{result.get('id')}")
        except APIError as e:
            print(f"POST请求失败：{e}")
        
        # 测试错误处理
        print("\n测试错误处理：")
        try:
            # 请求不存在的端点
            client.get('/nonexistent')
        except APIError as e:
            print(f"预期的错误：{e}")
        
    except Exception as e:
        print(f"API客户端测试失败：{e}")

# 练习4.2：数据验证框架
def exercise_4_2():
    """
    练习4.2：实现一个数据验证框架
    
    要求：
    1. 实现Validator基类和具体验证器：
       - RequiredValidator：必填验证
       - TypeValidator：类型验证
       - RangeValidator：范围验证
       - PatternValidator：正则表达式验证
       - CustomValidator：自定义验证
    2. 实现ValidationError异常，包含：
       - 字段名、错误消息、错误代码
       - 支持多个错误的聚合
    3. 实现Schema类，支持：
       - 字段定义和验证规则
       - 嵌套对象验证
       - 数组验证
    4. 提供友好的错误报告
    
    示例：
    schema = Schema({
        'name': [RequiredValidator(), TypeValidator(str)],
        'age': [RequiredValidator(), TypeValidator(int), RangeValidator(0, 150)],
        'email': [RequiredValidator(), PatternValidator(r'^[\w\.-]+@[\w\.-]+\.\w+$')]
    })
    
    try:
        schema.validate({'name': 'John', 'age': 25, 'email': 'john@example.com'})
    except ValidationError as e:
        print(e.get_error_report())
    """
    print("\n练习4.2：数据验证框架")
    
    import re
    from abc import ABC, abstractmethod
    
    # TODO: 定义验证相关异常
    class ValidationError(Exception):
        def __init__(self, field=None, message=None, code=None):
            pass
        
        def add_error(self, field, message, code=None):
            """添加错误"""
            pass
        
        def get_error_report(self):
            """获取错误报告"""
            pass
    
    # TODO: 实现验证器基类
    class Validator(ABC):
        @abstractmethod
        def validate(self, value, field_name=None):
            pass
    
    # TODO: 实现具体验证器
    class RequiredValidator(Validator):
        pass
    
    class TypeValidator(Validator):
        def __init__(self, expected_type):
            pass
    
    class RangeValidator(Validator):
        def __init__(self, min_value=None, max_value=None):
            pass
    
    class PatternValidator(Validator):
        def __init__(self, pattern):
            pass
    
    class CustomValidator(Validator):
        def __init__(self, validate_func, message="自定义验证失败"):
            pass
    
    # TODO: 实现Schema类
    class Schema:
        def __init__(self, field_validators):
            pass
        
        def validate(self, data):
            """验证数据"""
            pass
    
    # 测试代码
    try:
        # 定义验证模式
        user_schema = Schema({
            'name': [RequiredValidator(), TypeValidator(str)],
            'age': [RequiredValidator(), TypeValidator(int), RangeValidator(0, 150)],
            'email': [RequiredValidator(), PatternValidator(r'^[\w\.-]+@[\w\.-]+\.\w+$')],
            'score': [TypeValidator((int, float)), RangeValidator(0, 100)],
        })
        
        # 测试有效数据
        print("测试有效数据：")
        valid_data = {
            'name': 'Alice',
            'age': 25,
            'email': 'alice@example.com',
            'score': 95.5
        }
        
        try:
            user_schema.validate(valid_data)
            print("验证通过")
        except ValidationError as e:
            print(f"验证失败：{e.get_error_report()}")
        
        # 测试无效数据
        print("\n测试无效数据：")
        invalid_data = {
            'name': '',  # 空字符串
            'age': -5,   # 负数
            'email': 'invalid-email',  # 无效邮箱
            'score': 150  # 超出范围
        }
        
        try:
            user_schema.validate(invalid_data)
            print("验证通过")
        except ValidationError as e:
            print(f"验证失败：\n{e.get_error_report()}")
        
        # 测试缺失字段
        print("\n测试缺失字段：")
        incomplete_data = {
            'name': 'Bob'
            # 缺少age和email
        }
        
        try:
            user_schema.validate(incomplete_data)
            print("验证通过")
        except ValidationError as e:
            print(f"验证失败：\n{e.get_error_report()}")
        
    except Exception as e:
        print(f"验证框架测试失败：{e}")

# ============================================================================
# 练习5：综合应用
# ============================================================================

print("\n练习5：综合应用")
print("-" * 30)

# 练习5.1：任务调度系统
def exercise_5_1():
    """
    练习5.1：实现一个任务调度系统
    
    要求：
    1. 实现Task类，包含：
       - 任务ID、名称、执行函数、参数
       - 重试次数、超时时间
       - 状态（待执行、执行中、成功、失败）
    2. 实现TaskScheduler类，支持：
       - 添加任务、执行任务
       - 并发执行（使用线程）
       - 失败重试、超时处理
       - 任务依赖关系
    3. 定义任务相关异常：
       - TaskError：任务错误基类
       - TaskTimeoutError：任务超时
       - TaskDependencyError：依赖错误
    4. 实现任务执行报告
    
    示例：
    scheduler = TaskScheduler(max_workers=3)
    task1 = Task('task1', lambda: print('Task 1'), timeout=5)
    task2 = Task('task2', lambda: print('Task 2'), depends_on=['task1'])
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.run_all()
    """
    print("\n练习5.1：任务调度系统")
    
    import threading
    import time
    from enum import Enum
    from concurrent.futures import ThreadPoolExecutor, TimeoutError
    
    # TODO: 定义任务状态枚举
    class TaskStatus(Enum):
        PENDING = "pending"
        RUNNING = "running"
        SUCCESS = "success"
        FAILED = "failed"
        TIMEOUT = "timeout"
    
    # TODO: 定义任务相关异常
    class TaskError(Exception):
        pass
    
    # TODO: 实现Task类
    class Task:
        def __init__(self, task_id, func, args=None, kwargs=None, 
                     timeout=None, max_retries=0, depends_on=None):
            pass
        
        def execute(self):
            """执行任务"""
            pass
    
    # TODO: 实现TaskScheduler类
    class TaskScheduler:
        def __init__(self, max_workers=3):
            pass
        
        def add_task(self, task):
            """添加任务"""
            pass
        
        def run_all(self):
            """执行所有任务"""
            pass
        
        def get_report(self):
            """获取执行报告"""
            pass
    
    # 测试函数
    def quick_task(name, duration=1):
        print(f"开始执行任务：{name}")
        time.sleep(duration)
        print(f"任务完成：{name}")
        return f"结果：{name}"
    
    def failing_task(name):
        print(f"开始执行失败任务：{name}")
        raise RuntimeError(f"任务{name}失败")
    
    def timeout_task(name):
        print(f"开始执行超时任务：{name}")
        time.sleep(10)  # 模拟长时间运行
        return f"结果：{name}"
    
    # 测试任务调度器
    try:
        scheduler = TaskScheduler(max_workers=2)
        
        # 添加各种类型的任务
        tasks = [
            Task('task1', quick_task, args=['任务1'], timeout=5),
            Task('task2', quick_task, args=['任务2', 2], depends_on=['task1']),
            Task('task3', failing_task, args=['任务3'], max_retries=2),
            Task('task4', timeout_task, args=['任务4'], timeout=3),
            Task('task5', quick_task, args=['任务5'], depends_on=['task2']),
        ]
        
        for task in tasks:
            scheduler.add_task(task)
        
        print("开始执行所有任务...")
        scheduler.run_all()
        
        print("\n执行报告：")
        report = scheduler.get_report()
        print(report)
        
    except Exception as e:
        print(f"任务调度系统测试失败：{e}")

# 运行所有练习
if __name__ == "__main__":
    try:
        exercise_1_1()
        exercise_1_2()
        exercise_2_1()
        exercise_2_2()
        exercise_3_1()
        exercise_3_2()
        exercise_4_1()
        exercise_4_2()
        exercise_5_1()
        
        print("\n" + "=" * 60)
        print("所有练习题展示完成！")
        print("请根据要求完成每个练习的实现。")
        print("=" * 60)
        
    except Exception as e:
        print(f"练习执行过程中发生错误：{e}")
        import traceback
        traceback.print_exc()

print("\n=== 练习提示 ===")
print("""
完成这些练习时，请注意：

1. 基本异常处理
   - 使用具体的异常类型而不是通用的Exception
   - 提供有意义的错误消息
   - 合理使用else和finally子句

2. 自定义异常
   - 继承合适的异常基类
   - 包含足够的上下文信息
   - 使用清晰的异常层次结构

3. 高级技术
   - 实现装饰器时注意保留原函数的元数据
   - 使用上下文管理器确保资源正确释放
   - 考虑线程安全性

4. 实际应用
   - 记录详细的日志信息
   - 提供用户友好的错误消息
   - 考虑性能和可扩展性

5. 测试
   - 测试正常情况和异常情况
   - 验证错误消息的准确性
   - 确保资源正确清理
""")