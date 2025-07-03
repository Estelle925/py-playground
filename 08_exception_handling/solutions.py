#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
异常处理练习题参考答案

本文件包含了异常处理练习题的详细解答，展示了：
1. 基本异常处理的实现
2. 自定义异常的设计和使用
3. 高级异常处理技术
4. 实际应用场景的解决方案
5. 最佳实践和编程技巧
"""

import logging
import sys
import traceback
import time
import json
import re
import threading
import hashlib
import random
from typing import Any, Dict, List, Optional, Union, Callable
from pathlib import Path
from contextlib import contextmanager
from functools import wraps
from abc import ABC, abstractmethod
from enum import Enum
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError
from datetime import datetime, timedelta
from urllib.parse import urljoin

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

print("=" * 60)
print("异常处理练习题参考答案")
print("=" * 60)

# ============================================================================
# 练习1：基本异常处理 - 参考答案
# ============================================================================

print("\n练习1：基本异常处理 - 参考答案")
print("-" * 30)

# 练习1.1：安全的数学计算器 - 参考答案
def solution_1_1():
    """练习1.1参考答案：安全的数学计算器"""
    print("\n练习1.1参考答案：安全的数学计算器")
    
    class Calculator:
        """安全的数学计算器"""
        
        def __init__(self):
            self.operations = {
                '+': self.add,
                '-': self.subtract,
                '*': self.multiply,
                '/': self.divide
            }
        
        def _validate_numbers(self, a, b):
            """验证输入是否为数字"""
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError(f"操作数必须是数字，得到：{type(a).__name__}, {type(b).__name__}")
        
        def add(self, a, b):
            """加法"""
            self._validate_numbers(a, b)
            return a + b
        
        def subtract(self, a, b):
            """减法"""
            self._validate_numbers(a, b)
            return a - b
        
        def multiply(self, a, b):
            """乘法"""
            self._validate_numbers(a, b)
            return a * b
        
        def divide(self, a, b):
            """除法"""
            self._validate_numbers(a, b)
            if b == 0:
                raise ZeroDivisionError("除数不能为零")
            return a / b
        
        def safe_calculate(self, operator, a, b):
            """安全计算方法"""
            try:
                if operator not in self.operations:
                    raise ValueError(f"不支持的操作符：{operator}")
                
                operation = self.operations[operator]
                result = operation(a, b)
                
                return result
                
            except ZeroDivisionError as e:
                return f"错误：{e}"
            except TypeError as e:
                return f"类型错误：{e}"
            except ValueError as e:
                return f"值错误：{e}"
            except Exception as e:
                return f"未知错误：{e}"
    
    # 测试代码
    calc = Calculator()
    test_cases = [
        ('+', 10, 5),      # 正常加法
        ('-', 10, 5),      # 正常减法
        ('*', 10, 5),      # 正常乘法
        ('/', 10, 5),      # 正常除法
        ('/', 10, 0),      # 除零错误
        ('+', '10', 5),    # 类型错误
        ('%', 10, 5),      # 不支持的操作
        ('*', 3.14, 2),    # 浮点数运算
    ]
    
    for op, a, b in test_cases:
        result = calc.safe_calculate(op, a, b)
        print(f"{a} {op} {b} = {result}")

# 练习1.2：文件读取器 - 参考答案
def solution_1_2():
    """练习1.2参考答案：文件读取器"""
    print("\n练习1.2参考答案：文件读取器")
    
    class FileReader:
        """安全的文件读取器"""
        
        def __init__(self, encoding='utf-8'):
            self.encoding = encoding
        
        def read_file(self, filename, default=None):
            """安全读取文件内容"""
            try:
                with open(filename, 'r', encoding=self.encoding) as f:
                    content = f.read()
                    logger.info(f"成功读取文件：{filename}")
                    return content
                    
            except FileNotFoundError:
                logger.warning(f"文件不存在：{filename}")
                if default is not None:
                    return default
                raise
            
            except PermissionError:
                logger.error(f"没有权限读取文件：{filename}")
                if default is not None:
                    return default
                raise
            
            except UnicodeDecodeError as e:
                logger.error(f"文件编码错误：{filename}, {e}")
                if default is not None:
                    return default
                raise
            
            except Exception as e:
                logger.error(f"读取文件时发生未知错误：{filename}, {e}")
                if default is not None:
                    return default
                raise
        
        def read_json(self, filename, default=None):
            """安全读取JSON文件"""
            try:
                content = self.read_file(filename)
                data = json.loads(content)
                logger.info(f"成功解析JSON文件：{filename}")
                return data
                
            except json.JSONDecodeError as e:
                logger.error(f"JSON格式错误：{filename}, {e}")
                if default is not None:
                    return default
                raise
            
            except Exception as e:
                logger.error(f"读取JSON文件时发生错误：{filename}, {e}")
                if default is not None:
                    return default
                raise
        
        def read_lines(self, filename, default=None):
            """按行读取文件"""
            try:
                with open(filename, 'r', encoding=self.encoding) as f:
                    lines = f.readlines()
                    # 去除行尾换行符
                    lines = [line.rstrip('\n\r') for line in lines]
                    logger.info(f"成功读取文件行：{filename}, {len(lines)}行")
                    return lines
            except Exception as e:
                logger.error(f"按行读取文件失败：{filename}, {e}")
                if default is not None:
                    return default
                raise
    
    # 测试代码
    reader = FileReader()
    
    # 创建测试文件
    test_files = {
        'test.txt': '这是测试文件内容\n第二行内容',
        'config.json': '{"name": "test", "version": "1.0", "debug": true}',
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
        ('test.txt', None, 'read_file'),
        ('nonexistent.txt', '默认内容', 'read_file'),
        ('config.json', None, 'read_json'),
        ('invalid.json', {}, 'read_json'),
        ('nonexistent.json', {'default': True}, 'read_json'),
        ('test.txt', None, 'read_lines'),
    ]
    
    for filename, default, method in test_cases:
        try:
            if method == 'read_file':
                result = reader.read_file(filename, default=default)
            elif method == 'read_json':
                result = reader.read_json(filename, default=default)
            elif method == 'read_lines':
                result = reader.read_lines(filename, default=default)
            
            print(f"{method} {filename}：{result}")
        except Exception as e:
            print(f"{method} {filename} 失败：{e}")
    
    # 清理测试文件
    for filename in test_files.keys():
        try:
            Path(filename).unlink()
        except FileNotFoundError:
            pass

# ============================================================================
# 练习2：自定义异常 - 参考答案
# ============================================================================

print("\n练习2：自定义异常 - 参考答案")
print("-" * 30)

# 练习2.1：银行账户系统 - 参考答案
def solution_2_1():
    """练习2.1参考答案：银行账户系统"""
    print("\n练习2.1参考答案：银行账户系统")
    
    # 定义自定义异常
    class BankError(Exception):
        """银行系统异常基类"""
        def __init__(self, message, error_code=None, details=None):
            super().__init__(message)
            self.message = message
            self.error_code = error_code
            self.details = details or {}
        
        def __str__(self):
            if self.error_code:
                return f"[{self.error_code}] {self.message}"
            return self.message
    
    class InsufficientFundsError(BankError):
        """余额不足异常"""
        def __init__(self, account_number, requested_amount, available_balance):
            message = f"余额不足：请求金额 {requested_amount}，可用余额 {available_balance}"
            super().__init__(message, "INSUFFICIENT_FUNDS", {
                'account_number': account_number,
                'requested_amount': requested_amount,
                'available_balance': available_balance
            })
    
    class InvalidAmountError(BankError):
        """无效金额异常"""
        def __init__(self, amount):
            message = f"无效金额：{amount}，金额必须大于0"
            super().__init__(message, "INVALID_AMOUNT", {'amount': amount})
    
    class AccountNotFoundError(BankError):
        """账户不存在异常"""
        def __init__(self, account_number):
            message = f"账户不存在：{account_number}"
            super().__init__(message, "ACCOUNT_NOT_FOUND", {'account_number': account_number})
    
    class AccountFrozenError(BankError):
        """账户被冻结异常"""
        def __init__(self, account_number):
            message = f"账户已被冻结：{account_number}"
            super().__init__(message, "ACCOUNT_FROZEN", {'account_number': account_number})
    
    # 实现BankAccount类
    class BankAccount:
        """银行账户"""
        
        def __init__(self, account_number, initial_balance=0):
            self.account_number = account_number
            self.balance = initial_balance
            self.is_frozen = False
            self.transaction_history = []
            
            # 记录初始余额
            if initial_balance > 0:
                self._add_transaction('INITIAL_DEPOSIT', initial_balance)
        
        def _validate_amount(self, amount):
            """验证金额"""
            if not isinstance(amount, (int, float)):
                raise InvalidAmountError(f"金额必须是数字，得到：{type(amount).__name__}")
            if amount <= 0:
                raise InvalidAmountError(amount)
        
        def _check_frozen(self):
            """检查账户是否被冻结"""
            if self.is_frozen:
                raise AccountFrozenError(self.account_number)
        
        def _add_transaction(self, transaction_type, amount, description=None):
            """添加交易记录"""
            transaction = {
                'type': transaction_type,
                'amount': amount,
                'balance_after': self.balance,
                'timestamp': datetime.now(),
                'description': description
            }
            self.transaction_history.append(transaction)
        
        def deposit(self, amount):
            """存款"""
            self._validate_amount(amount)
            self._check_frozen()
            
            self.balance += amount
            self._add_transaction('DEPOSIT', amount)
            logger.info(f"账户 {self.account_number} 存款 {amount}，余额：{self.balance}")
            return self.balance
        
        def withdraw(self, amount):
            """取款"""
            self._validate_amount(amount)
            self._check_frozen()
            
            if amount > self.balance:
                raise InsufficientFundsError(self.account_number, amount, self.balance)
            
            self.balance -= amount
            self._add_transaction('WITHDRAWAL', amount)
            logger.info(f"账户 {self.account_number} 取款 {amount}，余额：{self.balance}")
            return self.balance
        
        def freeze(self):
            """冻结账户"""
            self.is_frozen = True
            self._add_transaction('FREEZE', 0, '账户被冻结')
            logger.warning(f"账户 {self.account_number} 已被冻结")
        
        def unfreeze(self):
            """解冻账户"""
            self.is_frozen = False
            self._add_transaction('UNFREEZE', 0, '账户解冻')
            logger.info(f"账户 {self.account_number} 已解冻")
        
        def get_balance(self):
            """获取余额"""
            return self.balance
        
        def get_transaction_history(self, limit=None):
            """获取交易历史"""
            if limit:
                return self.transaction_history[-limit:]
            return self.transaction_history.copy()
    
    # 实现Bank类
    class Bank:
        """银行"""
        
        def __init__(self, name="示例银行"):
            self.name = name
            self.accounts = {}
            self.transaction_log = []
        
        def create_account(self, account_number, initial_balance=0):
            """创建账户"""
            if account_number in self.accounts:
                raise BankError(f"账户已存在：{account_number}", "ACCOUNT_EXISTS")
            
            account = BankAccount(account_number, initial_balance)
            self.accounts[account_number] = account
            
            logger.info(f"创建账户：{account_number}，初始余额：{initial_balance}")
            return account
        
        def get_account(self, account_number):
            """获取账户"""
            if account_number not in self.accounts:
                raise AccountNotFoundError(account_number)
            return self.accounts[account_number]
        
        def transfer(self, from_account, to_account, amount):
            """转账"""
            try:
                # 获取账户
                source = self.get_account(from_account)
                target = self.get_account(to_account)
                
                # 验证金额
                if not isinstance(amount, (int, float)) or amount <= 0:
                    raise InvalidAmountError(amount)
                
                # 执行转账（原子操作）
                source.withdraw(amount)  # 可能抛出余额不足异常
                
                try:
                    target.deposit(amount)
                except Exception as e:
                    # 如果目标账户存款失败，回滚源账户
                    source.deposit(amount)
                    raise BankError(f"转账失败，已回滚：{e}", "TRANSFER_FAILED")
                
                # 记录转账日志
                transfer_record = {
                    'from_account': from_account,
                    'to_account': to_account,
                    'amount': amount,
                    'timestamp': datetime.now(),
                    'status': 'SUCCESS'
                }
                self.transaction_log.append(transfer_record)
                
                logger.info(f"转账成功：{from_account} -> {to_account}，金额：{amount}")
                return transfer_record
                
            except Exception as e:
                # 记录失败的转账
                transfer_record = {
                    'from_account': from_account,
                    'to_account': to_account,
                    'amount': amount,
                    'timestamp': datetime.now(),
                    'status': 'FAILED',
                    'error': str(e)
                }
                self.transaction_log.append(transfer_record)
                
                logger.error(f"转账失败：{from_account} -> {to_account}，错误：{e}")
                raise
        
        def get_all_accounts(self):
            """获取所有账户"""
            return list(self.accounts.values())
        
        def get_transfer_history(self, limit=None):
            """获取转账历史"""
            if limit:
                return self.transaction_log[-limit:]
            return self.transaction_log.copy()
    
    # 测试代码
    try:
        bank = Bank("测试银行")
        
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
        print("\n测试异常情况：")
        
        # 余额不足
        try:
            account1.withdraw(2000)
        except InsufficientFundsError as e:
            print(f"取款失败：{e}")
            print(f"错误详情：{e.details}")
        
        # 无效金额
        try:
            account1.deposit(-100)
        except InvalidAmountError as e:
            print(f"存款失败：{e}")
        
        # 账户冻结
        account1.freeze()
        try:
            account1.withdraw(100)
        except AccountFrozenError as e:
            print(f"冻结账户取款失败：{e}")
        
        # 解冻账户
        account1.unfreeze()
        account1.withdraw(50)
        print(f"解冻后取款成功，余额：{account1.balance}")
        
        # 账户不存在
        try:
            bank.transfer('999999', '123456', 100)
        except AccountNotFoundError as e:
            print(f"转账失败：{e}")
        
        # 显示交易历史
        print("\n账户1交易历史：")
        for transaction in account1.get_transaction_history():
            print(f"  {transaction['type']}: {transaction['amount']}, 余额: {transaction['balance_after']}")
        
    except Exception as e:
        print(f"银行系统错误：{e}")
        traceback.print_exc()

# 练习2.2：用户认证系统 - 参考答案
def solution_2_2():
    """练习2.2参考答案：用户认证系统"""
    print("\n练习2.2参考答案：用户认证系统")
    
    # 定义认证相关异常
    class AuthenticationError(Exception):
        """认证异常基类"""
        def __init__(self, message, error_code=None, user_id=None):
            super().__init__(message)
            self.message = message
            self.error_code = error_code
            self.user_id = user_id
        
        def __str__(self):
            if self.error_code:
                return f"[{self.error_code}] {self.message}"
            return self.message
    
    class InvalidCredentialsError(AuthenticationError):
        """用户名或密码错误"""
        def __init__(self, username):
            super().__init__("用户名或密码错误", "INVALID_CREDENTIALS", username)
    
    class AccountLockedError(AuthenticationError):
        """账户被锁定"""
        def __init__(self, username, lock_time):
            super().__init__(f"账户已被锁定，解锁时间：{lock_time}", "ACCOUNT_LOCKED", username)
            self.lock_time = lock_time
    
    class PasswordExpiredError(AuthenticationError):
        """密码已过期"""
        def __init__(self, username, expired_date):
            super().__init__(f"密码已过期，过期时间：{expired_date}", "PASSWORD_EXPIRED", username)
            self.expired_date = expired_date
    
    class TooManyAttemptsError(AuthenticationError):
        """尝试次数过多"""
        def __init__(self, username, attempts, max_attempts):
            super().__init__(
                f"登录尝试次数过多：{attempts}/{max_attempts}",
                "TOO_MANY_ATTEMPTS",
                username
            )
            self.attempts = attempts
            self.max_attempts = max_attempts
    
    class WeakPasswordError(AuthenticationError):
        """密码强度不足"""
        def __init__(self, requirements):
            super().__init__(f"密码强度不足，要求：{', '.join(requirements)}", "WEAK_PASSWORD")
            self.requirements = requirements
    
    # 实现User类
    class User:
        """用户类"""
        
        def __init__(self, username, password_hash, email=None):
            self.username = username
            self.password_hash = password_hash
            self.email = email
            self.is_locked = False
            self.failed_attempts = 0
            self.lock_time = None
            self.password_created = datetime.now()
            self.password_expires = datetime.now() + timedelta(days=90)  # 90天过期
            self.last_login = None
            self.login_history = []
        
        def is_password_expired(self):
            """检查密码是否过期"""
            return datetime.now() > self.password_expires
        
        def is_account_locked(self):
            """检查账户是否被锁定"""
            if not self.is_locked:
                return False
            
            # 检查是否到了解锁时间
            if self.lock_time and datetime.now() > self.lock_time:
                self.unlock_account()
                return False
            
            return True
        
        def lock_account(self, lock_duration_minutes=30):
            """锁定账户"""
            self.is_locked = True
            self.lock_time = datetime.now() + timedelta(minutes=lock_duration_minutes)
            logger.warning(f"账户 {self.username} 已被锁定，解锁时间：{self.lock_time}")
        
        def unlock_account(self):
            """解锁账户"""
            self.is_locked = False
            self.lock_time = None
            self.failed_attempts = 0
            logger.info(f"账户 {self.username} 已解锁")
        
        def record_login_attempt(self, success, ip_address=None):
            """记录登录尝试"""
            attempt = {
                'timestamp': datetime.now(),
                'success': success,
                'ip_address': ip_address,
                'failed_attempts_before': self.failed_attempts
            }
            self.login_history.append(attempt)
            
            if success:
                self.failed_attempts = 0
                self.last_login = datetime.now()
            else:
                self.failed_attempts += 1
    
    # 实现AuthenticationSystem类
    class AuthenticationSystem:
        """认证系统"""
        
        def __init__(self, max_attempts=3, lock_duration_minutes=30):
            self.users = {}
            self.max_attempts = max_attempts
            self.lock_duration_minutes = lock_duration_minutes
            self.password_requirements = {
                'min_length': 8,
                'require_uppercase': True,
                'require_lowercase': True,
                'require_digit': True,
                'require_special': True,
                'special_chars': '!@#$%^&*()_+-=[]{}|;:,.<>?'
            }
        
        def _hash_password(self, password):
            """密码哈希"""
            # 简单的哈希实现，实际应用中应使用bcrypt等安全哈希
            salt = "demo_salt"  # 实际应用中应使用随机盐
            return hashlib.sha256((password + salt).encode()).hexdigest()
        
        def _verify_password(self, password, password_hash):
            """验证密码"""
            return self._hash_password(password) == password_hash
        
        def validate_password_strength(self, password):
            """验证密码强度"""
            requirements = self.password_requirements
            failed_requirements = []
            
            # 检查长度
            if len(password) < requirements['min_length']:
                failed_requirements.append(f"至少{requirements['min_length']}个字符")
            
            # 检查大写字母
            if requirements['require_uppercase'] and not any(c.isupper() for c in password):
                failed_requirements.append("至少一个大写字母")
            
            # 检查小写字母
            if requirements['require_lowercase'] and not any(c.islower() for c in password):
                failed_requirements.append("至少一个小写字母")
            
            # 检查数字
            if requirements['require_digit'] and not any(c.isdigit() for c in password):
                failed_requirements.append("至少一个数字")
            
            # 检查特殊字符
            if requirements['require_special']:
                special_chars = requirements['special_chars']
                if not any(c in special_chars for c in password):
                    failed_requirements.append(f"至少一个特殊字符({special_chars[:10]}...)")
            
            if failed_requirements:
                raise WeakPasswordError(failed_requirements)
            
            return True
        
        def register(self, username, password, email=None):
            """用户注册"""
            # 检查用户是否已存在
            if username in self.users:
                raise AuthenticationError(f"用户名已存在：{username}", "USER_EXISTS")
            
            # 验证密码强度
            self.validate_password_strength(password)
            
            # 创建用户
            password_hash = self._hash_password(password)
            user = User(username, password_hash, email)
            self.users[username] = user
            
            logger.info(f"用户注册成功：{username}")
            return user
        
        def login(self, username, password, ip_address=None):
            """用户登录"""
            # 检查用户是否存在
            if username not in self.users:
                # 为了安全，不透露用户是否存在
                raise InvalidCredentialsError(username)
            
            user = self.users[username]
            
            # 检查账户是否被锁定
            if user.is_account_locked():
                raise AccountLockedError(username, user.lock_time)
            
            # 检查是否超过最大尝试次数
            if user.failed_attempts >= self.max_attempts:
                user.lock_account(self.lock_duration_minutes)
                raise TooManyAttemptsError(username, user.failed_attempts, self.max_attempts)
            
            # 验证密码
            if not self._verify_password(password, user.password_hash):
                user.record_login_attempt(False, ip_address)
                
                # 如果达到最大尝试次数，锁定账户
                if user.failed_attempts >= self.max_attempts:
                    user.lock_account(self.lock_duration_minutes)
                    raise TooManyAttemptsError(username, user.failed_attempts, self.max_attempts)
                
                raise InvalidCredentialsError(username)
            
            # 检查密码是否过期
            if user.is_password_expired():
                raise PasswordExpiredError(username, user.password_expires)
            
            # 登录成功
            user.record_login_attempt(True, ip_address)
            logger.info(f"用户登录成功：{username}")
            
            return {
                'username': username,
                'login_time': datetime.now(),
                'last_login': user.last_login,
                'session_token': self._generate_session_token(username)
            }
        
        def _generate_session_token(self, username):
            """生成会话令牌"""
            # 简单的令牌生成，实际应用中应使用JWT等
            timestamp = str(int(time.time()))
            data = f"{username}:{timestamp}"
            return hashlib.md5(data.encode()).hexdigest()
        
        def change_password(self, username, old_password, new_password):
            """修改密码"""
            if username not in self.users:
                raise AuthenticationError(f"用户不存在：{username}", "USER_NOT_FOUND")
            
            user = self.users[username]
            
            # 验证旧密码
            if not self._verify_password(old_password, user.password_hash):
                raise InvalidCredentialsError(username)
            
            # 验证新密码强度
            self.validate_password_strength(new_password)
            
            # 更新密码
            user.password_hash = self._hash_password(new_password)
            user.password_created = datetime.now()
            user.password_expires = datetime.now() + timedelta(days=90)
            
            logger.info(f"用户 {username} 密码修改成功")
            return True
        
        def get_user_info(self, username):
            """获取用户信息"""
            if username not in self.users:
                raise AuthenticationError(f"用户不存在：{username}", "USER_NOT_FOUND")
            
            user = self.users[username]
            return {
                'username': user.username,
                'email': user.email,
                'is_locked': user.is_locked,
                'failed_attempts': user.failed_attempts,
                'last_login': user.last_login,
                'password_expires': user.password_expires,
                'login_history_count': len(user.login_history)
            }
    
    # 测试代码
    try:
        auth = AuthenticationSystem()
        
        # 测试用户注册
        print("测试用户注册：")
        try:
            auth.register('alice', 'StrongPass123!')
            auth.register('bob', 'AnotherPass456@')
            print("用户注册成功")
        except WeakPasswordError as e:
            print(f"注册失败：{e}")
        
        # 测试弱密码注册
        print("\n测试弱密码注册：")
        try:
            auth.register('charlie', '123')  # 弱密码
        except WeakPasswordError as e:
            print(f"注册失败：{e}")
        
        # 测试成功登录
        print("\n测试成功登录：")
        try:
            result = auth.login('alice', 'StrongPass123!')
            print(f"登录成功：{result['username']}, 令牌：{result['session_token'][:10]}...")
        except AuthenticationError as e:
            print(f"登录失败：{e}")
        
        # 测试失败登录
        print("\n测试失败登录：")
        for i in range(4):  # 尝试4次错误密码
            try:
                auth.login('alice', 'wrongpassword')
            except AuthenticationError as e:
                print(f"登录尝试{i+1}失败：{e}")
                if isinstance(e, AccountLockedError):
                    break
        
        # 测试重复用户注册
        print("\n测试重复用户注册：")
        try:
            auth.register('alice', 'AnotherPass789!')
        except AuthenticationError as e:
            print(f"注册失败：{e}")
        
        # 显示用户信息
        print("\n用户信息：")
        try:
            user_info = auth.get_user_info('alice')
            for key, value in user_info.items():
                print(f"  {key}: {value}")
        except AuthenticationError as e:
            print(f"获取用户信息失败：{e}")
        
    except Exception as e:
        print(f"认证系统错误：{e}")
        traceback.print_exc()

# ============================================================================
# 练习3：高级异常处理 - 参考答案
# ============================================================================

print("\n练习3：高级异常处理 - 参考答案")
print("-" * 30)

# 练习3.1：重试装饰器 - 参考答案
def solution_3_1():
    """练习3.1参考答案：重试装饰器"""
    print("\n练习3.1参考答案：重试装饰器")
    
    import random
    import time
    from functools import wraps
    from typing import Type, Tuple, Callable, Any
    
    def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
        """重试装饰器
        
        Args:
            max_attempts: 最大重试次数
            delay: 初始延迟时间（秒）
            backoff: 延迟倍数
            exceptions: 需要重试的异常类型
        """
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                current_delay = delay
                
                for attempt in range(max_attempts):
                    try:
                        result = func(*args, **kwargs)
                        if attempt > 0:
                            logger.info(f"函数 {func.__name__} 在第{attempt + 1}次尝试后成功")
                        return result
                        
                    except exceptions as e:
                        last_exception = e
                        
                        if attempt < max_attempts - 1:  # 不是最后一次尝试
                            logger.warning(
                                f"函数 {func.__name__} 第{attempt + 1}次尝试失败：{e}，"
                                f"{current_delay}秒后重试"
                            )
                            time.sleep(current_delay)
                            current_delay *= backoff
                        else:
                            logger.error(
                                f"函数 {func.__name__} 在{max_attempts}次尝试后仍然失败"
                            )
                
                # 所有尝试都失败了，抛出最后一个异常
                raise last_exception
            
            return wrapper
        return decorator
    
    # 高级重试装饰器
    class RetryConfig:
        """重试配置"""
        def __init__(self, max_attempts=3, delay=1, backoff=2, 
                     exceptions=(Exception,), on_retry=None, on_failure=None):
            self.max_attempts = max_attempts
            self.delay = delay
            self.backoff = backoff
            self.exceptions = exceptions
            self.on_retry = on_retry  # 重试时的回调
            self.on_failure = on_failure  # 最终失败时的回调
    
    def advanced_retry(config: RetryConfig):
        """高级重试装饰器"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                current_delay = config.delay
                
                for attempt in range(config.max_attempts):
                    try:
                        result = func(*args, **kwargs)
                        if attempt > 0:
                            logger.info(f"函数 {func.__name__} 在第{attempt + 1}次尝试后成功")
                        return result
                        
                    except config.exceptions as e:
                        last_exception = e
                        
                        if attempt < config.max_attempts - 1:
                            # 调用重试回调
                            if config.on_retry:
                                config.on_retry(attempt + 1, e, current_delay)
                            
                            logger.warning(
                                f"函数 {func.__name__} 第{attempt + 1}次尝试失败：{e}，"
                                f"{current_delay}秒后重试"
                            )
                            time.sleep(current_delay)
                            current_delay *= config.backoff
                        else:
                            # 调用失败回调
                            if config.on_failure:
                                config.on_failure(config.max_attempts, e)
                            
                            logger.error(
                                f"函数 {func.__name__} 在{config.max_attempts}次尝试后仍然失败"
                            )
                
                raise last_exception
            
            return wrapper
        return decorator
    
    # 测试函数
    @retry(max_attempts=3, delay=0.5, exceptions=(ValueError, ConnectionError))
    def unreliable_network_call():
        """模拟不稳定的网络调用"""
        if random.random() < 0.7:  # 70%的失败率
            raise ConnectionError("网络连接失败")
        return "网络调用成功"
    
    @retry(max_attempts=4, delay=0.2, backoff=1.5)
    def unreliable_calculation():
        """模拟不稳定的计算"""
        if random.random() < 0.6:  # 60%的失败率
            raise ValueError("计算错误")
        return 42
    
    # 高级重试示例
    def on_retry_callback(attempt, exception, delay):
        print(f"  重试回调：第{attempt}次失败，异常：{exception}，延迟：{delay}秒")
    
    def on_failure_callback(max_attempts, exception):
        print(f"  失败回调：{max_attempts}次尝试后最终失败，异常：{exception}")
    
    retry_config = RetryConfig(
        max_attempts=3,
        delay=0.3,
        backoff=2,
        exceptions=(ValueError, RuntimeError),
        on_retry=on_retry_callback,
        on_failure=on_failure_callback
    )
    
    @advanced_retry(retry_config)
    def advanced_unreliable_function():
        """高级重试示例函数"""
        if random.random() < 0.8:  # 80%的失败率
            raise RuntimeError("运行时错误")
        return "高级重试成功"
    
    # 测试代码
    print("测试基本重试装饰器：")
    
    # 测试网络调用
    for i in range(3):
        try:
            result = unreliable_network_call()
            print(f"网络调用{i+1}：{result}")
        except Exception as e:
            print(f"网络调用{i+1}最终失败：{e}")
    
    print("\n测试计算重试：")
    for i in range(2):
        try:
            result = unreliable_calculation()
            print(f"计算{i+1}：{result}")
        except Exception as e:
            print(f"计算{i+1}最终失败：{e}")
    
    print("\n测试高级重试装饰器：")
    for i in range(2):
        try:
            result = advanced_unreliable_function()
            print(f"高级重试{i+1}：{result}")
        except Exception as e:
            print(f"高级重试{i+1}最终失败：{e}")

