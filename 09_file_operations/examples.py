#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作示例代码

本文件包含了Python文件操作的各种示例，涵盖：
1. 基础文件操作
2. 文本文件处理
3. 二进制文件处理
4. 文件系统操作
5. 高级文件操作
6. 实际应用场景

作者：Python学习助手
日期：2024年
"""

import os
import sys
import json
import csv
import pickle
import shutil
import tempfile
import zipfile
import tarfile
from pathlib import Path
from datetime import datetime
import hashlib
import mimetypes
from typing import Iterator, List, Dict, Any, Optional
import threading
import time

print("文件操作示例代码")
print("=" * 50)

# ============================================================================
# 1. 基础文件操作
# ============================================================================

print("\n1. 基础文件操作")
print("-" * 30)

# 1.1 文件的打开、读取、写入和关闭
print("\n1.1 基本文件操作")

# 创建示例文件
sample_text = """这是一个示例文件。
包含多行文本。
用于演示文件操作。
Hello, World!
你好，世界！"""

# 写入文件（文本模式）
with open('sample.txt', 'w', encoding='utf-8') as f:
    f.write(sample_text)
print("已创建示例文件 sample.txt")

# 读取整个文件
with open('sample.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(f"文件内容：\n{content}")

# 逐行读取
print("\n逐行读取：")
with open('sample.txt', 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        print(f"第{line_num}行: {line.rstrip()}")

# 读取所有行到列表
with open('sample.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"\n总共{len(lines)}行")

# 1.2 不同的文件模式
print("\n1.2 文件模式示例")

# 追加模式
with open('sample.txt', 'a', encoding='utf-8') as f:
    f.write("\n这是追加的内容。")
print("已追加内容到文件")

# 读写模式
with open('sample.txt', 'r+', encoding='utf-8') as f:
    content = f.read()
    f.seek(0)  # 回到文件开头
    f.write("[修改] " + content)
print("已修改文件内容")

# 1.3 文件指针操作
print("\n1.3 文件指针操作")

with open('sample.txt', 'r', encoding='utf-8') as f:
    print(f"当前位置: {f.tell()}")
    
    # 读取前10个字符
    chunk = f.read(10)
    print(f"读取内容: {repr(chunk)}")
    print(f"当前位置: {f.tell()}")
    
    # 移动到文件开头
    f.seek(0)
    print(f"移动到开头后位置: {f.tell()}")
    
    # 移动到文件末尾
    f.seek(0, 2)  # 2表示从文件末尾开始
    print(f"文件大小: {f.tell()} 字节")

# ============================================================================
# 2. 文本文件处理
# ============================================================================

print("\n\n2. 文本文件处理")
print("-" * 30)

# 2.1 编码处理
print("\n2.1 编码处理")

# 创建包含中文的文件
chinese_text = "你好，世界！\nHello, 世界！\n这是中文测试。"

# 使用UTF-8编码写入
with open('chinese.txt', 'w', encoding='utf-8') as f:
    f.write(chinese_text)

# 使用UTF-8编码读取
with open('chinese.txt', 'r', encoding='utf-8') as f:
    content = f.read()
print(f"UTF-8读取结果：\n{content}")

# 处理编码错误
print("\n处理编码错误：")
try:
    with open('chinese.txt', 'r', encoding='ascii') as f:
        content = f.read()
except UnicodeDecodeError as e:
    print(f"编码错误: {e}")

# 使用错误处理策略
with open('chinese.txt', 'r', encoding='ascii', errors='ignore') as f:
    content = f.read()
print(f"忽略错误后的内容: {repr(content)}")

# 2.2 CSV文件处理
print("\n2.2 CSV文件处理")

# 创建CSV数据
csv_data = [
    ['姓名', '年龄', '城市', '职业'],
    ['张三', '25', '北京', '工程师'],
    ['李四', '30', '上海', '设计师'],
    ['王五', '28', '广州', '产品经理'],
    ['赵六', '35', '深圳', '数据分析师']
]

# 写入CSV文件
with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)
print("已创建CSV文件")

# 读取CSV文件
print("\n读取CSV文件：")
with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row_num, row in enumerate(reader):
        print(f"第{row_num + 1}行: {row}")

# 使用DictReader读取CSV
print("\n使用DictReader读取：")
with open('employees.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']}: {row['年龄']}岁, 在{row['城市']}工作")

# 2.3 JSON文件处理
print("\n2.3 JSON文件处理")

# 创建JSON数据
json_data = {
    "users": [
        {
            "id": 1,
            "name": "张三",
            "email": "zhangsan@example.com",
            "profile": {
                "age": 25,
                "city": "北京",
                "interests": ["编程", "阅读", "旅行"]
            }
        },
        {
            "id": 2,
            "name": "李四",
            "email": "lisi@example.com",
            "profile": {
                "age": 30,
                "city": "上海",
                "interests": ["设计", "摄影", "音乐"]
            }
        }
    ],
    "metadata": {
        "version": "1.0",
        "created_at": datetime.now().isoformat(),
        "total_users": 2
    }
}

# 写入JSON文件
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
print("已创建JSON文件")

# 读取JSON文件
with open('users.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print("\n读取JSON数据：")
print(f"版本: {loaded_data['metadata']['version']}")
print(f"用户数量: {loaded_data['metadata']['total_users']}")
for user in loaded_data['users']:
    print(f"用户: {user['name']}, 邮箱: {user['email']}")

# ============================================================================
# 3. 二进制文件处理
# ============================================================================

print("\n\n3. 二进制文件处理")
print("-" * 30)

# 3.1 基本二进制文件操作
print("\n3.1 二进制文件操作")

# 创建二进制数据
binary_data = bytes(range(256))  # 0-255的字节序列

# 写入二进制文件
with open('binary_data.bin', 'wb') as f:
    f.write(binary_data)
print("已创建二进制文件")

# 读取二进制文件
with open('binary_data.bin', 'rb') as f:
    loaded_data = f.read()

print(f"二进制文件大小: {len(loaded_data)} 字节")
print(f"前10个字节: {list(loaded_data[:10])}")
print(f"后10个字节: {list(loaded_data[-10:])}")

# 3.2 使用pickle序列化Python对象
print("\n3.2 Pickle序列化")

# 创建复杂的Python对象
complex_data = {
    'numbers': [1, 2, 3, 4, 5],
    'text': '这是一个字符串',
    'nested': {
        'date': datetime.now(),
        'tuple': (1, 2, 3),
        'set': {1, 2, 3, 4, 5}
    },
    'function': lambda x: x * 2  # 注意：lambda函数不能被pickle
}

# 移除不能序列化的函数
serializable_data = {k: v for k, v in complex_data.items() if k != 'function'}

# 序列化到文件
with open('data.pickle', 'wb') as f:
    pickle.dump(serializable_data, f)
print("已序列化数据到pickle文件")

# 从文件反序列化
with open('data.pickle', 'rb') as f:
    loaded_data = pickle.load(f)

print("\n反序列化的数据：")
for key, value in loaded_data.items():
    print(f"{key}: {value} (类型: {type(value).__name__})")

# 3.3 文件压缩和解压
print("\n3.3 文件压缩")

# 创建ZIP文件
with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write('sample.txt')
    zipf.write('chinese.txt')
    zipf.write('employees.csv')
    zipf.write('users.json')
print("已创建ZIP压缩文件")

# 查看ZIP文件内容
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    print("\nZIP文件内容：")
    for info in zipf.infolist():
        print(f"  {info.filename}: {info.file_size} 字节 -> {info.compress_size} 字节")

# 解压ZIP文件
os.makedirs('extracted', exist_ok=True)
with zipfile.ZipFile('archive.zip', 'r') as zipf:
    zipf.extractall('extracted')
print("已解压文件到 extracted 目录")

# ============================================================================
# 4. 文件系统操作
# ============================================================================

print("\n\n4. 文件系统操作")
print("-" * 30)

# 4.1 目录操作
print("\n4.1 目录操作")

# 创建目录
os.makedirs('test_dir/sub_dir', exist_ok=True)
print("已创建目录结构")

# 列出目录内容
print("\n当前目录内容：")
for item in os.listdir('.'):
    if os.path.isfile(item):
        size = os.path.getsize(item)
        print(f"文件: {item} ({size} 字节)")
    elif os.path.isdir(item):
        print(f"目录: {item}/")

# 递归遍历目录
print("\n递归遍历目录：")
for root, dirs, files in os.walk('.'):
    level = root.replace('.', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        if not file.startswith('.'):
            print(f"{subindent}{file}")

# 4.2 使用pathlib进行路径操作
print("\n4.2 pathlib路径操作")

# 创建Path对象
current_dir = Path('.')
print(f"当前目录: {current_dir.absolute()}")

# 路径拼接
data_file = current_dir / 'data' / 'file.txt'
print(f"拼接路径: {data_file}")

# 路径信息
sample_path = Path('sample.txt')
if sample_path.exists():
    print(f"\n文件信息:")
    print(f"  名称: {sample_path.name}")
    print(f"  后缀: {sample_path.suffix}")
    print(f"  父目录: {sample_path.parent}")
    print(f"  绝对路径: {sample_path.absolute()}")
    print(f"  是否为文件: {sample_path.is_file()}")
    print(f"  文件大小: {sample_path.stat().st_size} 字节")
    print(f"  修改时间: {datetime.fromtimestamp(sample_path.stat().st_mtime)}")

# 查找文件
print("\n查找.txt文件：")
for txt_file in current_dir.glob('*.txt'):
    print(f"  {txt_file}")

# 递归查找
print("\n递归查找所有文件：")
for file_path in current_dir.rglob('*'):
    if file_path.is_file() and not file_path.name.startswith('.'):
        print(f"  {file_path.relative_to(current_dir)}")

# 4.3 文件操作
print("\n4.3 文件操作")

# 复制文件
shutil.copy2('sample.txt', 'sample_copy.txt')
print("已复制文件")

# 移动文件
shutil.move('sample_copy.txt', 'test_dir/sample_moved.txt')
print("已移动文件")

# 获取文件信息
file_stat = os.stat('sample.txt')
print(f"\n文件统计信息:")
print(f"  大小: {file_stat.st_size} 字节")
print(f"  创建时间: {datetime.fromtimestamp(file_stat.st_ctime)}")
print(f"  修改时间: {datetime.fromtimestamp(file_stat.st_mtime)}")
print(f"  访问时间: {datetime.fromtimestamp(file_stat.st_atime)}")

# ============================================================================
# 5. 高级文件操作
# ============================================================================

print("\n\n5. 高级文件操作")
print("-" * 30)

# 5.1 临时文件
print("\n5.1 临时文件")

# 创建临时文件
with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_file:
    temp_file.write("这是临时文件内容")
    temp_filename = temp_file.name
    print(f"创建临时文件: {temp_filename}")

# 读取临时文件
with open(temp_filename, 'r') as f:
    content = f.read()
print(f"临时文件内容: {content}")

# 删除临时文件
os.unlink(temp_filename)
print("已删除临时文件")

# 使用临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"临时目录: {temp_dir}")
    
    # 在临时目录中创建文件
    temp_file_path = Path(temp_dir) / 'temp_data.txt'
    temp_file_path.write_text("临时目录中的文件")
    
    print(f"临时目录内容: {list(Path(temp_dir).iterdir())}")
# 临时目录自动删除

# 5.2 文件锁定（简单实现）
print("\n5.2 文件锁定")

class FileLock:
    """简单的文件锁实现"""
    
    def __init__(self, filename):
        self.filename = filename
        self.lock_filename = filename + '.lock'
        self.locked = False
    
    def acquire(self, timeout=10):
        """获取锁"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                # 尝试创建锁文件
                with open(self.lock_filename, 'x') as f:
                    f.write(str(os.getpid()))
                self.locked = True
                return True
            except FileExistsError:
                time.sleep(0.1)
        return False
    
    def release(self):
        """释放锁"""
        if self.locked:
            try:
                os.remove(self.lock_filename)
                self.locked = False
                return True
            except FileNotFoundError:
                pass
        return False
    
    def __enter__(self):
        if not self.acquire():
            raise RuntimeError("无法获取文件锁")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

