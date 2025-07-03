#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 模块和包 - 练习题

本文件包含了Python模块和包的各种练习题，包括：
1. 基础模块操作
2. 包的创建和使用
3. 导入机制
4. 模块搜索和动态导入
5. 高级特性应用
6. 实际项目应用
7. 综合应用

每个练习都包含详细的要求和测试代码。

作者: Python学习者
日期: 2024年
"""

import os
import sys
from pathlib import Path

print("Python 模块和包 - 练习题")
print("=" * 50)

# ============================================================================
# 练习1: 基础模块操作
# ============================================================================

print("\n练习1: 基础模块操作")
print("-" * 30)

# 练习1.1: 创建数学工具模块
print("\n练习1.1: 创建数学工具模块")
print("""
要求:
1. 创建一个名为 'math_tools.py' 的模块
2. 实现以下函数:
   - factorial(n): 计算阶乘
   - fibonacci(n): 计算斐波那契数列的第n项
   - is_prime(n): 判断是否为质数
   - gcd(a, b): 计算最大公约数
   - lcm(a, b): 计算最小公倍数
3. 添加模块级常量:
   - GOLDEN_RATIO = 1.618033988749
   - EULER_NUMBER = 2.718281828459
4. 添加模块文档字符串和函数文档字符串
5. 实现 __all__ 列表控制导出的内容
""")

# TODO: 在这里实现 math_tools.py 模块
# 提示: 创建文件并实现所有要求的函数和常量

def test_math_tools():
    """测试数学工具模块"""
    try:
        # 导入模块
        import math_tools
        
        # 测试函数
        print(f"5! = {math_tools.factorial(5)}")
        print(f"fibonacci(10) = {math_tools.fibonacci(10)}")
        print(f"is_prime(17) = {math_tools.is_prime(17)}")
        print(f"gcd(48, 18) = {math_tools.gcd(48, 18)}")
        print(f"lcm(12, 8) = {math_tools.lcm(12, 8)}")
        
        # 测试常量
        print(f"黄金比例: {math_tools.GOLDEN_RATIO}")
        print(f"欧拉数: {math_tools.EULER_NUMBER}")
        
        # 测试 __all__
        print(f"模块导出: {math_tools.__all__}")
        
        print("✓ math_tools 模块测试通过")
        
    except ImportError:
        print("✗ 请先创建 math_tools.py 模块")
    except Exception as e:
        print(f"✗ 测试失败: {e}")

# 运行测试
# test_math_tools()

# 练习1.2: 模块属性和内省
print("\n练习1.2: 模块属性和内省")
print("""
要求:
1. 创建一个函数 analyze_module(module_name)
2. 该函数应该分析指定模块的以下信息:
   - 模块名称、文件路径、文档字符串
   - 模块中的所有函数（不包括私有函数）
   - 模块中的所有类
   - 模块中的所有常量（大写变量）
   - 模块的 __all__ 属性（如果存在）
3. 以格式化的方式输出分析结果
""")

def analyze_module(module_name):
    """分析模块信息
    
    Args:
        module_name (str): 模块名称
    """
    try:
        import importlib
        import inspect
        
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
    print("分析 os 模块:")
    analyze_module('os')
    
    print("\n分析 math 模块:")
    analyze_module('math')

# 运行测试
# test_analyze_module()

# ============================================================================
# 练习2: 包的创建和使用
# ============================================================================

print("\n\n练习2: 包的创建和使用")
print("-" * 30)

# 练习2.1: 创建工具包
print("\n练习2.1: 创建工具包")
print("""
要求:
1. 创建一个名为 'mytools' 的包，包含以下结构:
   mytools/
   ├── __init__.py
   ├── string_utils.py
   ├── file_utils.py
   ├── data_utils.py
   └── validators/
       ├── __init__.py
       ├── email_validator.py
       ├── phone_validator.py
       └── url_validator.py

2. string_utils.py 应包含:
   - reverse_string(s): 反转字符串
   - count_words(s): 统计单词数
   - remove_duplicates(s): 移除重复字符
   - is_palindrome(s): 判断是否为回文

3. file_utils.py 应包含:
   - read_lines(filename): 读取文件所有行
   - write_lines(filename, lines): 写入多行到文件
   - get_file_size(filename): 获取文件大小
   - backup_file(filename): 备份文件

4. data_utils.py 应包含:
   - flatten_list(nested_list): 扁平化嵌套列表
   - group_by_key(items, key): 按键分组
   - merge_dicts(*dicts): 合并多个字典
   - filter_dict(d, condition): 过滤字典

5. validators 子包应包含各种验证器

6. 在 __init__.py 中正确导入和组织这些模块
""")

# TODO: 创建完整的 mytools 包结构
# 提示: 使用 os.makedirs() 创建目录，用文件写入创建模块

def create_mytools_package():
    """创建 mytools 包"""
    from pathlib import Path
    
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
'''
    
    with open(package_dir / 'string_utils.py', 'w', encoding='utf-8') as f:
        f.write(string_utils_code)
    
    # 创建 file_utils.py
    file_utils_code = '''
"""文件操作工具模块

提供各种文件操作功能，包括读取、写入、
文件信息获取等。
"""

import os
from pathlib import Path
from typing import List, Union

__all__ = ['read_lines', 'write_lines', 'get_file_size', 'copy_file', 'file_exists']

def read_lines(file_path: Union[str, Path]) -> List[str]:
    """读取文件所有行
    
    Args:
        file_path: 文件路径
    
    Returns:
        List[str]: 文件内容行列表
    
    Example:
        >>> lines = read_lines('test.txt')
        >>> print(len(lines))
        10
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {file_path}")
    except Exception as e:
        raise IOError(f"读取文件失败: {e}")

def write_lines(file_path: Union[str, Path], lines: List[str]) -> None:
    """写入行到文件
    
    Args:
        file_path: 文件路径
        lines: 要写入的行列表
    
    Example:
        >>> write_lines('output.txt', ['line1\\n', 'line2\\n'])
    """
    try:
        # 确保目录存在
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except Exception as e:
        raise IOError(f"写入文件失败: {e}")

def get_file_size(file_path: Union[str, Path]) -> int:
    """获取文件大小（字节）
    
    Args:
        file_path: 文件路径
    
    Returns:
        int: 文件大小（字节）
    
    Example:
        >>> size = get_file_size('test.txt')
        >>> print(f"文件大小: {size} 字节")
    """
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {file_path}")
    except Exception as e:
        raise IOError(f"获取文件大小失败: {e}")

def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """复制文件
    
    Args:
        src: 源文件路径
        dst: 目标文件路径
    
    Example:
        >>> copy_file('source.txt', 'backup.txt')
    """
    import shutil
    try:
        # 确保目标目录存在
        Path(dst).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    except Exception as e:
        raise IOError(f"复制文件失败: {e}")

def file_exists(file_path: Union[str, Path]) -> bool:
    """检查文件是否存在
    
    Args:
        file_path: 文件路径
    
    Returns:
        bool: 文件是否存在
    
    Example:
        >>> if file_exists('config.txt'):
        ...     print("配置文件存在")
    """
    return Path(file_path).exists()
'''
    
    with open(package_dir / 'file_utils.py', 'w', encoding='utf-8') as f:
        f.write(file_utils_code)
    
    # 创建 data_utils.py
    data_utils_code = '''
"""数据处理工具模块

提供各种数据处理功能，包括列表扁平化、
字典合并、数据转换等。
"""

from typing import List, Dict, Any, Union
from collections import defaultdict
import json

