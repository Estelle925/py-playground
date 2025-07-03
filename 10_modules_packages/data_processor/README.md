
# 数据处理系统

一个可扩展的插件化数据处理框架。

## 特性

- 🔌 插件化架构
- 🚀 管道式数据处理
- ⚡ 并行处理支持
- 🛠️ 灵活的配置管理
- 🧪 完整的测试覆盖

## 快速开始

```python
from data_processor import DataProcessingPipeline, BasePlugin

# 创建管道
pipeline = DataProcessingPipeline()

# 添加处理阶段
pipeline.add_stage('text_cleaner')
pipeline.add_stage('text_splitter', {'delimiter': ' '})

# 执行处理
result = pipeline.execute("Hello World")
print(result)  # ['hello', 'world']
```

## 目录结构

```
data_processor/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── plugin.py
│   └── pipeline.py
├── plugins/
│   ├── __init__.py
│   ├── text_processor.py
│   └── data_processor.py
├── utils/
│   ├── __init__.py
│   └── config.py
├── config/
│   ├── __init__.py
│   └── example_config.json
├── tests/
│   ├── __init__.py
│   └── test_core.py
└── README.md
```

## 插件开发

继承 `BasePlugin` 类来创建自定义插件：

```python
from data_processor.core.plugin import BasePlugin

class MyPlugin(BasePlugin):
    def __init__(self):
        super().__init__('my_plugin', '1.0.0')
    
    def execute(self, data, **kwargs):
        # 实现你的处理逻辑
        return processed_data
```
