#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理示例代码

本文件包含了Python异常处理的各种示例，包括：
1. 基本异常处理语法
2. 常见内置异常
3. 自定义异常
4. 异常处理最佳实践
5. 高级异常处理技术
6. 调试和诊断
7. 实际应用场景
"""

import logging
import sys
import traceback
import time
import json
from typing import Any, Dict, List, Optional, Union
from pathlib import Path
from contextlib import contextmanager
from functools import wraps

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

print("=" * 60)
print("异常处理示例代码")
print("=" * 60)

# ============================================================================
# 1. 基本异常处理语法
# ============================================================================

print("\n1. 基本异常处理语法")
print("-" * 30)

# 1.1 基本try-except
def basic_exception_handling():
    """基本异常处理示例"""
    print("\n1.1 基本try-except")
    
    # 处理除零错误
    try:
        result = 10 / 0
        print(f"结果：{result}")
    except ZeroDivisionError:
        print("错误：不能除以零")
    
    # 处理类型错误
    try:
        result = "hello" + 5
        print(f"结果：{result}")
    except TypeError as e:
        print(f"类型错误：{e}")
    
    # 处理多种异常
    try:
        numbers = [1, 2, 3]
        index = int(input("请输入索引（0-2）：") or "0")
        print(f"数字：{numbers[index]}")
    except ValueError:
        print("请输入有效的数字")
    except IndexError:
        print("索引超出范围")
    except Exception as e:
        print(f"其他错误：{e}")

# 1.2 else和finally子句
def else_finally_example():
    """else和finally子句示例"""
    print("\n1.2 else和finally子句")
    
    def divide_numbers(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("除零错误")
            return None
        except TypeError:
            print("类型错误")
            return None
        else:
            # 没有异常时执行
            print(f"计算成功：{a} / {b} = {result}")
            return result
        finally:
            # 无论是否有异常都执行
            print("计算完成")
    
    # 测试不同情况
    print("正常情况：")
    divide_numbers(10, 2)
    
    print("\n除零错误：")
    divide_numbers(10, 0)
    
    print("\n类型错误：")
    divide_numbers("10", 2)

# 1.3 处理多个异常类型
def multiple_exceptions_example():
    """处理多个异常类型示例"""
    print("\n1.3 处理多个异常类型")
    
    def process_data(data):
        try:
            # 尝试各种操作
            if not isinstance(data, (list, tuple)):
                raise TypeError("数据必须是列表或元组")
            
            if len(data) == 0:
                raise ValueError("数据不能为空")
            
            # 计算平均值
            total = sum(data)
            average = total / len(data)
            
            return average
            
        except (TypeError, ValueError) as e:
            # 处理多种异常
            print(f"数据错误：{e}")
            return None
        except Exception as e:
            # 处理其他异常
            print(f"未知错误：{e}")
            return None
    
    # 测试不同数据
    test_data = [
        [1, 2, 3, 4, 5],  # 正常数据
        [],               # 空列表
        "not a list",     # 错误类型
        [1, 2, "3", 4]    # 包含非数字
    ]
    
    for data in test_data:
        print(f"处理数据 {data}：")
        result = process_data(data)
        print(f"结果：{result}\n")

# 运行基本示例
basic_exception_handling()
else_finally_example()
multiple_exceptions_example()

# ============================================================================
# 2. 常见内置异常
# ============================================================================

print("\n2. 常见内置异常")
print("-" * 30)

# 2.1 数值相关异常
def numeric_exceptions():
    """数值相关异常示例"""
    print("\n2.1 数值相关异常")
    
    # ZeroDivisionError
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    
    # ValueError
    try:
        number = int("not_a_number")
    except ValueError as e:
        print(f"ValueError: {e}")
    
    # OverflowError（在某些情况下）
    try:
        import math
        result = math.exp(1000)  # 可能导致溢出
    except OverflowError as e:
        print(f"OverflowError: {e}")
    except Exception as e:
        print(f"其他数值错误: {e}")

# 2.2 类型和属性相关异常
def type_attribute_exceptions():
    """类型和属性相关异常示例"""
    print("\n2.2 类型和属性相关异常")
    
    # TypeError
    try:
        result = "hello" + 5
    except TypeError as e:
        print(f"TypeError: {e}")
    
    # AttributeError
    try:
        number = 42
        result = number.append(1)  # int没有append方法
    except AttributeError as e:
        print(f"AttributeError: {e}")
    
    # NameError
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")

# 2.3 索引和键相关异常
def index_key_exceptions():
    """索引和键相关异常示例"""
    print("\n2.3 索引和键相关异常")
    
    # IndexError
    try:
        my_list = [1, 2, 3]
        value = my_list[10]
    except IndexError as e:
        print(f"IndexError: {e}")
    
    # KeyError
    try:
        my_dict = {'a': 1, 'b': 2}
        value = my_dict['c']
    except KeyError as e:
        print(f"KeyError: {e}")
    
    # StopIteration
    try:
        my_iter = iter([1, 2, 3])
        while True:
            value = next(my_iter)
            print(f"迭代值：{value}")
    except StopIteration:
        print("迭代完成")

# 2.4 文件和IO相关异常
def file_io_exceptions():
    """文件和IO相关异常示例"""
    print("\n2.4 文件和IO相关异常")
    
    # FileNotFoundError
    try:
        with open('nonexistent_file.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    
    # PermissionError
    try:
        # 尝试写入只读文件（如果存在）
        with open('/etc/passwd', 'w') as f:
            f.write('test')
    except PermissionError as e:
        print(f"PermissionError: {e}")
    except FileNotFoundError:
        print("文件不存在（这是正常的）")
    
    # IOError/OSError
    try:
        # 模拟IO错误
        import os
        os.remove('nonexistent_file.txt')
    except OSError as e:
        print(f"OSError: {e}")

# 运行内置异常示例
numeric_exceptions()
type_attribute_exceptions()
index_key_exceptions()
file_io_exceptions()

# ============================================================================
# 3. 自定义异常
# ============================================================================

print("\n3. 自定义异常")
print("-" * 30)

# 3.1 基本自定义异常
class CustomError(Exception):
    """自定义异常基类"""
    pass

class ValidationError(CustomError):
    """数据验证异常"""
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value
        self.message = message
    
    def __str__(self):
        if self.field:
            return f"验证错误 [{self.field}]: {self.message}"
        return f"验证错误: {self.message}"

class BusinessLogicError(CustomError):
    """业务逻辑异常"""
    def __init__(self, message, error_code=None, details=None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details or {}
        self.message = message
    
    def __str__(self):
        if self.error_code:
            return f"业务错误 [{self.error_code}]: {self.message}"
        return f"业务错误: {self.message}"

class ConfigurationError(CustomError):
    """配置错误异常"""
    def __init__(self, message, config_key=None, config_file=None):
        super().__init__(message)
        self.config_key = config_key
        self.config_file = config_file
        self.message = message
    
    def __str__(self):
        parts = ["配置错误"]
        if self.config_file:
            parts.append(f"文件: {self.config_file}")
        if self.config_key:
            parts.append(f"键: {self.config_key}")
        parts.append(self.message)
        return " - ".join(parts)

# 3.2 使用自定义异常的示例
def custom_exception_examples():
    """自定义异常使用示例"""
    print("\n3.1 自定义异常示例")
    
    def validate_user_data(data):
        """验证用户数据"""
        if not isinstance(data, dict):
            raise ValidationError("数据必须是字典类型")
        
        # 验证必需字段
        required_fields = ['name', 'email', 'age']
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"缺少必需字段", field=field)
        
        # 验证邮箱格式
        email = data['email']
        if '@' not in email:
            raise ValidationError("邮箱格式无效", field='email', value=email)
        
        # 验证年龄
        age = data['age']
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValidationError("年龄必须是0-150之间的整数", field='age', value=age)
        
        return True
    
    def process_business_logic(user_id, amount):
        """处理业务逻辑"""
        if amount <= 0:
            raise BusinessLogicError(
                "金额必须大于0",
                error_code="INVALID_AMOUNT",
                details={'user_id': user_id, 'amount': amount}
            )
        
        if amount > 10000:
            raise BusinessLogicError(
                "单次转账金额不能超过10000",
                error_code="AMOUNT_LIMIT_EXCEEDED",
                details={'user_id': user_id, 'amount': amount, 'limit': 10000}
            )
        
        return f"处理成功：用户{user_id}转账{amount}元"
    
    # 测试数据验证
    test_users = [
        {'name': '张三', 'email': 'zhang@example.com', 'age': 25},  # 正常
        {'name': '李四', 'email': 'invalid-email', 'age': 30},      # 邮箱无效
        {'name': '王五', 'age': 35},                               # 缺少邮箱
        {'name': '赵六', 'email': 'zhao@example.com', 'age': -5},   # 年龄无效
    ]
    
    for i, user_data in enumerate(test_users, 1):
        try:
            validate_user_data(user_data)
            print(f"用户{i}验证通过：{user_data['name']}")
        except ValidationError as e:
            print(f"用户{i}验证失败：{e}")
    
    print()
    
    # 测试业务逻辑
    test_transactions = [
        (1001, 500),    # 正常
        (1002, -100),   # 金额无效
        (1003, 15000),  # 超过限额
    ]
    
    for user_id, amount in test_transactions:
        try:
            result = process_business_logic(user_id, amount)
            print(result)
        except BusinessLogicError as e:
            print(f"业务处理失败：{e}")
            if e.details:
                print(f"  详细信息：{e.details}")

custom_exception_examples()

# ============================================================================
# 4. 异常处理最佳实践
# ============================================================================

print("\n4. 异常处理最佳实践")
print("-" * 30)

# 4.1 EAFP vs LBYL
def eafp_vs_lbyl_examples():
    """EAFP vs LBYL 示例"""
    print("\n4.1 EAFP vs LBYL")
    
    # 示例数据
    data = {'name': '张三', 'age': 25}
    
    # LBYL (Look Before You Leap) - 不推荐
    print("LBYL方式：")
    if 'email' in data:
        email = data['email']
        print(f"邮箱：{email}")
    else:
        print("没有邮箱信息")
    
    # EAFP (Easier to Ask for Forgiveness than Permission) - 推荐
    print("\nEAFP方式：")
    try:
        email = data['email']
        print(f"邮箱：{email}")
    except KeyError:
        print("没有邮箱信息")
    
    # 文件操作示例
    print("\n文件操作示例：")
    
    # LBYL方式
    filename = 'test.txt'
    if Path(filename).exists():
        try:
            with open(filename, 'r') as f:
                content = f.read()
                print(f"LBYL读取成功：{len(content)}字符")
        except IOError as e:
            print(f"LBYL读取失败：{e}")
    else:
        print("LBYL：文件不存在")
    
    # EAFP方式（推荐）
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"EAFP读取成功：{len(content)}字符")
    except FileNotFoundError:
        print("EAFP：文件不存在")
    except IOError as e:
        print(f"EAFP读取失败：{e}")

# 4.2 异常链和上下文
def exception_chaining_examples():
    """异常链示例"""
    print("\n4.2 异常链")
    
    def low_level_operation():
        """低级操作"""
        raise ValueError("低级操作失败")
    
    def high_level_operation():
        """高级操作"""
        try:
            low_level_operation()
        except ValueError as e:
            # 使用from保留原始异常
            raise BusinessLogicError("高级操作失败") from e
    
    def another_operation():
        """另一个操作"""
        try:
            low_level_operation()
        except ValueError:
            # 不使用from，但仍保留上下文
            raise BusinessLogicError("另一个操作失败")
    
    # 测试异常链
    print("带异常链的错误：")
    try:
        high_level_operation()
    except BusinessLogicError as e:
        print(f"捕获异常：{e}")
        print(f"原因：{e.__cause__}")
        print(f"上下文：{e.__context__}")
    
    print("\n不带异常链的错误：")
    try:
        another_operation()
    except BusinessLogicError as e:
        print(f"捕获异常：{e}")
        print(f"原因：{e.__cause__}")
        print(f"上下文：{e.__context__}")

# 4.3 资源管理和清理
def resource_management_examples():
    """资源管理示例"""
    print("\n4.3 资源管理")
    
    # 使用try-finally
    def manual_resource_management():
        """手动资源管理"""
        print("手动资源管理：")
        file_handle = None
        try:
            file_handle = open('temp.txt', 'w')
            file_handle.write('测试内容')
            # 模拟可能的错误
            if True:  # 改为False测试正常情况
                raise ValueError("模拟错误")
        except ValueError as e:
            print(f"处理错误：{e}")
        finally:
            if file_handle:
                file_handle.close()
                print("文件已关闭")
    
    # 使用上下文管理器（推荐）
    def context_manager_resource_management():
        """上下文管理器资源管理"""
        print("\n上下文管理器资源管理：")
        try:
            with open('temp.txt', 'w') as f:
                f.write('测试内容')
                # 模拟可能的错误
                if True:  # 改为False测试正常情况
                    raise ValueError("模拟错误")
        except ValueError as e:
            print(f"处理错误：{e}")
        # 文件会自动关闭
        print("文件自动关闭")
    
    manual_resource_management()
    context_manager_resource_management()
    
    # 清理临时文件
    try:
        Path('temp.txt').unlink()
    except FileNotFoundError:
        pass

# 运行最佳实践示例
eafp_vs_lbyl_examples()
exception_chaining_examples()
resource_management_examples()

# ============================================================================
# 5. 高级异常处理
# ============================================================================

print("\n5. 高级异常处理")
print("-" * 30)

# 5.1 自定义上下文管理器
class DatabaseConnection:
    """数据库连接上下文管理器"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None
        self.transaction = None
    
    def __enter__(self):
        print(f"连接数据库：{self.connection_string}")
        self.connection = f"connection_to_{self.connection_string}"
        self.transaction = "transaction_123"
        print("开始事务")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("提交事务")
        else:
            print(f"回滚事务，原因：{exc_value}")
        
        print("关闭数据库连接")
        self.connection = None
        self.transaction = None
        
        # 返回False表示不抑制异常
        return False
    
    def execute(self, query):
        if not self.connection:
            raise RuntimeError("数据库未连接")
        print(f"执行查询：{query}")
        return f"result_of_{query}"

