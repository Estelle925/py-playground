# 异常处理 (Exception Handling)

## 学习目标

通过本章学习，你将掌握：

1. **异常基础概念**
   - 什么是异常
   - 异常的类型和层次结构
   - 异常的传播机制

2. **异常处理语法**
   - try-except语句
   - else和finally子句
   - 多个异常的处理

3. **异常类型**
   - 内置异常类型
   - 自定义异常
   - 异常的继承关系

4. **异常处理最佳实践**
   - 何时使用异常
   - 异常处理的原则
   - 日志记录和调试

5. **高级异常处理**
   - 异常链
   - 上下文管理器与异常
   - 异常处理的性能考虑

## 1. 异常基础

### 1.1 什么是异常

异常是程序执行过程中发生的错误事件，它会中断程序的正常执行流程。Python使用异常来处理错误情况，而不是返回错误代码。

### 1.2 异常的优势

- **错误处理与业务逻辑分离**：使代码更清晰
- **错误信息丰富**：提供详细的错误信息和调用栈
- **强制错误处理**：确保错误不会被忽略
- **统一的错误处理机制**：所有错误都通过异常处理

### 1.3 异常层次结构

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      |    +-- OverflowError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- ValueError
      +-- TypeError
      +-- FileNotFoundError
      +-- PermissionError
      +-- ...
```

## 2. 基本异常处理语法

### 2.1 try-except语句

```python
try:
    # 可能出现异常的代码
    risky_operation()
except SpecificException:
    # 处理特定异常
    handle_specific_error()
except Exception as e:
    # 处理其他异常
    handle_general_error(e)
```

### 2.2 else子句

```python
try:
    operation()
except Exception:
    print("发生异常")
else:
    # 没有异常时执行
    print("操作成功")
```

### 2.3 finally子句

```python
try:
    operation()
except Exception:
    print("发生异常")
finally:
    # 无论是否有异常都会执行
    cleanup()
```

### 2.4 完整语法

```python
try:
    # 尝试执行的代码
    pass
except SpecificException as e:
    # 处理特定异常
    pass
except (Exception1, Exception2) as e:
    # 处理多种异常
    pass
except Exception as e:
    # 处理其他异常
    pass
else:
    # 没有异常时执行
    pass
finally:
    # 清理代码
    pass
```

## 3. 常见内置异常

### 3.1 数值相关异常

- **ZeroDivisionError**：除零错误
- **OverflowError**：数值溢出
- **ValueError**：值错误（类型正确但值不合适）

### 3.2 类型相关异常

- **TypeError**：类型错误
- **AttributeError**：属性错误
- **NameError**：名称错误

### 3.3 索引和键相关异常

- **IndexError**：索引超出范围
- **KeyError**：字典键不存在
- **StopIteration**：迭代器耗尽

### 3.4 文件和IO相关异常

- **FileNotFoundError**：文件不存在
- **PermissionError**：权限错误
- **IOError**：输入输出错误

## 4. 自定义异常

### 4.1 创建自定义异常

```python
class CustomError(Exception):
    """自定义异常基类"""
    pass

class ValidationError(CustomError):
    """数据验证异常"""
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

class BusinessLogicError(CustomError):
    """业务逻辑异常"""
    def __init__(self, message, error_code=None):
        super().__init__(message)
        self.error_code = error_code
```

### 4.2 异常设计原则

- **继承合适的基类**：通常继承Exception
- **提供有意义的名称**：异常名应该清楚表达错误类型
- **包含有用信息**：提供足够的上下文信息
- **文档化异常**：说明何时抛出和如何处理

## 5. 抛出异常

### 5.1 raise语句

```python
# 抛出异常
raise ValueError("无效的值")

# 重新抛出当前异常
try:
    risky_operation()
except Exception:
    log_error()
    raise  # 重新抛出

# 异常链
try:
    operation()
except OriginalError as e:
    raise NewError("新错误") from e
```

### 5.2 断言

```python
# 断言语句
assert condition, "错误信息"

# 等价于
if not condition:
    raise AssertionError("错误信息")
```

## 6. 异常处理最佳实践

### 6.1 具体异常优于通用异常

```python
# 好的做法
try:
    value = int(user_input)
except ValueError:
    print("请输入有效数字")

# 避免的做法
try:
    value = int(user_input)