__all__ = ['flatten_list', 'merge_dicts', 'group_by', 'filter_dict', 'to_json']

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """扁平化嵌套列表
    
    Args:
        nested_list: 嵌套列表
    
    Returns:
        List[Any]: 扁平化后的列表
    
    Example:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """合并多个字典
    
    Args:
        *dicts: 要合并的字典
    
    Returns:
        Dict[str, Any]: 合并后的字典
    
    Example:
        >>> d1 = {'a': 1, 'b': 2}
        >>> d2 = {'b': 3, 'c': 4}
        >>> merge_dicts(d1, d2)
        {'a': 1, 'b': 3, 'c': 4}
    """
    result = {}
    for d in dicts:
        if isinstance(d, dict):
            result.update(d)
    return result

def group_by(items: List[Any], key_func) -> Dict[Any, List[Any]]:
    """按指定函数分组
    
    Args:
        items: 要分组的项目列表
        key_func: 分组键函数
    
    Returns:
        Dict[Any, List[Any]]: 分组结果
    
    Example:
        >>> words = ['apple', 'banana', 'apricot', 'blueberry']
        >>> group_by(words, lambda x: x[0])
        {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    """
    groups = defaultdict(list)
    for item in items:
        key = key_func(item)
        groups[key].append(item)
    return dict(groups)

def filter_dict(d: Dict[str, Any], predicate) -> Dict[str, Any]:
    """过滤字典
    
    Args:
        d: 要过滤的字典
        predicate: 过滤条件函数
    
    Returns:
        Dict[str, Any]: 过滤后的字典
    
    Example:
        >>> data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        >>> filter_dict(data, lambda k, v: v > 2)
        {'c': 3, 'd': 4}
    """
    return {k: v for k, v in d.items() if predicate(k, v)}

def to_json(data: Any, indent: int = 2) -> str:
    """转换为JSON字符串
    
    Args:
        data: 要转换的数据
        indent: 缩进空格数
    
    Returns:
        str: JSON字符串
    
    Example:
        >>> data = {'name': 'Alice', 'age': 30}
        >>> print(to_json(data))
        {
          "name": "Alice",
          "age": 30
        }
    """
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except TypeError as e:
        raise ValueError(f"数据无法序列化为JSON: {e}")
'''
    
    with open(package_dir / 'data_utils.py', 'w', encoding='utf-8') as f:
        f.write(data_utils_code)
    
    # 创建 validators 子包的 __init__.py
    validators_init_code = '''
"""验证器子包

提供各种数据验证功能，包括邮箱、电话、URL等验证。
"""

from .email_validator import validate as validate_email
from .phone_validator import validate as validate_phone
from .url_validator import validate as validate_url

__all__ = ['validate_email', 'validate_phone', 'validate_url']

print("验证器模块已加载")
'''
    
    with open(validators_dir / '__init__.py', 'w', encoding='utf-8') as f:
        f.write(validators_init_code)
    
    # 创建 email_validator.py
    email_validator_code = '''
"""邮箱验证器模块"""

import re

__all__ = ['validate', 'is_valid_domain']

def validate(email: str) -> bool:
    """验证邮箱地址
    
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
    
    # 基本的邮箱正则表达式
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False
    
    # 检查域名部分
    domain = email.split('@')[1]
    return is_valid_domain(domain)

def is_valid_domain(domain: str) -> bool:
    """验证域名
    
    Args:
        domain (str): 域名
    
    Returns:
        bool: 是否为有效域名
    """
    if not domain or len(domain) > 255:
        return False
    
    # 检查域名格式
    domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
    parts = domain.split('.')
    
    if len(parts) < 2:
        return False
    
    for part in parts:
        if not re.match(domain_pattern, part):
            return False
    
    return True
'''
    
    with open(validators_dir / 'email_validator.py', 'w', encoding='utf-8') as f:
        f.write(email_validator_code)
    
    # 创建 phone_validator.py
    phone_validator_code = '''
"""电话号码验证器模块"""

import re

__all__ = ['validate', 'format_phone']

def validate(phone: str) -> bool:
    """验证电话号码
    
    Args:
        phone (str): 电话号码
    
    Returns:
        bool: 是否为有效电话号码
    
    Example:
        >>> validate("+86-138-0013-8000")
        True
        >>> validate("13800138000")
        True
        >>> validate("invalid")
        False
    """
    if not isinstance(phone, str):
        return False
    
    # 清理电话号码（移除空格、横线等）
    cleaned = re.sub(r'[\\s\\-\\(\\)]', '', phone)
    
    # 支持多种格式
    patterns = [
        r'^\\+?86[1-9]\\d{10}$',  # 中国手机号（带国家码）
        r'^1[3-9]\\d{9}$',        # 中国手机号
        r'^\\+?1[2-9]\\d{2}[2-9]\\d{2}\\d{4}$',  # 美国电话
        r'^\\+?[1-9]\\d{1,14}$'   # 国际格式
    ]
    
    return any(re.match(pattern, cleaned) for pattern in patterns)

def format_phone(phone: str, format_type: str = 'standard') -> str:
    """格式化电话号码
    
    Args:
        phone (str): 电话号码
        format_type (str): 格式类型 ('standard', 'international')
    
    Returns:
        str: 格式化后的电话号码
    
    Example:
        >>> format_phone("13800138000")
        '138-0013-8000'
    """
    if not validate(phone):
        raise ValueError("无效的电话号码")
    
    cleaned = re.sub(r'[\\s\\-\\(\\)]', '', phone)
    
    if format_type == 'standard' and len(cleaned) == 11 and cleaned.startswith('1'):
        # 中国手机号格式
        return f"{cleaned[:3]}-{cleaned[3:7]}-{cleaned[7:]}"
    elif format_type == 'international':
        if not cleaned.startswith('+'):
            cleaned = '+86' + cleaned
        return cleaned
    
    return cleaned
'''
    
    with open(validators_dir / 'phone_validator.py', 'w', encoding='utf-8') as f:
        f.write(phone_validator_code)
    
    # 创建 url_validator.py
    url_validator_code = '''
"""URL验证器模块"""

import re
from urllib.parse import urlparse

__all__ = ['validate', 'is_valid_scheme', 'extract_domain']

def validate(url: str) -> bool:
    """验证URL
    
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
    
    try:
        result = urlparse(url)
        
        # 检查基本组件
        if not all([result.scheme, result.netloc]):
            return False
        
        # 检查协议
        if not is_valid_scheme(result.scheme):
            return False
        
        # 检查域名格式
        domain_pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?$'
        domain_parts = result.netloc.split('.')
        
        if len(domain_parts) < 2:
            return False
        
        for part in domain_parts:
            if not re.match(domain_pattern, part):
                return False
        
        return True
        
    except Exception:
        return False

def is_valid_scheme(scheme: str) -> bool:
    """验证URL协议
    
    Args:
        scheme (str): URL协议
    
    Returns:
        bool: 是否为有效协议
    """
    valid_schemes = {'http', 'https', 'ftp', 'ftps', 'file', 'mailto'}
    return scheme.lower() in valid_schemes

def extract_domain(url: str) -> str:
    """提取URL的域名
    
    Args:
        url (str): URL地址
    
    Returns:
        str: 域名
    
    Example:
        >>> extract_domain("https://www.example.com/path")
        'www.example.com'
    """
    if not validate(url):
        raise ValueError("无效的URL")
    
    result = urlparse(url)
    return result.netloc
'''
    
    with open(validators_dir / 'url_validator.py', 'w', encoding='utf-8') as f:
        f.write(url_validator_code)
    
    print("✓ mytools 包创建完成")

def test_mytools_package():
    """测试 mytools 包"""
    print("\n=== 测试 mytools 包 ===")
    
    try:
        # 首先创建包（如果不存在）
        create_mytools_package()
        
        # 测试导入主包
        print("\n1. 测试包导入...")
        import mytools
        print(f"✓ 包版本: {mytools.__version__}")
        print(f"✓ 包作者: {mytools.__author__}")
        
        # 测试字符串工具
        print("\n2. 测试字符串工具...")
        from mytools import string_utils
        
        test_str = "hello world"
        reversed_str = string_utils.reverse_string(test_str)
        print(f"✓ 反转字符串: '{test_str}' -> '{reversed_str}'")
        
        word_count = string_utils.count_words(test_str)
        print(f"✓ 单词统计: '{test_str}' 有 {word_count} 个单词")
        
        palindrome_test = string_utils.is_palindrome("racecar")
        print(f"✓ 回文检测: 'racecar' 是回文: {palindrome_test}")
        
        # 测试文件工具
        print("\n3. 测试文件工具...")
        from mytools import file_utils
        
        # 创建测试文件
        test_lines = ["第一行\n", "第二行\n", "第三行\n"]
        test_file = "test_output.txt"
        
        file_utils.write_lines(test_file, test_lines)
        print(f"✓ 写入文件: {test_file}")
        
        if file_utils.file_exists(test_file):
            file_size = file_utils.get_file_size(test_file)
            print(f"✓ 文件大小: {file_size} 字节")
            
            read_lines = file_utils.read_lines(test_file)
            print(f"✓ 读取文件: 共 {len(read_lines)} 行")
        
        # 测试数据工具
        print("\n4. 测试数据工具...")
        from mytools import data_utils
        
        nested_list = [1, [2, 3], [4, [5, 6]]]
        flattened = data_utils.flatten_list(nested_list)
        print(f"✓ 列表扁平化: {nested_list} -> {flattened}")
        
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        merged = data_utils.merge_dicts(dict1, dict2)
        print(f"✓ 字典合并: {dict1} + {dict2} = {merged}")
        
        # 测试验证器
        print("\n5. 测试验证器...")
        from mytools.validators import email_validator, phone_validator, url_validator
        
        # 邮箱验证
        email_tests = ["test@example.com", "invalid-email"]
        for email in email_tests:
            is_valid = email_validator.validate(email)
            print(f"✓ 邮箱验证: '{email}' -> {is_valid}")
        
        # 电话验证
        phone_tests = ["13800138000", "+86-138-0013-8000", "invalid"]
        for phone in phone_tests:
            is_valid = phone_validator.validate(phone)
            print(f"✓ 电话验证: '{phone}' -> {is_valid}")
        
        # URL验证
        url_tests = ["https://www.example.com", "invalid-url"]
        for url in url_tests:
            is_valid = url_validator.validate(url)
            print(f"✓ URL验证: '{url}' -> {is_valid}")
        
        # 测试包级别的导入
        print("\n6. 测试包级别导入...")
        from mytools import reverse_string, validate_email, flatten_list
        
        print(f"✓ 直接导入函数: reverse_string('test') = '{reverse_string('test')}'")
        print(f"✓ 直接导入验证器: validate_email('test@example.com') = {validate_email('test@example.com')}")
        print(f"✓ 直接导入数据工具: flatten_list([1, [2, 3]]) = {flatten_list([1, [2, 3]])}")
        
        print("\n✅ mytools 包测试完成！所有功能正常工作。")
        
        # 清理测试文件
        import os
        if os.path.exists(test_file):
            os.remove(test_file)
            print(f"✓ 清理测试文件: {test_file}")
            
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        print("请确保 mytools 包已正确创建")
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

# 运行测试
# create_mytools_package()
# test_mytools_package()

# 练习2.2: 相对导入和绝对导入
print("\n练习2.2: 相对导入和绝对导入")
print("""
要求:
1. 在 mytools 包中演示相对导入的使用
2. 创建一个模块使用相对导入引用同包中的其他模块
3. 创建一个模块使用绝对导入引用其他包的模块
4. 比较两种导入方式的优缺点
5. 处理循环导入问题
""")

# TODO: 实现相对导入和绝对导入的示例

# ============================================================================
# 练习3: 导入机制和模块搜索
# ============================================================================

print("\n\n练习3: 导入机制和模块搜索")
print("-" * 30)

# 练习3.1: 自定义模块查找器
print("\n练习3.1: 自定义模块查找器")
print("""
要求:
1. 创建一个自定义的模块查找器类 CustomFinder
2. 实现从特定目录或URL加载模块的功能
3. 将查找器添加到 sys.meta_path
4. 测试自定义模块的加载
5. 实现模块的缓存机制
""")

class CustomFinder:
    """自定义模块查找器"""
    
    def __init__(self, search_paths):
        self.search_paths = search_paths
    
    def find_spec(self, fullname, path, target=None):
        """查找模块规范"""
        # TODO: 实现模块查找逻辑
        pass
    
    def find_module(self, fullname, path=None):
        """查找模块（兼容旧版本）"""
        # TODO: 实现模块查找逻辑
        pass

def test_custom_finder():
    """测试自定义查找器"""
    # TODO: 实现测试逻辑
    pass

# 练习3.2: 动态模块加载系统
print("\n练习3.2: 动态模块加载系统")
print("""
要求:
1. 创建一个 ModuleLoader 类
2. 支持从配置文件动态加载模块
3. 支持模块的热重载
4. 支持模块依赖关系管理
5. 实现模块加载的错误处理和回滚
""")

class ModuleLoader:
    """动态模块加载器"""
    
    def __init__(self, config_file=None):
        self.loaded_modules = {}
        self.dependencies = {}
        self.config_file = config_file
    
    def load_module(self, module_name, force_reload=False):
        """加载模块
        
        Args:
            module_name (str): 模块名称
            force_reload (bool): 是否强制重载
        
        Returns:
            module: 加载的模块对象
        """
        import importlib
        import sys
        
        try:
            # 如果模块已经加载且不强制重载，直接返回
            if module_name in self.loaded_modules and not force_reload:
                print(f"模块 '{module_name}' 已加载，返回缓存版本")
                return self.loaded_modules[module_name]
            
            # 加载或重载模块
            if force_reload and module_name in sys.modules:
                module = importlib.reload(sys.modules[module_name])
            else:
                module = importlib.import_module(module_name)
            
            # 缓存模块
            self.loaded_modules[module_name] = module
            
            # 分析依赖
            self.dependencies[module_name] = self._analyze_dependencies(module)
            
            print(f"✓ 成功加载模块: {module_name}")
            return module
            
        except Exception as e:
            print(f"❌ 加载模块失败 '{module_name}': {e}")
            raise
    
    def _analyze_dependencies(self, module):
        """分析模块依赖"""
        dependencies = set()
        
        # 检查模块的 __file__ 属性
        if hasattr(module, '__file__') and module.__file__:
            try:
                import ast
                with open(module.__file__, 'r', encoding='utf-8') as f:
                    source = f.read()
                
                tree = ast.parse(source)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            dependencies.add(alias.name.split('.')[0])
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            dependencies.add(node.module.split('.')[0])
            except:
                pass
        
        return list(dependencies)
    
    def unload_module(self, module_name):
        """卸载模块
        
        Args:
            module_name (str): 模块名称
        
        Returns:
            bool: 是否成功卸载
        """
        import sys
        
        try:
            # 从缓存中移除
            if module_name in self.loaded_modules:
                del self.loaded_modules[module_name]
            
            # 从依赖中移除
            if module_name in self.dependencies:
                del self.dependencies[module_name]
            
            # 从系统模块中移除
            if module_name in sys.modules:
                del sys.modules[module_name]
            
            print(f"✓ 成功卸载模块: {module_name}")
            return True
            
        except Exception as e:
            print(f"❌ 卸载模块失败 '{module_name}': {e}")
            return False
    
    def reload_module(self, module_name):
        """重载模块
        
        Args:
            module_name (str): 模块名称
        
        Returns:
            module: 重载的模块对象
        """
        try:
            # 使用 force_reload=True 来重载模块
            return self.load_module(module_name, force_reload=True)
        except Exception as e:
            print(f"❌ 重载模块失败 '{module_name}': {e}")
            raise
    
    def get_dependencies(self, module_name):
        """获取模块依赖
        
        Args:
            module_name (str): 模块名称
        
        Returns:
            list: 依赖模块列表
        """
        try:
            # 如果模块已加载，返回缓存的依赖
            if module_name in self.dependencies:
                return self.dependencies[module_name]
            
            # 如果模块未加载，先加载模块
            if module_name not in self.loaded_modules:
                self.load_module(module_name)
            
            return self.dependencies.get(module_name, [])
            
        except Exception as e:
            print(f"❌ 获取模块依赖失败 '{module_name}': {e}")
            return []
    
    def load_from_config(self):
        """从配置文件加载模块
        
        Returns:
            dict: 加载的模块字典
        """
        import json
        from pathlib import Path
        
        if not self.config_file:
            print("❌ 未指定配置文件")
            return {}
        
        try:
            config_path = Path(self.config_file)
            if not config_path.exists():
                # 创建默认配置文件
                default_config = {
                    "modules": [
                        "math",
                        "os",
                        "sys",
                        {"name": "json", "auto_load": True},
                        {"name": "datetime", "auto_load": False}
                    ]
                }
                with open(config_path, 'w', encoding='utf-8') as f:
                    json.dump(default_config, f, indent=2, ensure_ascii=False)
                print(f"✓ 创建默认配置文件: {config_path}")
            
            # 读取配置文件
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            loaded_modules = {}
            
            # 处理模块配置
            if 'modules' in config:
                for module_config in config['modules']:
                    if isinstance(module_config, str):
                        # 简单的模块名
                        module_name = module_config
                        auto_load = True
                    elif isinstance(module_config, dict):
                        # 详细配置
                        module_name = module_config.get('name')
                        auto_load = module_config.get('auto_load', True)
                    else:
                        continue
                    
                    if module_name and auto_load:
                        try:
                            loaded_module = self.load_module(module_name)
                            loaded_modules[module_name] = loaded_module
                        except Exception as e:
                            print(f"⚠️ 跳过模块 '{module_name}': {e}")
            
            print(f"✓ 从配置文件加载了 {len(loaded_modules)} 个模块")
            return loaded_modules
            
        except Exception as e:
            print(f"❌ 从配置文件加载失败: {e}")
            return {}

def test_module_loader():
    """测试模块加载器"""
    loader = ModuleLoader()
    
    # 测试加载
    try:
        math_module = loader.load_module('math')
        print(f"加载模块成功: {math_module}")
        
        # 测试重载
        reloaded_module = loader.reload_module('math')
        print(f"重载模块成功: {reloaded_module}")
        
        print("✓ 模块加载器测试通过")
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")

# 运行测试
# test_module_loader()

# ============================================================================
# 练习4: 高级特性应用
# ============================================================================

print("\n\n练习4: 高级特性应用")
print("-" * 30)

# 练习4.1: 模块代理和懒加载
print("\n练习4.1: 模块代理和懒加载")
print("""
要求:
1. 创建一个 LazyModule 类实现模块的懒加载
2. 只有在实际访问模块属性时才加载模块
3. 支持模块属性的缓存
4. 实现模块加载失败的优雅处理
5. 提供加载状态的查询接口
""")

class LazyModule:
    """懒加载模块代理"""
    
    def __init__(self, module_name):
        self._module_name = module_name
        self._module = None
        self._loaded = False
        self._loading = False
    
    def _load_module(self):
        """加载模块"""
        if self._loaded or self._loading:
            return
        
        self._loading = True
        try:
            import importlib
            print(f"懒加载模块: {self._module_name}")
            self._module = importlib.import_module(self._module_name)
            self._loaded = True
            print(f"✓ 成功加载模块: {self._module_name}")
        except Exception as e:
            print(f"❌ 懒加载失败 '{self._module_name}': {e}")
            raise
        finally:
            self._loading = False
    
    def __getattr__(self, name):
        """获取模块属性"""
        # 避免无限递归
        if name.startswith('_'):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        
        # 确保模块已加载
        if not self._loaded:
            self._load_module()
        
        # 从实际模块获取属性
        if self._module is None:
            raise AttributeError(f"模块 '{self._module_name}' 未成功加载")
        
        try:
            return getattr(self._module, name)
        except AttributeError:
            raise AttributeError(f"模块 '{self._module_name}' 没有属性 '{name}'")
    
    def __dir__(self):
        """获取模块属性列表"""
        # 确保模块已加载
        if not self._loaded:
            self._load_module()
        
        # 返回实际模块的属性列表
        if self._module is None:
            return []
        
        return dir(self._module)
    
    @property
    def is_loaded(self):
        """检查模块是否已加载"""
        return self._loaded
    
    @property
    def is_loading(self):
        """检查模块是否正在加载"""
        return self._loading

def test_lazy_module():
    """测试懒加载模块"""
    print("\n=== 测试懒加载模块 ===")
    
    try:
        # 创建懒加载模块代理
        lazy_math = LazyModule('math')
        print(f"✓ 创建懒加载代理: {lazy_math._module_name}")
        
        # 检查初始状态
        print(f"初始加载状态: {lazy_math.is_loaded}")
        print(f"初始加载中状态: {lazy_math.is_loading}")
        
        # 访问模块属性（触发懒加载）
        print("\n访问 math.pi...")
        pi_value = lazy_math.pi
        print(f"✓ math.pi = {pi_value}")
        
        # 检查加载后状态
        print(f"加载后状态: {lazy_math.is_loaded}")
        
        # 访问模块函数
        print("\n访问 math.sqrt...")
        sqrt_result = lazy_math.sqrt(16)
        print(f"✓ math.sqrt(16) = {sqrt_result}")
        
        # 测试 dir() 功能
        print("\n测试 dir() 功能...")
        math_attrs = dir(lazy_math)
        print(f"✓ math 模块有 {len(math_attrs)} 个属性")
        print(f"部分属性: {math_attrs[:5]}...")
        
        # 测试不存在的属性
        print("\n测试不存在的属性...")
        try:
            _ = lazy_math.nonexistent_attr
            print("❌ 应该抛出 AttributeError")
        except AttributeError as e:
            print(f"✓ 正确抛出异常: {e}")
        
        # 测试无效模块
        print("\n测试无效模块...")
        try:
            lazy_invalid = LazyModule('nonexistent_module_12345')
            _ = lazy_invalid.some_attr  # 触发加载
            print("❌ 应该抛出 ImportError")
        except (ImportError, ModuleNotFoundError) as e:
            print(f"✓ 正确处理无效模块: {type(e).__name__}")
        
        print("\n✅ 懒加载模块测试完成！")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

# 练习4.2: 模块装饰器和元编程
print("\n练习4.2: 模块装饰器和元编程")
print("""
要求:
1. 创建一个模块装饰器 @module_decorator
2. 支持在模块加载时自动注册函数
3. 支持模块级别的缓存装饰器
4. 实现模块的版本控制和兼容性检查
5. 创建模块的性能监控装饰器
""")

def module_decorator(func):
    """模块装饰器
    
    Args:
        func: 被装饰的函数
    
    Returns:
        function: 装饰后的函数
    """
    import functools
    import inspect
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 获取函数信息
        module_name = func.__module__
        func_name = func.__name__
        
        print(f"🔧 调用模块 {module_name} 中的函数 {func_name}")
        print(f"📝 参数: args={args}, kwargs={kwargs}")
        
        try:
            # 执行原函数
            result = func(*args, **kwargs)
            print(f"✅ 函数 {func_name} 执行成功")
            return result
        except Exception as e:
            print(f"❌ 函数 {func_name} 执行失败: {e}")
            raise
    
    # 添加装饰器信息
    wrapper._is_decorated = True
    wrapper._original_func = func
    wrapper._decorator_info = {
        'decorator': 'module_decorator',
        'applied_at': time.time(),
        'module': func.__module__
    }
    
    return wrapper

def cache_module_result(expire_time=3600):
    """模块结果缓存装饰器
    
    Args:
        expire_time (int): 缓存过期时间（秒）
    
    Returns:
        function: 装饰器函数
    """
    import functools
    import time
    import hashlib
    import pickle
    
    def decorator(func):
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 生成缓存键
            key_data = (args, tuple(sorted(kwargs.items())))
            key_str = pickle.dumps(key_data)
            cache_key = hashlib.md5(key_str).hexdigest()
            
            current_time = time.time()
            
            # 检查缓存
            if cache_key in cache:
                cached_result, cached_time = cache[cache_key]
                if current_time - cached_time < expire_time:
                    print(f"💾 从缓存返回结果 (键: {cache_key[:8]}...)")
                    return cached_result
                else:
                    print(f"⏰ 缓存已过期，重新计算 (键: {cache_key[:8]}...)")
                    del cache[cache_key]
            
            # 执行函数并缓存结果
            print(f"🔄 计算并缓存结果 (键: {cache_key[:8]}...)")
            result = func(*args, **kwargs)
            cache[cache_key] = (result, current_time)
            
            return result
        
        # 添加缓存管理方法
        wrapper.clear_cache = lambda: cache.clear()
        wrapper.cache_info = lambda: {
            'cache_size': len(cache),
            'expire_time': expire_time,
            'cached_keys': list(cache.keys())
        }
        
        return wrapper
    
    return decorator

def monitor_module_performance(func):
    """模块性能监控装饰器
    
    Args:
        func: 被装饰的函数
    
    Returns:
        function: 装饰后的函数
    """
    import functools
    import time
    import psutil
    import os
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 获取进程信息
        process = psutil.Process(os.getpid())
        
        # 记录开始状态
        start_time = time.time()
        start_memory = process.memory_info().rss / 1024 / 1024  # MB
        start_cpu_percent = process.cpu_percent()
        
        print(f"📊 开始监控函数 {func.__name__}")
        print(f"🕐 开始时间: {time.strftime('%H:%M:%S', time.localtime(start_time))}")
        print(f"💾 开始内存: {start_memory:.2f} MB")
        
        try:
            # 执行函数
            result = func(*args, **kwargs)
            
            # 记录结束状态
            end_time = time.time()
            end_memory = process.memory_info().rss / 1024 / 1024  # MB
            end_cpu_percent = process.cpu_percent()
            
            # 计算性能指标
            execution_time = end_time - start_time
            memory_usage = end_memory - start_memory
            
            print(f"✅ 函数 {func.__name__} 执行完成")
            print(f"⏱️  执行时间: {execution_time:.4f} 秒")
            print(f"💾 内存变化: {memory_usage:+.2f} MB")
            print(f"🔄 CPU使用率: {end_cpu_percent:.1f}%")
            
            # 性能警告
            if execution_time > 1.0:
                print(f"⚠️  警告: 函数执行时间较长 ({execution_time:.2f}s)")
            if memory_usage > 100:
                print(f"⚠️  警告: 内存使用量较大 ({memory_usage:.2f}MB)")
            
            return result
            
        except Exception as e:
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"❌ 函数 {func.__name__} 执行失败")
            print(f"⏱️  失败前执行时间: {execution_time:.4f} 秒")
            print(f"🐛 错误信息: {e}")
            raise
    
    # 添加性能统计信息
    wrapper._performance_stats = {
        'call_count': 0,
        'total_time': 0,
        'avg_time': 0,
        'max_time': 0,
        'min_time': float('inf')
    }
    
    return wrapper

def test_module_decorators():
    """测试模块装饰器"""
    print("\n🧪 测试模块装饰器功能")
    print("-" * 40)
    
    # 测试基础装饰器
    @module_decorator
    def sample_function(x, y):
        """示例函数"""
        time.sleep(0.1)  # 模拟一些处理时间
        return x + y
    
    print("\n1. 测试基础模块装饰器:")
    result = sample_function(3, 5)
    print(f"结果: {result}")
    print(f"装饰器信息: {getattr(sample_function, '_decorator_info', 'None')}")
    
    # 测试缓存装饰器
    @cache_module_result(expire_time=5)
    def expensive_calculation(n):
        """耗时计算函数"""
        print(f"正在计算 {n} 的平方...")
        time.sleep(0.2)  # 模拟耗时操作
        return n ** 2
    
    print("\n2. 测试缓存装饰器:")
    print("第一次调用:")
    result1 = expensive_calculation(10)
    print(f"结果: {result1}")
    
    print("\n第二次调用 (应该从缓存返回):")
    result2 = expensive_calculation(10)
    print(f"结果: {result2}")
    
    print(f"\n缓存信息: {expensive_calculation.cache_info()}")
    
    # 测试性能监控装饰器（如果psutil可用）
    try:
        import psutil
        
        @monitor_module_performance
        def cpu_intensive_task(iterations=1000000):
            """CPU密集型任务"""
            total = 0
            for i in range(iterations):
                total += i * i
            return total
        
        print("\n3. 测试性能监控装饰器:")
        result3 = cpu_intensive_task(500000)
        print(f"计算结果: {result3}")
        
    except ImportError:
        print("\n3. 性能监控装饰器测试跳过 (需要 psutil 库)")
    
    # 测试组合装饰器
    @module_decorator
    @cache_module_result(expire_time=10)
    def combined_function(a, b, c=1):
        """组合装饰器测试函数"""
        time.sleep(0.1)
        return a * b + c
    
    print("\n4. 测试组合装饰器:")
    result4 = combined_function(2, 3, c=5)
    print(f"结果: {result4}")
    
    print("\n再次调用 (应该从缓存返回):")
    result5 = combined_function(2, 3, c=5)
    print(f"结果: {result5}")
    
    print("\n✅ 模块装饰器测试完成!")

# ============================================================================
# 练习5: 包管理和虚拟环境
# ============================================================================

print("\n\n练习5: 包管理和虚拟环境")
print("-" * 30)

# 练习5.1: 依赖管理工具
print("\n练习5.1: 依赖管理工具")
print("""
要求:
1. 创建一个 DependencyManager 类
2. 解析 requirements.txt 文件
3. 检查已安装包的版本
4. 检测版本冲突
5. 生成依赖关系图
6. 支持依赖的自动安装和卸载
""")

class DependencyManager:
    """依赖管理器"""
    
    def __init__(self, requirements_file='requirements.txt'):
        self.requirements_file = requirements_file
        self.dependencies = {}
        self.installed_packages = {}
    
    def parse_requirements(self):
        """解析 requirements.txt 文件
        
        Returns:
            dict: 依赖包信息
        """
        # TODO: 实现 requirements.txt 解析
        pass
    
    def check_installed_packages(self):
        """检查已安装的包
        
        Returns:
            dict: 已安装包信息
        """
        # TODO: 实现已安装包检查
        pass
    
    def detect_conflicts(self):
        """检测版本冲突
        
        Returns:
            list: 冲突列表
        """
        # TODO: 实现冲突检测
        pass
    
    def generate_dependency_graph(self):
        """生成依赖关系图
        
        Returns:
            dict: 依赖关系图
        """
        # TODO: 实现依赖图生成
        pass
    
    def install_dependencies(self, dry_run=False):
        """安装依赖
        
        Args:
            dry_run (bool): 是否为试运行
        
        Returns:
            bool: 是否成功
        """
        # TODO: 实现依赖安装
        pass
    
    def uninstall_dependencies(self, packages, dry_run=False):
        """卸载依赖
        
        Args:
            packages (list): 要卸载的包列表
            dry_run (bool): 是否为试运行
        
        Returns:
            bool: 是否成功
        """
        # TODO: 实现依赖卸载
        pass

def test_dependency_manager():
    """测试依赖管理器"""
    # TODO: 实现测试逻辑
    pass

# 练习5.2: 虚拟环境管理器
print("\n练习5.2: 虚拟环境管理器")
print("""
要求:
1. 创建一个 VirtualEnvManager 类
2. 支持创建、删除、激活虚拟环境
3. 管理多个虚拟环境
4. 支持环境的导出和导入
5. 提供环境信息查询功能
""")

class VirtualEnvManager:
    """虚拟环境管理器"""
    
    def __init__(self, base_dir='venvs'):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)
        self.current_env = None
    
    def create_env(self, env_name, python_version=None):
        """创建虚拟环境
        
        Args:
            env_name (str): 环境名称
            python_version (str): Python版本
        
        Returns:
            bool: 是否成功创建
        """
        # TODO: 实现虚拟环境创建
        pass
    
    def delete_env(self, env_name):
        """删除虚拟环境
        
        Args:
            env_name (str): 环境名称
        
        Returns:
            bool: 是否成功删除
        """
        # TODO: 实现虚拟环境删除
        pass
    
    def activate_env(self, env_name):
        """激活虚拟环境
        
        Args:
            env_name (str): 环境名称
        
        Returns:
            bool: 是否成功激活
        """
        # TODO: 实现虚拟环境激活
        pass
    
    def deactivate_env(self):
        """停用当前虚拟环境
        
        Returns:
            bool: 是否成功停用
        """
        # TODO: 实现虚拟环境停用
        pass
    
    def list_envs(self):
        """列出所有虚拟环境
        
        Returns:
            list: 环境列表
        """
        # TODO: 实现环境列表获取
        pass
    
    def export_env(self, env_name, output_file):
        """导出虚拟环境
        
        Args:
            env_name (str): 环境名称
            output_file (str): 输出文件
        
        Returns:
            bool: 是否成功导出
        """
        # TODO: 实现环境导出
        pass
    
    def import_env(self, env_name, import_file):
        """导入虚拟环境
        
        Args:
            env_name (str): 环境名称
            import_file (str): 导入文件
        
        Returns:
            bool: 是否成功导入
        """
        # TODO: 实现环境导入
        pass

def test_virtual_env_manager():
    """测试虚拟环境管理器"""
    # TODO: 实现测试逻辑
    pass

# ============================================================================
# 练习6: 实际项目应用
# ============================================================================

print("\n\n练习6: 实际项目应用")
print("-" * 30)

# 练习6.1: 微服务模块系统
print("\n练习6.1: 微服务模块系统")
print("""
要求:
1. 设计一个微服务架构的模块系统
2. 每个服务作为独立的包
3. 实现服务间的通信接口
4. 支持服务的动态发现和注册
5. 实现服务的健康检查和监控
6. 支持服务的版本管理和升级
""")

class MicroserviceRegistry:
    """微服务注册中心"""
    
    def __init__(self):
        self.services = {}
        self.health_checks = {}
    
    def register_service(self, service_name, service_instance):
        """注册服务
        
        Args:
            service_name (str): 服务名称
            service_instance: 服务实例
        
        Returns:
            bool: 是否成功注册
        """
        # TODO: 实现服务注册
        pass
    
    def unregister_service(self, service_name):
        """注销服务
        
        Args:
            service_name (str): 服务名称
        
        Returns:
            bool: 是否成功注销
        """
        # TODO: 实现服务注销
        pass
    
    def discover_service(self, service_name):
        """发现服务
        
        Args:
            service_name (str): 服务名称
        
        Returns:
            object: 服务实例
        """
        # TODO: 实现服务发现
        pass
    
    def health_check(self, service_name):
        """健康检查
        
        Args:
            service_name (str): 服务名称
        
        Returns:
            bool: 服务是否健康
        """
        # TODO: 实现健康检查
        pass

class BaseService:
    """基础服务类"""
    
    def __init__(self, name, version='1.0.0'):
        self.name = name
        self.version = version
        self.status = 'stopped'
    
    def start(self):
        """启动服务"""
        # TODO: 实现服务启动
        pass
    
    def stop(self):
        """停止服务"""
        # TODO: 实现服务停止
        pass
    
    def health_check(self):
        """健康检查"""
        # TODO: 实现健康检查
        pass
    
    def get_info(self):
        """获取服务信息"""
        # TODO: 实现服务信息获取
        pass

def test_microservice_system():
    """测试微服务系统"""
    # TODO: 实现测试逻辑
    pass

# 练习6.2: 配置驱动的应用框架
print("\n练习6.2: 配置驱动的应用框架")
print("""
要求:
1. 创建一个配置驱动的应用框架
2. 支持从配置文件动态加载模块
3. 支持模块的依赖注入
4. 实现模块的生命周期管理
5. 支持配置的热重载
6. 提供模块的监控和日志功能
""")

class ApplicationFramework:
    """应用框架"""
    
    def __init__(self, config_file='app_config.json'):
        self.config_file = config_file
        self.config = {}
        self.modules = {}
        self.dependencies = {}
        self.lifecycle_hooks = {}
    
    def load_config(self):
        """加载配置
        
        Returns:
            bool: 是否成功加载
        """
        # TODO: 实现配置加载
        pass
    
    def reload_config(self):
        """重新加载配置
        
        Returns:
            bool: 是否成功重载
        """
        # TODO: 实现配置重载
        pass
    
    def load_modules(self):
        """加载模块
        
        Returns:
            bool: 是否成功加载
        """
        # TODO: 实现模块加载
        pass
    
    def inject_dependencies(self):
        """注入依赖
        
        Returns:
            bool: 是否成功注入
        """
        # TODO: 实现依赖注入
        pass
    
    def start_application(self):
        """启动应用
        
        Returns:
            bool: 是否成功启动
        """
        # TODO: 实现应用启动
        pass
    
    def stop_application(self):
        """停止应用
        
        Returns:
            bool: 是否成功停止
        """
        # TODO: 实现应用停止
        pass
    
    def register_lifecycle_hook(self, event, callback):
        """注册生命周期钩子
        
        Args:
            event (str): 事件名称
            callback (function): 回调函数
        """
        # TODO: 实现生命周期钩子注册
        pass

def test_application_framework():
    """测试应用框架"""
    # TODO: 实现测试逻辑
    pass

# ============================================================================
# 练习7: 综合应用 - 插件化的数据处理系统
# ============================================================================

print("\n\n练习7: 综合应用 - 插件化的数据处理系统")
print("-" * 30)

print("""
综合练习要求:
1. 设计并实现一个插件化的数据处理系统
2. 系统应该包含以下组件:
   - 数据源插件（文件、数据库、API等）
   - 数据处理插件（清洗、转换、聚合等）
   - 数据输出插件（文件、数据库、可视化等）
   - 插件管理器
   - 配置管理器
   - 任务调度器

3. 技术要求:
   - 使用包和模块组织代码
   - 实现插件的动态加载和卸载
   - 支持插件的依赖管理
   - 实现数据处理管道
   - 支持并行处理
   - 提供监控和日志功能
   - 支持配置的热重载

4. 包结构设计:
   data_processor/
   ├── __init__.py
   ├── core/
   │   ├── __init__.py
   │   ├── plugin_manager.py
   │   ├── config_manager.py
   │   ├── task_scheduler.py
   │   └── pipeline.py
   ├── plugins/
   │   ├── __init__.py
   │   ├── base.py
   │   ├── sources/
   │   │   ├── __init__.py
   │   │   ├── file_source.py
   │   │   ├── db_source.py
   │   │   └── api_source.py
   │   ├── processors/
   │   │   ├── __init__.py
   │   │   ├── cleaner.py
   │   │   ├── transformer.py
   │   │   └── aggregator.py
   │   └── outputs/
   │       ├── __init__.py
   │       ├── file_output.py
   │       ├── db_output.py
   │       └── chart_output.py
   ├── utils/
   │   ├── __init__.py
   │   ├── logger.py
   │   ├── monitor.py
   │   └── helpers.py
   └── tests/
       ├── __init__.py
       ├── test_core.py
       ├── test_plugins.py
       └── test_integration.py
""")

# 基础插件接口
class BasePlugin:
    """基础插件类"""
    
    def __init__(self, name, version='1.0.0'):
        self.name = name
        self.version = version
        self.dependencies = []
        self.config = {}
    
    def initialize(self, config):
        """初始化插件
        
        Args:
            config (dict): 插件配置
        
        Returns:
            bool: 是否成功初始化
        """
        try:
            print(f"🔧 初始化插件: {self.name} v{self.version}")
            
            # 更新配置
            if config:
                self.config.update(config)
                print(f"📝 应用配置: {self.config}")
            
            # 检查依赖
            if self.dependencies:
                print(f"🔍 检查依赖: {self.dependencies}")
                for dep in self.dependencies:
                    try:
                        __import__(dep)
                        print(f"✅ 依赖 {dep} 可用")
                    except ImportError:
                        print(f"❌ 依赖 {dep} 不可用")
                        return False
            
            # 执行自定义初始化逻辑
            self._custom_initialize()
            
            print(f"✅ 插件 {self.name} 初始化成功")
            return True
            
        except Exception as e:
            print(f"❌ 插件 {self.name} 初始化失败: {e}")
            return False
    
    def _custom_initialize(self):
        """自定义初始化逻辑（子类可重写）"""
        pass
    
    def execute(self, data, **kwargs):
        """执行插件功能
        
        Args:
            data: 输入数据
            **kwargs: 其他参数
        
        Returns:
            any: 处理结果
        """
        try:
            print(f"⚡ 执行插件: {self.name}")
            print(f"📥 输入数据类型: {type(data).__name__}")
            
            # 数据预处理
            processed_data = self._preprocess_data(data, **kwargs)
            
            # 执行核心逻辑
            result = self._execute_core(processed_data, **kwargs)
            
            # 数据后处理
            final_result = self._postprocess_data(result, **kwargs)
            
            print(f"📤 输出数据类型: {type(final_result).__name__}")
            print(f"✅ 插件 {self.name} 执行完成")
            
            return final_result
            
        except Exception as e:
            print(f"❌ 插件 {self.name} 执行失败: {e}")
            raise
    
    def _preprocess_data(self, data, **kwargs):
        """数据预处理（子类可重写）"""
        return data
    
    def _execute_core(self, data, **kwargs):
        """核心执行逻辑（子类必须重写）"""
        # 默认实现：直接返回数据
        print(f"🔄 使用默认处理逻辑")
        return data
    
    def _postprocess_data(self, data, **kwargs):
        """数据后处理（子类可重写）"""
        return data
    
    def cleanup(self):
        """清理插件资源
        
        Returns:
            bool: 是否成功清理
        """
        try:
            print(f"🧹 清理插件: {self.name}")
            
            # 执行自定义清理逻辑
            self._custom_cleanup()
            
            # 清理配置
            self.config.clear()
            
            print(f"✅ 插件 {self.name} 清理完成")
            return True
            
        except Exception as e:
            print(f"❌ 插件 {self.name} 清理失败: {e}")
            return False
    
    def _custom_cleanup(self):
        """自定义清理逻辑（子类可重写）"""
        pass
    
    def get_info(self):
        """获取插件信息
        
        Returns:
            dict: 插件信息
        """
        return {
            'name': self.name,
            'version': self.version,
            'dependencies': self.dependencies,
            'config': self.config
        }

class DataProcessingPipeline:
    """数据处理管道"""
    
    def __init__(self):
        self.stages = []
        self.plugins = {}
        self.config = {}
    
    def add_stage(self, plugin_name, config=None):
        """添加处理阶段
        
        Args:
            plugin_name (str): 插件名称
            config (dict): 阶段配置
        
        Returns:
            bool: 是否成功添加
        """
        try:
            print(f"➕ 添加处理阶段: {plugin_name}")
            
            # 创建阶段配置
            stage_config = {
                'plugin_name': plugin_name,
                'config': config or {},
                'stage_id': len(self.stages),
                'enabled': True
            }
            
            # 添加到管道
            self.stages.append(stage_config)
            
            # 如果插件不存在，创建默认插件实例
            if plugin_name not in self.plugins:
                plugin_instance = BasePlugin(plugin_name)
                plugin_instance.initialize(config)
                self.plugins[plugin_name] = plugin_instance
            
            print(f"✅ 阶段 {plugin_name} 添加成功 (位置: {stage_config['stage_id']})")
            return True
            
        except Exception as e:
            print(f"❌ 添加阶段 {plugin_name} 失败: {e}")
            return False
    
    def remove_stage(self, stage_index):
        """移除处理阶段
        
        Args:
            stage_index (int): 阶段索引
        
        Returns:
            bool: 是否成功移除
        """
        try:
            if not (0 <= stage_index < len(self.stages)):
                print(f"❌ 无效的阶段索引: {stage_index}")
                return False
            
            # 获取要移除的阶段
            stage_to_remove = self.stages[stage_index]
            plugin_name = stage_to_remove['plugin_name']
            
            print(f"➖ 移除处理阶段: {plugin_name} (索引: {stage_index})")
            
            # 从管道中移除
            removed_stage = self.stages.pop(stage_index)
            
            # 重新编号后续阶段
            for i, stage in enumerate(self.stages[stage_index:], stage_index):
                stage['stage_id'] = i
            
            # 检查是否还有其他阶段使用该插件
            plugin_still_used = any(stage['plugin_name'] == plugin_name for stage in self.stages)
            
            # 如果插件不再被使用，清理插件实例
            if not plugin_still_used and plugin_name in self.plugins:
                self.plugins[plugin_name].cleanup()
                del self.plugins[plugin_name]
                print(f"🧹 清理未使用的插件: {plugin_name}")
            
            print(f"✅ 阶段移除成功")
            return True
            
        except Exception as e:
            print(f"❌ 移除阶段失败: {e}")
            return False
    
    def execute(self, input_data):
        """执行管道
        
        Args:
            input_data: 输入数据
        
        Returns:
            any: 处理结果
        """
        try:
            print(f"🚀 开始执行数据处理管道")
            print(f"📥 输入数据: {type(input_data).__name__}")
            print(f"🔗 管道阶段数: {len(self.stages)}")
            
            if not self.stages:
                print(f"⚠️  管道为空，直接返回输入数据")
                return input_data
            
            current_data = input_data
            
            # 逐个执行管道阶段
            for i, stage in enumerate(self.stages):
                if not stage.get('enabled', True):
                    print(f"⏭️  跳过禁用的阶段 {i}: {stage['plugin_name']}")
                    continue
                
                plugin_name = stage['plugin_name']
                stage_config = stage['config']
                
                print(f"\n🔄 执行阶段 {i}: {plugin_name}")
                
                # 获取插件实例
                if plugin_name not in self.plugins:
                    print(f"❌ 插件 {plugin_name} 不存在")
                    raise ValueError(f"Plugin {plugin_name} not found")
                
                plugin = self.plugins[plugin_name]
                
                # 执行插件
                try:
                    current_data = plugin.execute(current_data, **stage_config)
                    print(f"✅ 阶段 {i} 执行成功")
                except Exception as e:
                    print(f"❌ 阶段 {i} 执行失败: {e}")
                    raise
            
            print(f"\n🎉 管道执行完成")
            print(f"📤 输出数据: {type(current_data).__name__}")
            return current_data
            
        except Exception as e:
            print(f"❌ 管道执行失败: {e}")
            raise
    
    def execute_parallel(self, input_data, max_workers=4):
        """并行执行管道
        
        Args:
            input_data: 输入数据
            max_workers (int): 最大工作线程数
        
        Returns:
            any: 处理结果
        """
        import concurrent.futures
        import copy
        
        try:
            print(f"🚀 开始并行执行数据处理管道")
            print(f"📥 输入数据: {type(input_data).__name__}")
            print(f"🔗 管道阶段数: {len(self.stages)}")
            print(f"👥 最大工作线程数: {max_workers}")
            
            if not self.stages:
                print(f"⚠️  管道为空，直接返回输入数据")
                return input_data
            
            # 检查是否可以并行执行（简单实现：假设所有阶段都可以并行）
            # 在实际应用中，需要分析阶段间的依赖关系
            
            # 如果只有一个阶段或数据不可分割，使用串行执行
            if len(self.stages) <= 1 or not hasattr(input_data, '__iter__') or isinstance(input_data, (str, dict)):
                print(f"📝 数据不适合并行处理，使用串行执行")
                return self.execute(input_data)
            
            # 尝试将输入数据分块进行并行处理
            if isinstance(input_data, (list, tuple)):
                # 将数据分块
                chunk_size = max(1, len(input_data) // max_workers)
                data_chunks = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]
                
                print(f"📦 将数据分为 {len(data_chunks)} 个块进行并行处理")
                
                def process_chunk(chunk):
                    """处理数据块"""
                    # 为每个线程创建独立的管道副本
                    pipeline_copy = copy.deepcopy(self)
                    return pipeline_copy.execute(chunk)
                
                # 使用线程池并行处理
                with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                    print(f"🔄 提交 {len(data_chunks)} 个处理任务")
                    
                    # 提交所有任务
                    future_to_chunk = {executor.submit(process_chunk, chunk): i 
                                     for i, chunk in enumerate(data_chunks)}
                    
                    results = []
                    
                    # 收集结果
                    for future in concurrent.futures.as_completed(future_to_chunk):
                        chunk_index = future_to_chunk[future]
                        try:
                            result = future.result()
                            results.append((chunk_index, result))
                            print(f"✅ 块 {chunk_index} 处理完成")
                        except Exception as e:
                            print(f"❌ 块 {chunk_index} 处理失败: {e}")
                            raise
                    
                    # 按原始顺序合并结果
                    results.sort(key=lambda x: x[0])
                    final_result = []
                    for _, result in results:
                        if isinstance(result, (list, tuple)):
                            final_result.extend(result)
                        else:
                            final_result.append(result)
                    
                    print(f"\n🎉 并行管道执行完成")
                    print(f"📤 输出数据: {type(final_result).__name__} (长度: {len(final_result)})")
                    return final_result
            
            else:
                # 对于其他类型的数据，使用串行执行
                print(f"📝 数据类型不支持并行处理，使用串行执行")
                return self.execute(input_data)
                
        except Exception as e:
            print(f"❌ 并行管道执行失败: {e}")
            raise

def create_data_processor_package():
    """创建数据处理系统包"""
    print("\n🏗️  创建数据处理系统包")
    print("-" * 40)
    
    try:
        # 创建主包目录
        package_dir = Path('data_processor')
        package_dir.mkdir(exist_ok=True)
        
        # 创建子目录
        (package_dir / 'core').mkdir(exist_ok=True)
        (package_dir / 'plugins').mkdir(exist_ok=True)
        (package_dir / 'utils').mkdir(exist_ok=True)
        (package_dir / 'config').mkdir(exist_ok=True)
        (package_dir / 'tests').mkdir(exist_ok=True)
        
        print(f"📁 创建目录结构完成")
        
        # 创建主包 __init__.py
        main_init = package_dir / '__init__.py'
        main_init.write_text('''
"""数据处理系统包

一个可扩展的插件化数据处理框架。
"""

__version__ = '1.0.0'
__author__ = 'Data Processing Team'

from .core.pipeline import DataProcessingPipeline
from .core.plugin import BasePlugin
from .utils.config import ConfigManager

__all__ = ['DataProcessingPipeline', 'BasePlugin', 'ConfigManager']
''')
        
        # 创建核心模块
        core_init = package_dir / 'core' / '__init__.py'
        core_init.write_text('"""核心模块"""\n')
        
        # 创建插件基类文件
        plugin_file = package_dir / 'core' / 'plugin.py'
        plugin_file.write_text('''
"""插件基类模块"""

class BasePlugin:
    """数据处理插件基类"""
    
    def __init__(self, name, version='1.0.0'):
        self.name = name
        self.version = version
        self.dependencies = []
        self.config = {}
    
    def initialize(self, config):
        """初始化插件"""
        self.config.update(config or {})
        return True
    
    def execute(self, data, **kwargs):
        """执行插件功能"""
        return data
    
    def cleanup(self):
        """清理插件资源"""
        self.config.clear()
        return True
    
    def get_info(self):
        """获取插件信息"""
        return {
            'name': self.name,
            'version': self.version,
            'dependencies': self.dependencies,
            'config': self.config
        }
''')
        
        # 创建管道文件
        pipeline_file = package_dir / 'core' / 'pipeline.py'
        pipeline_file.write_text('''
"""数据处理管道模块"""

from .plugin import BasePlugin

class DataProcessingPipeline:
    """数据处理管道"""
    
    def __init__(self):
        self.stages = []
        self.plugins = {}
        self.config = {}
    
    def add_stage(self, plugin_name, config=None):
        """添加处理阶段"""
        stage_config = {
            'plugin_name': plugin_name,
            'config': config or {},
            'stage_id': len(self.stages),
            'enabled': True
        }
        self.stages.append(stage_config)
        
        if plugin_name not in self.plugins:
            plugin_instance = BasePlugin(plugin_name)
            plugin_instance.initialize(config)
            self.plugins[plugin_name] = plugin_instance
        
        return True
    
    def execute(self, input_data):
        """执行管道"""
        current_data = input_data
        
        for stage in self.stages:
            if not stage.get('enabled', True):
                continue
            
            plugin_name = stage['plugin_name']
            plugin = self.plugins[plugin_name]
            current_data = plugin.execute(current_data, **stage['config'])
        
        return current_data
''')
        
        # 创建示例插件
        plugins_init = package_dir / 'plugins' / '__init__.py'
        plugins_init.write_text('"""插件模块"""\n')
        
        # 文本处理插件
        text_plugin = package_dir / 'plugins' / 'text_processor.py'
        text_plugin.write_text('''
"""文本处理插件"""

from ..core.plugin import BasePlugin

class TextCleanerPlugin(BasePlugin):
    """文本清理插件"""
    
    def __init__(self):
        super().__init__('text_cleaner', '1.0.0')
    
    def execute(self, data, **kwargs):
        """清理文本数据"""
        if isinstance(data, str):
            # 移除多余空格，转换为小写
            return data.strip().lower()
        elif isinstance(data, list):
            return [item.strip().lower() if isinstance(item, str) else item for item in data]
        return data

class TextSplitterPlugin(BasePlugin):
    """文本分割插件"""
    
    def __init__(self):
        super().__init__('text_splitter', '1.0.0')
    
    def execute(self, data, **kwargs):
        """分割文本"""
        delimiter = kwargs.get('delimiter', ' ')
        if isinstance(data, str):
            return data.split(delimiter)
        return data
''')
        
        # 数据处理插件
        data_plugin = package_dir / 'plugins' / 'data_processor.py'
        data_plugin.write_text('''
"""数据处理插件"""

from ..core.plugin import BasePlugin

class FilterPlugin(BasePlugin):
    """数据过滤插件"""
    
    def __init__(self):
        super().__init__('filter', '1.0.0')
    
    def execute(self, data, **kwargs):
        """过滤数据"""
        filter_func = kwargs.get('filter_func')
        if filter_func and isinstance(data, list):
            return [item for item in data if filter_func(item)]
        return data

class TransformPlugin(BasePlugin):
    """数据转换插件"""
    
    def __init__(self):
        super().__init__('transform', '1.0.0')
    
    def execute(self, data, **kwargs):
        """转换数据"""
        transform_func = kwargs.get('transform_func')
        if transform_func:
            if isinstance(data, list):
                return [transform_func(item) for item in data]
            else:
                return transform_func(data)
        return data
''')
        
        # 创建配置管理器
        utils_init = package_dir / 'utils' / '__init__.py'
        utils_init.write_text('"""工具模块"""\n')
        
        config_file = package_dir / 'utils' / 'config.py'
        config_file.write_text('''
"""配置管理模块"""

import json
from pathlib import Path

class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_file='config.json'):
        self.config_file = Path(config_file)
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """加载配置"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = self.get_default_config()
            self.save_config()
    
    def save_config(self):
        """保存配置"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
    
    def get_default_config(self):
        """获取默认配置"""
        return {
            'pipeline': {
                'max_workers': 4,
                'timeout': 300
            },
            'plugins': {
                'auto_load': True,
                'plugin_dirs': ['plugins']
            },
            'logging': {
                'level': 'INFO',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        }
    
    def get(self, key, default=None):
        """获取配置值"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value != {} else default
    
    def set(self, key, value):
        """设置配置值"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            config = config.setdefault(k, {})
        config[keys[-1]] = value
        self.save_config()
''')
        
        # 创建示例配置文件
        config_dir = package_dir / 'config'
        config_init = config_dir / '__init__.py'
        config_init.write_text('"""配置文件"""\n')
        
        example_config = config_dir / 'example_config.json'
        example_config.write_text('''
{
  "pipeline": {
    "max_workers": 4,
    "timeout": 300
  },
  "plugins": {
    "auto_load": true,
    "plugin_dirs": ["plugins"]
  },
  "stages": [
    {
      "plugin": "text_cleaner",
      "config": {}
    },
    {
      "plugin": "text_splitter",
      "config": {
        "delimiter": " "
      }
    }
  ]
}
''')
        
        # 创建测试文件
        tests_init = package_dir / 'tests' / '__init__.py'
        tests_init.write_text('"""测试模块"""\n')
        
        test_core = package_dir / 'tests' / 'test_core.py'
        test_core.write_text('''
"""核心功能测试"""

def test_base_plugin():
    """测试基础插件"""
    from data_processor.core.plugin import BasePlugin
    
    plugin = BasePlugin('test_plugin')
    assert plugin.name == 'test_plugin'
    assert plugin.initialize({}) == True
    assert plugin.execute('test_data') == 'test_data'
    assert plugin.cleanup() == True

def test_pipeline():
    """测试数据管道"""
    from data_processor.core.pipeline import DataProcessingPipeline
    
    pipeline = DataProcessingPipeline()
    assert pipeline.add_stage('test_stage') == True
    assert len(pipeline.stages) == 1
    
    result = pipeline.execute('test_data')
    assert result == 'test_data'

if __name__ == '__main__':
    test_base_plugin()
    test_pipeline()
    print("✅ 所有核心测试通过")
''')
        
        # 创建 README 文件
        readme_file = package_dir / 'README.md'
        readme_file.write_text('''
# 数据处理系统

一个可扩展的插件化数据处理框架。

## 特性

- 🔌 插件化架构
- 🚀 管道式数据处理
- ⚡ 并行处理支持
- 🛠️ 灵活的配置管理
- 🧪 完整的测试覆盖

## 快速开始

```python
from data_processor import DataProcessingPipeline, BasePlugin

# 创建管道
pipeline = DataProcessingPipeline()

# 添加处理阶段
pipeline.add_stage('text_cleaner')
pipeline.add_stage('text_splitter', {'delimiter': ' '})

# 执行处理
result = pipeline.execute("Hello World")
print(result)  # ['hello', 'world']
```

## 目录结构

```
data_processor/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── plugin.py
│   └── pipeline.py
├── plugins/
│   ├── __init__.py
│   ├── text_processor.py
│   └── data_processor.py
├── utils/
│   ├── __init__.py
│   └── config.py
├── config/
│   ├── __init__.py
│   └── example_config.json
├── tests/
│   ├── __init__.py
│   └── test_core.py
└── README.md
```

## 插件开发

继承 `BasePlugin` 类来创建自定义插件：

```python
from data_processor.core.plugin import BasePlugin

class MyPlugin(BasePlugin):
    def __init__(self):
        super().__init__('my_plugin', '1.0.0')
    
    def execute(self, data, **kwargs):
        # 实现你的处理逻辑
        return processed_data
```
''')
        
        print(f"✅ 数据处理系统包创建完成")
        print(f"📁 包位置: {package_dir.absolute()}")
        print(f"📝 包含 {len(list(package_dir.rglob('*.py')))} 个 Python 文件")
        
        return True
        
    except Exception as e:
        print(f"❌ 创建数据处理系统包失败: {e}")
        return False

def test_data_processor_system():
    """测试数据处理系统"""
    print("\n🧪 测试数据处理系统")
    print("=" * 50)
    
    try:
        # 1. 创建数据处理包
        print("\n1️⃣ 创建数据处理包...")
        if not create_data_processor_package():
            print("❌ 包创建失败")
            return False
        
        # 2. 测试基础插件功能
        print("\n2️⃣ 测试基础插件功能...")
        from data_processor.core.plugin import BasePlugin
        
        # 创建测试插件
        plugin = BasePlugin('test_plugin', '1.0.0')
        assert plugin.name == 'test_plugin'
        assert plugin.version == '1.0.0'
        
        # 测试初始化
        config = {'param1': 'value1', 'param2': 42}
        assert plugin.initialize(config) == True
        assert plugin.config == config
        
        # 测试执行
        test_data = "Hello World"
        result = plugin.execute(test_data)
        assert result == test_data
        
        # 测试信息获取
        info = plugin.get_info()
        assert info['name'] == 'test_plugin'
        assert info['version'] == '1.0.0'
        
        # 测试清理
        assert plugin.cleanup() == True
        assert plugin.config == {}
        
        print("✅ 基础插件测试通过")
        
        # 3. 测试数据处理管道
        print("\n3️⃣ 测试数据处理管道...")
        from data_processor.core.pipeline import DataProcessingPipeline
        
        pipeline = DataProcessingPipeline()
        assert len(pipeline.stages) == 0
        assert len(pipeline.plugins) == 0
        
        # 添加处理阶段
        assert pipeline.add_stage('stage1', {'param': 'value'}) == True
        assert len(pipeline.stages) == 1
        assert len(pipeline.plugins) == 1
        
        # 添加更多阶段
        pipeline.add_stage('stage2')
        pipeline.add_stage('stage3', {'enabled': True})
        assert len(pipeline.stages) == 3
        
        # 测试管道执行
        test_input = "pipeline test data"
        result = pipeline.execute(test_input)
        assert result == test_input  # 基础插件只是返回原数据
        
        print("✅ 数据处理管道测试通过")
        
        # 4. 测试文本处理插件
        print("\n4️⃣ 测试文本处理插件...")
        from data_processor.plugins.text_processor import TextCleanerPlugin, TextSplitterPlugin
        
        # 测试文本清理插件
        cleaner = TextCleanerPlugin()
        assert cleaner.name == 'text_cleaner'
        
        # 测试字符串清理
        dirty_text = "  HELLO WORLD  "
        clean_text = cleaner.execute(dirty_text)
        assert clean_text == "hello world"
        
        # 测试列表清理
        dirty_list = ["  HELLO  ", "  WORLD  ", 123]
        clean_list = cleaner.execute(dirty_list)
        assert clean_list == ["hello", "world", 123]
        
        # 测试文本分割插件
        splitter = TextSplitterPlugin()
        assert splitter.name == 'text_splitter'
        
        # 测试默认分割
        text = "hello world python"
        words = splitter.execute(text)
        assert words == ["hello", "world", "python"]
        
        # 测试自定义分割符
        csv_text = "apple,banana,orange"
        fruits = splitter.execute(csv_text, delimiter=',')
        assert fruits == ["apple", "banana", "orange"]
        
        print("✅ 文本处理插件测试通过")
        
        # 5. 测试数据处理插件
        print("\n5️⃣ 测试数据处理插件...")
        from data_processor.plugins.data_processor import FilterPlugin, TransformPlugin
        
        # 测试过滤插件
        filter_plugin = FilterPlugin()
        assert filter_plugin.name == 'filter'
        
        # 过滤偶数
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        odd_numbers = filter_plugin.execute(numbers, filter_func=lambda x: x % 2 == 1)
        assert odd_numbers == [1, 3, 5, 7, 9]
        
        # 测试转换插件
        transform_plugin = TransformPlugin()
        assert transform_plugin.name == 'transform'
        
        # 转换为平方
        numbers = [1, 2, 3, 4, 5]
        squares = transform_plugin.execute(numbers, transform_func=lambda x: x ** 2)
        assert squares == [1, 4, 9, 16, 25]
        
        # 转换单个值
        single_value = transform_plugin.execute(10, transform_func=lambda x: x * 2)
        assert single_value == 20
        
        print("✅ 数据处理插件测试通过")
        
        # 6. 测试配置管理器
        print("\n6️⃣ 测试配置管理器...")
        from data_processor.utils.config import ConfigManager
        
        # 创建临时配置文件
        import tempfile
        import os
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_config_file = f.name
            f.write('{"test": {"value": 42}}')
        
        try:
            config_manager = ConfigManager(temp_config_file)
            
            # 测试配置读取
            assert config_manager.get('test.value') == 42
            assert config_manager.get('nonexistent', 'default') == 'default'
            
            # 测试配置设置
            config_manager.set('new.setting', 'test_value')
            assert config_manager.get('new.setting') == 'test_value'
            
            # 测试默认配置
            default_config = config_manager.get_default_config()
            assert 'pipeline' in default_config
            assert 'plugins' in default_config
            assert 'logging' in default_config
            
        finally:
            # 清理临时文件
            os.unlink(temp_config_file)
        
        print("✅ 配置管理器测试通过")
        
        # 7. 测试完整的数据处理流程
        print("\n7️⃣ 测试完整数据处理流程...")
        
        # 创建复杂的处理管道
        complex_pipeline = DataProcessingPipeline()
        
        # 使用实际的插件类
        complex_pipeline.plugins['text_cleaner'] = TextCleanerPlugin()
        complex_pipeline.plugins['text_splitter'] = TextSplitterPlugin()
        complex_pipeline.plugins['filter'] = FilterPlugin()
        complex_pipeline.plugins['transform'] = TransformPlugin()
        
        # 添加处理阶段
        complex_pipeline.stages = [
            {'plugin_name': 'text_cleaner', 'config': {}, 'enabled': True},
            {'plugin_name': 'text_splitter', 'config': {'delimiter': ' '}, 'enabled': True},
            {'plugin_name': 'filter', 'config': {'filter_func': lambda x: len(x) > 2}, 'enabled': True},
            {'plugin_name': 'transform', 'config': {'transform_func': lambda x: x.upper()}, 'enabled': True}
        ]
        
        # 执行复杂处理流程
        input_text = "  Hello Beautiful World of Python Programming  "
        result = complex_pipeline.execute(input_text)
        
        # 验证结果：清理 -> 分割 -> 过滤长度>2 -> 转大写
        expected = ['HELLO', 'BEAUTIFUL', 'WORLD', 'PYTHON', 'PROGRAMMING']
        assert result == expected
        
        print("✅ 完整数据处理流程测试通过")
        
        # 8. 测试包导入
        print("\n8️⃣ 测试包导入...")
        
        # 测试主包导入
        import data_processor
        assert hasattr(data_processor, '__version__')
        assert hasattr(data_processor, '__author__')
        assert data_processor.__version__ == '1.0.0'
        
        # 测试主要类导入
        from data_processor import DataProcessingPipeline, BasePlugin, ConfigManager
        
        # 验证类可以正常实例化
        test_pipeline = DataProcessingPipeline()
        test_plugin = BasePlugin('import_test')
        test_config = ConfigManager()
        
        assert isinstance(test_pipeline, DataProcessingPipeline)
        assert isinstance(test_plugin, BasePlugin)
        assert isinstance(test_config, ConfigManager)
        
        print("✅ 包导入测试通过")
        
        # 9. 性能测试
        print("\n9️⃣ 性能测试...")
        import time
        
        # 测试大量数据处理
        large_text = " ".join([f"word{i}" for i in range(1000)])
        
        start_time = time.time()
        result = complex_pipeline.execute(large_text)
        end_time = time.time()
        
        processing_time = end_time - start_time
        assert len(result) == 1000  # 应该有1000个处理后的单词
        assert all(word.startswith('WORD') for word in result)
        
        print(f"✅ 性能测试通过 (处理1000个单词用时: {processing_time:.4f}秒)")
        
        # 10. 错误处理测试
        print("\n🔟 错误处理测试...")
        
        # 测试插件错误处理
        error_plugin = BasePlugin('error_test')
        
        # 测试无效配置
        try:
            error_plugin.initialize(None)
            # 应该能处理 None 配置
            assert error_plugin.config == {}
        except Exception as e:
            print(f"配置处理异常: {e}")
        
        # 测试管道错误处理
        empty_pipeline = DataProcessingPipeline()
        result = empty_pipeline.execute("test")
        assert result == "test"  # 空管道应该返回原数据
        
        print("✅ 错误处理测试通过")
        
        print("\n🎉 所有测试通过！数据处理系统功能完整！")
        print("\n📊 测试统计:")
        print(f"  • 基础插件功能: ✅")
        print(f"  • 数据处理管道: ✅")
        print(f"  • 文本处理插件: ✅")
        print(f"  • 数据处理插件: ✅")
        print(f"  • 配置管理器: ✅")
        print(f"  • 完整处理流程: ✅")
        print(f"  • 包导入功能: ✅")
        print(f"  • 性能测试: ✅")
        print(f"  • 错误处理: ✅")
        
        return True
        
    except Exception as e:
        print(f"❌ 数据处理系统测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# 练习总结和学习要点
# ============================================================================

print("\n\n练习总结和学习要点")
print("=" * 50)

print("""
📚 通过这些练习，你将掌握:

1. 模块基础
   ✓ 模块的创建、导入和使用
   ✓ 模块属性和内省机制
   ✓ __all__ 的使用和作用
   ✓ 模块文档和元数据管理

2. 包管理
   ✓ 包结构的设计和组织
   ✓ __init__.py 的作用和配置
   ✓ 相对导入和绝对导入
   ✓ 包的版本管理和发布

3. 导入机制
   ✓ 模块搜索路径和查找机制
   ✓ 动态导入和模块重载
   ✓ 自定义模块查找器
   ✓ 模块缓存和性能优化

4. 高级特性
   ✓ 懒加载和代理模式
   ✓ 模块装饰器和元编程
   ✓ 插件系统的设计和实现
   ✓ 依赖注入和控制反转

5. 实际应用
   ✓ 微服务架构中的模块设计
   ✓ 配置驱动的应用框架
   ✓ 插件化系统的架构设计
   ✓ 大型项目的模块组织

💡 关键概念:
- 模块是Python代码组织的基本单位
- 包提供了层次化的命名空间
- 导入机制支持灵活的模块加载
- 插件系统实现了代码的可扩展性
- 依赖管理确保了项目的可维护性

🎯 最佳实践:
- 使用清晰的命名约定
- 合理设计包的层次结构
- 正确处理循环导入问题
- 实现完善的错误处理
- 提供充分的文档和测试
- 遵循单一职责原则
- 使用虚拟环境隔离依赖

🚀 进阶方向:
- 学习setuptools和pip的高级用法
- 研究Python的导入机制源码
- 探索异步模块加载技术
- 学习微服务架构设计模式
- 掌握容器化部署技术
""")

print("\n🎉 完成这些练习后，你将成为Python模块和包的专家！")
print("继续探索Python的其他高级特性，如装饰器、生成器、异步编程等。")