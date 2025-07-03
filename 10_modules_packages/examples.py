#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python 模块和包 - 示例代码

本文件包含了Python模块和包的各种使用示例，包括：
1. 模块基础操作
2. 包的创建和使用
3. 导入机制详解
4. 模块搜索路径
5. 动态导入
6. 第三方包管理
7. 实际应用场景

作者: Python学习者
日期: 2024年
"""

import os
import sys
import importlib
import types
from pathlib import Path

print("Python 模块和包 - 示例代码")
print("=" * 50)

# ============================================================================
# 1. 模块基础操作
# ============================================================================

print("\n1. 模块基础操作")
print("-" * 30)

# 1.1 创建简单模块
print("\n1.1 创建和使用简单模块")

# 创建一个简单的数学工具模块
math_utils_code = '''
"""数学工具模块"""

def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# 模块级常量
PI = 3.14159265359
E = 2.71828182846

# 模块级变量
_calculation_count = 0

def get_calculation_count():
    """获取计算次数"""
    return _calculation_count

def reset_calculation_count():
    """重置计算次数"""
    global _calculation_count
    _calculation_count = 0

# 模块初始化代码
print(f"数学工具模块已加载，PI = {PI}")
'''

# 将代码写入文件
with open('math_utils.py', 'w', encoding='utf-8') as f:
    f.write(math_utils_code)

print("已创建 math_utils.py 模块")

# 导入并使用模块
try:
    import math_utils
    
    print(f"模块名: {math_utils.__name__}")
    print(f"模块文件: {math_utils.__file__}")
    print(f"模块文档: {math_utils.__doc__}")
    
    # 使用模块函数
    result1 = math_utils.add(10, 5)
    result2 = math_utils.multiply(3, 4)
    print(f"10 + 5 = {result1}")
    print(f"3 × 4 = {result2}")
    print(f"PI = {math_utils.PI}")
    
except ImportError as e:
    print(f"导入模块失败: {e}")

# 1.2 不同的导入方式
print("\n1.2 不同的导入方式")

# 完整导入
print("完整导入:")
import math_utils as mu
print(f"使用别名: {mu.add(1, 2)}")

# 部分导入
print("\n部分导入:")
from math_utils import add, subtract, PI
print(f"直接使用函数: {add(5, 3)}")
print(f"直接使用常量: PI = {PI}")

# 别名导入
print("\n别名导入:")
from math_utils import multiply as mul, divide as div
print(f"使用别名函数: {mul(4, 5)}")

# 1.3 模块属性和内省
print("\n1.3 模块属性和内省")

print(f"模块所有属性: {dir(math_utils)}")
print(f"模块中的函数:")
for name in dir(math_utils):
    obj = getattr(math_utils, name)
    if callable(obj) and not name.startswith('_'):
        print(f"  {name}: {obj.__doc__}")

# 检查属性是否存在
if hasattr(math_utils, 'add'):
    print("模块包含 add 函数")

# 动态获取属性
func_name = 'subtract'
if hasattr(math_utils, func_name):
    func = getattr(math_utils, func_name)
    result = func(10, 3)
    print(f"动态调用 {func_name}: {result}")

# ============================================================================
# 2. 包的创建和使用
# ============================================================================

print("\n\n2. 包的创建和使用")
print("-" * 30)

# 2.1 创建包结构
print("\n2.1 创建包结构")

# 创建包目录结构
package_dir = Path('mypackage')
package_dir.mkdir(exist_ok=True)

# 创建子包
subpackage_dir = package_dir / 'utils'
subpackage_dir.mkdir(exist_ok=True)

# 创建 __init__.py 文件
init_code = '''
"""MyPackage - 示例包