except Exception:
    print("出错了")
```

### 6.2 异常处理的EAFP原则

EAFP (Easier to Ask for Forgiveness than Permission)

```python
# EAFP风格（推荐）
try:
    return my_dict[key]
except KeyError:
    return default_value

# LBYL风格（不推荐）
if key in my_dict:
    return my_dict[key]
else:
    return default_value
```

### 6.3 资源管理

```python
# 使用try-finally
file = None
try:
    file = open('data.txt')
    process_file(file)
finally:
    if file:
        file.close()

# 更好的方式：使用上下文管理器
with open('data.txt') as file:
    process_file(file)
```

### 6.4 日志记录

```python
import logging

try:
    risky_operation()
except Exception as e:
    logging.error(f"操作失败: {e}", exc_info=True)
    # 或者重新抛出
    raise
```

## 7. 高级异常处理

### 7.1 异常链

```python
try:
    low_level_operation()
except LowLevelError as e:
    # 保留原始异常信息
    raise HighLevelError("高级操作失败") from e
```

### 7.2 异常组（Python 3.11+）

```python
# 处理多个异常
try:
    operations()
except* ValueError as eg:
    for error in eg.exceptions:
        handle_value_error(error)
except* TypeError as eg:
    for error in eg.exceptions:
        handle_type_error(error)
```

### 7.3 上下文管理器中的异常

```python
class DatabaseTransaction:
    def __enter__(self):
        self.begin_transaction()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()
        return False  # 不抑制异常
```

## 8. 调试和诊断

### 8.1 获取异常信息

```python
import traceback
import sys

try:
    risky_operation()
except Exception as e:
    # 获取异常类型
    exc_type = type(e).__name__
    
    # 获取异常信息
    exc_message = str(e)
    
    # 获取调用栈
    exc_traceback = traceback.format_exc()
    
    # 获取当前异常信息
    exc_info = sys.exc_info()
```

### 8.2 自定义异常钩子

```python
def custom_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    logging.error(
        "未捕获的异常",
        exc_info=(exc_type, exc_value, exc_traceback)
    )

sys.excepthook = custom_exception_handler
```

## 9. 性能考虑

### 9.1 异常的性能成本

- 抛出和捕获异常比正常控制流慢
- 异常应该用于异常情况，不是正常控制流
- 避免在循环中频繁使用异常

### 9.2 优化建议

```python
# 避免：在循环中使用异常控制流
results = []
for item in items:
    try:
        result = process(item)
        results.append(result)
    except ProcessError:
        continue

# 推荐：预先检查
results = []
for item in items:
    if can_process(item):
        results.append(process(item))
```

## 10. 常见陷阱

### 10.1 捕获过于宽泛的异常

```python
# 错误：捕获所有异常
try:
    operation()
except:
    pass  # 可能隐藏重要错误

# 正确：捕获具体异常
try:
    operation()
except SpecificError:
    handle_error()
```

### 10.2 忽略异常

```python
# 错误：静默忽略异常
try:
    operation()
except Exception:
    pass

# 正确：至少记录异常
try:
    operation()
except Exception as e:
    logging.warning(f"操作失败，继续执行: {e}")
```

### 10.3 finally中的异常

```python
# 注意：finally中的异常会覆盖try中的异常
try:
    raise ValueError("原始异常")
finally:
    raise RuntimeError("finally异常")  # 这个异常会覆盖ValueError
```

## 练习建议

1. **基础练习**：编写处理不同类型异常的代码
2. **自定义异常**：为特定应用创建异常层次结构
3. **文件处理**：实现健壮的文件操作异常处理
4. **网络请求**：处理网络相关的各种异常
5. **数据验证**：创建数据验证框架
6. **资源管理**：实现自定义上下文管理器
7. **日志系统**：集成异常处理和日志记录
8. **错误恢复**：实现自动重试和错误恢复机制

## 总结

异常处理是Python编程的重要组成部分，正确使用异常可以让程序更加健壮和用户友好。记住：

- 异常用于处理异常情况，不是正常控制流
- 捕获具体的异常类型，避免过于宽泛
- 提供有意义的错误信息和上下文
- 合理使用日志记录异常信息
- 在适当的层级处理异常
- 使用上下文管理器管理资源

通过大量练习和实际项目经验，你将能够熟练掌握Python的异常处理机制。