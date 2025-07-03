
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
    words = re.findall(r'\b\w+\b', s.lower())
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
