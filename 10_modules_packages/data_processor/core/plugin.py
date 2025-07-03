
"""插件基类模块"""

class BasePlugin:
    """数据处理插件基类"""
    
    def __init__(self, name, version='1.0.0'):
        self.name = name
        self.version = version
        self.dependencies = []
        self.config = {}
    
    def initialize(self, config):
        """初始化插件"""
        self.config.update(config or {})
        return True
    
    def execute(self, data, **kwargs):
        """执行插件功能"""
        return data
    
    def cleanup(self):
        """清理插件资源"""
        self.config.clear()
        return True
    
    def get_info(self):
        """获取插件信息"""
        return {
            'name': self.name,
            'version': self.version,
            'dependencies': self.dependencies,
            'config': self.config
        }
