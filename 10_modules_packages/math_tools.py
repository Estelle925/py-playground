
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
    print("简单测试:")
    print(f"5! = {factorial(5)}")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"is_prime(17) = {is_prime(17)}")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"lcm(12, 8) = {lcm(12, 8)}")
else:
    print(f"数学工具模块已导入 (v{__version__})")