@contextmanager
def timer_context(operation_name):
    """计时上下文管理器"""
    start_time = time.time()
    print(f"开始{operation_name}...")
    try:
        yield
    except Exception as e:
        print(f"{operation_name}失败：{e}")
        raise
    else:
        print(f"{operation_name}成功")
    finally:
        end_time = time.time()
        duration = end_time - start_time
        print(f"{operation_name}耗时：{duration:.3f}秒")

def context_manager_examples():
    """上下文管理器示例"""
    print("\n5.1 自定义上下文管理器")
    
    # 测试数据库连接上下文管理器
    print("数据库操作（成功）：")
    try:
        with DatabaseConnection("localhost:5432/mydb") as db:
            result = db.execute("SELECT * FROM users")
            print(f"查询结果：{result}")
    except Exception as e:
        print(f"数据库操作失败：{e}")
    
    print("\n数据库操作（失败）：")
    try:
        with DatabaseConnection("localhost:5432/mydb") as db:
            result = db.execute("SELECT * FROM users")
            raise ValueError("模拟业务逻辑错误")
    except Exception as e:
        print(f"数据库操作失败：{e}")
    
    # 测试计时上下文管理器
    print("\n计时操作（成功）：")
    try:
        with timer_context("数据处理"):
            time.sleep(0.1)  # 模拟耗时操作
            print("处理数据...")
    except Exception as e:
        print(f"操作失败：{e}")
    
    print("\n计时操作（失败）：")
    try:
        with timer_context("错误操作"):
            time.sleep(0.05)
            raise RuntimeError("模拟操作失败")
    except Exception as e:
        print(f"操作失败：{e}")

