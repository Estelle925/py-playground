
"""数据处理系统包

一个可扩展的插件化数据处理框架。
"""

__version__ = '1.0.0'
__author__ = 'Data Processing Team'

from .core.pipeline import DataProcessingPipeline
from .core.plugin import BasePlugin
from .utils.config import ConfigManager

__all__ = ['DataProcessingPipeline', 'BasePlugin', 'ConfigManager']
