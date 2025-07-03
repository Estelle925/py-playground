
"""数据处理管道模块"""

from .plugin import BasePlugin

class DataProcessingPipeline:
    """数据处理管道"""
    
    def __init__(self):
        self.stages = []
        self.plugins = {}
        self.config = {}
    
    def add_stage(self, plugin_name, config=None):
        """添加处理阶段"""
        stage_config = {
            'plugin_name': plugin_name,
            'config': config or {},
            'stage_id': len(self.stages),
            'enabled': True
        }
        self.stages.append(stage_config)
        
        if plugin_name not in self.plugins:
            plugin_instance = BasePlugin(plugin_name)
            plugin_instance.initialize(config)
            self.plugins[plugin_name] = plugin_instance
        
        return True
    
    def execute(self, input_data):
        """执行管道"""
        current_data = input_data
        
        for stage in self.stages:
            if not stage.get('enabled', True):
                continue
            
            plugin_name = stage['plugin_name']
            plugin = self.plugins[plugin_name]
            current_data = plugin.execute(current_data, **stage['config'])
        
        return current_data
