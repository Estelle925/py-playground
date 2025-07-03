
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
