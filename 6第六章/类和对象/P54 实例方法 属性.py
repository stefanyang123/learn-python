# 实例方法
# 在类的内部，使用def关键字可以定义实例方法
# 实例方法归于 类的实例所有，类的实例（对象）可以调用
# 实例方法:在类的内部，使用def关键是来定义，第一个参数默认是self,不满足以上两个条件就不是实体函数
# self[名字标识可以是其他名字，但是位置必须被占用]

class Person:  #类的命名 大驼峰命名法，每个单词首字母为大写
    """
    对应人的特征，到底有哪些特征 就看你如何描述这个对象了
    """
    # name='小明' #类属性
    age='20'   #类属性
    """
    对应人的行为，
    """

    def __init__(self):
        self.name='小白'    #实例属性
        pass



    def eat(self):  #实体函数
        print('大口的吃饭')
        pass
    def run(self):  #实体函数
        print('飞速的跑')
        pass
    pass
# 创建一个对象（类的具象化）即类的实例
xm=Person()
# 创建另一个对象
xw=Person()
xw.run()

# 属性（在类的内部定义的变量）  类属性  实例属性
# 在类的内部定义的变量称为类属性
# 定义在实例方法里，使用self引用的属性称之为实例属性，归属于实例属性
# 在方法内部定义的[通过类似于 self.变量名]








