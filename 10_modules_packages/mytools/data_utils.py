
"""数据处理工具模块

提供各种数据处理功能，包括列表扁平化、
字典合并、数据转换等。
"""

from typing import List, Dict, Any, Union
from collections import defaultdict
import json

__all__ = ['flatten_list', 'merge_dicts', 'group_by', 'filter_dict', 'to_json']

def flatten_list(nested_list: List[Any]) -> List[Any]:
    """扁平化嵌套列表
    
    Args:
        nested_list: 嵌套列表
    
    Returns:
        List[Any]: 扁平化后的列表
    
    Example:
        >>> flatten_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def merge_dicts(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """合并多个字典
    
    Args:
        *dicts: 要合并的字典
    
    Returns:
        Dict[str, Any]: 合并后的字典
    
    Example:
        >>> d1 = {'a': 1, 'b': 2}
        >>> d2 = {'b': 3, 'c': 4}
        >>> merge_dicts(d1, d2)
        {'a': 1, 'b': 3, 'c': 4}
    """
    result = {}
    for d in dicts:
        if isinstance(d, dict):
            result.update(d)
    return result

def group_by(items: List[Any], key_func) -> Dict[Any, List[Any]]:
    """按指定函数分组
    
    Args:
        items: 要分组的项目列表
        key_func: 分组键函数
    
    Returns:
        Dict[Any, List[Any]]: 分组结果
    
    Example:
        >>> words = ['apple', 'banana', 'apricot', 'blueberry']
        >>> group_by(words, lambda x: x[0])
        {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
    """
    groups = defaultdict(list)
    for item in items:
        key = key_func(item)
        groups[key].append(item)
    return dict(groups)

def filter_dict(d: Dict[str, Any], predicate) -> Dict[str, Any]:
    """过滤字典
    
    Args:
        d: 要过滤的字典
        predicate: 过滤条件函数
    
    Returns:
        Dict[str, Any]: 过滤后的字典
    
    Example:
        >>> data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        >>> filter_dict(data, lambda k, v: v > 2)
        {'c': 3, 'd': 4}
    """
    return {k: v for k, v in d.items() if predicate(k, v)}

def to_json(data: Any, indent: int = 2) -> str:
    """转换为JSON字符串
    
    Args:
        data: 要转换的数据
        indent: 缩进空格数
    
    Returns:
        str: JSON字符串
    
    Example:
        >>> data = {'name': 'Alice', 'age': 30}
        >>> print(to_json(data))
        {
          "name": "Alice",
          "age": 30
        }
    """
    try:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    except TypeError as e:
        raise ValueError(f"数据无法序列化为JSON: {e}")