# 练习3.2：异常聚合器 - 参考答案
def solution_3_2():
    """练习3.2参考答案：异常聚合器"""
    print("\n练习3.2参考答案：异常聚合器")
    
    from typing import List, Dict, Any, Optional
    from collections import defaultdict
    
    class ExceptionAggregator:
        """异常聚合器"""
        
        def __init__(self, continue_on_error=True):
            self.continue_on_error = continue_on_error
            self.exceptions = []
            self.results = []
            self.task_count = 0
            self.success_count = 0
            self.error_count = 0
        
        def execute(self, func, *args, **kwargs):
            """执行单个任务"""
            self.task_count += 1
            task_id = self.task_count
            
            try:
                result = func(*args, **kwargs)
                self.results.append({
                    'task_id': task_id,
                    'success': True,
                    'result': result,
                    'function': func.__name__,
                    'args': args,
                    'kwargs': kwargs
                })
                self.success_count += 1
                return result
                
            except Exception as e:
                self.error_count += 1
                exception_info = {
                    'task_id': task_id,
                    'exception': e,
                    'exception_type': type(e).__name__,
                    'message': str(e),
                    'function': func.__name__,
                    'args': args,
                    'kwargs': kwargs,
                    'traceback': traceback.format_exc()
                }
                self.exceptions.append(exception_info)
                
                self.results.append({
                    'task_id': task_id,
                    'success': False,
                    'error': exception_info,
                    'function': func.__name__,
                    'args': args,
                    'kwargs': kwargs
                })
                
                if not self.continue_on_error:
                    raise
                
                return None
        
        def execute_batch(self, tasks):
            """批量执行任务
            
            Args:
                tasks: 任务列表，每个任务是(func, args, kwargs)的元组
            """
            results = []
            
            for task in tasks:
                if isinstance(task, tuple):
                    if len(task) == 1:
                        func, args, kwargs = task[0], (), {}
                    elif len(task) == 2:
                        func, args, kwargs = task[0], task[1], {}
                    else:
                        func, args, kwargs = task[0], task[1], task[2]
                else:
                    func, args, kwargs = task, (), {}
                
                result = self.execute(func, *args, **kwargs)
                results.append(result)
            
            return results
        
        def has_errors(self):
            """是否有错误"""
            return len(self.exceptions) > 0
        
        def get_error_summary(self):
            """获取错误摘要"""
            if not self.has_errors():
                return "没有错误"
            
            error_types = defaultdict(int)
            for exc_info in self.exceptions:
                error_types[exc_info['exception_type']] += 1
            
            summary = f"总共{self.error_count}个错误："
            for error_type, count in error_types.items():
                summary += f" {error_type}({count})"
            
            return summary
        
        def get_detailed_errors(self):
            """获取详细错误信息"""
            return self.exceptions.copy()
        
        def get_statistics(self):
            """获取统计信息"""
            return {
                'total_tasks': self.task_count,
                'successful_tasks': self.success_count,
                'failed_tasks': self.error_count,
                'success_rate': self.success_count / self.task_count if self.task_count > 0 else 0,
                'error_rate': self.error_count / self.task_count if self.task_count > 0 else 0
            }
        
        def raise_if_errors(self, error_message="批量操作中发生错误"):
            """如果有错误则抛出聚合异常"""
            if self.has_errors():
                raise AggregatedError(error_message, self.exceptions)
        
        def reset(self):
            """重置聚合器"""
            self.exceptions.clear()
            self.results.clear()
            self.task_count = 0
            self.success_count = 0
            self.error_count = 0
    
    class AggregatedError(Exception):
        """聚合异常"""
        
        def __init__(self, message, exceptions):
            super().__init__(message)
            self.exceptions = exceptions
            self.message = message
        
        def __str__(self):
            error_summary = defaultdict(int)
            for exc_info in self.exceptions:
                error_summary[exc_info['exception_type']] += 1
            
            summary = f"{self.message}："
            for error_type, count in error_summary.items():
                summary += f" {error_type}({count})"
            
            return summary
        
        def get_exceptions_by_type(self, exception_type):
            """按类型获取异常"""
            return [exc for exc in self.exceptions if exc['exception_type'] == exception_type]
        
        def print_detailed_errors(self):
            """打印详细错误信息"""
            for i, exc_info in enumerate(self.exceptions, 1):
                print(f"错误 {i}:")
                print(f"  任务ID: {exc_info['task_id']}")
                print(f"  函数: {exc_info['function']}")
                print(f"  异常类型: {exc_info['exception_type']}")
                print(f"  错误信息: {exc_info['message']}")
                print(f"  参数: {exc_info['args']}")
                if exc_info['kwargs']:
                    print(f"  关键字参数: {exc_info['kwargs']}")
                print()
    
    # 测试函数
    def successful_task(x):
        return x * 2
    
    def failing_task(x):
        if x % 2 == 0:
            raise ValueError(f"偶数不被允许：{x}")
        return x ** 2
    
    def division_task(a, b):
        if b == 0:
            raise ZeroDivisionError("除数不能为零")
        return a / b
    
    def network_task(url):
        if 'invalid' in url:
            raise ConnectionError(f"无法连接到：{url}")
        return f"从 {url} 获取数据成功"
    
    # 测试代码
    print("测试异常聚合器：")
    
    # 测试1：继续执行模式
    print("\n测试1：继续执行模式")
    aggregator = ExceptionAggregator(continue_on_error=True)
    
    # 执行单个任务
    aggregator.execute(successful_task, 5)
    aggregator.execute(failing_task, 4)  # 会失败
    aggregator.execute(successful_task, 3)
    aggregator.execute(division_task, 10, 0)  # 会失败
    
    print(f"错误摘要：{aggregator.get_error_summary()}")
    print(f"统计信息：{aggregator.get_statistics()}")
    
    # 测试2：批量执行
    print("\n测试2：批量执行")
    aggregator.reset()
    
    tasks = [
        (successful_task, (1,)),
        (successful_task, (2,)),
        (failing_task, (4,)),  # 会失败
        (division_task, (10, 2)),
        (division_task, (5, 0)),  # 会失败
        (network_task, ('http://example.com',)),
        (network_task, ('http://invalid.com',)),  # 会失败
    ]
    
    results = aggregator.execute_batch(tasks)
    print(f"批量执行结果：{[r for r in results if r is not None]}")
    print(f"错误摘要：{aggregator.get_error_summary()}")
    
    # 测试3：抛出聚合异常
    print("\n测试3：抛出聚合异常")
    try:
        aggregator.raise_if_errors("批量任务执行失败")
    except AggregatedError as e:
        print(f"捕获聚合异常：{e}")
        print("详细错误信息：")
        e.print_detailed_errors()
    
    # 测试4：停止执行模式
    print("\n测试4：停止执行模式")
    aggregator_stop = ExceptionAggregator(continue_on_error=False)
    
    try:
        aggregator_stop.execute(successful_task, 1)
        aggregator_stop.execute(failing_task, 2)  # 会失败并停止
        aggregator_stop.execute(successful_task, 3)  # 不会执行
    except Exception as e:
        print(f"停止执行模式捕获异常：{e}")
        print(f"统计信息：{aggregator_stop.get_statistics()}")

