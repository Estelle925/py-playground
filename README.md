# Python基础知识学习大纲

## 环境配置
使用pyenv管理Python版本，建议使用Python 3.9+

```bash
# 安装pyenv (macOS)
brew install pyenv

# 安装Python 3.11
pyenv install 3.11.0
pyenv local 3.11.0

# 验证版本
python --version
```

## 学习大纲

### 第一部分：Python基础语法
1. **变量与数据类型** (`01_variables_and_types/`)
   - 基本数据类型：int, float, str, bool
   - 变量命名规则
   - 类型转换
   - 常量

2. **运算符** (`02_operators/`)
   - 算术运算符
   - 比较运算符
   - 逻辑运算符
   - 位运算符
   - 赋值运算符
   - 成员运算符
   - 身份运算符

3. **字符串操作** (`03_strings/`)
   - 字符串创建和访问
   - 字符串方法
   - 格式化字符串
   - 正则表达式基础

### 第二部分：控制结构
4. **条件语句** (`04_conditionals/`)
   - if, elif, else
   - 三元运算符
   - 嵌套条件

5. **循环结构** (`05_loops/`)
   - for循环
   - while循环
   - break和continue
   - 循环嵌套
   - 循环else子句

### 第三部分：数据结构
6. **列表(List)** (`06_lists/`)
   - 列表创建和访问
   - 列表方法
   - 列表推导式
   - 切片操作

7. **元组(Tuple)** (`07_tuples/`)
   - 元组特性
   - 元组操作
   - 命名元组

8. **字典(Dictionary)** (`08_dictionaries/`)
   - 字典创建和访问
   - 字典方法
   - 字典推导式

9. **集合(Set)** (`09_sets/`)
   - 集合创建和操作
   - 集合运算
   - 集合推导式

### 第四部分：函数
10. **函数基础** (`10_functions/`)
    - 函数定义和调用
    - 参数传递
    - 返回值
    - 作用域

11. **高级函数特性** (`11_advanced_functions/`)
    - 默认参数
    - 可变参数(*args, **kwargs)
    - 匿名函数(lambda)
    - 装饰器基础
    - 递归函数

### 第五部分：面向对象编程
12. **类和对象** (`12_classes_objects/`)
    - 类的定义
    - 实例化对象
    - 属性和方法
    - 构造函数和析构函数

13. **面向对象特性** (`13_oop_features/`)
    - 继承
    - 多态
    - 封装
    - 抽象类
    - 特殊方法(魔法方法)

### 第六部分：异常处理
14. **异常处理** (`14_exceptions/`)
    - try, except, else, finally
    - 异常类型
    - 自定义异常
    - 异常链

### 第七部分：文件操作
15. **文件I/O** (`15_file_io/`)
    - 文件读写
    - 文件模式
    - 上下文管理器(with语句)
    - 路径操作

### 第八部分：模块和包
16. **模块** (`16_modules/`)
    - 模块导入
    - 标准库模块
    - 自定义模块
    - __name__ == '__main__'

17. **包管理** (`17_packages/`)
    - 包的创建
    - __init__.py
    - 相对导入和绝对导入
    - pip包管理

### 第九部分：高级特性
18. **迭代器和生成器** (`18_iterators_generators/`)
    - 迭代器协议
    - 生成器函数
    - 生成器表达式
    - yield关键字

19. **装饰器** (`19_decorators/`)
    - 装饰器原理
    - 函数装饰器
    - 类装饰器
    - 带参数的装饰器

20. **上下文管理器** (`20_context_managers/`)
    - with语句
    - __enter__和__exit__方法
    - contextlib模块

### 第十部分：常用标准库
21. **常用标准库** (`21_standard_library/`)
    - datetime - 日期时间处理
    - os - 操作系统接口
    - sys - 系统相关参数
    - json - JSON数据处理
    - re - 正则表达式
    - collections - 特殊容器
    - itertools - 迭代工具
    - functools - 函数工具

### 第十一部分：调试和测试
22. **调试技巧** (`22_debugging/`)
    - print调试
    - pdb调试器
    - logging模块
    - 断言(assert)

23. **单元测试** (`23_testing/`)
    - unittest模块
    - pytest框架基础
    - 测试用例编写
    - 模拟(mock)

## 学习建议

1. **循序渐进**：按照大纲顺序学习，每个知识点都要动手实践
2. **多写代码**：理论结合实践，每个概念都要写代码验证
3. **项目实战**：学完基础后，尝试做一些小项目巩固知识
4. **阅读源码**：阅读优秀的Python代码，学习最佳实践
5. **持续练习**：定期回顾和练习，保持编程手感

## 推荐资源

- 官方文档：https://docs.python.org/3/
- Python教程：https://docs.python.org/3/tutorial/
- PEP 8 代码风格指南：https://pep8.org/
- Real Python：https://realpython.com/

## 项目结构说明

每个知识点目录包含：
- `README.md` - 知识点说明和理论
- `examples.py` - 基础示例代码
- `exercises.py` - 练习题
- `solutions.py` - 练习题答案
- `advanced.py` - 高级用法示例(部分章节)