# 使用文件锁
lock_file = 'shared_resource.txt'
with FileLock(lock_file):
    print("获取文件锁成功")
    # 安全地操作文件
    with open(lock_file, 'w') as f:
        f.write("被锁定的文件内容")
    time.sleep(1)  # 模拟长时间操作
print("文件锁已释放")

# 5.3 大文件处理
print("\n5.3 大文件处理")

def process_large_file(filename: str, chunk_size: int = 8192) -> Iterator[str]:
    """分块处理大文件"""
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            yield chunk

def count_lines_in_large_file(filename: str) -> int:
    """高效计算大文件行数"""
    line_count = 0
    with open(filename, 'rb') as f:
        buffer = bytearray(8192)
        while f.readinto(buffer):
            line_count += buffer.count(b'\n')
    return line_count

# 创建一个较大的测试文件
large_file = 'large_test.txt'
with open(large_file, 'w', encoding='utf-8') as f:
    for i in range(1000):
        f.write(f"这是第{i+1}行内容，包含一些测试数据。\n")

print(f"创建了包含1000行的测试文件")

# 分块处理文件
print("\n分块处理文件：")
chunk_count = 0
total_chars = 0
for chunk in process_large_file(large_file, chunk_size=1024):
    chunk_count += 1
    total_chars += len(chunk)
    if chunk_count <= 3:  # 只显示前3个块的信息
        print(f"块{chunk_count}: {len(chunk)}字符")

