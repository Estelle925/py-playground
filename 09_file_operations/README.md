# 文件操作

## 学习目标

通过本章学习，你将掌握：

1. **文件基础操作**
   - 文件的打开、读取、写入和关闭
   - 文件模式和编码
   - 文件指针和定位

2. **文本文件处理**
   - 逐行读取和批量读取
   - 文本编码和解码
   - CSV文件处理
   - JSON文件处理

3. **二进制文件处理**
   - 二进制文件读写
   - 图片和音频文件处理
   - 文件压缩和解压

4. **文件系统操作**
   - 目录操作（创建、删除、遍历）
   - 文件属性和权限
   - 路径处理和操作

5. **高级文件操作**
   - 文件监控和变化检测
   - 临时文件和内存文件
   - 文件锁和并发访问
   - 大文件处理技术

6. **文件操作最佳实践**
   - 异常处理和资源管理
   - 性能优化技巧
   - 安全性考虑
   - 跨平台兼容性

## 核心概念

### 1. 文件对象和上下文管理器

```python
# 推荐的文件操作方式
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 文件自动关闭，即使发生异常
```

### 2. 文件模式

- **'r'**: 只读模式（默认）
- **'w'**: 写入模式（覆盖）
- **'a'**: 追加模式
- **'x'**: 独占创建模式
- **'b'**: 二进制模式
- **'t'**: 文本模式（默认）
- **'+'**: 读写模式

### 3. 编码处理

```python
# 指定编码
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 处理编码错误
with open('file.txt', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
```

### 4. 路径处理

```python
from pathlib import Path

# 现代路径处理
path = Path('data/file.txt')
if path.exists():
    content = path.read_text(encoding='utf-8')
```

## 常用模块

### 内置模块
- **open()**: 基础文件操作
- **os**: 操作系统接口
- **os.path**: 路径操作
- **pathlib**: 面向对象的路径处理
- **shutil**: 高级文件操作
- **tempfile**: 临时文件
- **glob**: 文件名模式匹配

### 第三方模块
- **csv**: CSV文件处理
- **json**: JSON文件处理
- **pickle**: Python对象序列化
- **zipfile**: ZIP文件处理
- **tarfile**: TAR文件处理
- **watchdog**: 文件系统监控

## 学习路径

### 初级阶段
1. 掌握基本的文件读写操作
2. 理解文件模式和编码
3. 学习使用上下文管理器
4. 练习文本文件处理

### 中级阶段
1. 学习二进制文件处理
2. 掌握目录操作和路径处理
3. 学习CSV和JSON文件处理
4. 理解文件异常处理

### 高级阶段
1. 掌握大文件处理技术
2. 学习文件监控和并发访问
3. 理解文件系统安全性
4. 掌握跨平台文件操作

## 实际应用场景

### 1. 数据处理
- 日志文件分析
- CSV数据导入导出
- 配置文件管理
- 报告生成

### 2. 文件管理
- 批量文件操作
- 文件备份和同步
- 文件格式转换
- 文件清理和整理

### 3. Web开发
- 文件上传和下载
- 静态文件服务
- 缓存文件管理
- 模板文件处理

### 4. 系统管理
- 系统监控脚本
- 自动化部署
- 配置管理
- 日志轮转

## 最佳实践

### 1. 资源管理
```python
# 使用上下文管理器
with open('file.txt') as f:
    data = f.read()

# 处理多个文件
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())
```

### 2. 异常处理
```python
try:
    with open('file.txt') as f:
        data = f.read()
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("没有权限访问文件")
except UnicodeDecodeError:
    print("文件编码错误")
```

### 3. 性能优化
```python
# 大文件逐行处理
with open('large_file.txt') as f:
    for line in f:
        process_line(line)

# 批量读取
with open('file.txt') as f:
    while True:
        chunk = f.read(8192)  # 8KB chunks
        if not chunk:
            break
        process_chunk(chunk)
```

### 4. 安全性考虑
```python
# 验证文件路径
import os.path

def safe_join(directory, filename):
    """安全地连接目录和文件名"""
    filepath = os.path.join(directory, filename)
    if not filepath.startswith(directory):
        raise ValueError("不安全的文件路径")
    return filepath
```

## 常见陷阱

### 1. 忘记关闭文件
```python
# 错误：可能导致资源泄漏
f = open('file.txt')
data = f.read()
# 忘记调用 f.close()

# 正确：使用上下文管理器
with open('file.txt') as f:
    data = f.read()
```

### 2. 编码问题
```python
# 错误：可能导致编码错误
with open('file.txt') as f:  # 使用系统默认编码
    data = f.read()

# 正确：明确指定编码
with open('file.txt', encoding='utf-8') as f:
    data = f.read()
```

### 3. 路径分隔符问题
```python
# 错误：硬编码路径分隔符
path = 'data/files/file.txt'  # 在Windows上可能有问题

# 正确：使用os.path.join或pathlib
import os
path = os.path.join('data', 'files', 'file.txt')

# 或者使用pathlib
from pathlib import Path
path = Path('data') / 'files' / 'file.txt'
```

### 4. 大文件内存问题
```python
# 错误：一次性读取大文件
with open('huge_file.txt') as f:
    data = f.read()  # 可能导致内存不足

# 正确：逐行或分块处理
with open('huge_file.txt') as f:
    for line in f:
        process_line(line)
```

## 练习建议

1. **基础练习**
   - 实现文件复制功能
   - 编写日志文件分析器
   - 创建简单的文本编辑器

2. **进阶练习**
   - 实现文件同步工具
   - 编写CSV数据处理器
   - 创建文件监控系统

3. **项目练习**
   - 开发文件管理器
   - 实现备份工具
   - 创建日志分析系统

通过系统学习和大量练习，你将能够熟练掌握Python文件操作，为后续的项目开发打下坚实基础。