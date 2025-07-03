# 第五部分：数据结构

## 学习目标

通过本章学习，你将掌握：
- Python内置数据结构的使用（列表、元组、字典、集合）
- 各种数据结构的特点和适用场景
- 数据结构的常用操作和方法
- 数据结构的性能特点
- 高级数据结构的应用
- 数据结构的选择策略

## 1. 列表（List）

### 1.1 特点
- 有序、可变的序列
- 允许重复元素
- 支持不同类型的元素
- 使用方括号 `[]` 定义

### 1.2 基本操作
```python
# 创建列表
my_list = [1, 2, 3, 4, 5]
empty_list = []
mixed_list = [1, "hello", 3.14, True]

# 访问元素
first = my_list[0]  # 第一个元素
last = my_list[-1]  # 最后一个元素

# 切片
sublist = my_list[1:4]  # 获取子列表

# 修改元素
my_list[0] = 10

# 添加元素
my_list.append(6)        # 末尾添加
my_list.insert(0, 0)     # 指定位置插入
my_list.extend([7, 8])   # 扩展列表

# 删除元素
my_list.remove(10)       # 删除指定值
popped = my_list.pop()   # 删除并返回最后一个元素
del my_list[0]           # 删除指定位置
```

### 1.3 常用方法
- `len()`: 获取长度
- `count()`: 统计元素出现次数
- `index()`: 查找元素索引
- `sort()`: 原地排序
- `reverse()`: 原地反转
- `copy()`: 浅拷贝
- `clear()`: 清空列表

## 2. 元组（Tuple）

### 2.1 特点
- 有序、不可变的序列
- 允许重复元素
- 支持不同类型的元素
- 使用圆括号 `()` 定义
- 可以作为字典的键

### 2.2 基本操作
```python
# 创建元组
my_tuple = (1, 2, 3, 4, 5)
empty_tuple = ()
single_tuple = (1,)  # 单元素元组需要逗号

# 访问元素
first = my_tuple[0]
last = my_tuple[-1]

# 切片
subtuple = my_tuple[1:4]

# 元组解包
a, b, c = (1, 2, 3)

# 命名元组
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
```

### 2.3 使用场景
- 存储不可变的数据
- 函数返回多个值
- 作为字典的键
- 配置信息存储

## 3. 字典（Dictionary）

### 3.1 特点
- 无序（Python 3.7+保持插入顺序）
- 键值对存储
- 键必须是不可变类型
- 值可以是任意类型
- 使用花括号 `{}` 定义

### 3.2 基本操作
```python
# 创建字典
my_dict = {"name": "张三", "age": 25, "city": "北京"}
empty_dict = {}

# 访问元素
name = my_dict["name"]
age = my_dict.get("age", 0)  # 安全访问

# 修改和添加
my_dict["age"] = 26
my_dict["email"] = "zhang@example.com"

# 删除元素
del my_dict["city"]
popped = my_dict.pop("email")

# 遍历
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
```

### 3.3 常用方法
- `keys()`: 获取所有键
- `values()`: 获取所有值
- `items()`: 获取所有键值对
- `get()`: 安全获取值
- `setdefault()`: 设置默认值
- `update()`: 更新字典
- `clear()`: 清空字典

## 4. 集合（Set）

### 4.1 特点
- 无序、可变
- 元素唯一（自动去重）
- 元素必须是不可变类型
- 使用花括号 `{}` 或 `set()` 定义
- 支持数学集合运算

### 4.2 基本操作
```python
# 创建集合
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # 注意：{}创建的是空字典
from_list = set([1, 2, 2, 3, 3])  # 自动去重

# 添加元素
my_set.add(6)
my_set.update([7, 8, 9])

# 删除元素
my_set.remove(1)     # 元素不存在会报错
my_set.discard(10)   # 元素不存在不报错
popped = my_set.pop()  # 随机删除一个元素

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2        # 并集
intersection = set1 & set2  # 交集
difference = set1 - set2    # 差集
sym_diff = set1 ^ set2      # 对称差集
```