# ============================================================================
# 练习4：实际应用场景 - 参考答案
# ============================================================================

print("\n练习4：实际应用场景 - 参考答案")
print("-" * 30)

# 练习4.1：Web API客户端 - 参考答案
def solution_4_1():
    """练习4.1参考答案：Web API客户端"""
    print("\n练习4.1参考答案：Web API客户端")
    
    import json
    import time
    from urllib.parse import urljoin, urlparse
    from typing import Dict, Any, Optional, Union
    
    # 定义API相关异常
    class APIError(Exception):
        """API异常基类"""
        def __init__(self, message, status_code=None, response_data=None):
            super().__init__(message)
            self.message = message
            self.status_code = status_code
            self.response_data = response_data
    
    class ConnectionError(APIError):
        """连接错误"""
        pass
    
    class TimeoutError(APIError):
        """超时错误"""
        pass
    
    class HTTPError(APIError):
        """HTTP错误"""
        pass
    
    class AuthenticationError(APIError):
        """认证错误"""
        pass
    
    class RateLimitError(APIError):
        """限流错误"""
        def __init__(self, message, retry_after=None, **kwargs):
            super().__init__(message, **kwargs)
            self.retry_after = retry_after
    
    class ValidationError(APIError):
        """验证错误"""
        pass
    
    # 模拟HTTP响应
    class MockResponse:
        def __init__(self, status_code, data=None, headers=None):
            self.status_code = status_code
            self.data = data or {}
            self.headers = headers or {}
        
        def json(self):
            return self.data
        
        def text(self):
            return json.dumps(self.data)
    
    # 模拟HTTP客户端
    class MockHTTPClient:
        def __init__(self):
            self.request_count = 0
            self.fail_requests = set()  # 设置哪些请求会失败
        
        def request(self, method, url, **kwargs):
            self.request_count += 1
            
            # 模拟网络问题
            if self.request_count in self.fail_requests:
                if self.request_count % 3 == 1:
                    raise ConnectionError("网络连接失败")
                elif self.request_count % 3 == 2:
                    raise TimeoutError("请求超时")
            
            # 模拟不同的响应
            if 'auth' in url and kwargs.get('headers', {}).get('Authorization') != 'Bearer valid_token':
                return MockResponse(401, {'error': '认证失败'})
            
            if 'ratelimit' in url:
                return MockResponse(429, {'error': '请求过于频繁'}, {'Retry-After': '60'})
            
            if 'error' in url:
                return MockResponse(500, {'error': '服务器内部错误'})
            
            if 'validation' in url:
                return MockResponse(400, {'error': '参数验证失败', 'details': ['name字段必填']})
            
            # 成功响应
            return MockResponse(200, {'message': '请求成功', 'data': {'id': 1, 'name': 'test'}})
    
    class APIClient:
        """Web API客户端"""
        
        def __init__(self, base_url, timeout=30, max_retries=3, retry_delay=1):
            self.base_url = base_url.rstrip('/')
            self.timeout = timeout
            self.max_retries = max_retries
            self.retry_delay = retry_delay
            self.session_headers = {}
            self.http_client = MockHTTPClient()  # 在实际应用中使用requests
        
        def set_auth_token(self, token):
            """设置认证令牌"""
            self.session_headers['Authorization'] = f'Bearer {token}'
        
        def _build_url(self, endpoint):
            """构建完整URL"""
            return urljoin(self.base_url + '/', endpoint.lstrip('/'))
        
        def _handle_response(self, response):
            """处理响应"""
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                raise AuthenticationError(
                    "认证失败", 
                    status_code=response.status_code,
                    response_data=response.json()
                )
            elif response.status_code == 400:
                data = response.json()
                raise ValidationError(
                    f"请求验证失败：{data.get('error', '未知错误')}",
                    status_code=response.status_code,
                    response_data=data
                )
            elif response.status_code == 429:
                retry_after = response.headers.get('Retry-After')
                raise RateLimitError(
                    "请求频率限制",
                    status_code=response.status_code,
                    retry_after=int(retry_after) if retry_after else None,
                    response_data=response.json()
                )
            elif response.status_code >= 500:
                raise HTTPError(
                    f"服务器错误：{response.status_code}",
                    status_code=response.status_code,
                    response_data=response.json()
                )
            else:
                raise HTTPError(
                    f"HTTP错误：{response.status_code}",
                    status_code=response.status_code,
                    response_data=response.json()
                )
        
        def _make_request(self, method, endpoint, **kwargs):
            """发起HTTP请求"""
            url = self._build_url(endpoint)
            headers = {**self.session_headers, **kwargs.pop('headers', {})}
            
            # 设置超时
            kwargs.setdefault('timeout', self.timeout)
            
            try:
                response = self.http_client.request(
                    method, url, headers=headers, **kwargs
                )
                return self._handle_response(response)
                
            except (ConnectionError, TimeoutError) as e:
                # 网络相关错误，重新抛出
                raise e
            except Exception as e:
                # 其他未预期的错误
                raise APIError(f"请求失败：{e}")
        
        def _request_with_retry(self, method, endpoint, **kwargs):
            """带重试的请求"""
            last_exception = None
            
            for attempt in range(self.max_retries + 1):
                try:
                    return self._make_request(method, endpoint, **kwargs)
                    
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    
                    if attempt < self.max_retries:
                        delay = self.retry_delay * (2 ** attempt)  # 指数退避
                        logger.warning(
                            f"请求失败，{delay}秒后重试 (尝试 {attempt + 1}/{self.max_retries + 1})：{e}"
                        )
                        time.sleep(delay)
                    else:
                        logger.error(f"请求在{self.max_retries + 1}次尝试后仍然失败")
                        raise
                
                except RateLimitError as e:
                    if attempt < self.max_retries and e.retry_after:
                        delay = min(e.retry_after, 300)  # 最多等待5分钟
                        logger.warning(f"遇到限流，{delay}秒后重试")
                        time.sleep(delay)
                    else:
                        raise
                
                except (AuthenticationError, ValidationError, HTTPError) as e:
                    # 这些错误通常不需要重试
                    raise
            
            # 如果到这里，说明所有重试都失败了
            raise last_exception
        
        def get(self, endpoint, params=None, **kwargs):
            """GET请求"""
            if params:
                kwargs['params'] = params
            return self._request_with_retry('GET', endpoint, **kwargs)
        
        def post(self, endpoint, data=None, json_data=None, **kwargs):
            """POST请求"""
            if json_data:
                kwargs['json'] = json_data
                kwargs.setdefault('headers', {})['Content-Type'] = 'application/json'
            elif data:
                kwargs['data'] = data
            
            return self._request_with_retry('POST', endpoint, **kwargs)
        
        def put(self, endpoint, data=None, json_data=None, **kwargs):
            """PUT请求"""
            if json_data:
                kwargs['json'] = json_data
                kwargs.setdefault('headers', {})['Content-Type'] = 'application/json'
            elif data:
                kwargs['data'] = data
            
            return self._request_with_retry('PUT', endpoint, **kwargs)
        
        def delete(self, endpoint, **kwargs):
            """DELETE请求"""
            return self._request_with_retry('DELETE', endpoint, **kwargs)
    
    # 测试代码
    print("测试Web API客户端：")
    
    client = APIClient('https://api.example.com', max_retries=2, retry_delay=0.1)
    
    # 测试成功请求
    print("\n测试成功请求：")
    try:
        result = client.get('/users')
        print(f"成功获取用户列表：{result}")
    except APIError as e:
        print(f"请求失败：{e}")
    
    # 测试认证错误
    print("\n测试认证错误：")
    try:
        result = client.get('/auth/profile')
    except AuthenticationError as e:
        print(f"认证失败：{e}")
        print(f"状态码：{e.status_code}")
        print(f"响应数据：{e.response_data}")
    
    # 设置有效令牌后重试
    client.set_auth_token('valid_token')
    try:
        result = client.get('/auth/profile')
        print(f"认证成功：{result}")
    except APIError as e:
        print(f"认证请求失败：{e}")
    
    # 测试验证错误
    print("\n测试验证错误：")
    try:
        result = client.post('/validation/user', json_data={'email': 'invalid'})
    except ValidationError as e:
        print(f"验证失败：{e}")
        print(f"错误详情：{e.response_data}")
    
    # 测试限流错误
    print("\n测试限流错误：")
    try:
        result = client.get('/ratelimit/data')
    except RateLimitError as e:
        print(f"限流错误：{e}")
        print(f"重试时间：{e.retry_after}秒")
    
    # 测试服务器错误
    print("\n测试服务器错误：")
    try:
        result = client.get('/error/500')
    except HTTPError as e:
        print(f"服务器错误：{e}")
        print(f"状态码：{e.status_code}")
    
    # 测试网络重试
    print("\n测试网络重试：")
    client.http_client.fail_requests = {1, 2}  # 前两次请求失败
    try:
        result = client.get('/users/retry')
        print(f"重试成功：{result}")
    except APIError as e:
        print(f"重试失败：{e}")