这是一个演示包的使用的示例包。
"""

__version__ = '1.0.0'
__author__ = 'Python学习者'

# 从子模块导入
from .calculator import Calculator
from .utils.string_utils import format_text
from .utils.file_utils import read_config

# 定义 __all__ 控制 from package import * 的行为
__all__ = ['Calculator', 'format_text', 'read_config']

print(f"MyPackage v{__version__} 已加载")
'''

with open(package_dir / '__init__.py', 'w', encoding='utf-8') as f:
    f.write(init_code)

# 创建计算器模块
calculator_code = '''
"""计算器模块"""

class Calculator:
    """简单计算器类"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """加法"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """减法"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """乘法"""
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def get_history(self):
        """获取计算历史"""
        return self.history.copy()
    
    def clear_history(self):
        """清空计算历史"""
        self.history.clear()
'''

with open(package_dir / 'calculator.py', 'w', encoding='utf-8') as f:
    f.write(calculator_code)

# 创建子包的 __init__.py
utils_init_code = '''
"""工具子包"""

from .string_utils import format_text, validate_email
from .file_utils import read_config, write_config

__all__ = ['format_text', 'validate_email', 'read_config', 'write_config']
'''

with open(subpackage_dir / '__init__.py', 'w', encoding='utf-8') as f:
    f.write(utils_init_code)

# 创建字符串工具模块
string_utils_code = '''
"""字符串工具模块"""

import re

def format_text(text, style='title'):
    """格式化文本
    
    Args:
        text: 要格式化的文本
        style: 格式化样式 ('title', 'upper', 'lower', 'capitalize')
    
    Returns:
        格式化后的文本
    """
    if style == 'title':
        return text.title()
    elif style == 'upper':
        return text.upper()
    elif style == 'lower':
        return text.lower()
    elif style == 'capitalize':
        return text.capitalize()
    else:
        return text

def validate_email(email):
    """验证邮箱格式
    
    Args:
        email: 邮箱地址
    
    Returns:
        bool: 是否为有效邮箱
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def truncate_text(text, max_length=50, suffix='...'):
    """截断文本
    
    Args:
        text: 原始文本
        max_length: 最大长度
        suffix: 后缀
    
    Returns:
        截断后的文本
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
'''

with open(subpackage_dir / 'string_utils.py', 'w', encoding='utf-8') as f:
    f.write(string_utils_code)

# 创建文件工具模块
file_utils_code = '''
"""文件工具模块"""

import json
import os
from pathlib import Path

def read_config(config_file):
    """读取配置文件
    
    Args:
        config_file: 配置文件路径
    
    Returns:
        dict: 配置数据
    """
    config_path = Path(config_file)
    
    if not config_path.exists():
        return {}
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            if config_path.suffix.lower() == '.json':
                return json.load(f)
            else:
                # 简单的键值对格式
                config = {}
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            config[key.strip()] = value.strip()
                return config
    except Exception as e:
        print(f"读取配置文件失败: {e}")
        return {}

def write_config(config_file, config_data):
    """写入配置文件
    
    Args:
        config_file: 配置文件路径
        config_data: 配置数据
    
    Returns:
        bool: 是否成功
    """
    try:
        config_path = Path(config_file)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_path, 'w', encoding='utf-8') as f:
            if config_path.suffix.lower() == '.json':
                json.dump(config_data, f, indent=2, ensure_ascii=False)
            else:
                for key, value in config_data.items():
                    f.write(f"{key} = {value}\n")
        return True
    except Exception as e:
        print(f"写入配置文件失败: {e}")
        return False

def ensure_directory(directory):
    """确保目录存在
    
    Args:
        directory: 目录路径
    
    Returns:
        Path: 目录路径对象
    """
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path
'''

with open(subpackage_dir / 'file_utils.py', 'w', encoding='utf-8') as f:
    f.write(file_utils_code)

print("已创建包结构:")
print("mypackage/")
print("  __init__.py")
print("  calculator.py")
print("  utils/")
print("    __init__.py")
print("    string_utils.py")
print("    file_utils.py")

# 2.2 使用包
print("\n2.2 使用包")

try:
    # 导入整个包
    import mypackage
    print(f"包版本: {mypackage.__version__}")
    print(f"包作者: {mypackage.__author__}")
    
    # 使用包中的类
    calc = mypackage.Calculator()
    result1 = calc.add(10, 5)
    result2 = calc.multiply(3, 4)
    print(f"计算结果: {result1}, {result2}")
    print(f"计算历史: {calc.get_history()}")
    
    # 使用包中的函数
    formatted_text = mypackage.format_text('hello world', 'title')
    print(f"格式化文本: {formatted_text}")
    
    # 从子包导入
    from mypackage.utils import string_utils
    email_valid = string_utils.validate_email('test@example.com')
    print(f"邮箱验证: {email_valid}")
    
    # 相对导入示例（在包内部使用）
    print("\n相对导入示例:")
    print("在包内部，可以使用相对导入:")
    print("from .utils import string_utils")
    print("from ..parent_package import something")
    
except ImportError as e:
    print(f"导入包失败: {e}")

# ============================================================================
# 3. 导入机制详解
# ============================================================================

print("\n\n3. 导入机制详解")
print("-" * 30)

# 3.1 模块搜索路径
print("\n3.1 模块搜索路径")

print("Python模块搜索路径:")
for i, path in enumerate(sys.path):
    print(f"  {i+1}. {path}")

# 添加自定义搜索路径
custom_path = os.path.abspath('.')
if custom_path not in sys.path:
    sys.path.insert(0, custom_path)
    print(f"\n已添加自定义路径: {custom_path}")

# 3.2 模块缓存
print("\n3.2 模块缓存")

print("已加载的模块数量:", len(sys.modules))
print("\n部分已加载的模块:")
loaded_modules = list(sys.modules.keys())[:10]
for module in loaded_modules:
    print(f"  {module}")

# 检查特定模块是否已加载
if 'math_utils' in sys.modules:
    print("\nmath_utils 模块已在缓存中")
    print(f"模块对象: {sys.modules['math_utils']}")

# 3.3 动态导入
print("\n3.3 动态导入")

# 使用 importlib 动态导入
module_name = 'math_utils'
try:
    dynamic_module = importlib.import_module(module_name)
    print(f"动态导入成功: {dynamic_module}")
    
    # 动态调用函数
    if hasattr(dynamic_module, 'add'):
        result = dynamic_module.add(100, 200)
        print(f"动态调用结果: {result}")
        
except ImportError as e:
    print(f"动态导入失败: {e}")

# 动态导入包中的模块
try:
    utils_module = importlib.import_module('mypackage.utils.string_utils')
    formatted = utils_module.format_text('dynamic import', 'upper')
    print(f"动态导入包模块结果: {formatted}")
except ImportError as e:
    print(f"动态导入包模块失败: {e}")

# 3.4 模块重载
print("\n3.4 模块重载")

# 修改模块文件
modified_code = math_utils_code.replace(
    'print(f"数学工具模块已加载，PI = {PI}")',
    'print(f"数学工具模块已重新加载，PI = {PI}, E = {E}")')

with open('math_utils.py', 'w', encoding='utf-8') as f:
    f.write(modified_code)

# 重新加载模块
try:
    importlib.reload(math_utils)
    print("模块重载成功")
except Exception as e:
    print(f"模块重载失败: {e}")

# 3.5 条件导入
print("\n3.5 条件导入")

# 尝试导入可选依赖
try:
    import json
    HAS_JSON = True
    print("JSON模块可用")
except ImportError:
    HAS_JSON = False
    print("JSON模块不可用")

# 尝试导入第三方库
try:
    import requests
    HAS_REQUESTS = True
    print("requests库可用")
except ImportError:
    HAS_REQUESTS = False
    print("requests库不可用")

# 根据可用性选择实现
if HAS_JSON:
    def save_data(data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)
else:
    def save_data(data, filename):
        with open(filename, 'w') as f:
            f.write(str(data))

print("已定义条件化的save_data函数")

# ============================================================================
# 4. 模块和包的高级特性
# ============================================================================

print("\n\n4. 模块和包的高级特性")
print("-" * 30)

# 4.1 __all__ 的使用
print("\n4.1 __all__ 的使用")

# 创建一个带有 __all__ 的模块
module_with_all_code = '''
"""带有 __all__ 的模块示例"""

__all__ = ['public_function', 'PublicClass', 'PUBLIC_CONSTANT']

def public_function():
    """公共函数"""
    return "这是公共函数"

def _private_function():
    """私有函数"""
    return "这是私有函数"

class PublicClass:
    """公共类"""
    pass

class _PrivateClass:
    """私有类"""
    pass

PUBLIC_CONSTANT = "公共常量"
_PRIVATE_CONSTANT = "私有常量"
'''

with open('module_with_all.py', 'w', encoding='utf-8') as f:
    f.write(module_with_all_code)

# 测试 __all__ 的效果
try:
    import module_with_all
    print(f"模块的 __all__: {module_with_all.__all__}")
    
    # 显示所有属性
    all_attrs = dir(module_with_all)
    public_attrs = [attr for attr in all_attrs if not attr.startswith('_')]
    print(f"所有公共属性: {public_attrs}")
    
    # from module import * 只会导入 __all__ 中的内容
    print("使用 from module_with_all import * 只会导入:", module_with_all.__all__)
    
except ImportError as e:
    print(f"导入失败: {e}")

# 4.2 模块的元数据
print("\n4.2 模块的元数据")

# 创建带有完整元数据的模块
module_with_metadata_code = '''
"""带有完整元数据的模块

