# 第四部分：控制结构

## 学习目标

通过本章学习，你将掌握：
- 条件语句的使用（if、elif、else）
- 循环语句的使用（for、while）
- 循环控制语句（break、continue、pass）
- 条件表达式（三元运算符）
- 嵌套控制结构
- 循环优化技巧

## 1. 条件语句

### 1.1 基本if语句
```python
if condition:
    # 条件为真时执行的代码
    pass
```

### 1.2 if-else语句
```python
if condition:
    # 条件为真时执行
    pass
else:
    # 条件为假时执行
    pass
```

### 1.3 if-elif-else语句
```python
if condition1:
    # 条件1为真时执行
    pass
elif condition2:
    # 条件2为真时执行
    pass
else:
    # 所有条件都为假时执行
    pass
```

### 1.4 条件表达式（三元运算符）
```python
result = value_if_true if condition else value_if_false
```

## 2. 循环语句

### 2.1 for循环

#### 遍历序列
```python
for item in sequence:
    # 处理每个元素
    pass
```

#### 使用range()
```python
for i in range(start, stop, step):
    # 使用索引
    pass
```

#### enumerate()函数
```python
for index, value in enumerate(sequence):
    # 同时获取索引和值
    pass
```

#### zip()函数
```python
for item1, item2 in zip(list1, list2):
    # 同时遍历多个序列
    pass
```

### 2.2 while循环
```python
while condition:
    # 条件为真时重复执行
    # 注意更新条件，避免无限循环
    pass
```

## 3. 循环控制语句

### 3.1 break语句
- 立即退出当前循环
- 只影响最内层循环

### 3.2 continue语句
- 跳过当前迭代的剩余部分
- 继续下一次迭代

### 3.3 pass语句
- 空操作语句
- 用作占位符

### 3.4 else子句
- for-else和while-else
- 循环正常结束时执行（没有被break中断）

## 4. 嵌套控制结构

### 4.1 嵌套循环
```python
for i in range(rows):
    for j in range(cols):
        # 处理二维数据
        pass
```

### 4.2 循环中的条件语句
```python
for item in items:
    if condition:
        # 处理满足条件的项
        pass
    else:
        # 处理不满足条件的项
        pass
```

## 5. 高级技巧

### 5.1 列表推导式
```python
result = [expression for item in iterable if condition]
```

### 5.2 字典推导式
```python
result = {key_expr: value_expr for item in iterable if condition}
```

### 5.3 集合推导式
```python
result = {expression for item in iterable if condition}
```

### 5.4 生成器表达式
```python
result = (expression for item in iterable if condition)
```

## 6. 性能优化

### 6.1 避免不必要的计算
- 将循环外的计算移到循环外
- 使用局部变量缓存频繁访问的属性

### 6.2 选择合适的数据结构
- 使用set进行成员测试
- 使用dict进行快速查找

### 6.3 使用内置函数
- any()和all()函数
- map()、filter()、reduce()函数

## 7. 常见模式

### 7.1 计数器模式
```python
count = 0
for item in items:
    if condition:
        count += 1
```

### 7.2 累加器模式
```python
total = 0
for item in items:
    total += item
```

### 7.3 查找模式
```python
found = False
for item in items:
    if item == target:
        found = True
        break
```

### 7.4 过滤模式
```python
result = []
for item in items:
    if condition:
        result.append(item)
```

## 8. 最佳实践

1. **避免无限循环**：确保循环条件会在某个时候变为False
2. **使用有意义的变量名**：让代码更易读
3. **避免过深的嵌套**：考虑提取函数或使用continue
4. **优先使用for循环**：当知道迭代次数时
5. **合理使用break和continue**：提高代码可读性
6. **利用Python的内置函数**：如any()、all()、sum()等
7. **使用推导式**：简洁且高效
8. **注意循环变量的作用域**：避免意外的变量泄露

## 9. 调试技巧

1. **添加打印语句**：观察循环变量的变化
2. **使用调试器**：逐步执行代码
3. **检查边界条件**：空序列、单元素序列等
4. **验证循环不变量**：确保循环逻辑正确

## 练习建议

1. 完成`exercises.py`中的所有练习
2. 尝试用不同的方法解决同一个问题
3. 比较不同方法的性能
4. 练习嵌套循环和复杂条件
5. 学习使用推导式重写循环

## 下一步

掌握控制结构后，建议学习：
- 函数定义和调用
- 数据结构（列表、字典、集合等）
- 异常处理
- 面向对象编程

控制结构是编程的基础，熟练掌握它们对于编写高效、可读的Python代码至关重要。