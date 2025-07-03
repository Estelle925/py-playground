#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 模块和包 - 练习题参考答案

本文件包含了Python模块和包练习题的详细参考答案，包括：
1. 基础模块操作
2. 包的创建和使用
3. 导入机制
4. 模块搜索和动态导入
5. 高级特性应用
6. 实际项目应用
7. 综合应用

每个答案都包含完整的实现和详细的注释说明。

作者: Python学习者
日期: 2024年
"""

import os
import sys
import importlib
import importlib.util
import inspect
import json
import shutil
import subprocess
import threading
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from abc import ABC, abstractmethod
from functools import wraps
from concurrent.futures import ThreadPoolExecutor, as_completed

print("Python 模块和包 - 练习题参考答案")
print("=" * 50)

# ============================================================================
# 练习1: 基础模块操作 - 参考答案
# ============================================================================

print("\n练习1: 基础模块操作 - 参考答案")
print("-" * 40)

# 练习1.1: 创建数学工具模块 - 参考答案
print("\n练习1.1: 创建数学工具模块 - 参考答案")

# 创建 math_tools.py 模块
math_tools_code = '''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数学工具模块

提供常用的数学计算函数，包括阶乘、斐波那契数列、质数判断、
最大公约数和最小公倍数计算等功能。

Example:
    >>> import math_tools
    >>> math_tools.factorial(5)
    120
    >>> math_tools.fibonacci(10)
    55
    >>> math_tools.is_prime(17)
    True

Attributes:
    GOLDEN_RATIO (float): 黄金比例常数
    EULER_NUMBER (float): 欧拉数常数
"""

__version__ = '1.0.0'
__author__ = 'Python学习者'

# 模块级常量
GOLDEN_RATIO = 1.618033988749
EULER_NUMBER = 2.718281828459

# 控制导出的内容
__all__ = [
    'factorial', 'fibonacci', 'is_prime', 'gcd', 'lcm',
    'GOLDEN_RATIO', 'EULER_NUMBER'
]

