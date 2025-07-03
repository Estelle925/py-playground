# 🐍 Python基础知识学习大纲

![Python Logo](assets/python-logo.svg)

一个系统性的Python学习项目，涵盖从基础语法到高级特性的完整知识体系。

## 🚀 快速开始

### 环境配置
使用pyenv管理Python版本，建议使用Python 3.9+

```bash
# 安装pyenv (macOS)
brew install pyenv

# 安装Python 3.11
pyenv install 3.11.0
pyenv local 3.11.0

# 验证版本
python --version

# 安装依赖
pip install -r requirements.txt

# 运行快速开始脚本
./setup_env.sh
```

### 项目特色

- 📚 **系统化学习路径** - 从基础到高级的完整知识体系
- 💻 **实践导向** - 每个模块都包含丰富的示例和练习
- 🧪 **测试驱动** - 完整的测试覆盖和验证机制
- 🔧 **工具集成** - 包含实用的工具模块和数据处理框架
- 📊 **可视化学习** - 每个模块都有对应的SVG图标和说明

## 📚 学习大纲

### 第一部分：Python基础语法

#### ![Variables Icon](assets/variables-icon.svg) 1. **变量与数据类型** (`01_variables_and_types/`)
   - 基本数据类型：int, float, str, bool
   - 变量命名规则和最佳实践
   - 类型转换和类型检查
   - 常量定义和使用
   - 内存管理基础

#### ![Operators Icon](assets/operators-icon.svg) 2. **运算符** (`02_operators/`)
   - 算术运算符 (+, -, *, /, //, %, **)
   - 比较运算符 (==, !=, <, >, <=, >=)
   - 逻辑运算符 (and, or, not)
   - 位运算符 (&, |, ^, ~, <<, >>)
   - 赋值运算符 (=, +=, -=, *=, /=)
   - 成员运算符 (in, not in)
   - 身份运算符 (is, is not)
   - 运算符优先级

#### ![Strings Icon](assets/strings-icon.svg) 3. **字符串操作** (`03_strings/`)
   - 字符串创建和访问
   - 字符串方法和属性
   - 格式化字符串 (f-strings, format, %)
   - 字符串编码和解码
   - 正则表达式基础

### 第二部分：控制结构

#### ![Control Icon](assets/control-icon.svg) 4. **控制结构** (`04_control_structures/`)
   - 条件语句 (if, elif, else)
   - 循环结构 (for, while)
   - 控制流语句 (break, continue, pass)
   - 三元运算符
   - 嵌套结构和最佳实践

### 第三部分：数据结构

#### ![Data Structures Icon](assets/data-structures-icon.svg) 5. **数据结构** (`05_data_structures/`)
   - 列表 (List) - 创建、访问、方法、推导式
   - 元组 (Tuple) - 特性、操作、命名元组
   - 字典 (Dictionary) - 创建、访问、方法、推导式
   - 集合 (Set) - 创建、操作、集合运算
   - 切片操作和高级技巧

### 第四部分：函数

#### ![Functions Icon](assets/functions-icon.svg) 6. **函数** (`06_functions/`)
   - 函数定义和调用
   - 参数传递 (位置参数、关键字参数)
   - 默认参数和可变参数 (*args, **kwargs)
   - 返回值和多返回值
   - 作用域和闭包
   - 匿名函数 (lambda)
   - 递归函数
   - 装饰器基础

### 第五部分：面向对象编程

#### ![OOP Icon](assets/oop-icon.svg) 7. **面向对象编程** (`07_oop/`)
   - 类和对象的概念
   - 类的定义和实例化
   - 属性和方法
   - 构造函数和析构函数
   - 继承和多继承
   - 多态和方法重写
   - 封装和访问控制
   - 抽象类和接口
   - 特殊方法 (魔法方法)
   - 属性装饰器 (@property)

### 第六部分：异常处理

#### ![Exception Icon](assets/exception-icon.svg) 8. **异常处理** (`08_exception_handling/`)
   - 异常的概念和类型
   - try, except, else, finally 语句
   - 异常捕获和处理
   - 自定义异常类
   - 异常链和上下文
   - 最佳实践和调试技巧

### 第七部分：文件操作

#### ![File Icon](assets/file-icon.svg) 9. **文件操作** (`09_file_operations/`)
   - 文件读写操作
   - 文件模式和编码
   - 上下文管理器 (with 语句)
   - 路径操作 (pathlib)
   - CSV、JSON 文件处理
   - 二进制文件操作
   - 文件系统操作

### 第八部分：模块和包

#### ![Modules Icon](assets/modules-icon.svg) 10. **模块和包** (`10_modules_packages/`)
   - 模块的概念和导入
   - 标准库模块
   - 自定义模块创建
   - 包的创建和管理
   - `__init__.py` 文件
   - 相对导入和绝对导入
   - `__name__ == '__main__'` 模式
   - 包管理工具 (pip)
   - 虚拟环境管理
   - **实战项目**: 数据处理框架 (`data_processor/`)
     - 插件化架构设计
     - 配置管理系统
     - 测试驱动开发

## 📁 项目结构

```
pythondemo/
├── README.md                 # 项目说明文档
├── .gitignore               # Git忽略文件配置
├── requirements.txt         # 项目依赖
├── assets/                  # SVG图标资源
│   ├── basics.svg
│   ├── data_types.svg
│   ├── control_structures.svg
│   ├── functions.svg
│   ├── oop.svg
│   ├── exceptions.svg
│   ├── file_operations.svg
│   ├── modules.svg
│   ├── standard_library.svg
│   ├── advanced_features.svg
│   ├── debugging_testing.svg
│   └── data_processor.svg
├── exercises.py             # 练习代码和实现
├── math_tools.py           # 数学工具模块
├── data_processor/         # 数据处理框架包
│   ├── __init__.py
│   ├── core/              # 核心模块
│   ├── plugins/           # 插件模块
│   ├── utils/             # 工具模块
│   ├── config/            # 配置模块
│   └── tests/             # 测试模块
└── __pycache__/           # Python缓存文件
```

## 📚 学习建议

1. **循序渐进**: 按照大纲顺序学习，每个知识点都要动手实践
2. **多写代码**: 理论结合实践，通过编写代码加深理解
3. **查阅文档**: 养成查阅官方文档的习惯
4. **解决问题**: 遇到问题时，学会使用调试工具和搜索引擎
5. **项目实战**: 完成小项目来综合运用所学知识
6. **代码规范**: 遵循PEP 8编码规范，编写可读性强的代码
7. **版本控制**: 学会使用Git进行代码版本管理
8. **测试驱动**: 养成编写测试代码的习惯

## 🔗 推荐资源

### 官方文档
- [Python官方文档](https://docs.python.org/3/)
- [Python标准库](https://docs.python.org/3/library/)
- [PEP 8 编码规范](https://www.python.org/dev/peps/pep-0008/)

### 在线教程
- [Python教程 - 廖雪峰](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [Real Python](https://realpython.com/)
- [Python之禅](https://www.python.org/dev/peps/pep-0020/)

### 实践平台
- [LeetCode](https://leetcode.com/) - 算法练习
- [HackerRank](https://www.hackerrank.com/) - 编程挑战
- [Codewars](https://www.codewars.com/) - 代码练习

### 开发工具
- [PyCharm](https://www.jetbrains.com/pycharm/) - 专业IDE
- [VS Code](https://code.visualstudio.com/) - 轻量级编辑器
- [Jupyter Notebook](https://jupyter.org/) - 交互式开发环境

---

**Happy Coding! 🐍✨**

> "Simple is better than complex. Complex is better than complicated." - The Zen of Python