# 练习4.2：数据验证框架 - 参考答案
def solution_4_2():
    """练习4.2参考答案：数据验证框架"""
    print("\n练习4.2参考答案：数据验证框架")
    
    import re
    from typing import Any, Dict, List, Optional, Union, Callable
    from abc import ABC, abstractmethod
    from datetime import datetime
    
    # 定义验证相关异常
    class ValidationError(Exception):
        """验证异常基类"""
        def __init__(self, message, field=None, value=None, code=None):
            super().__init__(message)
            self.message = message
            self.field = field
            self.value = value
            self.code = code
        
        def __str__(self):
            if self.field:
                return f"字段 '{self.field}': {self.message}"
            return self.message
    
    class MultipleValidationError(Exception):
        """多个验证错误"""
        def __init__(self, errors):
            self.errors = errors
            messages = [str(error) for error in errors]
            super().__init__(f"验证失败：{'; '.join(messages)}")
        
        def get_errors_by_field(self, field):
            """按字段获取错误"""
            return [error for error in self.errors if error.field == field]
        
        def has_field_error(self, field):
            """检查字段是否有错误"""
            return any(error.field == field for error in self.errors)
        
        def to_dict(self):
            """转换为字典格式"""
            result = {}
            for error in self.errors:
                field = error.field or 'general'
                if field not in result:
                    result[field] = []
                result[field].append({
                    'message': error.message,
                    'code': error.code,
                    'value': error.value
                })
            return result
    
    # 验证器基类
    class Validator(ABC):
        """验证器基类"""
        
        def __init__(self, message=None, code=None):
            self.message = message
            self.code = code
        
        @abstractmethod
        def validate(self, value, field=None):
            """验证值"""
            pass
        
        def __call__(self, value, field=None):
            """使验证器可调用"""
            return self.validate(value, field)
    
    # 具体验证器实现
    class RequiredValidator(Validator):
        """必填验证器"""
        
        def __init__(self, message="此字段为必填项", code="required"):
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            if value is None or value == "" or (isinstance(value, (list, dict)) and len(value) == 0):
                raise ValidationError(self.message, field, value, self.code)
            return value
    
    class TypeValidator(Validator):
        """类型验证器"""
        
        def __init__(self, expected_type, message=None, code="invalid_type"):
            self.expected_type = expected_type
            if message is None:
                type_name = expected_type.__name__ if hasattr(expected_type, '__name__') else str(expected_type)
                message = f"值必须是 {type_name} 类型"
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            if value is not None and not isinstance(value, self.expected_type):
                raise ValidationError(self.message, field, value, self.code)
            return value
    
    class LengthValidator(Validator):
        """长度验证器"""
        
        def __init__(self, min_length=None, max_length=None, message=None, code="invalid_length"):
            self.min_length = min_length
            self.max_length = max_length
            
            if message is None:
                if min_length is not None and max_length is not None:
                    message = f"长度必须在 {min_length} 到 {max_length} 之间"
                elif min_length is not None:
                    message = f"长度不能少于 {min_length}"
                elif max_length is not None:
                    message = f"长度不能超过 {max_length}"
                else:
                    message = "长度无效"
            
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            if value is None:
                return value
            
            try:
                length = len(value)
            except TypeError:
                raise ValidationError("值必须有长度属性", field, value, "no_length")
            
            if self.min_length is not None and length < self.min_length:
                raise ValidationError(self.message, field, value, self.code)
            
            if self.max_length is not None and length > self.max_length:
                raise ValidationError(self.message, field, value, self.code)
            
            return value
    
    class RangeValidator(Validator):
        """范围验证器"""
        
        def __init__(self, min_value=None, max_value=None, message=None, code="out_of_range"):
            self.min_value = min_value
            self.max_value = max_value
            
            if message is None:
                if min_value is not None and max_value is not None:
                    message = f"值必须在 {min_value} 到 {max_value} 之间"
                elif min_value is not None:
                    message = f"值不能小于 {min_value}"
                elif max_value is not None:
                    message = f"值不能大于 {max_value}"
                else:
                    message = "值超出范围"
            
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            if value is None:
                return value
            
            if self.min_value is not None and value < self.min_value:
                raise ValidationError(self.message, field, value, self.code)
            
            if self.max_value is not None and value > self.max_value:
                raise ValidationError(self.message, field, value, self.code)
            
            return value
    
    class RegexValidator(Validator):
        """正则表达式验证器"""
        
        def __init__(self, pattern, message="格式不正确", code="invalid_format"):
            self.pattern = re.compile(pattern) if isinstance(pattern, str) else pattern
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            if value is None:
                return value
            
            if not isinstance(value, str):
                raise ValidationError("值必须是字符串", field, value, "not_string")
            
            if not self.pattern.match(value):
                raise ValidationError(self.message, field, value, self.code)
            
            return value
    
    class EmailValidator(RegexValidator):
        """邮箱验证器"""
        
        def __init__(self, message="邮箱格式不正确", code="invalid_email"):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            super().__init__(pattern, message, code)
    
    class ChoiceValidator(Validator):
        """选择验证器"""
        
        def __init__(self, choices, message=None, code="invalid_choice"):
            self.choices = choices
            if message is None:
                message = f"值必须是以下选项之一：{', '.join(map(str, choices))}"
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            if value is not None and value not in self.choices:
                raise ValidationError(self.message, field, value, self.code)
            return value
    
    class CustomValidator(Validator):
        """自定义验证器"""
        
        def __init__(self, validator_func, message="验证失败", code="custom_validation"):
            self.validator_func = validator_func
            super().__init__(message, code)
        
        def validate(self, value, field=None):
            try:
                if not self.validator_func(value):
                    raise ValidationError(self.message, field, value, self.code)
            except Exception as e:
                if isinstance(e, ValidationError):
                    raise
                raise ValidationError(f"验证过程中发生错误：{e}", field, value, "validation_error")
            return value
    
    # 字段定义
    class Field:
        """字段定义"""
        
        def __init__(self, validators=None, required=True, default=None, transform=None):
            self.validators = validators or []
            self.required = required
            self.default = default
            self.transform = transform  # 值转换函数
            
            # 如果字段是必填的，自动添加必填验证器
            if required and not any(isinstance(v, RequiredValidator) for v in self.validators):
                self.validators.insert(0, RequiredValidator())
        
        def validate(self, value, field_name=None):
            """验证字段值"""
            # 如果值为None且有默认值，使用默认值
            if value is None and self.default is not None:
                value = self.default() if callable(self.default) else self.default
            
            # 应用转换函数
            if self.transform and value is not None:
                try:
                    value = self.transform(value)
                except Exception as e:
                    raise ValidationError(f"值转换失败：{e}", field_name, value, "transform_error")
            
            # 运行所有验证器
            for validator in self.validators:
                value = validator.validate(value, field_name)
            
            return value
    
    # 数据验证框架
    class Schema:
        """数据模式"""
        
        def __init__(self, fields=None, strict=True):
            self.fields = fields or {}
            self.strict = strict  # 是否严格模式（不允许额外字段）
        
        def add_field(self, name, field):
            """添加字段"""
            self.fields[name] = field
        
        def validate(self, data, raise_on_error=True):
            """验证数据"""
            if not isinstance(data, dict):
                if raise_on_error:
                    raise ValidationError("数据必须是字典类型", code="invalid_data_type")
                return False, [ValidationError("数据必须是字典类型", code="invalid_data_type")]
            
            errors = []
            validated_data = {}
            
            # 验证定义的字段
            for field_name, field in self.fields.items():
                try:
                    value = data.get(field_name)
                    validated_value = field.validate(value, field_name)
                    validated_data[field_name] = validated_value
                except ValidationError as e:
                    errors.append(e)
            
            # 检查额外字段（严格模式）
            if self.strict:
                extra_fields = set(data.keys()) - set(self.fields.keys())
                for field_name in extra_fields:
                    errors.append(ValidationError(
                        f"不允许的字段", field_name, data[field_name], "extra_field"
                    ))
            else:
                # 非严格模式，保留额外字段
                for field_name, value in data.items():
                    if field_name not in self.fields:
                        validated_data[field_name] = value
            
            if errors:
                if raise_on_error:
                    raise MultipleValidationError(errors)
                return False, errors
            
            return True, validated_data
        
        def is_valid(self, data):
            """检查数据是否有效"""
            try:
                self.validate(data)
                return True
            except (ValidationError, MultipleValidationError):
                return False
    
    # 预定义的常用模式
    class UserSchema(Schema):
        """用户数据模式"""
        
        def __init__(self):
            fields = {
                'username': Field([
                    RequiredValidator(),
                    TypeValidator(str),
                    LengthValidator(min_length=3, max_length=20),
                    RegexValidator(r'^[a-zA-Z0-9_]+$', "用户名只能包含字母、数字和下划线")
                ]),
                'email': Field([
                    RequiredValidator(),
                    TypeValidator(str),
                    EmailValidator()
                ]),
                'age': Field([
                    TypeValidator(int),
                    RangeValidator(min_value=0, max_value=150)
                ], required=False),
                'gender': Field([
                    ChoiceValidator(['male', 'female', 'other'])
                ], required=False),
                'password': Field([
                    RequiredValidator(),
                    TypeValidator(str),
                    LengthValidator(min_length=8),
                    CustomValidator(
                        lambda x: any(c.isupper() for c in x) and any(c.islower() for c in x) and any(c.isdigit() for c in x),
                        "密码必须包含大写字母、小写字母和数字"
                    )
                ])
            }
            super().__init__(fields)
    
    # 测试代码
    print("测试数据验证框架：")
    
    # 测试单个验证器
    print("\n测试单个验证器：")
    
    # 必填验证器
    required_validator = RequiredValidator()
    try:
        required_validator.validate(None, "test_field")
    except ValidationError as e:
        print(f"必填验证失败：{e}")
    
    # 类型验证器
    type_validator = TypeValidator(int)
    try:
        type_validator.validate("not_int", "number_field")
    except ValidationError as e:
        print(f"类型验证失败：{e}")
    
    # 长度验证器
    length_validator = LengthValidator(min_length=5, max_length=10)
    try:
        length_validator.validate("abc", "text_field")
    except ValidationError as e:
        print(f"长度验证失败：{e}")
    
    # 邮箱验证器
    email_validator = EmailValidator()
    try:
        email_validator.validate("invalid-email", "email_field")
    except ValidationError as e:
        print(f"邮箱验证失败：{e}")
    
    # 测试字段
    print("\n测试字段：")
    username_field = Field([
        RequiredValidator(),
        TypeValidator(str),
        LengthValidator(min_length=3, max_length=20)
    ])
    
    try:
        result = username_field.validate("ab", "username")
        print(f"用户名验证成功：{result}")
    except ValidationError as e:
        print(f"用户名验证失败：{e}")
    
    # 测试模式
    print("\n测试用户模式：")
    user_schema = UserSchema()
    
    # 有效数据
    valid_data = {
        'username': 'john_doe',
        'email': 'john@example.com',
        'age': 25,
        'gender': 'male',
        'password': 'SecurePass123'
    }
    
    try:
        is_valid, result = user_schema.validate(valid_data)
        print(f"有效数据验证成功：{result}")
    except MultipleValidationError as e:
        print(f"验证失败：{e}")
        print(f"错误详情：{e.to_dict()}")
    
    # 无效数据
    print("\n测试无效数据：")
    invalid_data = {
        'username': 'ab',  # 太短
        'email': 'invalid-email',  # 格式错误
        'age': -5,  # 超出范围
        'gender': 'unknown',  # 不在选择列表中
        'password': '123',  # 太短且不符合复杂度要求
        'extra_field': 'not_allowed'  # 额外字段
    }
    
    try:
        user_schema.validate(invalid_data)
    except MultipleValidationError as e:
        print(f"多个验证错误：{e}")
        print("错误详情：")
        for field, field_errors in e.to_dict().items():
            print(f"  {field}:")
            for error in field_errors:
                print(f"    - {error['message']} (代码: {error['code']})")
    
    # 测试非严格模式
    print("\n测试非严格模式：")
    flexible_schema = Schema({
        'name': Field([RequiredValidator(), TypeValidator(str)])
    }, strict=False)
    
    data_with_extra = {
        'name': 'John',
        'extra_info': 'This is allowed in non-strict mode'
    }
    
    try:
        is_valid, result = flexible_schema.validate(data_with_extra)
        print(f"非严格模式验证成功：{result}")
    except MultipleValidationError as e:
        print(f"非严格模式验证失败：{e}")