def factorial(n):
    """计算阶乘
    
    Args:
        n (int): 非负整数
    
    Returns:
        int: n的阶乘
    
    Raises:
        ValueError: 当n为负数时
        TypeError: 当n不是整数时
    
    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError("参数必须是整数")
    if n < 0:
        raise ValueError("参数必须是非负整数")
    
    if n <= 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """计算斐波那契数列的第n项
    
    Args:
        n (int): 位置索引（从0开始）
    
    Returns:
        int: 斐波那契数列的第n项
    
    Raises:
        ValueError: 当n为负数时
        TypeError: 当n不是整数时
    
    Example:
        >>> fibonacci(10)
        55
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
    """
    if not isinstance(n, int):
        raise TypeError("参数必须是整数")
    if n < 0:
        raise ValueError("参数必须是非负整数")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(n):
    """判断是否为质数
    
    Args:
        n (int): 要判断的整数
    
    Returns:
        bool: 是否为质数
    
    Example:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(2)
        True
    """
    if not isinstance(n, int):
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 只需要检查到sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """计算最大公约数（使用欧几里得算法）
    
    Args:
        a (int): 第一个整数
        b (int): 第二个整数
    
    Returns:
        int: 最大公约数
    
    Example:
        >>> gcd(48, 18)
        6
        >>> gcd(17, 13)
        1
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("参数必须是整数")
    
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """计算最小公倍数
    
    Args:
        a (int): 第一个整数
        b (int): 第二个整数
    
    Returns:
        int: 最小公倍数
    
    Example:
        >>> lcm(12, 8)
        24
        >>> lcm(17, 13)
        221
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("参数必须是整数")
    
    if a == 0 or b == 0:
        return 0
    
    return abs(a * b) // gcd(a, b)

# 模块级别的初始化代码
if __name__ == '__main__':
    print(f"数学工具模块 v{__version__}")
    print(f"作者: {__author__}")
    print(f"黄金比例: {GOLDEN_RATIO}")
    print(f"欧拉数: {EULER_NUMBER}")
    
    # 简单测试
    print("\n简单测试:")
    print(f"5! = {factorial(5)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"lcm(12, 8) = {lcm(12, 8)}")
else:
    print(f"数学工具模块已导入 (v{__version__})")
'''

# 写入 math_tools.py 文件
with open('math_tools.py', 'w', encoding='utf-8') as f:
    f.write(math_tools_code)

print("已创建 math_tools.py 模块")

# 测试 math_tools 模块
def test_math_tools():
    """测试数学工具模块"""
    try:
        # 导入模块
        import math_tools
        
        print("\n测试结果:")
        
        # 测试函数
        print(f"5! = {math_tools.factorial(5)}")
        print(f"fibonacci(10) = {math_tools.fibonacci(10)}")
        print(f"is_prime(17) = {math_tools.is_prime(17)}")
        print(f"is_prime(4) = {math_tools.is_prime(4)}")
        print(f"gcd(48, 18) = {math_tools.gcd(48, 18)}")
        print(f"lcm(12, 8) = {math_tools.lcm(12, 8)}")
        
        # 测试常量
        print(f"黄金比例: {math_tools.GOLDEN_RATIO}")
        print(f"欧拉数: {math_tools.EULER_NUMBER}")
        
        # 测试 __all__
        print(f"模块导出: {math_tools.__all__}")
        
        # 测试模块元数据
        print(f"模块版本: {math_tools.__version__}")
        print(f"模块作者: {math_tools.__author__}")
        print(f"模块文档: {math_tools.__doc__[:50]}...")
        
        print("✓ math_tools 模块测试通过")
        
    except ImportError:
        print("✗ 请先创建 math_tools.py 模块")
    except Exception as e:
        print(f"✗ 测试失败: {e}")

# 运行测试
test_math_tools()

# 练习1.2: 模块属性和内省 - 参考答案
print("\n练习1.2: 模块属性和内省 - 参考答案")

def analyze_module(module_name):
    """分析模块信息
    
    Args:
        module_name (str): 模块名称
    """
    try:
        # 动态导入模块
        module = importlib.import_module(module_name)
        
        print(f"\n=== 模块分析: {module_name} ===")
        
        # 基本信息
        print("\n📋 基本信息:")
        print(f"  模块名称: {module.__name__}")
        print(f"  文件路径: {getattr(module, '__file__', '内置模块')}")
        print(f"  包名: {getattr(module, '__package__', 'None')}")
        
        # 文档字符串
        doc = getattr(module, '__doc__', None)
        if doc:
            print(f"  文档字符串: {doc[:100]}{'...' if len(doc) > 100 else ''}")
        else:
            print("  文档字符串: 无")
        
        # 版本信息
        version = getattr(module, '__version__', None)
        if version:
            print(f"  版本: {version}")
        
        # 作者信息
        author = getattr(module, '__author__', None)
        if author:
            print(f"  作者: {author}")
        
        # 获取所有属性
        all_attrs = dir(module)
        
        # 分析函数
        print("\n🔧 函数列表:")
        functions = []
        for name in all_attrs:
            if not name.startswith('_'):
                obj = getattr(module, name)
                if inspect.isfunction(obj):
                    functions.append(name)
                    # 获取函数签名
                    try:
                        sig = inspect.signature(obj)
                        doc = obj.__doc__
                        doc_summary = doc.split('\n')[0] if doc else '无文档'
                        print(f"  {name}{sig} - {doc_summary}")
                    except Exception:
                        print(f"  {name}() - 无法获取签名")
        
        if not functions:
            print("  无公共函数")
        
        # 分析类
        print("\n📦 类列表:")
        classes = []
        for name in all_attrs:
            if not name.startswith('_'):
                obj = getattr(module, name)
                if inspect.isclass(obj):
                    classes.append(name)
                    doc = obj.__doc__
                    doc_summary = doc.split('\n')[0] if doc else '无文档'
                    print(f"  {name} - {doc_summary}")
        
        if not classes:
            print("  无公共类")
        
        # 分析常量
        print("\n📊 常量列表:")
        constants = []
        for name in all_attrs:
            if not name.startswith('_') and name.isupper():
                obj = getattr(module, name)
                if not callable(obj) and not inspect.isclass(obj):
                    constants.append(name)
                    print(f"  {name} = {obj} ({type(obj).__name__})")
        
        if not constants:
            print("  无公共常量")
        
        # __all__ 属性
        print("\n📤 导出控制:")
        all_list = getattr(module, '__all__', None)
        if all_list:
            print(f"  __all__ = {all_list}")
        else:
            print("  __all__ = 未定义（导出所有公共属性）")
        
        # 统计信息
        print("\n📈 统计信息:")
        print(f"  总属性数: {len(all_attrs)}")
        print(f"  公共属性数: {len([name for name in all_attrs if not name.startswith('_')])}")
        print(f"  函数数: {len(functions)}")
        print(f"  类数: {len(classes)}")
        print(f"  常量数: {len(constants)}")
        
    except ImportError as e:
        print(f"✗ 无法导入模块 '{module_name}': {e}")
    except Exception as e:
        print(f"✗ 分析模块时出错: {e}")

def test_analyze_module():
    """测试模块分析功能"""
    print("\n测试模块分析功能:")
    
    # 分析内置模块
    analyze_module('math')
    
    # 分析标准库模块
    analyze_module('os')
    
    # 分析自定义模块
    analyze_module('math_tools')

# 运行测试
test_analyze_module()

# ============================================================================
# 练习2: 包的创建和使用 - 参考答案
# ============================================================================

print("\n\n练习2: 包的创建和使用 - 参考答案")
print("-" * 40)

# 练习2.1: 创建工具包 - 参考答案
print("\n练习2.1: 创建工具包 - 参考答案")

def create_mytools_package():
    """创建 mytools 包"""
    print("正在创建 mytools 包...")
    
    # 创建包目录结构
    package_dir = Path('mytools')
    validators_dir = package_dir / 'validators'
    
    # 创建目录
    package_dir.mkdir(exist_ok=True)
    validators_dir.mkdir(exist_ok=True)
    
    # 创建主包的 __init__.py
    init_code = '''
"""MyTools - 实用工具包

