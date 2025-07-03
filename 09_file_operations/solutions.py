#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件操作练习题参考答案

本文件包含了Python文件操作练习题的参考答案，涵盖：
1. 基础文件操作
2. 文本文件处理
3. 二进制文件处理
4. 文件系统操作
5. 高级文件操作
6. 综合应用

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
from typing import Iterator, List, Dict, Any, Optional, Union
import threading
import time
import re
from collections import defaultdict, Counter
import sqlite3

print("文件操作练习题参考答案")
print("=" * 50)

# ============================================================================
# 1. 基础文件操作练习答案
# ============================================================================

print("\n1. 基础文件操作练习答案")
print("-" * 30)

# 练习 1.1: 文件读写基础
print("\n练习 1.1: 文件读写基础")

def file_reader_writer_demo():
    """文件读写基础演示"""
    filename = 'demo_file.txt'
    
    # 1. 创建文件并写入内容
    print("1. 创建文件并写入内容")
    content = [
        "这是第一行内容\n",
        "这是第二行内容\n",
        "这是第三行内容\n",
        "这是第四行内容\n",
        "这是第五行内容\n"
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print(f"已创建文件 {filename}")
    
    # 2. 读取整个文件内容
    print("\n2. 读取整个文件内容")
    with open(filename, 'r', encoding='utf-8') as f:
        full_content = f.read()
    print(f"文件内容：\n{full_content}")
    
    # 3. 逐行读取文件内容
    print("3. 逐行读取文件内容")
    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            print(f"第{line_num}行: {line.rstrip()}")
    
    # 4. 将文件内容读取到列表
    print("\n4. 将文件内容读取到列表")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"文件行数: {len(lines)}")
    print(f"列表内容: {[line.rstrip() for line in lines]}")
    
    # 5. 追加内容
    print("\n5. 追加内容")
    with open(filename, 'a', encoding='utf-8') as f:
        f.write("这是追加的第六行内容\n")
        f.write("这是追加的第七行内容\n")
    print("已追加两行内容")
    
    # 6. 再次读取整个文件
    print("\n6. 再次读取整个文件")
    with open(filename, 'r', encoding='utf-8') as f:
        updated_content = f.read()
    print(f"更新后的文件内容：\n{updated_content}")
    
    # 清理
    os.remove(filename)
    print(f"已删除文件 {filename}")

file_reader_writer_demo()

# 练习 1.2: 文件指针操作
print("\n\n练习 1.2: 文件指针操作")

def file_pointer_demo():
    """文件指针操作演示"""
    filename = 'pointer_demo.txt'
    
    # 1. 创建文件
    content = """第一行：这是一个多行文本文件
第二行：用于演示文件指针操作
第三行：包含中文和英文内容
第四行：Hello, World!
第五行：文件指针操作示例"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"已创建文件 {filename}")
    
    with open(filename, 'r', encoding='utf-8') as f:
        # 2. 读取前10个字符
        print("\n2. 读取前10个字符")
        first_10_chars = f.read(10)
        print(f"前10个字符: {repr(first_10_chars)}")
        
        # 3. 获取当前文件指针位置
        print("\n3. 当前文件指针位置")
        current_pos = f.tell()
        print(f"当前位置: {current_pos}")
        
        # 4. 移动到文件开头，读取5个字符
        print("\n4. 移动到文件开头，读取5个字符")
        f.seek(0)
        first_5_chars = f.read(5)
        print(f"前5个字符: {repr(first_5_chars)}")
        print(f"移动后位置: {f.tell()}")
        
        # 5. 移动到文件中间位置
        print("\n5. 移动到文件中间位置")
        f.seek(0, 2)  # 移动到文件末尾
        file_size = f.tell()
        middle_pos = file_size // 2
        f.seek(middle_pos)
        print(f"文件大小: {file_size}, 中间位置: {middle_pos}")
        
        # 读取该位置开始的一行
        remaining = f.read()
        first_line_from_middle = remaining.split('\n')[0]
        print(f"从中间位置开始的内容: {repr(first_line_from_middle)}")
        
        # 6. 移动到文件末尾尝试读取
        print("\n6. 移动到文件末尾尝试读取")
        f.seek(0, 2)
        end_content = f.read()
        print(f"文件末尾读取结果: {repr(end_content)} (空字符串，因为已到文件末尾)")
        
        # 7. 计算文件总字节数
        print("\n7. 计算文件总字节数")
        f.seek(0, 2)
        total_bytes = f.tell()
        print(f"文件总字节数: {total_bytes}")
    
    # 清理
    os.remove(filename)
    print(f"已删除文件 {filename}")

file_pointer_demo()

# 练习 1.3: 安全的文件操作
print("\n\n练习 1.3: 安全的文件操作")

def safe_read(filename: str) -> tuple[bool, str]:
    """安全地读取文件内容
    
    Args:
        filename: 文件名
        
    Returns:
        (成功标志, 内容或错误信息)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return True, content
    except FileNotFoundError:
        return False, f"文件不存在: {filename}"
    except PermissionError:
        return False, f"没有权限读取文件: {filename}"
    except UnicodeDecodeError as e:
        return False, f"文件编码错误: {e}"
    except Exception as e:
        return False, f"读取文件时发生未知错误: {e}"