# ============================================================================
# 练习5：综合应用 - 参考答案
# ============================================================================

print("\n练习5：综合应用 - 参考答案")
print("-" * 30)

# 练习5.1：任务调度系统 - 参考答案
def solution_5_1():
    """练习5.1参考答案：任务调度系统"""
    print("\n练习5.1参考答案：任务调度系统")
    
    import threading
    import queue
    import time
    from enum import Enum
    from typing import Callable, Any, Dict, List, Optional
    from concurrent.futures import ThreadPoolExecutor, Future, TimeoutError as FutureTimeoutError
    from datetime import datetime, timedelta
    
    # 定义任务调度相关异常
    class TaskError(Exception):
        """任务异常基类"""
        def __init__(self, message, task_id=None, task_name=None):
            super().__init__(message)
            self.message = message
            self.task_id = task_id
            self.task_name = task_name
    
    class TaskExecutionError(TaskError):
        """任务执行错误"""
        def __init__(self, message, task_id=None, task_name=None, original_exception=None):
            super().__init__(message, task_id, task_name)
            self.original_exception = original_exception
    
    class TaskTimeoutError(TaskError):
        """任务超时错误"""
        pass
    
    class TaskNotFoundError(TaskError):
        """任务不存在错误"""
        pass
    
    class SchedulerError(Exception):
        """调度器错误"""
        pass
    
    # 任务状态枚举
    class TaskStatus(Enum):
        PENDING = "pending"
        RUNNING = "running"
        COMPLETED = "completed"
        FAILED = "failed"
        CANCELLED = "cancelled"
        TIMEOUT = "timeout"
    
    # 任务优先级枚举
    class TaskPriority(Enum):
        LOW = 1
        NORMAL = 2
        HIGH = 3
        CRITICAL = 4
    
    # 任务定义
    class Task:
        """任务类"""
        
        def __init__(self, task_id, name, func, args=None, kwargs=None, 
                     priority=TaskPriority.NORMAL, timeout=None, max_retries=0, retry_delay=1):
            self.task_id = task_id
            self.name = name
            self.func = func
            self.args = args or ()
            self.kwargs = kwargs or {}
            self.priority = priority
            self.timeout = timeout
            self.max_retries = max_retries
            self.retry_delay = retry_delay
            
            # 状态信息
            self.status = TaskStatus.PENDING
            self.created_at = datetime.now()
            self.started_at = None
            self.completed_at = None
            self.result = None
            self.error = None
            self.retry_count = 0
            self.execution_history = []
        
        def __lt__(self, other):
            """用于优先级队列排序"""
            return self.priority.value > other.priority.value
        
        def execute(self):
            """执行任务"""
            self.status = TaskStatus.RUNNING
            self.started_at = datetime.now()
            
            execution_record = {
                'attempt': self.retry_count + 1,
                'started_at': self.started_at,
                'completed_at': None,
                'success': False,
                'result': None,
                'error': None
            }
            
            try:
                # 执行任务函数
                result = self.func(*self.args, **self.kwargs)
                
                # 任务成功完成
                self.status = TaskStatus.COMPLETED
                self.completed_at = datetime.now()
                self.result = result
                
                execution_record.update({
                    'completed_at': self.completed_at,
                    'success': True,
                    'result': result
                })
                
                logger.info(f"任务 {self.name} ({self.task_id}) 执行成功")
                return result
                
            except Exception as e:
                # 任务执行失败
                self.status = TaskStatus.FAILED
                self.completed_at = datetime.now()
                self.error = e
                
                execution_record.update({
                    'completed_at': self.completed_at,
                    'success': False,
                    'error': str(e)
                })
                
                logger.error(f"任务 {self.name} ({self.task_id}) 执行失败：{e}")
                raise TaskExecutionError(
                    f"任务执行失败：{e}",
                    self.task_id,
                    self.name,
                    e
                )
            
            finally:
                self.execution_history.append(execution_record)
        
        def can_retry(self):
            """检查是否可以重试"""
            return self.retry_count < self.max_retries
        
        def prepare_retry(self):
            """准备重试"""
            if self.can_retry():
                self.retry_count += 1
                self.status = TaskStatus.PENDING
                self.started_at = None
                self.completed_at = None
                self.error = None
                logger.info(f"任务 {self.name} ({self.task_id}) 准备第{self.retry_count}次重试")
                return True
            return False
        
        def get_execution_time(self):
            """获取执行时间"""
            if self.started_at and self.completed_at:
                return (self.completed_at - self.started_at).total_seconds()
            return None
        
        def to_dict(self):
            """转换为字典"""
            return {
                'task_id': self.task_id,
                'name': self.name,
                'status': self.status.value,
                'priority': self.priority.value,
                'created_at': self.created_at.isoformat(),
                'started_at': self.started_at.isoformat() if self.started_at else None,
                'completed_at': self.completed_at.isoformat() if self.completed_at else None,
                'execution_time': self.get_execution_time(),
                'retry_count': self.retry_count,
                'max_retries': self.max_retries,
                'result': str(self.result) if self.result is not None else None,
                'error': str(self.error) if self.error else None
            }
    
    # 任务调度器
    class TaskScheduler:
        """任务调度器"""
        
        def __init__(self, max_workers=4, enable_retry=True):
            self.max_workers = max_workers
            self.enable_retry = enable_retry
            
            # 任务存储
            self.tasks = {}  # task_id -> Task
            self.task_queue = queue.PriorityQueue()
            self.running_tasks = {}  # task_id -> Future
            
            # 线程池
            self.executor = ThreadPoolExecutor(max_workers=max_workers)
            
            # 调度器状态
            self.is_running = False
            self.scheduler_thread = None
            self.stats = {
                'total_tasks': 0,
                'completed_tasks': 0,
                'failed_tasks': 0,
                'cancelled_tasks': 0,
                'timeout_tasks': 0
            }
            
            # 锁
            self.lock = threading.Lock()
        
        def add_task(self, task_id, name, func, args=None, kwargs=None, 
                     priority=TaskPriority.NORMAL, timeout=None, max_retries=0, retry_delay=1):
            """添加任务"""
            with self.lock:
                if task_id in self.tasks:
                    raise TaskError(f"任务ID已存在：{task_id}", task_id)
                
                task = Task(
                    task_id, name, func, args, kwargs,
                    priority, timeout, max_retries, retry_delay
                )
                
                self.tasks[task_id] = task
                self.task_queue.put((task.priority.value, time.time(), task))
                self.stats['total_tasks'] += 1
                
                logger.info(f"任务已添加：{name} ({task_id})")
                return task
        
        def get_task(self, task_id):
            """获取任务"""
            if task_id not in self.tasks:
                raise TaskNotFoundError(f"任务不存在：{task_id}", task_id)
            return self.tasks[task_id]
        
        def cancel_task(self, task_id):
            """取消任务"""
            with self.lock:
                task = self.get_task(task_id)
                
                if task.status == TaskStatus.RUNNING:
                    # 取消正在运行的任务
                    if task_id in self.running_tasks:
                        future = self.running_tasks[task_id]
                        future.cancel()
                        del self.running_tasks[task_id]
                
                task.status = TaskStatus.CANCELLED
                task.completed_at = datetime.now()
                self.stats['cancelled_tasks'] += 1
                
                logger.info(f"任务已取消：{task.name} ({task_id})")
                return True
        
        def _execute_task_with_timeout(self, task):
            """带超时的任务执行"""
            try:
                if task.timeout:
                    # 使用Future的超时功能
                    future = self.executor.submit(task.execute)
                    try:
                        result = future.result(timeout=task.timeout)
                        return result
                    except FutureTimeoutError:
                        future.cancel()
                        task.status = TaskStatus.TIMEOUT
                        task.completed_at = datetime.now()
                        self.stats['timeout_tasks'] += 1
                        raise TaskTimeoutError(
                            f"任务执行超时（{task.timeout}秒）",
                            task.task_id,
                            task.name
                        )
                else:
                    # 无超时限制
                    return task.execute()
                    
            except TaskExecutionError:
                # 重新抛出任务执行错误
                raise
            except Exception as e:
                # 包装其他异常
                raise TaskExecutionError(
                    f"任务执行过程中发生未知错误：{e}",
                    task.task_id,
                    task.name,
                    e
                )
        
        def _process_task(self, task):
            """处理单个任务"""
            try:
                # 执行任务
                result = self._execute_task_with_timeout(task)
                
                # 任务成功完成
                with self.lock:
                    self.stats['completed_tasks'] += 1
                    if task.task_id in self.running_tasks:
                        del self.running_tasks[task.task_id]
                
                return result
                
            except (TaskExecutionError, TaskTimeoutError) as e:
                # 任务执行失败或超时
                with self.lock:
                    if task.task_id in self.running_tasks:
                        del self.running_tasks[task.task_id]
                    
                    # 检查是否可以重试
                    if self.enable_retry and task.can_retry() and not isinstance(e, TaskTimeoutError):
                        # 准备重试
                        if task.prepare_retry():
                            # 延迟后重新加入队列
                            def retry_task():
                                time.sleep(task.retry_delay)
                                with self.lock:
                                    self.task_queue.put((task.priority.value, time.time(), task))
                            
                            threading.Thread(target=retry_task, daemon=True).start()
                            return
                    
                    # 不能重试或重试次数已用完
                    if isinstance(e, TaskTimeoutError):
                        self.stats['timeout_tasks'] += 1
                    else:
                        self.stats['failed_tasks'] += 1
                
                logger.error(f"任务最终失败：{task.name} ({task.task_id}) - {e}")
                raise
        
        def _scheduler_loop(self):
            """调度器主循环"""
            logger.info("任务调度器已启动")
            
            while self.is_running:
                try:
                    # 从队列获取任务（带超时）
                    try:
                        priority, timestamp, task = self.task_queue.get(timeout=1)
                    except queue.Empty:
                        continue
                    
                    # 检查任务是否已被取消
                    if task.status == TaskStatus.CANCELLED:
                        continue
                    
                    # 提交任务到线程池
                    future = self.executor.submit(self._process_task, task)
                    
                    with self.lock:
                        self.running_tasks[task.task_id] = future
                    
                    logger.debug(f"任务已提交执行：{task.name} ({task.task_id})")
                    
                except Exception as e:
                    logger.error(f"调度器循环中发生错误：{e}")
                    time.sleep(1)
            
            logger.info("任务调度器已停止")
        
        def start(self):
            """启动调度器"""
            if self.is_running:
                raise SchedulerError("调度器已在运行")
            
            self.is_running = True
            self.scheduler_thread = threading.Thread(target=self._scheduler_loop, daemon=True)
            self.scheduler_thread.start()
            
            logger.info("任务调度器启动成功")
        
        def stop(self, wait_for_completion=True, timeout=30):
            """停止调度器"""
            if not self.is_running:
                return
            
            logger.info("正在停止任务调度器...")
            self.is_running = False
            
            if wait_for_completion:
                # 等待当前运行的任务完成
                start_time = time.time()
                while self.running_tasks and (time.time() - start_time) < timeout:
                    time.sleep(0.1)
                
                # 取消剩余的运行任务
                with self.lock:
                    for task_id, future in list(self.running_tasks.items()):
                        future.cancel()
                        task = self.tasks[task_id]
                        task.status = TaskStatus.CANCELLED
                        task.completed_at = datetime.now()
            
            # 关闭线程池
            self.executor.shutdown(wait=True)
            
            # 等待调度器线程结束
            if self.scheduler_thread:
                self.scheduler_thread.join(timeout=5)
            
            logger.info("任务调度器已停止")
        
        def get_statistics(self):
            """获取统计信息"""
            with self.lock:
                running_count = len(self.running_tasks)
                pending_count = self.task_queue.qsize()
                
                return {
                    **self.stats,
                    'running_tasks': running_count,
                    'pending_tasks': pending_count,
                    'success_rate': (
                        self.stats['completed_tasks'] / max(1, self.stats['total_tasks'])
                    ) * 100
                }
        
        def get_task_status(self, task_id):
            """获取任务状态"""
            task = self.get_task(task_id)
            return task.to_dict()
        
        def list_tasks(self, status_filter=None):
            """列出任务"""
            tasks = []
            for task in self.tasks.values():
                if status_filter is None or task.status == status_filter:
                    tasks.append(task.to_dict())
            return tasks
    
    # 测试函数
    def successful_task(name, duration=1):
        """成功的任务"""
        time.sleep(duration)
        return f"任务 {name} 完成"
    
    def failing_task(name, fail_rate=0.7):
        """可能失败的任务"""
        time.sleep(0.5)
        if random.random() < fail_rate:
            raise RuntimeError(f"任务 {name} 执行失败")
        return f"任务 {name} 成功"
    
    def timeout_task(name, duration=5):
        """超时任务"""
        time.sleep(duration)
        return f"任务 {name} 完成"
    
    # 测试代码
    print("测试任务调度系统：")
    
    # 创建调度器
    scheduler = TaskScheduler(max_workers=3, enable_retry=True)
    
    try:
        # 启动调度器
        scheduler.start()
        
        # 添加各种类型的任务
        print("\n添加任务：")
        
        # 成功任务
        scheduler.add_task(
            'task1', '快速任务', successful_task,
            args=('快速任务', 0.5), priority=TaskPriority.HIGH
        )
        
        # 可能失败的任务（带重试）
        scheduler.add_task(
            'task2', '不稳定任务', failing_task,
            args=('不稳定任务',), max_retries=2, retry_delay=1
        )
        
        # 超时任务
        scheduler.add_task(
            'task3', '超时任务', timeout_task,
            args=('超时任务', 3), timeout=2
        )
        
        # 低优先级任务
        scheduler.add_task(
            'task4', '低优先级任务', successful_task,
            args=('低优先级', 1), priority=TaskPriority.LOW
        )
        
        # 批量添加任务
        for i in range(5, 10):
            scheduler.add_task(
                f'batch_task_{i}', f'批量任务{i}', successful_task,
                args=(f'批量{i}', 0.3)
            )
        
        print(f"已添加 {len(scheduler.tasks)} 个任务")
        
        # 等待一些任务完成
        time.sleep(3)
        
        # 显示统计信息
        print("\n当前统计信息：")
        stats = scheduler.get_statistics()
        for key, value in stats.items():
            print(f"  {key}: {value}")
        
        # 显示任务状态
        print("\n任务状态：")
        for task_info in scheduler.list_tasks():
            print(f"  {task_info['name']} ({task_info['task_id']}): {task_info['status']}")
            if task_info['error']:
                print(f"    错误: {task_info['error']}")
        
        # 取消一个任务
        print("\n取消任务：")
        try:
            scheduler.cancel_task('batch_task_8')
            print("任务取消成功")
        except TaskNotFoundError as e:
            print(f"取消任务失败：{e}")
        
        # 等待更多任务完成
        time.sleep(5)
        
        # 最终统计
        print("\n最终统计信息：")
        final_stats = scheduler.get_statistics()
        for key, value in final_stats.items():
            print(f"  {key}: {value}")
        
        # 显示详细的任务信息
        print("\n详细任务信息：")
        for task_id in ['task1', 'task2', 'task3']:
            try:
                task_status = scheduler.get_task_status(task_id)
                print(f"\n任务 {task_id}:")
                for key, value in task_status.items():
                    if value is not None:
                        print(f"  {key}: {value}")
            except TaskNotFoundError:
                print(f"任务 {task_id} 不存在")
        
    except Exception as e:
        print(f"调度器测试过程中发生错误：{e}")
        traceback.print_exc()
    
    finally:
        # 停止调度器
        print("\n停止调度器...")
        scheduler.stop()
        print("调度器已停止")

