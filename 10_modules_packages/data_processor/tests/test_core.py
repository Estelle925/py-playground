
"""核心功能测试"""

def test_base_plugin():
    """测试基础插件"""
    from data_processor.core.plugin import BasePlugin
    
    plugin = BasePlugin('test_plugin')
    assert plugin.name == 'test_plugin'
    assert plugin.initialize({}) == True
    assert plugin.execute('test_data') == 'test_data'
    assert plugin.cleanup() == True

def test_pipeline():
    """测试数据管道"""
    from data_processor.core.pipeline import DataProcessingPipeline
    
    pipeline = DataProcessingPipeline()
    assert pipeline.add_stage('test_stage') == True
    assert len(pipeline.stages) == 1
    
    result = pipeline.execute('test_data')
    assert result == 'test_data'

if __name__ == '__main__':
    test_base_plugin()
    test_pipeline()
    print("✅ 所有核心测试通过")