def safe_write(filename: str, content: str) -> tuple[bool, str]:
    """安全地写入文件内容
    
    Args:
        filename: 文件名
        content: 要写入的内容
        
    Returns:
        (成功标志, 成功或错误信息)
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, f"成功写入文件: {filename}"
    except PermissionError:
        return False, f"没有权限写入文件: {filename}"
    except OSError as e:
        return False, f"写入文件时发生系统错误: {e}"
    except Exception as e:
        return False, f"写入文件时发生未知错误: {e}"

def test_safe_file_operations():
    """测试安全文件操作函数"""
    print("测试安全文件操作函数")
    
    # 测试写入文件
    test_content = "这是测试内容\n包含多行文本\n用于测试安全文件操作"
    success, message = safe_write('test_safe.txt', test_content)
    print(f"写入测试: {message}")
    
    if success:
        # 测试读取存在的文件
        success, content = safe_read('test_safe.txt')
        if success:
            print(f"读取成功，内容长度: {len(content)}")
            print(f"内容预览: {repr(content[:50])}...")
        else:
            print(f"读取失败: {content}")
        
        # 清理测试文件
        os.remove('test_safe.txt')
    
    # 测试读取不存在的文件
    success, message = safe_read('nonexistent_file.txt')
    print(f"读取不存在文件测试: {message}")
    
    # 测试写入到只读目录（如果可能）
    try:
        success, message = safe_write('/root/test.txt', 'test')
        print(f"写入受限目录测试: {message}")
    except:
        print("写入受限目录测试: 无法测试（权限限制）")

test_safe_file_operations()

# ============================================================================
# 2. 文本文件处理练习答案
# ============================================================================

print("\n\n2. 文本文件处理练习答案")
print("-" * 30)

# 练习 2.1: CSV文件处理
print("\n练习 2.1: CSV文件处理")

def csv_processor_demo():
    """CSV文件处理演示"""
    filename = 'employees.csv'
    
    # 1. 创建CSV文件
    print("1. 创建CSV文件")
    employees_data = [
        ['姓名', '年龄', '城市', '职业'],
        ['张三', '25', '北京', '软件工程师'],
        ['李四', '30', '上海', '产品经理'],
        ['王五', '28', '广州', '数据分析师'],
        ['赵六', '35', '深圳', '架构师'],
        ['钱七', '26', '北京', '前端工程师'],
        ['孙八', '32', '上海', '运维工程师']
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(employees_data)
    print(f"已创建CSV文件 {filename}")
    
    # 2. 读取CSV文件
    print("\n2. 读取CSV文件")
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row_num, row in enumerate(reader):
            print(f"第{row_num + 1}行: {row}")
    
    # 3. 计算平均年龄
    print("\n3. 计算平均年龄")
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        ages = [int(row['年龄']) for row in reader]
    
    average_age = sum(ages) / len(ages)
    print(f"平均年龄: {average_age:.1f}岁")
    
    # 4. 按城市分组
    print("\n4. 按城市分组")
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        city_groups = defaultdict(list)
        for row in reader:
            city_groups[row['城市']].append(row['姓名'])
    
    for city, names in city_groups.items():
        print(f"{city}: {', '.join(names)}")
    
    # 5. 按年龄排序并写入新文件
    print("\n5. 按年龄排序")
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        sorted_employees = sorted(reader, key=lambda x: int(x['年龄']))
    
    sorted_filename = 'employees_sorted.csv'
    with open(sorted_filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['姓名', '年龄', '城市', '职业']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_employees)
    
    print(f"已创建按年龄排序的文件 {sorted_filename}")
    
    # 显示排序结果
    with open(sorted_filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['姓名']}: {row['年龄']}岁")
    
    # 清理
    os.remove(filename)
    os.remove(sorted_filename)
    print("已清理临时文件")

csv_processor_demo()

# 练习 2.2: JSON文件处理
print("\n\n练习 2.2: JSON文件处理")

def json_processor_demo():
    """JSON文件处理演示"""
    filename = 'school_data.json'
    
    # 1. 创建复杂的数据结构
    print("1. 创建学校数据")
    school_data = {
        "school_info": {
            "name": "北京理工大学",
            "address": "北京市海淀区中关村南大街5号",
            "founded_year": 1940
        },
        "courses": [
            {
                "course_name": "Python编程",
                "teacher": "张教授",
                "credits": 3
            },
            {
                "course_name": "数据结构",
                "teacher": "李教授",
                "credits": 4
            },
            {
                "course_name": "算法设计",
                "teacher": "王教授",
                "credits": 3
            }
        ],
        "students": [
            {
                "id": 1,
                "name": "张三",
                "age": 20,
                "grades": [85, 92, 78, 88, 95]
            },
            {
                "id": 2,
                "name": "李四",
                "age": 21,
                "grades": [90, 87, 93, 89, 91]
            },
            {
                "id": 3,
                "name": "王五",
                "age": 19,
                "grades": [78, 85, 82, 79, 88]
            },
            {
                "id": 4,
                "name": "赵六",
                "age": 22,
                "grades": [95, 98, 92, 96, 94]
            }
        ]
    }
    
    # 2. 保存为JSON文件
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(school_data, f, ensure_ascii=False, indent=2)
    print(f"已创建JSON文件 {filename}")
    
    # 3. 从JSON文件读取数据
    print("\n2. 读取JSON数据")
    with open(filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    print(f"学校: {loaded_data['school_info']['name']}")
    print(f"建校年份: {loaded_data['school_info']['founded_year']}")
    print(f"课程数量: {len(loaded_data['courses'])}")
    print(f"学生数量: {len(loaded_data['students'])}")
    
    # 4. 计算每个学生的平均成绩
    print("\n3. 计算学生平均成绩")
    for student in loaded_data['students']:
        avg_grade = sum(student['grades']) / len(student['grades'])
        student['average_grade'] = round(avg_grade, 2)
        print(f"{student['name']}: {avg_grade:.2f}")
    
    # 5. 找出平均成绩最高的学生
    print("\n4. 找出平均成绩最高的学生")
    best_student = max(loaded_data['students'], key=lambda x: x['average_grade'])
    print(f"最高平均分学生: {best_student['name']} ({best_student['average_grade']}分)")
    
    # 6. 修改学生信息
    print("\n5. 修改学生信息")
    # 为张三添加一门新成绩
    for student in loaded_data['students']:
        if student['name'] == '张三':
            student['grades'].append(96)
            student['average_grade'] = sum(student['grades']) / len(student['grades'])
            print(f"已为{student['name']}添加新成绩，新平均分: {student['average_grade']:.2f}")
            break
    
    # 7. 保存修改后的数据
    updated_filename = 'school_data_updated.json'
    with open(updated_filename, 'w', encoding='utf-8') as f:
        json.dump(loaded_data, f, ensure_ascii=False, indent=2)
    print(f"已保存修改后的数据到 {updated_filename}")
    
    # 清理
    os.remove(filename)
    os.remove(updated_filename)
    print("已清理临时文件")

json_processor_demo()

# 练习 2.3: 文本文件分析器
print("\n\n练习 2.3: 文本文件分析器")

class TextAnalyzer:
    """文本分析器类"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.stats = {
            'total_chars': 0,
            'total_chars_no_spaces': 0,
            'total_words': 0,
            'total_lines': 0,
            'avg_chars_per_line': 0,
            'avg_words_per_line': 0,
            'most_common_words': [],
            'longest_sentence': '',
            'punctuation_count': {}
        }
    
    def analyze(self) -> dict:
        """分析文本文件"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self._analyze_content(content)
            return self.stats
            
        except Exception as e:
            raise Exception(f"分析文件时出错: {e}")
    
    def _analyze_content(self, content: str):
        """分析文本内容"""
        lines = content.split('\n')
        words = re.findall(r'\b\w+\b', content.lower())
        sentences = re.split(r'[.!?]+', content)
        
        # 基本统计
        self.stats['total_chars'] = len(content)
        self.stats['total_chars_no_spaces'] = len(content.replace(' ', ''))
        self.stats['total_words'] = len(words)
        self.stats['total_lines'] = len(lines)
        
        # 平均值
        if self.stats['total_lines'] > 0:
            self.stats['avg_chars_per_line'] = self.stats['total_chars'] / self.stats['total_lines']
            self.stats['avg_words_per_line'] = self.stats['total_words'] / self.stats['total_lines']
        
        # 最常见的单词
        word_counter = Counter(words)
        self.stats['most_common_words'] = word_counter.most_common(10)
        
        # 最长的句子
        if sentences:
            self.stats['longest_sentence'] = max(sentences, key=len).strip()
        
        # 标点符号统计
        punctuation = '.,;:!?"()[]{}'
        for char in content:
            if char in punctuation:
                self.stats['punctuation_count'][char] = self.stats['punctuation_count'].get(char, 0) + 1
    
    def save_report(self, report_filename: str):
        """保存分析报告"""
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(f"文本分析报告\n")
            f.write(f"=" * 30 + "\n\n")
            f.write(f"文件名: {self.filename}\n")
            f.write(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write(f"基本统计:\n")
            f.write(f"  总字符数: {self.stats['total_chars']}\n")
            f.write(f"  总字符数(不含空格): {self.stats['total_chars_no_spaces']}\n")
            f.write(f"  总单词数: {self.stats['total_words']}\n")
            f.write(f"  总行数: {self.stats['total_lines']}\n")
            f.write(f"  平均每行字符数: {self.stats['avg_chars_per_line']:.2f}\n")
            f.write(f"  平均每行单词数: {self.stats['avg_words_per_line']:.2f}\n\n")
            
            f.write(f"最常见的10个单词:\n")
            for word, count in self.stats['most_common_words']:
                f.write(f"  {word}: {count}次\n")
            
            f.write(f"\n最长的句子:\n")
            f.write(f"  {self.stats['longest_sentence'][:100]}...\n")
            
            f.write(f"\n标点符号统计:\n")
            for punct, count in sorted(self.stats['punctuation_count'].items()):
                f.write(f"  '{punct}': {count}次\n")

def text_analyzer_demo():
    """文本分析器演示"""
    # 创建示例文本文件
    sample_text = """这是一个示例文本文件，用于演示文本分析器的功能。
文本分析是自然语言处理的重要组成部分。
通过分析文本，我们可以了解文本的基本特征，如字符数、单词数、句子数等。
这个分析器还可以统计最常见的单词和标点符号的使用情况。

Python是一种强大的编程语言，特别适合文本处理和数据分析。
使用Python，我们可以轻松地读取文件、处理字符串、统计数据。
正则表达式是文本处理中的利器，可以帮助我们提取和匹配特定的模式。