这是一个包含各种实用工具的Python包，包括字符串处理、
文件操作、数据处理和验证器等功能。

Example:
    >>> from mytools import string_utils
    >>> string_utils.reverse_string("hello")
    'olleh'
    
    >>> from mytools.validators import email_validator
    >>> email_validator.validate("test@example.com")
    True
"""

__version__ = '1.0.0'
__author__ = 'Python学习者'
__email__ = 'learner@example.com'

# 从子模块导入常用功能
from .string_utils import reverse_string, count_words, is_palindrome
from .file_utils import read_lines, write_lines, get_file_size
from .data_utils import flatten_list, merge_dicts

# 从验证器子包导入
from .validators.email_validator import validate as validate_email
from .validators.phone_validator import validate as validate_phone
from .validators.url_validator import validate as validate_url

# 定义包的公共接口
__all__ = [
    # 字符串工具
    'reverse_string', 'count_words', 'is_palindrome',
    # 文件工具
    'read_lines', 'write_lines', 'get_file_size',
    # 数据工具
    'flatten_list', 'merge_dicts',
    # 验证器
    'validate_email', 'validate_phone', 'validate_url',
    # 子模块
    'string_utils', 'file_utils', 'data_utils'
]

print(f"MyTools v{__version__} 包已加载")
'''
    
    with open(package_dir / '__init__.py', 'w', encoding='utf-8') as f:
        f.write(init_code)
    
    # 创建 string_utils.py
    string_utils_code = '''
"""字符串处理工具模块