# 5.2 装饰器异常处理
def exception_handler(exceptions=None, default_return=None, log_errors=True):
    """异常处理装饰器"""
    if exceptions is None:
        exceptions = (Exception,)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                if log_errors:
                    logger.error(f"函数 {func.__name__} 发生异常：{e}")
                return default_return
        return wrapper
    return decorator

def retry(max_attempts=3, delay=1, exceptions=None):
    """重试装饰器"""
    if exceptions is None:
        exceptions = (Exception,)
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        logger.warning(
                            f"函数 {func.__name__} 第{attempt + 1}次尝试失败：{e}，"
                            f"{delay}秒后重试"
                        )
                        time.sleep(delay)
                    else:
                        logger.error(
                            f"函数 {func.__name__} 在{max_attempts}次尝试后仍然失败"
                        )
            
            raise last_exception
        return wrapper
    return decorator

def decorator_examples():
    """装饰器异常处理示例"""
    print("\n5.2 装饰器异常处理")
    
    @exception_handler(exceptions=(ValueError, TypeError), default_return=0)
    def safe_divide(a, b):
        """安全除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b
    
    @retry(max_attempts=3, delay=0.1, exceptions=(ConnectionError, TimeoutError))
    def unreliable_network_call(success_rate=0.3):
        """不可靠的网络调用"""
        import random
        if random.random() < success_rate:
            return "网络调用成功"
        else:
            raise ConnectionError("网络连接失败")
    
    # 测试异常处理装饰器
    print("安全除法测试：")
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"'10' / 2 = {safe_divide('10', 2)}")
    
    # 测试重试装饰器
    print("\n重试机制测试：")
    try:
        result = unreliable_network_call(success_rate=0.8)
        print(f"网络调用结果：{result}")
    except Exception as e:
        print(f"网络调用最终失败：{e}")

# 运行高级异常处理示例
context_manager_examples()
decorator_examples()

# ============================================================================
# 6. 调试和诊断
# ============================================================================

print("\n6. 调试和诊断")
print("-" * 30)

# 6.1 异常信息收集
def exception_info_examples():
    """异常信息收集示例"""
    print("\n6.1 异常信息收集")
    
    def detailed_exception_handler():
        """详细异常处理"""
        try:
            # 模拟复杂的调用栈
            def level1():
                def level2():
                    def level3():
                        raise ValueError("深层异常")
                    level3()
                level2()
            level1()
            
        except Exception as e:
            # 收集异常信息
            exc_type, exc_value, exc_traceback = sys.exc_info()
            
            print(f"异常类型：{exc_type.__name__}")
            print(f"异常值：{exc_value}")
            print(f"异常消息：{str(e)}")
            
            # 获取调用栈信息
            print("\n调用栈：")
            traceback.print_exc()
            
            # 格式化调用栈
            print("\n格式化调用栈：")
            tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            for line in tb_lines:
                print(line.strip())
            
            # 获取最后一个调用帧
            print("\n最后调用帧信息：")
            tb = exc_traceback
            while tb.tb_next:
                tb = tb.tb_next
            
            frame = tb.tb_frame
            print(f"文件：{frame.f_code.co_filename}")
            print(f"函数：{frame.f_code.co_name}")
            print(f"行号：{tb.tb_lineno}")
            print(f"局部变量：{frame.f_locals}")
    
    detailed_exception_handler()

# 6.2 自定义异常钩子
def custom_exception_hook_examples():
    """自定义异常钩子示例"""
    print("\n6.2 自定义异常钩子")
    
    def custom_excepthook(exc_type, exc_value, exc_traceback):
        """自定义异常钩子"""
        # 对于KeyboardInterrupt，使用默认处理
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        
        # 记录异常到日志
        logger.error(
            "未捕获的异常",
            exc_info=(exc_type, exc_value, exc_traceback)
        )
        
        # 显示用户友好的错误信息
        print(f"\n程序遇到错误：{exc_type.__name__}: {exc_value}")
        print("详细错误信息已记录到日志中。")
    
    # 保存原始钩子
    original_excepthook = sys.excepthook
    
    # 设置自定义钩子
    sys.excepthook = custom_excepthook
    
    print("设置自定义异常钩子")
    
    # 模拟未捕获的异常（注释掉以避免程序终止）
    # raise RuntimeError("这是一个未捕获的异常")
    
    # 恢复原始钩子
    sys.excepthook = original_excepthook
    print("恢复原始异常钩子")

# 6.3 异常统计和监控
class ExceptionMonitor:
    """异常监控器"""
    
    def __init__(self):
        self.exception_counts = {}
        self.exception_details = []
    
    def record_exception(self, exc_type, exc_value, context=None):
        """记录异常"""
        exc_name = exc_type.__name__
        
        # 统计异常次数
        self.exception_counts[exc_name] = self.exception_counts.get(exc_name, 0) + 1
        
        # 记录异常详情
        self.exception_details.append({
            'type': exc_name,
            'message': str(exc_value),
            'context': context,
            'timestamp': time.time()
        })
    
    def get_statistics(self):
        """获取异常统计"""
        return {
            'total_exceptions': len(self.exception_details),
            'exception_counts': self.exception_counts.copy(),
            'recent_exceptions': self.exception_details[-5:]  # 最近5个异常
        }
    
    def clear_statistics(self):
        """清除统计信息"""
        self.exception_counts.clear()
        self.exception_details.clear()

def monitoring_examples():
    """异常监控示例"""
    print("\n6.3 异常监控")
    
    monitor = ExceptionMonitor()
    
    # 模拟各种异常
    test_operations = [
        lambda: 1 / 0,
        lambda: int('abc'),
        lambda: [1, 2, 3][10],
        lambda: {'a': 1}['b'],
        lambda: 1 / 0,  # 重复异常
    ]
    
    for i, operation in enumerate(test_operations, 1):
        try:
            operation()
        except Exception as e:
            monitor.record_exception(
                type(e), e, 
                context=f"测试操作{i}"
            )
            print(f"操作{i}发生异常：{type(e).__name__}: {e}")
    
    # 显示统计信息
    stats = monitor.get_statistics()
    print(f"\n异常统计：")
    print(f"总异常数：{stats['total_exceptions']}")
    print(f"异常类型统计：{stats['exception_counts']}")
    print(f"最近异常：")
    for exc in stats['recent_exceptions']:
        print(f"  - {exc['type']}: {exc['message']} (上下文: {exc['context']})")

# 运行调试和诊断示例
exception_info_examples()
custom_exception_hook_examples()
monitoring_examples()

# ============================================================================
# 7. 实际应用场景
# ============================================================================

print("\n7. 实际应用场景")
print("-" * 30)

# 7.1 配置文件处理
class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}
    
    def load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            logger.info(f"配置文件加载成功：{self.config_file}")
            
        except FileNotFoundError:
            raise ConfigurationError(
                f"配置文件不存在",
                config_file=self.config_file
            )
        
        except json.JSONDecodeError as e:
            raise ConfigurationError(
                f"配置文件格式错误：{e}",
                config_file=self.config_file
            )
        
        except PermissionError:
            raise ConfigurationError(
                f"没有权限读取配置文件",
                config_file=self.config_file
            )
    
    def get_config(self, key, default=None):
        """获取配置项"""
        try:
            keys = key.split('.')
            value = self.config
            
            for k in keys:
                value = value[k]
            
            return value
            
        except (KeyError, TypeError):
            if default is not None:
                return default
            raise ConfigurationError(
                f"配置项不存在：{key}",
                config_key=key,
                config_file=self.config_file
            )
    
    def validate_config(self, required_keys):
        """验证配置"""
        missing_keys = []
        
        for key in required_keys:
            try:
                self.get_config(key)
            except ConfigurationError:
                missing_keys.append(key)
        
        if missing_keys:
            raise ConfigurationError(
                f"缺少必需的配置项：{', '.join(missing_keys)}",
                config_file=self.config_file
            )

# 7.2 网络请求处理
class NetworkClient:
    """网络客户端"""
    
    def __init__(self, base_url, timeout=30, max_retries=3):
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
    
    def make_request(self, endpoint, method='GET', data=None):
        """发起网络请求"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        for attempt in range(self.max_retries):
            try:
                # 模拟网络请求
                print(f"尝试请求 {method} {url} (第{attempt + 1}次)")
                
                # 模拟各种网络错误
                import random
                error_type = random.choice(['success', 'timeout', 'connection', 'server_error'])
                
                if error_type == 'timeout':
                    raise TimeoutError("请求超时")
                elif error_type == 'connection':
                    raise ConnectionError("连接失败")
                elif error_type == 'server_error':
                    raise RuntimeError("服务器错误")
                else:
                    # 成功
                    return {'status': 'success', 'data': f'response_from_{endpoint}'}
                
            except (TimeoutError, ConnectionError) as e:
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt  # 指数退避
                    logger.warning(f"请求失败，{wait_time}秒后重试：{e}")
                    time.sleep(wait_time)
                else:
                    logger.error(f"请求在{self.max_retries}次尝试后仍然失败")
                    raise
            
            except Exception as e:
                logger.error(f"请求发生未预期错误：{e}")
                raise