这个示例包含了中文和英文内容，以及各种标点符号：,.;:!?"()[]{}。
通过分析这些内容，我们可以得到有用的统计信息。
"""
    
    test_filename = 'sample_text.txt'
    with open(test_filename, 'w', encoding='utf-8') as f:
        f.write(sample_text)
    
    print("文本分析器演示")
    
    # 创建分析器并分析文件
    analyzer = TextAnalyzer(test_filename)
    stats = analyzer.analyze()
    
    # 显示分析结果
    print(f"\n分析结果:")
    print(f"  总字符数: {stats['total_chars']}")
    print(f"  总字符数(不含空格): {stats['total_chars_no_spaces']}")
    print(f"  总单词数: {stats['total_words']}")
    print(f"  总行数: {stats['total_lines']}")
    print(f"  平均每行字符数: {stats['avg_chars_per_line']:.2f}")
    print(f"  平均每行单词数: {stats['avg_words_per_line']:.2f}")
    
    print(f"\n最常见的5个单词:")
    for word, count in stats['most_common_words'][:5]:
        print(f"  {word}: {count}次")
    
    print(f"\n最长的句子: {stats['longest_sentence'][:50]}...")
    
    print(f"\n标点符号统计:")
    for punct, count in list(stats['punctuation_count'].items())[:5]:
        print(f"  '{punct}': {count}次")
    
    # 保存报告
    report_filename = 'text_analysis_report.txt'
    analyzer.save_report(report_filename)
    print(f"\n分析报告已保存到 {report_filename}")
    
    # 清理
    os.remove(test_filename)
    os.remove(report_filename)
    print("已清理临时文件")

text_analyzer_demo()

# ============================================================================
# 3. 二进制文件处理练习答案
# ============================================================================

print("\n\n3. 二进制文件处理练习答案")
print("-" * 30)

# 练习 3.1: 图像文件元数据读取器
print("\n练习 3.1: 图像文件元数据读取器")

class ImageMetadataReader:
    """图像文件元数据读取器"""
    
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.metadata = {}
    
    def read_metadata(self) -> dict:
        """读取图像元数据"""
        try:
            # 基本文件信息
            file_stat = os.stat(self.image_path)
            self.metadata['file_size'] = file_stat.st_size
            self.metadata['created_time'] = datetime.fromtimestamp(file_stat.st_ctime)
            self.metadata['modified_time'] = datetime.fromtimestamp(file_stat.st_mtime)
            
            # 尝试读取图像信息（简化版，不使用PIL）
            self._read_basic_image_info()
            
            return self.metadata
            
        except Exception as e:
            raise Exception(f"读取图像元数据失败: {e}")
    
    def _read_basic_image_info(self):
        """读取基本图像信息（简化实现）"""
        with open(self.image_path, 'rb') as f:
            # 读取文件头
            header = f.read(20)
            
            # 检测文件格式
            if header.startswith(b'\xff\xd8\xff'):
                self.metadata['format'] = 'JPEG'
                self._read_jpeg_info(f)
            elif header.startswith(b'\x89PNG\r\n\x1a\n'):
                self.metadata['format'] = 'PNG'
                self._read_png_info(f)
            elif header.startswith(b'GIF87a') or header.startswith(b'GIF89a'):
                self.metadata['format'] = 'GIF'
                self._read_gif_info(f)
            else:
                self.metadata['format'] = 'Unknown'
                self.metadata['width'] = 'Unknown'
                self.metadata['height'] = 'Unknown'
    
    def _read_jpeg_info(self, f):
        """读取JPEG信息（简化实现）"""
        # 这是一个简化的JPEG解析，实际应用中建议使用PIL
        self.metadata['width'] = 'Unknown (需要PIL库)'
        self.metadata['height'] = 'Unknown (需要PIL库)'
        self.metadata['color_depth'] = 'Unknown (需要PIL库)'
    
    def _read_png_info(self, f):
        """读取PNG信息（简化实现）"""
        f.seek(16)  # 跳到IHDR块
        width_bytes = f.read(4)
        height_bytes = f.read(4)
        
        if len(width_bytes) == 4 and len(height_bytes) == 4:
            self.metadata['width'] = int.from_bytes(width_bytes, 'big')
            self.metadata['height'] = int.from_bytes(height_bytes, 'big')
        else:
            self.metadata['width'] = 'Unknown'
            self.metadata['height'] = 'Unknown'
        
        self.metadata['color_depth'] = 'Unknown (需要详细解析)'
    
    def _read_gif_info(self, f):
        """读取GIF信息（简化实现）"""
        f.seek(6)  # 跳到尺寸信息
        width_bytes = f.read(2)
        height_bytes = f.read(2)
        
        if len(width_bytes) == 2 and len(height_bytes) == 2:
            self.metadata['width'] = int.from_bytes(width_bytes, 'little')
            self.metadata['height'] = int.from_bytes(height_bytes, 'little')
        else:
            self.metadata['width'] = 'Unknown'
            self.metadata['height'] = 'Unknown'
        
        self.metadata['color_depth'] = 'Unknown (需要详细解析)'

def create_sample_image():
    """创建一个简单的PNG图像文件用于测试"""
    # 创建一个最小的PNG文件（1x1像素，白色）
    png_data = (
        b'\x89PNG\r\n\x1a\n'  # PNG签名
        b'\x00\x00\x00\rIHDR'  # IHDR块头
        b'\x00\x00\x00\x01'    # 宽度：1
        b'\x00\x00\x00\x01'    # 高度：1
        b'\x08\x02\x00\x00\x00'  # 位深度、颜色类型等
        b'\x90wS\xde'         # CRC
        b'\x00\x00\x00\nIDAT'  # IDAT块头
        b'x\x9cc```\x00\x00\x00\x02\x00\x01'  # 压缩的图像数据
        b'\xe2!\xbc3'         # CRC
        b'\x00\x00\x00\x00IEND'  # IEND块头
        b'\xaeB`\x82'         # CRC
    )
    
    with open('sample_image.png', 'wb') as f:
        f.write(png_data)
    
    return 'sample_image.png'

def image_metadata_demo():
    """图像元数据读取器演示"""
    print("图像元数据读取器演示")
    
    # 创建示例图像
    image_file = create_sample_image()
    print(f"已创建示例图像: {image_file}")
    
    # 读取元数据
    reader = ImageMetadataReader(image_file)
    metadata = reader.read_metadata()
    
    print(f"\n图像元数据:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")
    
    # 清理
    os.remove(image_file)
    print(f"已删除示例图像")

image_metadata_demo()

# 练习 3.2: 简单文件加密解密器
print("\n\n练习 3.2: 简单文件加密解密器")

class SimpleFileEncryptor:
    """简单文件加密解密器"""
    
    @staticmethod
    def encrypt_file(input_file: str, output_file: str, key: str) -> bool:
        """加密文件
        
        Args:
            input_file: 输入文件路径
            output_file: 输出文件路径
            key: 加密密钥
            
        Returns:
            是否成功
        """
        try:
            with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
                key_bytes = key.encode('utf-8')
                key_len = len(key_bytes)
                
                while True:
                    chunk = infile.read(8192)  # 8KB块
                    if not chunk:
                        break
                    
                    # 使用XOR加密
                    encrypted_chunk = bytearray()
                    for i, byte in enumerate(chunk):
                        encrypted_byte = byte ^ key_bytes[i % key_len]
                        encrypted_chunk.append(encrypted_byte)
                    
                    outfile.write(encrypted_chunk)
            
            return True
            
        except Exception as e:
            print(f"加密失败: {e}")
            return False
    
    @staticmethod
    def decrypt_file(input_file: str, output_file: str, key: str) -> bool:
        """解密文件
        
        Args:
            input_file: 输入文件路径
            output_file: 输出文件路径
            key: 解密密钥
            
        Returns:
            是否成功
        """
        # XOR加密的特性：加密和解密使用相同的操作
        return SimpleFileEncryptor.encrypt_file(input_file, output_file, key)
    
    @staticmethod
    def verify_files_identical(file1: str, file2: str) -> bool:
        """验证两个文件是否相同"""
        try:
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
                while True:
                    chunk1 = f1.read(8192)
                    chunk2 = f2.read(8192)
                    
                    if chunk1 != chunk2:
                        return False
                    
                    if not chunk1:  # 两个文件都到达末尾
                        return True
                        
        except Exception:
            return False

def file_encryption_demo():
    """文件加密解密演示"""
    print("文件加密解密演示")
    
    # 创建测试文件
    original_file = 'original.txt'
    encrypted_file = 'encrypted.bin'
    decrypted_file = 'decrypted.txt'
    
    test_content = """这是一个测试文件，用于演示文件加密和解密功能。