提供各种字符串处理功能，包括反转、单词统计、
去重、回文检测等。
"""

import re
from collections import Counter

__all__ = ['reverse_string', 'count_words', 'remove_duplicates', 'is_palindrome']

def reverse_string(s):
    """反转字符串
    
    Args:
        s (str): 输入字符串
    
    Returns:
        str: 反转后的字符串
    
    Example:
        >>> reverse_string("hello")
        'olleh'
    """
    if not isinstance(s, str):
        raise TypeError("参数必须是字符串")
    return s[::-1]

def count_words(s):
    """统计单词数
    
    Args:
        s (str): 输入字符串
    
    Returns:
        int: 单词数量
    
    Example:
        >>> count_words("hello world python")
        3
    """
    if not isinstance(s, str):
        raise TypeError("参数必须是字符串")
    
    # 使用正则表达式分割单词
    words = re.findall(r'\\b\\w+\\b', s.lower())
    return len(words)

def remove_duplicates(s):
    """移除重复字符（保持顺序）
    
    Args:
        s (str): 输入字符串
    
    Returns:
        str: 去重后的字符串
    
    Example:
        >>> remove_duplicates("hello")
        'helo'
    """
    if not isinstance(s, str):
        raise TypeError("参数必须是字符串")
    
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def is_palindrome(s):
    """判断是否为回文
    
    Args:
        s (str): 输入字符串
    
    Returns:
        bool: 是否为回文
    
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    if not isinstance(s, str):
        raise TypeError("参数必须是字符串")
    
    # 只考虑字母和数字，忽略大小写
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]

def get_word_frequency(s):
    """获取单词频率统计
    
    Args:
        s (str): 输入字符串
    
    Returns:
        dict: 单词频率字典
    
    Example:
        >>> get_word_frequency("hello world hello")
        {'hello': 2, 'world': 1}
    """
    if not isinstance(s, str):
        raise TypeError("参数必须是字符串")
    
    words = re.findall(r'\\b\\w+\\b', s.lower())
    return dict(Counter(words))
'''
    
    with open(package_dir / 'string_utils.py', 'w', encoding='utf-8') as f:
        f.write(string_utils_code)
    
    # 创建 file_utils.py
    file_utils_code = '''
"""文件操作工具模块

提供各种文件操作功能，包括读写文件、获取文件信息、
备份文件等。
"""

import os
import shutil
from pathlib import Path
from typing import List, Union

__all__ = ['read_lines', 'write_lines', 'get_file_size', 'backup_file']

def read_lines(filename):
    """读取文件所有行
    
    Args:
        filename (str): 文件路径
    
    Returns:
        list: 文件行列表
    
    Raises:
        FileNotFoundError: 文件不存在
        IOError: 读取文件失败
    
    Example:
        >>> lines = read_lines("test.txt")
        >>> print(len(lines))
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {filename}")
    except Exception as e:
        raise IOError(f"读取文件失败: {e}")

def write_lines(filename, lines):
    """写入多行到文件
    
    Args:
        filename (str): 文件路径
        lines (list): 要写入的行列表
    
    Returns:
        bool: 是否成功写入
    
    Example:
        >>> write_lines("output.txt", ["line1\\n", "line2\\n"])
        True
    """
    try:
        # 确保目录存在
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        return True
    except Exception as e:
        print(f"写入文件失败: {e}")
        return False

def get_file_size(filename):
    """获取文件大小
    
    Args:
        filename (str): 文件路径
    
    Returns:
        int: 文件大小（字节）
    
    Raises:
        FileNotFoundError: 文件不存在
    
    Example:
        >>> size = get_file_size("test.txt")
        >>> print(f"文件大小: {size} 字节")
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"文件不存在: {filename}")
    
    return os.path.getsize(filename)

def backup_file(filename, backup_suffix='.bak'):
    """备份文件
    
    Args:
        filename (str): 要备份的文件路径
        backup_suffix (str): 备份文件后缀
    
    Returns:
        str: 备份文件路径，失败时返回None
    
    Example:
        >>> backup_path = backup_file("important.txt")
        >>> print(f"备份到: {backup_path}")
    """
    if not os.path.exists(filename):
        print(f"文件不存在: {filename}")
        return None
    
    try:
        backup_path = filename + backup_suffix
        shutil.copy2(filename, backup_path)
        return backup_path
    except Exception as e:
        print(f"备份文件失败: {e}")
        return None

