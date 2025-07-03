#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第五部分：面向对象编程 - 练习题

本文件包含面向对象编程的各种练习题，帮助巩固类、对象、继承、封装、多态等概念
"""

print("第五部分：面向对象编程练习题")
print("=" * 50)

# ============================================================================
# 1. 类和对象基础练习
# ============================================================================

print("\n1. 类和对象基础练习")
print("-" * 30)

"""
练习 1.1：创建一个简单的类

创建一个名为Book的类，包含以下属性和方法：
- 属性：title（标题）、author（作者）、pages（页数）、published_year（出版年份）
- 方法：
  - __init__：初始化所有属性
  - __str__：返回格式化的书籍信息
  - get_age：返回书籍出版至今的年数
  - is_long：如果页数超过500，返回True，否则返回False

然后创建几个Book实例并测试所有方法。
"""

# 在这里编写你的代码


"""
练习 1.2：类属性和实例属性

创建一个名为Student的类，包含以下内容：
- 类属性：school_name（学校名称）、total_students（学生总数）
- 实例属性：name（姓名）、student_id（学号）、courses（所选课程，初始为空列表）
- 方法：
  - __init__：初始化实例属性，并增加学生总数
  - add_course：添加一门课程到courses列表
  - remove_course：从courses列表中移除一门课程
  - get_courses_count：返回所选课程数量
  - __str__：返回学生信息，包括姓名、学号和所选课程数量

创建多个Student实例，测试所有方法，并验证total_students属性是否正确更新。
"""

# 在这里编写你的代码


"""
练习 1.3：实例方法、类方法和静态方法

创建一个名为MathUtils的类，包含以下方法：
- 实例方法：
  - set_value：设置一个数值
  - square：返回设置值的平方
  - cube：返回设置值的立方
- 类方法：
  - from_string：接收一个字符串，转换为数值并创建实例
  - from_list：接收一个列表，使用列表第一个元素创建实例
- 静态方法：
  - is_even：判断一个数是否为偶数
  - is_prime：判断一个数是否为质数
  - gcd：计算两个数的最大公约数

创建实例并测试所有方法。
"""

# 在这里编写你的代码


# ============================================================================
# 2. 继承练习
# ============================================================================

print("\n2. 继承练习")
print("-" * 30)

"""
练习 2.1：基本继承

创建一个名为Vehicle的基类，包含以下属性和方法：
- 属性：make（制造商）、model（型号）、year（年份）、fuel_capacity（燃油容量）
- 方法：
  - __init__：初始化所有属性
  - fuel_efficiency：返回燃油效率（抽象方法，子类必须实现）
  - max_distance：根据燃油容量和燃油效率计算最大行驶距离
  - __str__：返回车辆基本信息

然后创建两个子类：
1. Car：增加属性passengers（载客量）和trunk_size（后备箱大小）
   - 重写fuel_efficiency方法，返回一个固定值（如10km/L）
   - 添加is_family_car方法，如果载客量>=5，返回True

2. Motorcycle：增加属性has_sidecar（是否有边车）
   - 重写fuel_efficiency方法，返回一个固定值（如20km/L）
   - 添加is_sport方法，根据某些条件判断是否为运动型摩托车

创建Car和Motorcycle的实例，测试所有方法。
"""

# 在这里编写你的代码


"""
练习 2.2：多重继承

创建以下类：
1. Device：包含属性brand、model和方法power_on、power_off
2. Portable：包含属性weight、battery_life和方法is_light（重量小于1kg）
3. Camera：继承自Device，增加属性megapixels和方法take_photo
4. Phone：继承自Device，增加属性number和方法make_call
5. SmartPhone：继承自Phone和Portable，增加属性os和方法install_app
6. DigitalCamera：继承自Camera和Portable，增加属性zoom和方法record_video

创建SmartPhone和DigitalCamera的实例，测试所有继承的方法。
打印SmartPhone和DigitalCamera的MRO（方法解析顺序）。
"""

# 在这里编写你的代码


"""
练习 2.3：方法重写和super()

创建一个名为Shape的基类，包含以下方法：
- __init__：接收color参数
- area：计算面积（返回0）
- perimeter：计算周长（返回0）
- describe：返回形状的描述，包括颜色、面积和周长

创建以下子类：
1. Circle：接收radius参数
   - 重写area和perimeter方法
   - 添加diameter方法

2. Rectangle：接收width和height参数
   - 重写area和perimeter方法
   - 添加is_square方法