文件包含中文和英文内容。
This file contains both Chinese and English content.
加密算法使用简单的XOR操作。
The encryption algorithm uses simple XOR operation.
测试数据：1234567890
Test data: abcdefghijklmnopqrstuvwxyz
"""
    
    with open(original_file, 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print(f"已创建原始文件: {original_file}")
    
    # 加密文件
    encryption_key = "MySecretKey123"
    success = SimpleFileEncryptor.encrypt_file(original_file, encrypted_file, encryption_key)
    
    if success:
        print(f"文件加密成功: {encrypted_file}")
        
        # 显示加密文件的前几个字节
        with open(encrypted_file, 'rb') as f:
            encrypted_data = f.read(50)
        print(f"加密数据预览: {encrypted_data.hex()}")
        
        # 解密文件
        success = SimpleFileEncryptor.decrypt_file(encrypted_file, decrypted_file, encryption_key)
        
        if success:
            print(f"文件解密成功: {decrypted_file}")
            
            # 验证解密后的文件与原始文件是否相同
            if SimpleFileEncryptor.verify_files_identical(original_file, decrypted_file):
                print("✓ 验证成功：解密后的文件与原始文件完全相同")
            else:
                print("✗ 验证失败：解密后的文件与原始文件不同")
            
            # 显示解密后的内容
            with open(decrypted_file, 'r', encoding='utf-8') as f:
                decrypted_content = f.read(100)
            print(f"解密内容预览: {decrypted_content[:100]}...")
        
        else:
            print("文件解密失败")
    else:
        print("文件加密失败")
    
    # 测试错误的密钥
    print("\n测试错误密钥:")
    wrong_key_file = 'wrong_key_decrypted.txt'
    SimpleFileEncryptor.decrypt_file(encrypted_file, wrong_key_file, "WrongKey")
    
    try:
        with open(wrong_key_file, 'r', encoding='utf-8', errors='ignore') as f:
            wrong_content = f.read(50)
        print(f"错误密钥解密结果: {repr(wrong_content)}")
    except:
        print("错误密钥解密结果无法读取（乱码）")
    
    # 清理
    for filename in [original_file, encrypted_file, decrypted_file, wrong_key_file]:
        if os.path.exists(filename):
            os.remove(filename)
    print("已清理临时文件")

file_encryption_demo()

# 练习 3.3: 对象序列化与反序列化
print("\n\n练习 3.3: 对象序列化与反序列化")

class Student:
    """学生类"""
    
    def __init__(self, student_id: int, name: str, age: int):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = []
        self.grades = {}
    
    def add_course(self, course_name: str):
        """添加课程"""
        if course_name not in self.courses:
            self.courses.append(course_name)
    
    def add_grade(self, course_name: str, grade: float):
        """添加成绩"""
        self.grades[course_name] = grade
    
    def calculate_average(self) -> float:
        """计算平均分"""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def display_info(self) -> str:
        """显示学生信息"""
        avg_grade = self.calculate_average()
        return f"学生ID: {self.student_id}, 姓名: {self.name}, 年龄: {self.age}, 平均分: {avg_grade:.2f}"
    
    def to_dict(self) -> dict:
        """转换为字典（用于JSON序列化）"""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'courses': self.courses,
            'grades': self.grades
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """从字典创建学生对象"""
        student = cls(data['student_id'], data['name'], data['age'])
        student.courses = data.get('courses', [])
        student.grades = data.get('grades', {})
        return student
    
    def __repr__(self):
        return f"Student({self.student_id}, '{self.name}', {self.age})"

class ObjectSerializer:
    """对象序列化器"""
    
    @staticmethod
    def serialize_with_pickle(objects: list, filename: str) -> bool:
        """使用pickle序列化对象"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(objects, f)
            return True
        except Exception as e:
            print(f"Pickle序列化失败: {e}")
            return False
    
    @staticmethod
    def deserialize_with_pickle(filename: str) -> list:
        """使用pickle反序列化对象"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            print(f"Pickle反序列化失败: {e}")
            return []
    
    @staticmethod
    def serialize_with_json(objects: list, filename: str) -> bool:
        """使用JSON序列化对象"""
        try:
            # 转换对象为字典
            data = [obj.to_dict() if hasattr(obj, 'to_dict') else obj for obj in objects]
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"JSON序列化失败: {e}")
            return False
    
    @staticmethod
    def deserialize_with_json(filename: str, object_class=None) -> list:
        """使用JSON反序列化对象"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 如果提供了对象类，尝试重建对象
            if object_class and hasattr(object_class, 'from_dict'):
                return [object_class.from_dict(item) for item in data]
            else:
                return data
                
        except Exception as e:
            print(f"JSON反序列化失败: {e}")
            return []

def object_serialization_demo():
    """对象序列化演示"""
    print("对象序列化与反序列化演示")
    
    # 创建学生对象
    students = [
        Student(1, "张三", 20),
        Student(2, "李四", 21),
        Student(3, "王五", 19),
        Student(4, "赵六", 22)
    ]
    
    # 添加课程和成绩
    courses = ["Python编程", "数据结构", "算法设计", "数据库原理"]
    
    for student in students:
        for course in courses:
            student.add_course(course)
            # 随机生成成绩
            import random
            grade = random.uniform(75, 95)
            student.add_grade(course, grade)
    
    print(f"创建了{len(students)}个学生对象")
    for student in students:
        print(f"  {student.display_info()}")
    
    # Pickle序列化
    print("\n1. Pickle序列化测试")
    pickle_file = 'students.pickle'
    
    if ObjectSerializer.serialize_with_pickle(students, pickle_file):
        print(f"Pickle序列化成功: {pickle_file}")
        
        # 反序列化
        loaded_students = ObjectSerializer.deserialize_with_pickle(pickle_file)
        print(f"Pickle反序列化成功，加载了{len(loaded_students)}个对象")
        
        # 验证对象完整性
        if loaded_students and hasattr(loaded_students[0], 'display_info'):
            print(f"第一个学生信息: {loaded_students[0].display_info()}")
        
        # 文件大小
        file_size = os.path.getsize(pickle_file)
        print(f"Pickle文件大小: {file_size} 字节")
    
    # JSON序列化
    print("\n2. JSON序列化测试")
    json_file = 'students.json'
    
    if ObjectSerializer.serialize_with_json(students, json_file):
        print(f"JSON序列化成功: {json_file}")
        
        # 反序列化
        loaded_data = ObjectSerializer.deserialize_with_json(json_file, Student)
        print(f"JSON反序列化成功，加载了{len(loaded_data)}个对象")
        
        # 验证对象完整性
        if loaded_data and hasattr(loaded_data[0], 'display_info'):
            print(f"第一个学生信息: {loaded_data[0].display_info()}")
        
        # 文件大小
        file_size = os.path.getsize(json_file)
        print(f"JSON文件大小: {file_size} 字节")
    
    # 比较两种方法
    print("\n3. 序列化方法比较")
    print("Pickle优点:")
    print("  - 可以序列化几乎所有Python对象")
    print("  - 保持对象的完整性（包括方法）")
    print("  - 文件通常更小")
    print("Pickle缺点:")
    print("  - 只能在Python中使用")
    print("  - 存在安全风险（不要加载不信任的pickle文件）")
    print("  - 不可读")
    
    print("\nJSON优点:")
    print("  - 跨语言兼容")
    print("  - 人类可读")
    print("  - 安全")
    print("JSON缺点:")
    print("  - 只能序列化基本数据类型")
    print("  - 需要自定义转换方法")
    print("  - 不保持对象方法")
    
    # 清理
    for filename in [pickle_file, json_file]:
        if os.path.exists(filename):
            os.remove(filename)
    print("\n已清理临时文件")