def get_file_info(filename):
    """获取文件详细信息
    
    Args:
        filename (str): 文件路径
    
    Returns:
        dict: 文件信息字典
    
    Example:
        >>> info = get_file_info("test.txt")
        >>> print(info['size'], info['modified'])
    """
    if not os.path.exists(filename):
        return None
    
    stat = os.stat(filename)
    return {
        'size': stat.st_size,
        'modified': stat.st_mtime,
        'created': stat.st_ctime,
        'is_file': os.path.isfile(filename),
        'is_dir': os.path.isdir(filename),
        'permissions': oct(stat.st_mode)[-3:]
    }
'''
    
    with open(package_dir / 'file_utils.py', 'w', encoding='utf-8') as f:
        f.write(file_utils_code)
    
    # 创建 data_utils.py
    data_utils_code = '''
"""数据处理工具模块

提供各种数据处理功能，包括列表扁平化、字典操作、
数据分组等。
"""

from typing import Any, Dict, List, Callable, Union
from collections import defaultdict
from functools import reduce

__all__ = ['flatten_list', 'group_by_key', 'merge_dicts', 'filter_dict']

def flatten_list(nested_list):
    """扁平化嵌套列表
    
    Args:
        nested_list: 嵌套列表
    
    Returns:
        list: 扁平化后的列表
    
    Example:
        >>> flatten_list([[1, 2], [3, [4, 5]], 6])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    
    def _flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                _flatten(sub_item)
        else:
            result.append(item)
    
    _flatten(nested_list)
    return result

def group_by_key(items, key):
    """按键分组
    
    Args:
        items (list): 要分组的项目列表
        key (str or function): 分组键或键函数
    
    Returns:
        dict: 分组结果字典
    
    Example:
        >>> data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}]
        >>> group_by_key(data, 'age')
        {25: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 25}]}
    """
    groups = defaultdict(list)
    
    for item in items:
        if callable(key):
            group_key = key(item)
        elif isinstance(item, dict):
            group_key = item.get(key)
        else:
            group_key = getattr(item, key, None)
        
        groups[group_key].append(item)
    
    return dict(groups)

def merge_dicts(*dicts):
    """合并多个字典
    
    Args:
        *dicts: 要合并的字典
    
    Returns:
        dict: 合并后的字典
    
    Example:
        >>> merge_dicts({'a': 1}, {'b': 2}, {'c': 3})
        {'a': 1, 'b': 2, 'c': 3}
    """
    result = {}
    for d in dicts:
        if isinstance(d, dict):
            result.update(d)
    return result

def filter_dict(d, condition):
    """过滤字典
    
    Args:
        d (dict): 要过滤的字典
        condition (function): 过滤条件函数
    
    Returns:
        dict: 过滤后的字典
    
    Example:
        >>> data = {'a': 1, 'b': 2, 'c': 3}
        >>> filter_dict(data, lambda k, v: v > 1)
        {'b': 2, 'c': 3}
    """
    return {k: v for k, v in d.items() if condition(k, v)}

def chunk_list(lst, chunk_size):
    """将列表分块
    
    Args:
        lst (list): 要分块的列表
        chunk_size (int): 块大小
    
    Returns:
        list: 分块后的列表
    
    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def unique_list(lst, key=None):
    """去除列表重复项（保持顺序）
    
    Args:
        lst (list): 输入列表
        key (function): 用于比较的键函数
    
    Returns:
        list: 去重后的列表
    
    Example:
        >>> unique_list([1, 2, 2, 3, 1])
        [1, 2, 3]
    """
    seen = set()
    result = []
    
    for item in lst:
        check_item = key(item) if key else item
        if check_item not in seen:
            seen.add(check_item)
            result.append(item)
    
    return result
'''
    
    with open(package_dir / 'data_utils.py', 'w', encoding='utf-8') as f:
        f.write(data_utils_code)
    
    # 创建验证器子包的 __init__.py
    validators_init_code = '''
"""验证器子包

提供各种数据验证功能，包括邮箱、电话号码、URL等验证器。
"""

from .email_validator import validate as validate_email
from .phone_validator import validate as validate_phone
from .url_validator import validate as validate_url

__all__ = ['validate_email', 'validate_phone', 'validate_url']