3. Square：继承自Rectangle
   - 修改__init__，只接收一个side参数
   - 使用super()调用父类的__init__
   - 重写describe方法，在父类方法基础上添加额外信息

创建每个类的实例并测试所有方法。
"""

# 在这里编写你的代码


# ============================================================================
# 3. 封装练习
# ============================================================================

print("\n3. 封装练习")
print("-" * 30)

"""
练习 3.1：访问控制

创建一个名为BankAccount的类，实现以下功能：
- 私有属性：__balance（余额）、__pin（密码）、__account_number（账号）、__transaction_history（交易历史）
- 公开方法：
  - __init__：初始化账号、密码和初始余额
  - deposit：存款（更新余额和交易历史）
  - withdraw：取款（需要密码，验证成功后更新余额和交易历史）
  - get_balance：获取当前余额（需要密码）
  - change_pin：修改密码（需要旧密码）
  - get_account_info：获取账户信息摘要（不包含完整账号）
  - print_statement：打印对账单（需要密码，显示交易历史）

确保所有私有属性无法从类外部直接访问，只能通过公开方法操作。
"""

# 在这里编写你的代码


"""
练习 3.2：属性装饰器

创建一个名为Person的类，使用属性装饰器实现以下功能：
- 私有属性：__name、__age、__email、__phone
- 公开属性（使用@property）：
  - name：获取姓名，设置时确保是有效的名称（不为空且只包含字母和空格）
  - age：获取年龄，设置时确保是有效的年龄（0-120之间）
  - email：获取邮箱，设置时验证格式（包含@和.）
  - phone：获取电话，设置时验证格式（纯数字，长度合理）
  - adult：只读属性，根据年龄判断是否成年（>=18）
  - contact_info：只读属性，返回格式化的联系信息

创建Person实例，测试所有属性的获取和设置，包括错误处理。
"""

# 在这里编写你的代码


"""
练习 3.3：数据封装和验证

创建一个名为Product的类，表示电子商务网站的商品：
- 私有属性：__id、__name、__price、__stock、__category、__ratings
- 公开方法和属性：
  - 使用属性装饰器为所有属性提供getter和setter
  - 在setter中实现数据验证：
    - id：必须是唯一的产品标识符（字符串或整数）
    - name：不能为空，长度在3-100之间
    - price：必须大于0
    - stock：必须是非负整数
    - category：必须是预定义类别列表中的一个
    - ratings：必须是0-5之间的数字列表
  - 添加方法：
    - add_rating：添加一个新评分
    - restock：增加库存数量
    - discount：计算折扣价格
    - is_available：检查是否有库存
    - average_rating：计算平均评分

创建Product实例，测试所有方法和属性验证。
"""

# 在这里编写你的代码


# ============================================================================
# 4. 多态练习
# ============================================================================

print("\n4. 多态练习")
print("-" * 30)

"""
练习 4.1：方法重写和多态

创建一个名为Employee的基类，包含以下属性和方法：
- 属性：name、id、base_salary
- 方法：
  - __init__：初始化所有属性
  - calculate_salary：计算月薪（返回base_salary）
  - get_info：返回员工基本信息

创建以下子类：
1. Manager：
   - 增加属性：bonus、team_size
   - 重写calculate_salary：基本工资 + 奖金 + (团队规模 * 100)

2. Developer：
   - 增加属性：programming_languages、overtime_hours
   - 重写calculate_salary：基本工资 + (编程语言数量 * 500) + (加班小时 * 150)

3. SalesPerson：
   - 增加属性：sales_volume、commission_rate
   - 重写calculate_salary：基本工资 + (销售额 * 佣金比例)

创建一个process_payroll函数，接收员工列表，使用多态计算并打印每个员工的工资。
创建不同类型的员工，测试process_payroll函数。
"""

# 在这里编写你的代码


"""
练习 4.2：抽象基类

使用abc模块创建一个名为PaymentMethod的抽象基类，包含以下抽象方法：
- process_payment：处理支付
- refund：处理退款
- get_transaction_fee：获取交易费用
- is_international：检查是否支持国际支付

创建以下具体子类：
1. CreditCard：实现所有抽象方法
2. PayPal：实现所有抽象方法
3. BankTransfer：实现所有抽象方法
4. Cryptocurrency：实现所有抽象方法

创建一个process_order函数，接收订单金额和支付方法对象，使用多态处理支付。
测试不同支付方法的process_order函数。
"""

# 在这里编写你的代码


"""
练习 4.3：接口和协议