### 4.3 使用场景
- 去重
- 成员测试
- 集合运算
- 快速查找

## 5. 字符串（String）

### 5.1 特点
- 不可变序列
- 字符的有序集合
- 支持索引和切片
- 丰富的字符串方法

### 5.2 常用操作
```python
# 创建字符串
my_string = "Hello, World!"
multiline = """多行
字符串"""

# 字符串格式化
formatted = f"Hello, {name}!"
formatted = "Hello, {}!".format(name)
formatted = "Hello, %s!" % name

# 字符串方法
upper_str = my_string.upper()
lower_str = my_string.lower()
split_list = my_string.split(", ")
joined = "-".join(["a", "b", "c"])
```

## 6. 高级数据结构

### 6.1 collections模块
```python
from collections import (
    Counter,      # 计数器
    defaultdict,  # 默认字典
    OrderedDict,  # 有序字典
    deque,        # 双端队列
    namedtuple    # 命名元组
)

# Counter示例
counter = Counter([1, 2, 2, 3, 3, 3])
print(counter.most_common(2))  # 最常见的2个元素

# defaultdict示例
dd = defaultdict(list)
dd['key'].append('value')  # 自动创建列表

# deque示例
dq = deque([1, 2, 3])
dq.appendleft(0)  # 左侧添加
dq.append(4)      # 右侧添加
```

### 6.2 heapq模块（堆）
```python
import heapq

# 创建堆
heap = [3, 1, 4, 1, 5, 9, 2, 6]
heapq.heapify(heap)

# 堆操作
heapq.heappush(heap, 0)
smallest = heapq.heappop(heap)
```

## 7. 性能比较

### 7.1 时间复杂度
| 操作 | 列表 | 元组 | 字典 | 集合 |
|------|------|------|------|------|
| 访问 | O(1) | O(1) | O(1) | - |
| 搜索 | O(n) | O(n) | O(1) | O(1) |
| 插入 | O(n) | - | O(1) | O(1) |
| 删除 | O(n) | - | O(1) | O(1) |

### 7.2 内存使用
- 元组比列表更节省内存
- 字典和集合有额外的哈希表开销
- 字符串是不可变的，拼接会创建新对象

## 8. 数据结构选择指南

### 8.1 选择列表的情况
- 需要有序存储
- 需要修改元素
- 需要索引访问
- 允许重复元素

### 8.2 选择元组的情况
- 数据不需要修改
- 作为字典的键
- 函数返回多个值
- 节省内存

### 8.3 选择字典的情况
- 键值对存储
- 快速查找
- 数据关联
- 配置存储

### 8.4 选择集合的情况
- 去重需求
- 成员测试
- 集合运算
- 快速查找

## 9. 最佳实践

1. **选择合适的数据结构**：根据使用场景选择最适合的数据结构
2. **避免不必要的转换**：减少数据结构之间的转换
3. **使用推导式**：简洁高效地创建数据结构
4. **注意可变性**：理解可变和不可变数据结构的区别
5. **利用内置方法**：使用内置方法而不是手动实现
6. **考虑性能**：在性能敏感的场景下选择合适的数据结构
7. **使用类型提示**：提高代码可读性和维护性

## 10. 常见陷阱

1. **可变默认参数**：避免使用可变对象作为默认参数
2. **浅拷贝vs深拷贝**：理解拷贝的区别
3. **字典键的可变性**：字典键必须是不可变类型
4. **集合元素的可变性**：集合元素必须是不可变类型
5. **字符串拼接性能**：大量字符串拼接使用join()

## 练习建议

1. 完成`exercises.py`中的所有练习
2. 比较不同数据结构的性能
3. 实践各种数据结构的组合使用
4. 学习collections模块的高级数据结构
5. 解决实际的数据处理问题

## 下一步

掌握数据结构后，建议学习：
- 函数定义和高级特性
- 面向对象编程
- 文件操作和数据持久化
- 算法设计和优化

数据结构是编程的基础，熟练掌握它们对于编写高效、可维护的Python代码至关重要。