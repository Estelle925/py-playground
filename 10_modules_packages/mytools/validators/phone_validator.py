
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
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    
    # 支持多种格式
    patterns = [
        r'^\+?86[1-9]\d{10}$',  # 中国手机号（带国家码）
        r'^1[3-9]\d{9}$',        # 中国手机号
        r'^\+?1[2-9]\d{2}[2-9]\d{2}\d{4}$',  # 美国电话
        r'^\+?[1-9]\d{1,14}$'   # 国际格式
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
    
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    
    if format_type == 'standard' and len(cleaned) == 11 and cleaned.startswith('1'):
        # 中国手机号格式
        return f"{cleaned[:3]}-{cleaned[3:7]}-{cleaned[7:]}"
    elif format_type == 'international':
        if not cleaned.startswith('+'):
            cleaned = '+86' + cleaned
        return cleaned
    
    return cleaned
