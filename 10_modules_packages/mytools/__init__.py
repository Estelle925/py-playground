
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