print("验证器子包已加载")
'''
    
    with open(validators_dir / '__init__.py', 'w', encoding='utf-8') as f:
        f.write(validators_init_code)
    
    # 创建 email_validator.py
    email_validator_code = '''
"""邮箱验证器模块

提供邮箱地址格式验证功能。
"""

import re

__all__ = ['validate', 'is_valid_domain', 'extract_domain']

# 邮箱正则表达式
EMAIL_PATTERN = re.compile(
    r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
)

def validate(email):
    """验证邮箱格式
    
    Args:
        email (str): 邮箱地址
    
    Returns:
        bool: 是否为有效邮箱
    
    Example:
        >>> validate("test@example.com")
        True
        >>> validate("invalid-email")
        False
    """
    if not isinstance(email, str):
        return False
    
    return bool(EMAIL_PATTERN.match(email.strip()))

def is_valid_domain(domain):
    """验证域名格式
    
    Args:
        domain (str): 域名
    
    Returns:
        bool: 是否为有效域名
    
    Example:
        >>> is_valid_domain("example.com")
        True
    """
    if not isinstance(domain, str):
        return False
    
    domain_pattern = re.compile(
        r'^[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    )
    return bool(domain_pattern.match(domain.strip()))

def extract_domain(email):
    """从邮箱地址提取域名
    
    Args:
        email (str): 邮箱地址
    
    Returns:
        str: 域名，无效邮箱返回None
    
    Example:
        >>> extract_domain("test@example.com")
        'example.com'
    """
    if not validate(email):
        return None
    
    return email.split('@')[1]
'''
    
    with open(validators_dir / 'email_validator.py', 'w', encoding='utf-8') as f:
        f.write(email_validator_code)
    
    # 创建 phone_validator.py
    phone_validator_code = '''
"""电话号码验证器模块

提供电话号码格式验证功能，支持多种格式。
"""

import re

__all__ = ['validate', 'format_phone', 'extract_digits']

# 电话号码正则表达式（支持多种格式）
PHONE_PATTERNS = [
    re.compile(r'^\\+?1?[-.\\s]?\\(?([0-9]{3})\\)?[-.\\s]?([0-9]{3})[-.\\s]?([0-9]{4})$'),  # 美国格式
    re.compile(r'^\\+?86[-.\\s]?1[3-9][0-9]{9}$'),  # 中国手机号
    re.compile(r'^\\+?[1-9][0-9]{7,14}$'),  # 国际格式
]

def validate(phone):
    """验证电话号码格式
    
    Args:
        phone (str): 电话号码
    
    Returns:
        bool: 是否为有效电话号码
    
    Example:
        >>> validate("+1-555-123-4567")
        True
        >>> validate("13812345678")
        True
    """
    if not isinstance(phone, str):
        return False
    
    phone = phone.strip()
    return any(pattern.match(phone) for pattern in PHONE_PATTERNS)

def format_phone(phone, format_type='standard'):
    """格式化电话号码
    
    Args:
        phone (str): 电话号码
        format_type (str): 格式类型 ('standard', 'dots', 'spaces')
    
    Returns:
        str: 格式化后的电话号码
    
    Example:
        >>> format_phone("5551234567", "standard")
        '(555) 123-4567'
    """
    digits = extract_digits(phone)
    if not digits or len(digits) < 10:
        return phone
    
    if len(digits) == 10:
        if format_type == 'standard':
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        elif format_type == 'dots':
            return f"{digits[:3]}.{digits[3:6]}.{digits[6:]}"
        elif format_type == 'spaces':
            return f"{digits[:3]} {digits[3:6]} {digits[6:]}"
    
    return phone

def extract_digits(phone):
    """提取电话号码中的数字
    
    Args:
        phone (str): 电话号码
    
    Returns:
        str: 纯数字字符串
    
    Example:
        >>> extract_digits("+1-555-123-4567")
        '15551234567'
    """
    if not isinstance(phone, str):
        return ''
    
    return re.sub(r'[^0-9]', '', phone)
'''
    
    with open(validators_dir / 'phone_validator.py', 'w', encoding='utf-8') as f:
        f.write(phone_validator_code)
    
    # 创建 url_validator.py
    url_validator_code = '''
"""URL验证器模块

提供URL格式验证功能。
"""

import re
from urllib.parse import urlparse

__all__ = ['validate', 'is_valid_scheme', 'extract_domain']

# URL正则表达式
URL_PATTERN = re.compile(
    r'^https?://'  # http:// 或 https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\\.)+'  # 域名
    r'(?:[A-Z]{2,6}\\.?|[A-Z0-9-]{2,}\\.?)|'  # 顶级域名
    r'localhost|'  # localhost
    r'\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})'  # IP地址
    r'(?::\\d+)?'  # 端口号
    r'(?:/?|[/?]\\S+)$', re.IGNORECASE)

def validate(url):
    """验证URL格式
    
    Args:
        url (str): URL地址
    
    Returns:
        bool: 是否为有效URL
    
    Example:
        >>> validate("https://www.example.com")
        True
        >>> validate("invalid-url")
        False
    """
    if not isinstance(url, str):
        return False
    
    return bool(URL_PATTERN.match(url.strip()))

def is_valid_scheme(url):
    """检查URL协议是否有效
    
    Args:
        url (str): URL地址
    
    Returns:
        bool: 协议是否有效
    
    Example:
        >>> is_valid_scheme("https://example.com")
        True
    """
    try:
        parsed = urlparse(url)
        return parsed.scheme in ['http', 'https']
    except Exception:
        return False

def extract_domain(url):
    """从URL提取域名
    
    Args:
        url (str): URL地址
    
    Returns:
        str: 域名，无效URL返回None
    
    Example:
        >>> extract_domain("https://www.example.com/path")
        'www.example.com'
    """
    try:
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return None
'''
    
    with open(validators_dir / 'url_validator.py', 'w', encoding='utf-8') as f:
        f.write(url_validator_code)
    
    print("✓ mytools 包创建完成")
    print("\n包结构:")
    print("mytools/")
    print("  __init__.py")
    print("  string_utils.py")
    print("  file_utils.py")
    print("  data_utils.py")
    print("  validators/")
    print("    __init__.py")
    print("    email_validator.py")
    print("    phone_validator.py")
    print("    url_validator.py")

def test_mytools_package():
    """测试 mytools 包"""
    try:
        print("\n测试 mytools 包:")
        
        # 测试导入
        import mytools
        print(f"包版本: {mytools.__version__}")
        print(f"包作者: {mytools.__author__}")
        
        # 测试字符串工具
        from mytools import string_utils
        print(f"\n字符串工具测试:")
        print(f"反转字符串: {string_utils.reverse_string('hello')}")
        print(f"单词计数: {string_utils.count_words('hello world python')}")
        print(f"去重: {string_utils.remove_duplicates('hello')}")
        print(f"回文检测: {string_utils.is_palindrome('racecar')}")
        
        # 测试数据工具
        from mytools import data_utils
        print(f"\n数据工具测试:")
        nested = [[1, 2], [3, [4, 5]], 6]
        print(f"扁平化列表: {data_utils.flatten_list(nested)}")
        
        dicts = [{'a': 1}, {'b': 2}, {'c': 3}]
        print(f"合并字典: {data_utils.merge_dicts(*dicts)}")
        
        # 测试验证器
        from mytools.validators import email_validator, phone_validator, url_validator
        print(f"\n验证器测试:")
        print(f"邮箱验证: {email_validator.validate('test@example.com')}")
        print(f"电话验证: {phone_validator.validate('+1-555-123-4567')}")
        print(f"URL验证: {url_validator.validate('https://www.example.com')}")
        
        # 测试包级别的导入
        print(f"\n包级别导入测试:")
        print(f"包级别反转: {mytools.reverse_string('world')}")
        print(f"包级别邮箱验证: {mytools.validate_email('user@domain.com')}")
        
        print("\n✓ mytools 包测试通过")
        
    except ImportError as e:
        print(f"✗ 导入失败: {e}")
    except Exception as e:
        print(f"✗ 测试失败: {e}")

# 创建并测试包
create_mytools_package()
test_mytools_package()