
"""文本处理插件"""

from ..core.plugin import BasePlugin

class TextCleanerPlugin(BasePlugin):
    """文本清理插件"""
    
    def __init__(self):
        super().__init__('text_cleaner', '1.0.0')
    
    def execute(self, data, **kwargs):
        """清理文本数据"""
        if isinstance(data, str):
            # 移除多余空格，转换为小写
            return data.strip().lower()
        elif isinstance(data, list):
            return [item.strip().lower() if isinstance(item, str) else item for item in data]
        return data

class TextSplitterPlugin(BasePlugin):
    """文本分割插件"""
    
    def __init__(self):
        super().__init__('text_splitter', '1.0.0')
    
    def execute(self, data, **kwargs):
        """分割文本"""
        delimiter = kwargs.get('delimiter', ' ')
        if isinstance(data, str):
            return data.split(delimiter)
        return data
