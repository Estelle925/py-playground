
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