使用Python的typing.Protocol创建以下协议：

1. Drawable协议：
   - 方法：draw() -> None

2. Resizable协议：
   - 方法：resize(width: int, height: int) -> None

3. Interactive协议：
   - 方法：handle_click(x: int, y: int) -> None
   - 方法：handle_hover(x: int, y: int) -> None

创建以下类，实现不同的协议组合：
1. Button：实现Drawable和Interactive
2. Image：实现Drawable和Resizable
3. Canvas：实现Drawable、Resizable和Interactive
4. Text：实现Drawable

创建一个render函数，接收Drawable对象列表并调用它们的draw方法。
创建一个resize_elements函数，接收Resizable对象列表并调用它们的resize方法。
创建一个handle_user_click函数，接收Interactive对象列表和点击坐标，调用它们的handle_click方法。

测试这些函数与不同类型的对象。
"""

# 在这里编写你的代码


# ============================================================================
# 5. 特殊方法练习
# ============================================================================

print("\n5. 特殊方法练习")
print("-" * 30)

"""
练习 5.1：运算符重载

创建一个名为Fraction的类，表示分数，包含以下内容：
- 属性：numerator（分子）、denominator（分母）
- 方法：
  - __init__：初始化分子和分母，并将分数化为最简形式
  - simplify：将分数化为最简形式
  - __str__和__repr__：字符串表示
  - __eq__、__ne__：相等和不相等比较
  - __lt__、__le__、__gt__、__ge__：大小比较
  - __add__、__sub__：加法和减法
  - __mul__、__truediv__：乘法和除法
  - __neg__：取负
  - __abs__：绝对值
  - to_decimal：转换为小数

创建多个Fraction实例，测试所有运算符和方法。
"""

# 在这里编写你的代码


"""
练习 5.2：容器和迭代

创建一个名为Playlist的类，表示音乐播放列表，包含以下内容：
- 属性：name、songs（歌曲列表）、current_position
- 方法：
  - __init__：初始化播放列表
  - add_song：添加歌曲
  - remove_song：移除歌曲
  - __len__：返回歌曲数量
  - __getitem__：通过索引获取歌曲
  - __setitem__：通过索引设置歌曲
  - __delitem__：通过索引删除歌曲
  - __iter__：返回迭代器
  - __next__：实现迭代器协议
  - __contains__：检查歌曲是否在播放列表中
  - shuffle：随机打乱歌曲顺序
  - sort：按指定关键字排序歌曲

创建Playlist实例，测试所有方法，特别是迭代和容器行为。
"""

# 在这里编写你的代码


"""
练习 5.3：上下文管理器

创建以下上下文管理器类：

1. FileManager：
   - __init__：接收文件路径和模式
   - __enter__：打开文件并返回文件对象
   - __exit__：关闭文件并处理异常

2. DatabaseConnection：
   - __init__：接收数据库连接参数
   - __enter__：建立连接并返回连接对象
   - __exit__：提交或回滚事务，关闭连接

3. Timer：
   - __init__：接收计时器名称
   - __enter__：记录开始时间并返回self
   - __exit__：计算经过时间并打印结果
   - elapsed：返回当前经过的时间

使用with语句测试这些上下文管理器，包括正常情况和异常情况。
"""

# 在这里编写你的代码


# ============================================================================
# 6. 设计模式练习
# ============================================================================

print("\n6. 设计模式练习")
print("-" * 30)

"""
练习 6.1：单例模式

实现一个名为Logger的单例类，确保整个应用程序只有一个Logger实例：
- 方法：
  - log_info：记录信息日志
  - log_warning：记录警告日志
  - log_error：记录错误日志
  - set_log_level：设置日志级别
  - get_logs：获取所有日志

使用两种不同的方法实现单例模式：
1. 使用__new__方法
2. 使用模块级别的实例

测试Logger类，确保多次创建实例时返回相同的对象。
"""

# 在这里编写你的代码


"""
练习 6.2：工厂模式

实现一个形状工厂系统：

1. 创建Shape抽象基类，包含draw和area方法

2. 创建具体形状类：
   - Circle：实现Shape方法
   - Rectangle：实现Shape方法
   - Triangle：实现Shape方法

3. 创建ShapeFactory类，包含以下静态方法：
   - create_shape：根据形状类型创建相应的形状对象
   - create_random_shape：创建随机形状
   - create_shapes_batch：创建多个形状

使用ShapeFactory创建不同的形状，测试工厂方法。
"""

# 在这里编写你的代码


"""
练习 6.3：观察者模式

