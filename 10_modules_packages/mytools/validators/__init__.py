
"""验证器子包

提供各种数据验证功能，包括邮箱、电话、URL等验证。
"""

from .email_validator import validate as validate_email
from .phone_validator import validate as validate_phone
from .url_validator import validate as validate_url

__all__ = ['validate_email', 'validate_phone', 'validate_url']

print("验证器模块已加载")