# 7.3 数据处理管道
class DataProcessor:
    """数据处理器"""
    
    def __init__(self):
        self.processors = []
        self.error_handler = None
    
    def add_processor(self, processor_func):
        """添加处理器"""
        self.processors.append(processor_func)
    
    def set_error_handler(self, error_handler):
        """设置错误处理器"""
        self.error_handler = error_handler
    
    def process(self, data):
        """处理数据"""
        result = data
        errors = []
        
        for i, processor in enumerate(self.processors):
            try:
                result = processor(result)
                logger.info(f"处理器{i + 1}执行成功")
                
            except Exception as e:
                error_info = {
                    'processor_index': i,
                    'processor_name': processor.__name__,
                    'error': e,
                    'input_data': result
                }
                errors.append(error_info)
                
                if self.error_handler:
                    try:
                        result = self.error_handler(error_info, result)
                        logger.warning(f"处理器{i + 1}失败，错误处理器已处理")
                    except Exception as handler_error:
                        logger.error(f"错误处理器也失败了：{handler_error}")
                        raise
                else:
                    logger.error(f"处理器{i + 1}失败，没有错误处理器")
                    raise
        
        return result, errors

def application_examples():
    """实际应用示例"""
    print("\n7.1 配置文件处理")
    
    # 创建测试配置文件
    test_config = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'mydb'
        },
        'api': {
            'key': 'secret_key',
            'timeout': 30
        }
    }
    
    config_file = 'test_config.json'
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(test_config, f, indent=2)
    
    # 测试配置管理器
    try:
        config_manager = ConfigManager(config_file)
        config_manager.load_config()
        
        # 获取配置项
        db_host = config_manager.get_config('database.host')
        print(f"数据库主机：{db_host}")
        
        # 验证必需配置
        required_keys = ['database.host', 'database.port', 'api.key']
        config_manager.validate_config(required_keys)
        print("配置验证通过")
        
        # 获取不存在的配置项
        missing_config = config_manager.get_config('missing.key', 'default_value')
        print(f"缺失配置项（使用默认值）：{missing_config}")
        
    except ConfigurationError as e:
        print(f"配置错误：{e}")
    
    # 清理测试文件
    try:
        Path(config_file).unlink()
    except FileNotFoundError:
        pass
    
    print("\n7.2 网络请求处理")
    
    # 测试网络客户端
    client = NetworkClient('https://api.example.com', max_retries=2)
    
    try:
        response = client.make_request('/users/123')
        print(f"请求成功：{response}")
    except Exception as e:
        print(f"请求失败：{e}")
    
    print("\n7.3 数据处理管道")
    
    # 定义处理器函数
    def validate_data(data):
        if not isinstance(data, dict):
            raise ValidationError("数据必须是字典")
        return data
    
    def normalize_data(data):
        # 模拟可能失败的标准化
        if 'error' in data:
            raise ValueError("数据包含错误标记")
        return {k: str(v).lower() for k, v in data.items()}
    
    def enrich_data(data):
        data['processed_at'] = time.time()
        return data
    
    def error_handler(error_info, data):
        """错误处理器"""
        print(f"处理器错误：{error_info['error']}")
        # 返回默认数据
        return {'error_handled': True, 'original_data': str(data)}
    
    # 创建数据处理器
    processor = DataProcessor()
    processor.add_processor(validate_data)
    processor.add_processor(normalize_data)
    processor.add_processor(enrich_data)
    processor.set_error_handler(error_handler)
    
    # 测试数据
    test_data_sets = [
        {'name': 'John', 'age': 30},           # 正常数据
        {'name': 'Jane', 'error': 'test'},     # 包含错误的数据
        'invalid_data',                        # 无效数据类型
    ]
    
    for i, test_data in enumerate(test_data_sets, 1):
        print(f"\n处理数据集{i}：{test_data}")
        try:
            result, errors = processor.process(test_data)
            print(f"处理结果：{result}")
            if errors:
                print(f"处理过程中的错误：{len(errors)}个")
        except Exception as e:
            print(f"处理失败：{e}")

# 运行实际应用示例
application_examples()

print("\n" + "=" * 60)
print("异常处理示例代码演示完成！")
print("=" * 60)

print("\n=== 异常处理要点总结 ===")
print("""
1. 异常处理基础
   - 使用try-except捕获和处理异常
   - 使用else处理无异常情况
   - 使用finally进行清理工作
   - 捕获具体的异常类型，避免过于宽泛

2. 自定义异常
   - 继承合适的异常基类
   - 提供有意义的异常名称和信息
   - 包含足够的上下文信息

3. 最佳实践
   - 遵循EAFP原则（请求原谅比请求许可更容易）
   - 使用异常链保留原始错误信息
   - 合理使用上下文管理器管理资源
   - 记录异常信息用于调试

4. 高级技术
   - 自定义上下文管理器
   - 装饰器异常处理
   - 异常监控和统计
   - 重试机制和错误恢复

5. 实际应用
   - 配置文件处理
   - 网络请求异常处理
   - 数据处理管道
   - 资源管理和清理
""")