实现一个简单的新闻发布-订阅系统：

1. 创建Observer抽象基类，包含update方法

2. 创建Subject抽象基类，包含以下方法：
   - add_observer：添加观察者
   - remove_observer：移除观察者
   - notify_observers：通知所有观察者

3. 创建具体类：
   - NewsPublisher：继承Subject，添加publish_news方法
   - EmailSubscriber：继承Observer，实现update方法发送邮件通知
   - SMSSubscriber：继承Observer，实现update方法发送短信通知
   - PushNotificationSubscriber：继承Observer，实现update方法发送推送通知

测试新闻发布系统，添加不同类型的订阅者，发布新闻并验证所有订阅者都收到通知。
"""

# 在这里编写你的代码


# ============================================================================
# 7. 综合应用练习
# ============================================================================

print("\n7. 综合应用练习")
print("-" * 30)

"""
练习 7.1：图书管理系统

设计一个简单的图书馆管理系统，包含以下类：

1. Book类：
   - 属性：id、title、author、publisher、publish_year、isbn、category、copies
   - 方法：display_info、update_copies等

2. Library类：
   - 属性：name、address、books（Book对象列表）、members（Member对象列表）
   - 方法：add_book、remove_book、search_books、display_all_books等

3. Member类：
   - 属性：id、name、email、borrowed_books（字典，键为Book对象，值为借阅日期）
   - 方法：borrow_book、return_book、display_borrowed_books等

4. Transaction类：
   - 属性：id、book、member、transaction_type、date
   - 方法：display_info等

实现以下功能：
- 添加和删除图书
- 搜索图书（按标题、作者、类别等）
- 会员借阅和归还图书
- 检查图书可用性
- 显示会员借阅历史
- 生成借阅和归还交易记录

创建一个简单的命令行界面来测试系统功能。
"""

# 在这里编写你的代码


"""
练习 7.2：电子商务系统

设计一个简单的电子商务系统，包含以下类：

1. Product类：
   - 属性：id、name、description、price、stock、category
   - 方法：display_info、update_stock等

2. User类：
   - 属性：id、name、email、address、payment_methods
   - 方法：add_payment_method、update_address等

3. Cart类：
   - 属性：user、items（字典，键为Product对象，值为数量）、created_at
   - 方法：add_item、remove_item、update_quantity、calculate_total等

4. Order类：
   - 属性：id、user、items、total_amount、status、created_at
   - 方法：process、cancel、refund、display_info等

5. PaymentProcessor类（抽象基类）：
   - 抽象方法：process_payment、refund_payment
   - 具体子类：CreditCardProcessor、PayPalProcessor等

6. ShippingService类（抽象基类）：
   - 抽象方法：calculate_shipping_cost、generate_label
   - 具体子类：StandardShipping、ExpressShipping等

实现以下功能：
- 用户浏览和搜索商品
- 将商品添加到购物车
- 结账并创建订单
- 处理支付
- 生成运输标签
- 跟踪订单状态

创建一个简单的命令行界面来测试系统功能。
"""

# 在这里编写你的代码


"""
练习 7.3：游戏角色系统

设计一个简单的游戏角色系统，包含以下类：

1. Character（抽象基类）：
   - 属性：name、level、health、mana、strength、agility、intelligence
   - 方法：attack、defend、use_ability、level_up、is_alive等

2. 具体角色类（继承Character）：
   - Warrior：偏重力量，特殊能力是重击
   - Mage：偏重智力，特殊能力是法术
   - Archer：偏重敏捷，特殊能力是精准射击
   - Healer：平衡属性，特殊能力是治疗

3. Item（抽象基类）：
   - 属性：name、description、value、weight
   - 方法：use、get_info等

4. 具体物品类（继承Item）：
   - Weapon：增加攻击力
   - Armor：增加防御力
   - Potion：恢复生命值或魔法值
   - Scroll：提供临时效果

5. Inventory类：
   - 属性：items（物品列表）、capacity
   - 方法：add_item、remove_item、get_total_weight等

6. Game类：
   - 属性：characters、current_map
   - 方法：create_character、start_battle、save_game、load_game等

实现以下功能：
- 创建不同类型的角色
- 角色升级和属性提升
- 装备和使用物品
- 角色之间的战斗
- 保存和加载游戏状态

创建一个简单的命令行界面来测试系统功能。
"""

# 在这里编写你的代码


print("\n" + "=" * 50)
print("面向对象编程练习完成！")
print("=" * 50)