object_serialization_demo()

# ============================================================================
# 4. 文件系统操作练习答案
# ============================================================================

print("\n\n4. 文件系统操作练习答案")
print("-" * 30)

# 练习 4.1: 文件系统浏览器
print("\n练习 4.1: 文件系统浏览器")

class FileExplorer:
    """简单的文件系统浏览器"""
    
    def __init__(self, start_dir: str = '.'):
        self.current_dir = Path(start_dir).resolve()
        self.running = True
    
    def run(self):
        """运行文件浏览器"""
        print("文件系统浏览器")
        print("命令: ls(列出), cd <dir>(进入目录), up(上级目录), info <file>(文件信息), search <pattern>(搜索), quit(退出)")
        
        while self.running:
            try:
                print(f"\n当前目录: {self.current_dir}")
                command = input("请输入命令: ").strip().split()
                
                if not command:
                    continue
                
                cmd = command[0].lower()
                
                if cmd == 'ls':
                    self.list_directory()
                elif cmd == 'cd' and len(command) > 1:
                    self.change_directory(command[1])
                elif cmd == 'up':
                    self.go_up()
                elif cmd == 'info' and len(command) > 1:
                    self.show_file_info(command[1])
                elif cmd == 'search' and len(command) > 1:
                    self.search_files(command[1])
                elif cmd == 'quit':
                    self.running = False
                else:
                    print("无效命令或缺少参数")
                    
            except KeyboardInterrupt:
                print("\n退出文件浏览器")
                break
            except Exception as e:
                print(f"错误: {e}")
    
    def list_directory(self):
        """列出当前目录内容"""
        try:
            items = list(self.current_dir.iterdir())
            items.sort(key=lambda x: (x.is_file(), x.name.lower()))
            
            print(f"\n目录内容 ({len(items)} 项):")
            for item in items:
                if item.is_dir():
                    print(f"  📁 {item.name}/")
                else:
                    size = item.stat().st_size
                    print(f"  📄 {item.name} ({self._format_size(size)})")
                    
        except PermissionError:
            print("没有权限访问此目录")
    
    def change_directory(self, dirname: str):
        """切换目录"""
        try:
            new_dir = self.current_dir / dirname
            if new_dir.exists() and new_dir.is_dir():
                self.current_dir = new_dir.resolve()
                print(f"已进入目录: {self.current_dir}")
            else:
                print(f"目录不存在: {dirname}")
        except Exception as e:
            print(f"无法进入目录: {e}")
    
    def go_up(self):
        """返回上级目录"""
        parent = self.current_dir.parent
        if parent != self.current_dir:  # 不是根目录
            self.current_dir = parent
            print(f"已返回上级目录: {self.current_dir}")
        else:
            print("已在根目录")
    
    def show_file_info(self, filename: str):
        """显示文件详细信息"""
        try:
            file_path = self.current_dir / filename
            if not file_path.exists():
                print(f"文件不存在: {filename}")
                return
            
            stat = file_path.stat()
            print(f"\n文件信息: {filename}")
            print(f"  路径: {file_path}")
            print(f"  类型: {'目录' if file_path.is_dir() else '文件'}")
            print(f"  大小: {self._format_size(stat.st_size)}")
            print(f"  创建时间: {datetime.fromtimestamp(stat.st_ctime)}")
            print(f"  修改时间: {datetime.fromtimestamp(stat.st_mtime)}")
            print(f"  访问时间: {datetime.fromtimestamp(stat.st_atime)}")
            
            if file_path.is_file():
                # 尝试确定文件类型
                mime_type, _ = mimetypes.guess_type(str(file_path))
                if mime_type:
                    print(f"  MIME类型: {mime_type}")
                
                # 如果是文本文件，显示前几行
                if mime_type and mime_type.startswith('text'):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lines = f.readlines()[:5]
                        print(f"  内容预览 (前5行):")
                        for i, line in enumerate(lines, 1):
                            print(f"    {i}: {line.rstrip()}")
                    except:
                        print("  无法预览文件内容")
                        
        except Exception as e:
            print(f"获取文件信息失败: {e}")
    
    def search_files(self, pattern: str):
        """搜索文件"""
        try:
            print(f"\n搜索模式: {pattern}")
            matches = []
            
            # 在当前目录及子目录中搜索
            for item in self.current_dir.rglob('*'):
                if pattern.lower() in item.name.lower():
                    matches.append(item)
            
            if matches:
                print(f"找到 {len(matches)} 个匹配项:")
                for match in matches[:20]:  # 限制显示数量
                    rel_path = match.relative_to(self.current_dir)
                    item_type = "📁" if match.is_dir() else "📄"
                    print(f"  {item_type} {rel_path}")
                
                if len(matches) > 20:
                    print(f"  ... 还有 {len(matches) - 20} 个匹配项")
            else:
                print("未找到匹配的文件")
                
        except Exception as e:
            print(f"搜索失败: {e}")
    
    def _format_size(self, size: int) -> str:
        """格式化文件大小"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

def file_explorer_demo():
    """文件浏览器演示（非交互式）"""
    print("文件系统浏览器演示")
    
    # 创建测试目录结构
    test_dir = Path('test_explorer')
    test_dir.mkdir(exist_ok=True)
    
    # 创建子目录和文件
    (test_dir / 'subdir1').mkdir(exist_ok=True)
    (test_dir / 'subdir2').mkdir(exist_ok=True)
    
    (test_dir / 'file1.txt').write_text('这是测试文件1')
    (test_dir / 'file2.py').write_text('print("Hello, World!")')
    (test_dir / 'subdir1' / 'nested_file.md').write_text('# 嵌套文件')
    
    # 创建浏览器实例
    explorer = FileExplorer(str(test_dir))
    
    print(f"\n演示目录结构: {test_dir}")
    explorer.list_directory()
    
    print("\n文件信息演示:")
    explorer.show_file_info('file1.txt')
    
    print("\n搜索演示:")
    explorer.search_files('file')
    
    # 清理
    shutil.rmtree(test_dir)
    print(f"\n已清理测试目录: {test_dir}")
    
    print("\n注意: 在实际使用中，可以调用 explorer.run() 进入交互模式")

file_explorer_demo()

# 练习 4.2: 目录同步工具
print("\n\n练习 4.2: 目录同步工具")

class DirectorySynchronizer:
    """目录同步工具"""
    
    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.sync_log = []
    
    def sync(self, delete_extra: bool = False) -> dict:
        """同步目录
        
        Args:
            delete_extra: 是否删除目标目录中多余的文件
            
        Returns:
            同步结果统计
        """
        stats = {
            'copied': 0,
            'updated': 0,
            'deleted': 0,
            'errors': 0
        }
        
        try:
            # 确保目标目录存在
            self.target_dir.mkdir(parents=True, exist_ok=True)
            
            # 同步源目录到目标目录
            self._sync_directory(self.source_dir, self.target_dir, stats)
            
            # 删除目标目录中多余的文件
            if delete_extra:
                self._delete_extra_files(self.source_dir, self.target_dir, stats)
            
        except Exception as e:
            self.sync_log.append(f"同步失败: {e}")
            stats['errors'] += 1
        
        return stats
    
    def _sync_directory(self, source: Path, target: Path, stats: dict):
        """递归同步目录"""
        for source_item in source.iterdir():
            target_item = target / source_item.name
            
            try:
                if source_item.is_dir():
                    # 创建目录
                    target_item.mkdir(exist_ok=True)
                    # 递归同步子目录
                    self._sync_directory(source_item, target_item, stats)
                else:
                    # 同步文件
                    self._sync_file(source_item, target_item, stats)
                    
            except Exception as e:
                self.sync_log.append(f"同步 {source_item} 失败: {e}")
                stats['errors'] += 1
    
    def _sync_file(self, source_file: Path, target_file: Path, stats: dict):
        """同步单个文件"""
        try:
            # 检查目标文件是否存在
            if not target_file.exists():
                # 复制新文件
                shutil.copy2(source_file, target_file)
                self.sync_log.append(f"复制: {source_file} -> {target_file}")
                stats['copied'] += 1
            else:
                # 比较文件修改时间和大小
                source_stat = source_file.stat()
                target_stat = target_file.stat()
                
                if (source_stat.st_mtime > target_stat.st_mtime or 
                    source_stat.st_size != target_stat.st_size):
                    # 更新文件
                    shutil.copy2(source_file, target_file)
                    self.sync_log.append(f"更新: {source_file} -> {target_file}")
                    stats['updated'] += 1
                    
        except Exception as e:
            self.sync_log.append(f"同步文件 {source_file} 失败: {e}")
            stats['errors'] += 1
    
    def _delete_extra_files(self, source: Path, target: Path, stats: dict):
        """删除目标目录中多余的文件"""
        try:
            for target_item in target.iterdir():
                source_item = source / target_item.name
                
                if not source_item.exists():
                    # 删除多余的文件或目录
                    if target_item.is_dir():
                        shutil.rmtree(target_item)
                    else:
                        target_item.unlink()
                    
                    self.sync_log.append(f"删除: {target_item}")
                    stats['deleted'] += 1
                elif target_item.is_dir() and source_item.is_dir():
                    # 递归处理子目录
                    self._delete_extra_files(source_item, target_item, stats)
                    
        except Exception as e:
            self.sync_log.append(f"删除多余文件失败: {e}")
            stats['errors'] += 1
    
    def get_sync_log(self) -> list:
        """获取同步日志"""
        return self.sync_log.copy()
    
    def clear_log(self):
        """清空同步日志"""
        self.sync_log.clear()

def directory_sync_demo():
    """目录同步演示"""
    print("目录同步工具演示")
    
    # 创建源目录和文件
    source_dir = Path('sync_source')
    target_dir = Path('sync_target')
    
    # 清理旧的测试目录
    for dir_path in [source_dir, target_dir]:
        if dir_path.exists():
            shutil.rmtree(dir_path)
    
    # 创建源目录结构
    source_dir.mkdir()
    (source_dir / 'subdir1').mkdir()
    (source_dir / 'subdir2').mkdir()
    
    # 创建测试文件
    (source_dir / 'file1.txt').write_text('文件1内容')
    (source_dir / 'file2.txt').write_text('文件2内容')
    (source_dir / 'subdir1' / 'nested1.txt').write_text('嵌套文件1')
    (source_dir / 'subdir2' / 'nested2.txt').write_text('嵌套文件2')
    
    print(f"已创建源目录: {source_dir}")
    
    # 第一次同步
    print("\n1. 首次同步")
    synchronizer = DirectorySynchronizer(str(source_dir), str(target_dir))
    stats = synchronizer.sync()
    
    print(f"同步结果: {stats}")
    print("同步日志:")
    for log_entry in synchronizer.get_sync_log():
        print(f"  {log_entry}")
    
    # 验证目标目录
    print(f"\n目标目录内容:")
    for item in target_dir.rglob('*'):
        if item.is_file():
            rel_path = item.relative_to(target_dir)
            print(f"  📄 {rel_path}")
    
    # 修改源文件
    print("\n2. 修改源文件后再次同步")
    import time
    time.sleep(1)  # 确保修改时间不同
    
    (source_dir / 'file1.txt').write_text('文件1修改后的内容')
    (source_dir / 'new_file.txt').write_text('新文件内容')
    
    synchronizer.clear_log()
    stats = synchronizer.sync()
    
    print(f"同步结果: {stats}")
    print("同步日志:")
    for log_entry in synchronizer.get_sync_log():
        print(f"  {log_entry}")
    
    # 在目标目录添加额外文件
    print("\n3. 测试删除多余文件")
    (target_dir / 'extra_file.txt').write_text('多余文件')
    
    synchronizer.clear_log()
    stats = synchronizer.sync(delete_extra=True)
    
    print(f"同步结果: {stats}")
    print("同步日志:")
    for log_entry in synchronizer.get_sync_log():
        print(f"  {log_entry}")
    
    # 清理
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)
    print("\n已清理测试目录")

directory_sync_demo()

# ============================================================================
# 5. 高级文件操作练习答案
# ============================================================================

print("\n\n5. 高级文件操作练习答案")
print("-" * 30)

# 练习 5.1: 大文件处理器
print("\n练习 5.1: 大文件处理器")

class LargeFileProcessor:
    """大文件处理器"""
    
    def __init__(self, chunk_size: int = 8192):
        self.chunk_size = chunk_size
    
    def split_file(self, input_file: str, chunk_size_mb: int = 10) -> list:
        """分割大文件
        
        Args:
            input_file: 输入文件路径
            chunk_size_mb: 每个分块的大小（MB）
            
        Returns:
            分块文件列表
        """
        chunk_size_bytes = chunk_size_mb * 1024 * 1024
        chunk_files = []
        
        try:
            input_path = Path(input_file)
            base_name = input_path.stem
            extension = input_path.suffix
            
            with open(input_file, 'rb') as infile:
                chunk_num = 0
                
                while True:
                    chunk_data = infile.read(chunk_size_bytes)
                    if not chunk_data:
                        break
                    
                    chunk_filename = f"{base_name}.part{chunk_num:03d}{extension}"
                    chunk_files.append(chunk_filename)
                    
                    with open(chunk_filename, 'wb') as chunk_file:
                        chunk_file.write(chunk_data)
                    
                    chunk_num += 1
                    print(f"创建分块: {chunk_filename} ({len(chunk_data)} 字节)")
            
            return chunk_files
            
        except Exception as e:
            print(f"分割文件失败: {e}")
            return []
    
    def merge_files(self, chunk_files: list, output_file: str) -> bool:
        """合并分块文件
        
        Args:
            chunk_files: 分块文件列表
            output_file: 输出文件路径
            
        Returns:
            是否成功
        """
        try:
            with open(output_file, 'wb') as outfile:
                for chunk_file in chunk_files:
                    if not Path(chunk_file).exists():
                        print(f"分块文件不存在: {chunk_file}")
                        return False
                    
                    with open(chunk_file, 'rb') as infile:
                        while True:
                            chunk = infile.read(self.chunk_size)
                            if not chunk:
                                break
                            outfile.write(chunk)
                    
                    print(f"合并分块: {chunk_file}")
            
            return True
            
        except Exception as e:
            print(f"合并文件失败: {e}")
            return False
    
    def calculate_file_hash(self, filename: str, algorithm: str = 'md5') -> str:
        """计算文件哈希值
        
        Args:
            filename: 文件路径
            algorithm: 哈希算法 (md5, sha1, sha256)
            
        Returns:
            哈希值
        """
        import hashlib
        
        try:
            if algorithm == 'md5':
                hasher = hashlib.md5()
            elif algorithm == 'sha1':
                hasher = hashlib.sha1()
            elif algorithm == 'sha256':
                hasher = hashlib.sha256()
            else:
                raise ValueError(f"不支持的哈希算法: {algorithm}")
            
            with open(filename, 'rb') as f:
                while True:
                    chunk = f.read(self.chunk_size)
                    if not chunk:
                        break
                    hasher.update(chunk)
            
            return hasher.hexdigest()
            
        except Exception as e:
            print(f"计算哈希失败: {e}")
            return ""
    
    def verify_file_integrity(self, original_file: str, restored_file: str) -> bool:
        """验证文件完整性"""
        try:
            original_hash = self.calculate_file_hash(original_file)
            restored_hash = self.calculate_file_hash(restored_file)
            
            return original_hash == restored_hash and original_hash != ""
            
        except Exception:
            return False

def large_file_demo():
    """大文件处理演示"""
    print("大文件处理器演示")
    
    # 创建一个较大的测试文件
    test_file = 'large_test_file.txt'
    print(f"创建测试文件: {test_file}")
    
    # 生成测试数据（约1MB）
    test_data = "这是测试数据行。" * 1000 + "\n"
    with open(test_file, 'w', encoding='utf-8') as f:
        for i in range(100):  # 约100KB
            f.write(f"第{i+1}行: {test_data}")
    
    file_size = os.path.getsize(test_file)
    print(f"测试文件大小: {file_size / 1024:.1f} KB")
    
    # 创建处理器
    processor = LargeFileProcessor()
    
    # 计算原始文件哈希
    original_hash = processor.calculate_file_hash(test_file)
    print(f"原始文件MD5: {original_hash}")
    
    # 分割文件
    print("\n分割文件:")
    chunk_files = processor.split_file(test_file, chunk_size_mb=1)  # 1MB分块
    
    if chunk_files:
        print(f"文件已分割为 {len(chunk_files)} 个分块")
        
        # 显示分块信息
        total_chunk_size = 0
        for chunk_file in chunk_files:
            chunk_size = os.path.getsize(chunk_file)
            total_chunk_size += chunk_size
            print(f"  {chunk_file}: {chunk_size} 字节")
        
        print(f"分块总大小: {total_chunk_size} 字节")
        
        # 合并文件
        print("\n合并文件:")
        restored_file = 'restored_file.txt'
        success = processor.merge_files(chunk_files, restored_file)
        
        if success:
            print(f"文件合并成功: {restored_file}")
            
            # 验证完整性
            restored_hash = processor.calculate_file_hash(restored_file)
            print(f"恢复文件MD5: {restored_hash}")
            
            if processor.verify_file_integrity(test_file, restored_file):
                print("✓ 文件完整性验证成功")
            else:
                print("✗ 文件完整性验证失败")
            
            # 比较文件大小
            original_size = os.path.getsize(test_file)
            restored_size = os.path.getsize(restored_file)
            print(f"原始文件大小: {original_size} 字节")
            print(f"恢复文件大小: {restored_size} 字节")
        
        # 清理分块文件
        for chunk_file in chunk_files:
            if os.path.exists(chunk_file):
                os.remove(chunk_file)
        print("\n已清理分块文件")
        
        # 清理测试文件
        if os.path.exists(restored_file):
            os.remove(restored_file)
    
    # 清理原始测试文件
    os.remove(test_file)
    print("已清理测试文件")

large_file_demo()

# 练习 5.2: 文件监控器
print("\n\n练习 5.2: 文件监控器")

class FileMonitor:
    """简单的文件监控器"""
    
    def __init__(self, watch_directory: str):
        self.watch_directory = Path(watch_directory)
        self.file_states = {}
        self.monitoring = False
        self.callbacks = {
            'created': [],
            'modified': [],
            'deleted': []
        }
    
    def add_callback(self, event_type: str, callback):
        """添加事件回调函数
        
        Args:
            event_type: 事件类型 ('created', 'modified', 'deleted')
            callback: 回调函数，接收文件路径作为参数
        """
        if event_type in self.callbacks:
            self.callbacks[event_type].append(callback)
    
    def scan_directory(self) -> dict:
        """扫描目录，返回当前文件状态"""
        current_states = {}
        
        try:
            if self.watch_directory.exists():
                for file_path in self.watch_directory.rglob('*'):
                    if file_path.is_file():
                        stat = file_path.stat()
                        current_states[str(file_path)] = {
                            'size': stat.st_size,
                            'mtime': stat.st_mtime
                        }
        except Exception as e:
            print(f"扫描目录失败: {e}")
        
        return current_states
    
    def detect_changes(self):
        """检测文件变化"""
        current_states = self.scan_directory()
        
        # 检测新文件和修改的文件
        for file_path, current_state in current_states.items():
            if file_path not in self.file_states:
                # 新文件
                self._trigger_callbacks('created', file_path)
            else:
                # 检查是否修改
                old_state = self.file_states[file_path]
                if (current_state['size'] != old_state['size'] or 
                    current_state['mtime'] != old_state['mtime']):
                    self._trigger_callbacks('modified', file_path)
        
        # 检测删除的文件
        for file_path in self.file_states:
            if file_path not in current_states:
                self._trigger_callbacks('deleted', file_path)
        
        # 更新文件状态
        self.file_states = current_states
    
    def _trigger_callbacks(self, event_type: str, file_path: str):
        """触发回调函数"""
        for callback in self.callbacks[event_type]:
            try:
                callback(file_path)
            except Exception as e:
                print(f"回调函数执行失败: {e}")
    
    def start_monitoring(self, interval: float = 1.0):
        """开始监控（简化版，使用轮询）
        
        Args:
            interval: 检查间隔（秒）
        """
        import time
        
        self.monitoring = True
        print(f"开始监控目录: {self.watch_directory}")
        
        # 初始扫描
        self.file_states = self.scan_directory()
        
        try:
            while self.monitoring:
                time.sleep(interval)
                self.detect_changes()
        except KeyboardInterrupt:
            print("\n监控已停止")
        finally:
            self.monitoring = False
    
    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False

def file_monitor_demo():
    """文件监控器演示"""
    print("文件监控器演示")
    
    # 创建监控目录
    watch_dir = Path('monitor_test')
    watch_dir.mkdir(exist_ok=True)
    
    # 创建监控器
    monitor = FileMonitor(str(watch_dir))
    
    # 添加回调函数
    def on_file_created(file_path):
        print(f"📄 文件创建: {Path(file_path).name}")
    
    def on_file_modified(file_path):
        print(f"✏️ 文件修改: {Path(file_path).name}")
    
    def on_file_deleted(file_path):
        print(f"🗑️ 文件删除: {Path(file_path).name}")
    
    monitor.add_callback('created', on_file_created)
    monitor.add_callback('modified', on_file_modified)
    monitor.add_callback('deleted', on_file_deleted)
    
    # 模拟文件操作
    print("\n模拟文件操作:")
    
    # 初始扫描
    monitor.file_states = monitor.scan_directory()
    print(f"初始文件数量: {len(monitor.file_states)}")
    
    # 创建文件
    test_file1 = watch_dir / 'test1.txt'
    test_file1.write_text('测试文件1')
    monitor.detect_changes()
    
    # 修改文件
    import time
    time.sleep(0.1)  # 确保修改时间不同
    test_file1.write_text('测试文件1 - 已修改')
    monitor.detect_changes()
    
    # 创建另一个文件
    test_file2 = watch_dir / 'test2.txt'
    test_file2.write_text('测试文件2')
    monitor.detect_changes()
    
    # 删除文件
    test_file1.unlink()
    monitor.detect_changes()
    
    # 清理
    shutil.rmtree(watch_dir)
    print("\n已清理测试目录")
    
    print("\n注意: 在实际使用中，可以调用 monitor.start_monitoring() 进入持续监控模式")

file_monitor_demo()

# ============================================================================
# 6. 综合应用练习答案
# ============================================================================

print("\n\n6. 综合应用练习答案")
print("-" * 30)

# 练习 6.1: 文件管理系统
print("\n练习 6.1: 文件管理系统")

class FileManager:
    """文件管理系统"""
    
    def __init__(self, base_directory: str):
        self.base_dir = Path(base_directory)
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.operation_log = []
    
    def create_file(self, filename: str, content: str = "") -> bool:
        """创建文件"""
        try:
            file_path = self.base_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self._log_operation(f"创建文件: {filename}")
            return True
            
        except Exception as e:
            self._log_operation(f"创建文件失败 {filename}: {e}")
            return False
    
    def read_file(self, filename: str) -> str:
        """读取文件内容"""
        try:
            file_path = self.base_dir / filename
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self._log_operation(f"读取文件: {filename}")
            return content
            
        except Exception as e:
            self._log_operation(f"读取文件失败 {filename}: {e}")
            return ""
    
    def update_file(self, filename: str, content: str) -> bool:
        """更新文件内容"""
        try:
            file_path = self.base_dir / filename
            if not file_path.exists():
                self._log_operation(f"更新文件失败 {filename}: 文件不存在")
                return False
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self._log_operation(f"更新文件: {filename}")
            return True
            
        except Exception as e:
            self._log_operation(f"更新文件失败 {filename}: {e}")
            return False
    
    def delete_file(self, filename: str) -> bool:
        """删除文件"""
        try:
            file_path = self.base_dir / filename
            if file_path.exists():
                file_path.unlink()
                self._log_operation(f"删除文件: {filename}")
                return True
            else:
                self._log_operation(f"删除文件失败 {filename}: 文件不存在")
                return False
                
        except Exception as e:
            self._log_operation(f"删除文件失败 {filename}: {e}")
            return False
    
    def list_files(self, pattern: str = "*") -> list:
        """列出文件"""
        try:
            files = []
            for file_path in self.base_dir.rglob(pattern):
                if file_path.is_file():
                    rel_path = file_path.relative_to(self.base_dir)
                    files.append(str(rel_path))
            
            self._log_operation(f"列出文件: {pattern} (找到 {len(files)} 个文件)")
            return sorted(files)
            
        except Exception as e:
            self._log_operation(f"列出文件失败: {e}")
            return []
    
    def search_files(self, keyword: str) -> list:
        """搜索文件内容"""
        results = []
        
        try:
            for file_path in self.base_dir.rglob('*.txt'):
                if file_path.is_file():
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        if keyword.lower() in content.lower():
                            rel_path = file_path.relative_to(self.base_dir)
                            results.append(str(rel_path))
                            
                    except Exception:
                        continue  # 跳过无法读取的文件
            
            self._log_operation(f"搜索关键词 '{keyword}': 找到 {len(results)} 个文件")
            return results
            
        except Exception as e:
            self._log_operation(f"搜索失败: {e}")
            return []
    
    def backup_files(self, backup_dir: str) -> bool:
        """备份文件"""
        try:
            backup_path = Path(backup_dir)
            backup_path.mkdir(parents=True, exist_ok=True)
            
            # 创建时间戳目录
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_subdir = backup_path / f"backup_{timestamp}"
            
            # 复制整个目录
            shutil.copytree(self.base_dir, backup_subdir)
            
            self._log_operation(f"备份完成: {backup_subdir}")
            return True
            
        except Exception as e:
            self._log_operation(f"备份失败: {e}")
            return False
    
    def get_file_info(self, filename: str) -> dict:
        """获取文件信息"""
        try:
            file_path = self.base_dir / filename
            if not file_path.exists():
                return {}
            
            stat = file_path.stat()
            info = {
                'name': filename,
                'size': stat.st_size,
                'created': datetime.fromtimestamp(stat.st_ctime),
                'modified': datetime.fromtimestamp(stat.st_mtime),
                'is_directory': file_path.is_dir()
            }
            
            if file_path.is_file():
                # 尝试获取MIME类型
                mime_type, _ = mimetypes.guess_type(str(file_path))
                info['mime_type'] = mime_type
            
            self._log_operation(f"获取文件信息: {filename}")
            return info
            
        except Exception as e:
            self._log_operation(f"获取文件信息失败 {filename}: {e}")
            return {}
    
    def _log_operation(self, message: str):
        """记录操作日志"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.operation_log.append(log_entry)
        
        # 限制日志大小
        if len(self.operation_log) > 1000:
            self.operation_log = self.operation_log[-500:]
    
    def get_operation_log(self, limit: int = 50) -> list:
        """获取操作日志"""
        return self.operation_log[-limit:]
    
    def export_log(self, log_file: str) -> bool:
        """导出操作日志"""
        try:
            with open(log_file, 'w', encoding='utf-8') as f:
                for log_entry in self.operation_log:
                    f.write(log_entry + '\n')
            return True
        except Exception:
            return False

