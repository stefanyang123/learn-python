# 类和对象
    # 类就是一个模板，模板里可以包含多个函数，函数里实现一下功能
    # 是一组相同或者相似特征（属性）和行为（方法）的一系列对象的组合
    # 对象则是根据模板创建的实例，通过实例对象可以执行类中的函数
# 类的组成三部分
    # 1.类的名称：类名
    # 2.类的属性：一组数据
    # 3.类的方法：允许对进行操作的方法（行为）
# 例如：创建一个人类
    # 事务名称（类名）：人（person）
    # 属性：身高（height），年龄（age）...
    # 方法：吃（eat），跑（run）...
# 现实世界     计算机世界
# 行为-------->方法
# 特征-------->属性
#对象：对象是实实在在的一个东西，类的实例化，类相当于图纸，对象相当于汽车
# 类是对象的抽象化，而对象是类的实例化


# 类的结构  类名 属性 方法
# class 类名:
#     属性
#     方法

class Person:  #类的命名 大驼峰命名法，每个单词首字母为大写
    """
    对应人的特征，到底有哪些特征 就看你如何描述这个对象了
    """
    name='小明'
    age='20'
    """
    对应人的行为，
    """
    def eat(self):
        print('大口的吃饭')
        pass
    def run(self):
        print('飞速的跑')
        pass
    pass

# 类在内存中不开辟任何空间，创建完成也无任何意义的
# 只有当类去创建一个对象时，内存才会给对象分配内存空间

# 对象  #对象是照着类的模板跟约束创造出来的
# 对象名=类名()

# 创建一个对象xm
xm = Person()  #对象是从类里面创建过来的，它具备一些类定义的一些些行为和属性
xm.run()
xm.eat()
print('{}的年龄是:{}'.format(xm.name,xm.age))