print(f"总共处理了{chunk_count}个块，{total_chars}个字符")

# 高效计算行数
line_count = count_lines_in_large_file(large_file)
print(f"文件行数: {line_count}")

# 5.4 文件哈希计算
print("\n5.4 文件哈希计算")

def calculate_file_hash(filename: str, algorithm: str = 'md5') -> str:
    """计算文件哈希值"""
    hash_obj = hashlib.new(algorithm)
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# 计算文件哈希
for filename in ['sample.txt', 'users.json', 'binary_data.bin']:
    if os.path.exists(filename):
        md5_hash = calculate_file_hash(filename, 'md5')
        sha256_hash = calculate_file_hash(filename, 'sha256')
        print(f"{filename}:")
        print(f"  MD5: {md5_hash}")
        print(f"  SHA256: {sha256_hash}")

# ============================================================================
# 6. 实际应用场景
# ============================================================================

print("\n\n6. 实际应用场景")
print("-" * 30)

# 6.1 日志文件分析器
print("\n6.1 日志文件分析器")

class LogAnalyzer:
    """简单的日志分析器"""
    
    def __init__(self, log_file: str):
        self.log_file = log_file
        self.stats = {
            'total_lines': 0,
            'error_count': 0,
            'warning_count': 0,
            'info_count': 0,
            'ip_addresses': set(),
            'status_codes': {}
        }
    
    def analyze(self):
        """分析日志文件"""
        with open(self.log_file, 'r', encoding='utf-8') as f:
            for line in f:
                self.stats['total_lines'] += 1
                self._analyze_line(line.strip())
        
        # 转换集合为列表以便JSON序列化
        self.stats['ip_addresses'] = list(self.stats['ip_addresses'])
        return self.stats
    
    def _analyze_line(self, line: str):
        """分析单行日志"""
        line_lower = line.lower()
        
        # 统计日志级别
        if 'error' in line_lower:
            self.stats['error_count'] += 1
        elif 'warning' in line_lower or 'warn' in line_lower:
            self.stats['warning_count'] += 1
        elif 'info' in line_lower:
            self.stats['info_count'] += 1
        
        # 提取IP地址（简单模式）
        import re
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        ips = re.findall(ip_pattern, line)
        self.stats['ip_addresses'].update(ips)
        
        # 提取HTTP状态码
        status_pattern = r'\b[1-5][0-9]{2}\b'
        status_codes = re.findall(status_pattern, line)
        for code in status_codes:
            self.stats['status_codes'][code] = self.stats['status_codes'].get(code, 0) + 1

