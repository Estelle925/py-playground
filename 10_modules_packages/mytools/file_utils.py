
"""文件操作工具模块

提供各种文件操作功能，包括读取、写入、
文件信息获取等。
"""

import os
from pathlib import Path
from typing import List, Union

__all__ = ['read_lines', 'write_lines', 'get_file_size', 'copy_file', 'file_exists']

def read_lines(file_path: Union[str, Path]) -> List[str]:
    """读取文件所有行
    
    Args:
        file_path: 文件路径
    
    Returns:
        List[str]: 文件内容行列表
    
    Example:
        >>> lines = read_lines('test.txt')
        >>> print(len(lines))
        10
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {file_path}")
    except Exception as e:
        raise IOError(f"读取文件失败: {e}")

def write_lines(file_path: Union[str, Path], lines: List[str]) -> None:
    """写入行到文件
    
    Args:
        file_path: 文件路径
        lines: 要写入的行列表
    
    Example:
        >>> write_lines('output.txt', ['line1\n', 'line2\n'])
    """
    try:
        # 确保目录存在
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    except Exception as e:
        raise IOError(f"写入文件失败: {e}")

def get_file_size(file_path: Union[str, Path]) -> int:
    """获取文件大小（字节）
    
    Args:
        file_path: 文件路径
    
    Returns:
        int: 文件大小（字节）
    
    Example:
        >>> size = get_file_size('test.txt')
        >>> print(f"文件大小: {size} 字节")
    """
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在: {file_path}")
    except Exception as e:
        raise IOError(f"获取文件大小失败: {e}")

def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """复制文件
    
    Args:
        src: 源文件路径
        dst: 目标文件路径
    
    Example:
        >>> copy_file('source.txt', 'backup.txt')
    """
    import shutil
    try:
        # 确保目标目录存在
        Path(dst).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    except Exception as e:
        raise IOError(f"复制文件失败: {e}")

def file_exists(file_path: Union[str, Path]) -> bool:
    """检查文件是否存在
    
    Args:
        file_path: 文件路径
    
    Returns:
        bool: 文件是否存在
    
    Example:
        >>> if file_exists('config.txt'):
        ...     print("配置文件存在")
    """
    return Path(file_path).exists()