# ============================================================================
# 学习要点总结
# ============================================================================

print("\n" + "=" * 60)
print("异常处理学习要点总结")
print("=" * 60)

print("""
1. 异常处理基础：
   - 使用try-except-else-finally结构
   - 捕获具体的异常类型而不是通用Exception
   - 合理使用else和finally子句
   - 理解异常的传播机制

2. 自定义异常设计：
   - 继承适当的内置异常类
   - 提供有意义的错误信息和错误代码
   - 包含相关的上下文信息
   - 设计异常层次结构

3. 异常处理最佳实践：
   - EAFP（Easier to Ask for Forgiveness than Permission）原则
   - 异常链和异常上下文
   - 资源管理和上下文管理器
   - 日志记录和错误监控

4. 高级异常处理技术：
   - 重试机制和指数退避
   - 异常聚合和批量处理
   - 装饰器模式的异常处理
   - 异步异常处理

5. 实际应用场景：
   - 网络请求的异常处理
   - 文件操作的异常处理
   - 数据验证和业务逻辑异常
   - 并发和多线程异常处理

6. 调试和诊断：
   - 异常信息的收集和分析
   - 堆栈跟踪的解读
   - 异常监控和告警
   - 性能影响的考虑

7. 编程最佳实践：
   - 异常安全的代码设计
   - 错误处理策略的选择
   - 异常文档和用户体验
   - 测试异常处理逻辑
""")