# 创建示例日志文件
log_content = """2024-01-01 10:00:01 INFO 192.168.1.100 GET /api/users 200 OK
2024-01-01 10:00:02 ERROR 192.168.1.101 POST /api/login 401 Unauthorized
2024-01-01 10:00:03 WARNING 192.168.1.102 GET /api/data 404 Not Found
2024-01-01 10:00:04 INFO 192.168.1.100 GET /api/profile 200 OK
2024-01-01 10:00:05 ERROR 192.168.1.103 POST /api/upload 500 Internal Server Error
2024-01-01 10:00:06 INFO 192.168.1.104 GET /api/status 200 OK
2024-01-01 10:00:07 WARNING 192.168.1.101 GET /api/admin 403 Forbidden
"""

with open('access.log', 'w', encoding='utf-8') as f:
    f.write(log_content)

# 分析日志
analyzer = LogAnalyzer('access.log')
stats = analyzer.analyze()

print("日志分析结果：")
print(f"  总行数: {stats['total_lines']}")
print(f"  错误数: {stats['error_count']}")
print(f"  警告数: {stats['warning_count']}")
print(f"  信息数: {stats['info_count']}")
print(f"  唯一IP数: {len(stats['ip_addresses'])}")
print(f"  状态码统计: {stats['status_codes']}")

# 6.2 配置文件管理器
print("\n6.2 配置文件管理器")