def file_manager_demo():
    """文件管理系统演示"""
    print("文件管理系统演示")
    
    # 创建文件管理器
    manager = FileManager('file_manager_test')
    
    # 创建文件
    print("\n1. 创建文件")
    manager.create_file('documents/readme.txt', '这是一个README文件\n包含项目说明')
    manager.create_file('documents/notes.txt', '学习笔记\nPython文件操作')
    manager.create_file('scripts/hello.py', 'print("Hello, World!")')
    manager.create_file('data/config.json', '{"debug": true, "version": "1.0"}')
    
    # 列出文件
    print("\n2. 列出所有文件")
    files = manager.list_files()
    for file in files:
        print(f"  📄 {file}")
    
    # 读取文件
    print("\n3. 读取文件内容")
    content = manager.read_file('documents/readme.txt')
    print(f"readme.txt 内容:\n{content}")
    
    # 更新文件
    print("\n4. 更新文件")
    new_content = content + "\n\n更新时间: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    manager.update_file('documents/readme.txt', new_content)
    
    # 搜索文件
    print("\n5. 搜索文件内容")
    search_results = manager.search_files('Python')
    print(f"包含'Python'的文件: {search_results}")
    
    # 获取文件信息
    print("\n6. 获取文件信息")
    file_info = manager.get_file_info('documents/readme.txt')
    if file_info:
        print(f"文件信息:")
        for key, value in file_info.items():
            print(f"  {key}: {value}")
    
    # 备份文件
    print("\n7. 备份文件")
    backup_success = manager.backup_files('backups')
    print(f"备份结果: {'成功' if backup_success else '失败'}")
    
    # 显示操作日志
    print("\n8. 操作日志")
    logs = manager.get_operation_log(10)
    for log in logs:
        print(f"  {log}")
    
    # 导出日志
    log_file = 'operation_log.txt'
    if manager.export_log(log_file):
        print(f"\n日志已导出到: {log_file}")
    
    # 清理
    shutil.rmtree('file_manager_test')
    if Path('backups').exists():
        shutil.rmtree('backups')
    if Path(log_file).exists():
        os.remove(log_file)
    print("\n已清理测试文件")