print("\n" + "=" * 60)
print("编程最佳实践")
print("=" * 60)

print("""
1. 异常设计原则：
   - 异常应该是异常情况，不是正常的控制流
   - 提供清晰、有用的错误信息
   - 使用异常层次结构组织相关异常
   - 包含足够的上下文信息用于调试

2. 异常处理策略：
   - 在适当的层级处理异常
   - 不要忽略异常或使用空的except块
   - 记录异常信息用于调试和监控
   - 考虑异常的恢复策略

3. 资源管理：
   - 使用上下文管理器确保资源释放
   - 在finally块中清理资源
   - 考虑异常情况下的资源泄漏
   - 使用RAII（Resource Acquisition Is Initialization）模式

4. 性能考虑：
   - 异常处理有性能开销，避免在热路径中使用
   - 使用条件检查而不是异常来处理预期的情况
   - 缓存异常对象以减少创建开销
   - 监控异常频率和性能影响

5. 测试和验证：
   - 编写测试用例覆盖异常路径
   - 使用模拟和注入技术测试异常处理
   - 验证异常信息的准确性和有用性
   - 测试异常恢复和重试逻辑
""")

# 运行所有示例
if __name__ == "__main__":
    try:
        # 运行基本异常处理示例
        solution_1_1()
        solution_1_2()
        solution_2_1()
        solution_2_2()
        solution_3_1()
        solution_3_2()
        solution_4_1()
        solution_4_2()
        solution_5_1()
        
        print("\n" + "=" * 60)
        print("所有异常处理练习题参考答案运行完成！")
        print("=" * 60)
        
    except Exception as e:
        print(f"运行示例时发生错误：{e}")
        traceback.print_exc()