class ConfigManager:
    """配置文件管理器"""
    
    def __init__(self, config_file: str = 'config.json'):
        self.config_file = config_file
        self.config = {}
        self.load_config()
    
    def load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            print(f"配置文件 {self.config_file} 不存在，使用默认配置")
            self.config = self._get_default_config()
            self.save_config()
        except json.JSONDecodeError as e:
            print(f"配置文件格式错误: {e}")
            self.config = self._get_default_config()
    
    def save_config(self):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def get(self, key: str, default=None):
        """获取配置值"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value
    
    def set(self, key: str, value):
        """设置配置值"""
        keys = key.split('.')
        config = self.config
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        config[keys[-1]] = value
        self.save_config()
    
    def _get_default_config(self):
        """获取默认配置"""
        return {
            "app": {
                "name": "MyApp",
                "version": "1.0.0",
                "debug": False
            },
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp_db"
            },
            "logging": {
                "level": "INFO",
                "file": "app.log"
            }
        }

# 使用配置管理器
config = ConfigManager('app_config.json')

print("配置管理器示例：")
print(f"应用名称: {config.get('app.name')}")
print(f"数据库端口: {config.get('database.port')}")
print(f"日志级别: {config.get('logging.level')}")

# 修改配置
config.set('app.debug', True)
config.set('database.host', '192.168.1.100')
print("\n已修改配置")

# 6.3 文件备份工具
print("\n6.3 文件备份工具")

class FileBackup:
    """简单的文件备份工具"""
    
    def __init__(self, backup_dir: str = 'backups'):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)
    
    def backup_file(self, source_file: str, keep_versions: int = 5):
        """备份单个文件"""
        source_path = Path(source_file)
        if not source_path.exists():
            raise FileNotFoundError(f"源文件不存在: {source_file}")
        
        # 生成备份文件名
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{source_path.stem}_{timestamp}{source_path.suffix}"
        backup_path = self.backup_dir / backup_name
        
        # 复制文件
        shutil.copy2(source_path, backup_path)
        print(f"已备份: {source_file} -> {backup_path}")
        
        # 清理旧版本
        self._cleanup_old_versions(source_path.name, keep_versions)
        
        return backup_path
    
    def _cleanup_old_versions(self, filename: str, keep_versions: int):
        """清理旧版本的备份"""
        stem = Path(filename).stem
        suffix = Path(filename).suffix
        
        # 查找所有相关备份文件
        pattern = f"{stem}_*{suffix}"
        backup_files = list(self.backup_dir.glob(pattern))
        
        # 按修改时间排序
        backup_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        # 删除多余的备份
        for old_backup in backup_files[keep_versions:]:
            old_backup.unlink()
            print(f"已删除旧备份: {old_backup}")
    
    def list_backups(self, filename: str = None):
        """列出备份文件"""
        if filename:
            stem = Path(filename).stem
            suffix = Path(filename).suffix
            pattern = f"{stem}_*{suffix}"
            backup_files = list(self.backup_dir.glob(pattern))
        else:
            backup_files = [f for f in self.backup_dir.iterdir() if f.is_file()]
        
        backup_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        return backup_files

# 使用备份工具
backup_tool = FileBackup()

# 备份一些文件
for file_to_backup in ['sample.txt', 'users.json']:
    if os.path.exists(file_to_backup):
        backup_tool.backup_file(file_to_backup)

# 列出备份
print("\n当前备份文件：")
for backup_file in backup_tool.list_backups():
    size = backup_file.stat().st_size
    mtime = datetime.fromtimestamp(backup_file.stat().st_mtime)
    print(f"  {backup_file.name}: {size} 字节, {mtime}")

# ============================================================================
# 清理示例文件
# ============================================================================

print("\n\n清理示例文件")
print("-" * 30)

# 清理创建的文件和目录
files_to_remove = [
    'sample.txt', 'chinese.txt', 'employees.csv', 'users.json',
    'binary_data.bin', 'data.pickle', 'archive.zip', 'access.log',
    'app_config.json', 'large_test.txt', 'shared_resource.txt'
]

dirs_to_remove = ['extracted', 'test_dir', 'backups']

print("清理文件：")
for filename in files_to_remove:
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"  已删除: {filename}")
    except Exception as e:
        print(f"  删除失败 {filename}: {e}")

print("\n清理目录：")
for dirname in dirs_to_remove:
    try:
        if os.path.exists(dirname):
            shutil.rmtree(dirname)
            print(f"  已删除目录: {dirname}")
    except Exception as e:
        print(f"  删除目录失败 {dirname}: {e}")

print("\n" + "=" * 50)
print("文件操作示例演示完成！")
print("=" * 50)

print("""
主要演示内容：
1. 基础文件操作 - 读写、模式、指针
2. 文本文件处理 - 编码、CSV、JSON
3. 二进制文件处理 - 二进制数据、pickle、压缩
4. 文件系统操作 - 目录、路径、文件信息
5. 高级文件操作 - 临时文件、锁定、大文件、哈希
6. 实际应用场景 - 日志分析、配置管理、备份工具

学习要点：
- 始终使用上下文管理器处理文件
- 明确指定文件编码
- 合理选择文件处理模式
- 注意异常处理和资源管理
- 使用pathlib进行现代路径操作
- 考虑大文件的内存效率
""")