file_manager_demo()

print("\n" + "=" * 50)
print("文件操作练习题参考答案 - 完整版")
print("包含：基础文件操作、文本文件处理、二进制文件处理、")
print("      文件系统操作、高级文件操作、综合应用")
print("=" * 50)

# ============================================================================
# 文件操作学习要点总结
# ============================================================================

print("\n\n📚 文件操作学习要点总结")
print("=" * 50)

print("""
🎯 核心概念:
1. 文件对象和文件模式
2. 文本文件 vs 二进制文件
3. 文件编码处理
4. 路径操作和pathlib
5. 异常处理和资源管理

📖 基础操作:
1. 文件打开、读取、写入、关闭
2. 文件指针操作
3. 上下文管理器 (with语句)
4. 文件模式选择

📝 文本文件处理:
1. 编码处理 (UTF-8, GBK等)
2. CSV文件读写
3. JSON文件处理
4. 配置文件管理
5. 日志文件处理

🔧 二进制文件处理:
1. 字节操作
2. 文件格式解析
3. 序列化和反序列化
4. 文件加密解密
5. 图像和媒体文件处理

📁 文件系统操作:
1. 目录创建、删除、遍历
2. 文件复制、移动、重命名
3. 文件属性和权限
4. 路径操作和解析
5. 文件搜索和过滤

🚀 高级特性:
1. 大文件处理和分块操作
2. 文件监控和变化检测
3. 文件压缩和解压
4. 临时文件和文件锁
5. 异步文件操作

💡 最佳实践:
1. 始终使用with语句管理文件资源
2. 正确处理文件编码
3. 适当的异常处理
4. 大文件分块处理
5. 路径使用pathlib而非字符串拼接
6. 文件操作前检查权限和存在性
7. 敏感数据的安全处理
8. 定期备份重要文件

⚠️ 常见陷阱:
1. 忘记关闭文件句柄
2. 编码问题导致的乱码
3. 路径分隔符的跨平台问题
4. 文件权限不足
5. 大文件内存溢出
6. 并发访问冲突
7. 文件锁定问题

🎓 进阶学习:
1. 文件系统监控 (watchdog库)
2. 异步文件操作 (aiofiles)
3. 数据库文件操作
4. 网络文件系统
5. 文件版本控制
6. 文件同步和备份策略
""")

print("\n🎉 恭喜！你已经完成了Python文件操作的全面学习！")
print("继续练习和实践，掌握更多高级技巧！")