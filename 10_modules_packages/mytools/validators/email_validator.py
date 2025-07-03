
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
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
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