这个模块演示了如何为模块添加完整的元数据信息。

Example:
    >>> from module_with_metadata import greet
    >>> greet("World")
    'Hello, World!'

Attributes:
    __version__ (str): 模块版本号
    __author__ (str): 作者信息
    __email__ (str): 联系邮箱
    __license__ (str): 许可证信息
"""

__version__ = '1.2.3'
__author__ = 'Python学习者'
__email__ = 'learner@example.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2024, Python学习者'
__credits__ = ['Python社区', '开源贡献者']
__maintainer__ = 'Python学习者'
__status__ = 'Development'  # Development, Production, Prototype

__all__ = ['greet', 'get_module_info']

def greet(name):
    """问候函数
    
    Args:
        name (str): 要问候的名字
    
    Returns:
        str: 问候语
    """
    return f"Hello, {name}!"

def get_module_info():
    """获取模块信息
    
    Returns:
        dict: 模块元数据
    """
    return {
        'version': __version__,
        'author': __author__,
        'email': __email__,
        'license': __license__,
        'copyright': __copyright__,
        'status': __status__
    }

# 模块级别的初始化代码
if __name__ == '__main__':
    print(f"模块 {__name__} 被直接执行")
    print(f"版本: {__version__}")
    print(greet("World"))
else:
    print(f"模块 {__name__} 被导入")
'''

with open('module_with_metadata.py', 'w', encoding='utf-8') as f:
    f.write(module_with_metadata_code)

# 导入并查看元数据
try:
    import module_with_metadata
    
    print("模块元数据:")
    metadata = module_with_metadata.get_module_info()
    for key, value in metadata.items():
        print(f"  {key}: {value}")
    
    print(f"\n模块文档: {module_with_metadata.__doc__[:100]}...")
    
except ImportError as e:
    print(f"导入失败: {e}")

# 4.3 命名空间和作用域
print("\n4.3 命名空间和作用域")

# 演示不同的命名空间
print("内置命名空间示例:")
print(f"内置函数 len: {len}")
print(f"内置异常 ValueError: {ValueError}")

print("\n全局命名空间示例:")
global_var = "全局变量"
print(f"全局变量: {global_var}")

def demo_local_namespace():
    """演示局部命名空间"""
    local_var = "局部变量"
    print(f"局部变量: {local_var}")
    print(f"访问全局变量: {global_var}")
    
    # 查看局部命名空间
    print(f"局部命名空间: {locals()}")

print("\n局部命名空间示例:")
demo_local_namespace()

# 查看全局命名空间
print("\n全局命名空间中的部分变量:")
global_vars = {k: v for k, v in globals().items() 
               if not k.startswith('_') and not callable(v)}
for key in list(global_vars.keys())[:5]:  # 只显示前5个
    print(f"  {key}: {type(global_vars[key])}")

# ============================================================================
# 5. 实际应用场景
# ============================================================================

print("\n\n5. 实际应用场景")
print("-" * 30)

# 5.1 配置管理系统
print("\n5.1 配置管理系统")

# 创建配置管理模块
config_manager_code = '''
"""配置管理模块"""

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = Path(config_file)
        self._config = {}
        self._defaults = {
            'debug': False,
            'log_level': 'INFO',
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp'
            }
        }
        self.load_config()
    
    def load_config(self) -> None:
        """加载配置文件"""
        self._config = self._defaults.copy()
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                self._merge_config(self._config, file_config)
            except Exception as e:
                print(f"加载配置文件失败: {e}")
    
    def save_config(self) -> bool:
        """保存配置文件"""
        try:
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self._config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"保存配置文件失败: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        keys = key.split('.')
        value = self._config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default
    
    def set(self, key: str, value: Any) -> None:
        """设置配置值"""
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def _merge_config(self, base: Dict, update: Dict) -> None:
        """合并配置"""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value
    
    def get_all(self) -> Dict:
        """获取所有配置"""
        return self._config.copy()

# 全局配置实例
config = ConfigManager()
'''

with open('config_manager.py', 'w', encoding='utf-8') as f:
    f.write(config_manager_code)

# 使用配置管理器
try:
    from config_manager import config
    
    # 设置配置
    config.set('debug', True)
    config.set('database.host', '192.168.1.100')
    config.set('app.name', 'MyApplication')
    
    # 获取配置
    debug_mode = config.get('debug')
    db_host = config.get('database.host')
    app_name = config.get('app.name', 'DefaultApp')
    
    print(f"调试模式: {debug_mode}")
    print(f"数据库主机: {db_host}")
    print(f"应用名称: {app_name}")
    
    # 保存配置
    if config.save_config():
        print("配置已保存")
    
except ImportError as e:
    print(f"导入配置管理器失败: {e}")

# 5.2 插件系统
print("\n5.2 插件系统")

# 创建插件基类
plugin_system_code = '''
"""插件系统模块"""

import importlib
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Type

class Plugin(ABC):
    """插件基类"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """插件名称"""
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        """插件版本"""
        pass
    
    @abstractmethod
    def initialize(self) -> None:
        """初始化插件"""
        pass
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> any:
        """执行插件功能"""
        pass
    
    def cleanup(self) -> None:
        """清理插件资源"""
        pass

class PluginManager:
    """插件管理器"""
    
    def __init__(self, plugin_dir: str = 'plugins'):
        self.plugin_dir = Path(plugin_dir)
        self.plugins: Dict[str, Plugin] = {}
        self.plugin_classes: Dict[str, Type[Plugin]] = {}
    
    def discover_plugins(self) -> None:
        """发现插件"""
        if not self.plugin_dir.exists():
            print(f"插件目录不存在: {self.plugin_dir}")
            return
        
        # 添加插件目录到Python路径
        plugin_path = str(self.plugin_dir.absolute())
        if plugin_path not in sys.path:
            sys.path.insert(0, plugin_path)
        
        # 扫描插件文件
        for plugin_file in self.plugin_dir.glob('*.py'):
            if plugin_file.name.startswith('_'):
                continue
            
            try:
                module_name = plugin_file.stem
                module = importlib.import_module(module_name)
                
                # 查找插件类
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (isinstance(attr, type) and 
                        issubclass(attr, Plugin) and 
                        attr != Plugin):
                        
                        self.plugin_classes[attr_name] = attr
                        print(f"发现插件类: {attr_name}")
                        
            except Exception as e:
                print(f"加载插件文件 {plugin_file} 失败: {e}")
    
    def load_plugin(self, plugin_class_name: str) -> bool:
        """加载插件"""
        if plugin_class_name not in self.plugin_classes:
            print(f"插件类不存在: {plugin_class_name}")
            return False
        
        try:
            plugin_class = self.plugin_classes[plugin_class_name]
            plugin_instance = plugin_class()
            plugin_instance.initialize()
            
            self.plugins[plugin_instance.name] = plugin_instance
            print(f"插件加载成功: {plugin_instance.name} v{plugin_instance.version}")
            return True
            
        except Exception as e:
            print(f"加载插件失败: {e}")
            return False
    
    def unload_plugin(self, plugin_name: str) -> bool:
        """卸载插件"""
        if plugin_name not in self.plugins:
            print(f"插件未加载: {plugin_name}")
            return False
        
        try:
            plugin = self.plugins[plugin_name]
            plugin.cleanup()
            del self.plugins[plugin_name]
            print(f"插件卸载成功: {plugin_name}")
            return True
            
        except Exception as e:
            print(f"卸载插件失败: {e}")
            return False
    
    def execute_plugin(self, plugin_name: str, *args, **kwargs) -> any:
        """执行插件"""
        if plugin_name not in self.plugins:
            print(f"插件未加载: {plugin_name}")
            return None
        
        try:
            return self.plugins[plugin_name].execute(*args, **kwargs)
        except Exception as e:
            print(f"执行插件失败: {e}")
            return None
    
    def list_plugins(self) -> List[str]:
        """列出已加载的插件"""
        return list(self.plugins.keys())
    
    def get_plugin_info(self, plugin_name: str) -> Dict:
        """获取插件信息"""
        if plugin_name not in self.plugins:
            return {}
        
        plugin = self.plugins[plugin_name]
        return {
            'name': plugin.name,
            'version': plugin.version,
            'class': plugin.__class__.__name__
        }
'''

with open('plugin_system.py', 'w', encoding='utf-8') as f:
    f.write(plugin_system_code)

# 创建插件目录和示例插件
plugins_dir = Path('plugins')
plugins_dir.mkdir(exist_ok=True)

# 创建示例插件1
sample_plugin1_code = '''
"""示例插件1 - 文本处理插件"""

from plugin_system import Plugin

class TextProcessorPlugin(Plugin):
    """文本处理插件"""
    
    @property
    def name(self) -> str:
        return "TextProcessor"
    
    @property
    def version(self) -> str:
        return "1.0.0"
    
    def initialize(self) -> None:
        print(f"初始化 {self.name} 插件")
    
    def execute(self, text: str, operation: str = 'upper') -> str:
        """执行文本处理"""
        if operation == 'upper':
            return text.upper()
        elif operation == 'lower':
            return text.lower()
        elif operation == 'reverse':
            return text[::-1]
        elif operation == 'count':
            return len(text)
        else:
            return text
    
    def cleanup(self) -> None:
        print(f"清理 {self.name} 插件")
'''

with open(plugins_dir / 'text_processor.py', 'w', encoding='utf-8') as f:
    f.write(sample_plugin1_code)

# 创建示例插件2
sample_plugin2_code = '''
"""示例插件2 - 数学计算插件"""

from plugin_system import Plugin
import math

class MathCalculatorPlugin(Plugin):
    """数学计算插件"""
    
    @property
    def name(self) -> str:
        return "MathCalculator"
    
    @property
    def version(self) -> str:
        return "1.1.0"
    
    def initialize(self) -> None:
        print(f"初始化 {self.name} 插件")
        self.operations = {
            'add': lambda x, y: x + y,
            'subtract': lambda x, y: x - y,
            'multiply': lambda x, y: x * y,
            'divide': lambda x, y: x / y if y != 0 else float('inf'),
            'power': lambda x, y: x ** y,
            'sqrt': lambda x: math.sqrt(x),
            'sin': lambda x: math.sin(x),
            'cos': lambda x: math.cos(x)
        }
    
    def execute(self, operation: str, *args) -> float:
        """执行数学计算"""
        if operation not in self.operations:
            raise ValueError(f"不支持的操作: {operation}")
        
        return self.operations[operation](*args)
    
    def cleanup(self) -> None:
        print(f"清理 {self.name} 插件")
        self.operations.clear()
'''

with open(plugins_dir / 'math_calculator.py', 'w', encoding='utf-8') as f:
    f.write(sample_plugin2_code)

# 使用插件系统
try:
    from plugin_system import PluginManager
    
    # 创建插件管理器
    plugin_manager = PluginManager()
    
    # 发现插件
    plugin_manager.discover_plugins()
    
    # 加载插件
    plugin_manager.load_plugin('TextProcessorPlugin')
    plugin_manager.load_plugin('MathCalculatorPlugin')
    
    # 列出已加载的插件
    loaded_plugins = plugin_manager.list_plugins()
    print(f"\n已加载的插件: {loaded_plugins}")
    
    # 执行插件功能
    text_result = plugin_manager.execute_plugin('TextProcessor', 'Hello World', 'upper')
    print(f"文本处理结果: {text_result}")
    
    math_result = plugin_manager.execute_plugin('MathCalculator', 'add', 10, 20)
    print(f"数学计算结果: {math_result}")
    
    # 获取插件信息
    for plugin_name in loaded_plugins:
        info = plugin_manager.get_plugin_info(plugin_name)
        print(f"插件信息 - {plugin_name}: {info}")
    
except ImportError as e:
    print(f"导入插件系统失败: {e}")

# ============================================================================
# 6. 清理和总结
# ============================================================================

print("\n\n6. 清理和总结")
print("-" * 30)

# 清理创建的文件和目录
print("\n清理演示文件...")

files_to_remove = [
    'math_utils.py',
    'module_with_all.py',
    'module_with_metadata.py',
    'config_manager.py',
    'plugin_system.py',
    'config.json'
]

for file_path in files_to_remove:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"已删除: {file_path}")

# 清理目录
import shutil

dirs_to_remove = ['mypackage', 'plugins']
for dir_path in dirs_to_remove:
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        print(f"已删除目录: {dir_path}")

print("\n" + "=" * 50)
print("Python 模块和包 - 示例代码演示完成")
print("=" * 50)

print("""
📚 本示例涵盖的内容:

1. 模块基础操作
   - 创建和导入模块
   - 不同的导入方式
   - 模块属性和内省

2. 包的创建和使用
   - 包结构设计
   - __init__.py 文件
   - 相对导入和绝对导入

3. 导入机制详解
   - 模块搜索路径
   - 模块缓存
   - 动态导入
   - 模块重载
   - 条件导入

4. 高级特性
   - __all__ 的使用
   - 模块元数据
   - 命名空间和作用域

5. 实际应用场景
   - 配置管理系统
   - 插件系统

💡 关键要点:
- 模块是代码组织的基本单位
- 包提供了层次化的模块组织
- 合理使用导入机制可以提高代码的可维护性
- __all__ 控制模块的公共接口
- 动态导入支持灵活的模块加载
- 插件系统是模块化设计的高级应用

🎯 最佳实践:
- 使用描述性的模块和包名
- 合理组织包结构
- 正确使用相对导入和绝对导入
- 为模块添加完整的文档和元数据
- 避免循环导入
- 使用虚拟环境管理依赖
""")

print("\n🎉 继续学习Python的其他高级特性！")