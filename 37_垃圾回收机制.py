# 垃圾回收机制
# 作用：从经历过引用计数器机制，仍未被释放的对象中，找到循环引用，干掉相关对象

"""
底层机制
    是如何找到循环引用的？
        1.收集所有的容器对象，通过一个双向链表进行引用
            容器对象，可以引用其他对象的对象 (列表 元组 字典 自定义的类对象)
                l=[p]
                t=(p)
                p.pet=Dog()
            非容器对象，数值型，字符串，布尔类型
            双向链表，把所有的容器对象放到一个集合里面，通过集合找到容器对象去操作
        2.针对于每一个容器对象，通过变量gc_refs来记录当前对于的引用计数
        3.对于每个容器对象，找到它引用的容器对象，并将这个容器对象的引用计数 -1
        4.经过步骤三后，如果一个容器对象的引用计数为0 就代表这玩意可以被回收了，肯定是循环引用导致它存活到现在
    产生问题
        如果程序中创建了很多对象，而针对于每一个对象都要参与检测过程，会非常的耗费性能
    基于问题提出假设
        如果一个对象很多次检测都没被清除，就会减少对这个对象的检测
    基于假设设计  分代回收机制
        1.默认一个对象被创建出来后，属于0代
        2.如果经历过这一代垃圾回收后，依然存活，则被划分到下一代
        3.垃圾回收的周期顺序为：
            0代垃圾回收一定次数，会触发0代和1代回收
                0代每检测10次会触发一次0代和一代的同时检测，0代检测次数11 1代检测次数1
            1代垃圾回收一定次数，会触发0代和1代和2代回收
        4.并不是创建一个对象之后就会触发分代回收机制，而是 新增个数-消亡个数达到一定的阈值时，才会触发

        查看和设置相关参数
            import gc
            print(gc.get_threshold())
            gc.set_threshold(700,10,5)


"""
import gc

print(gc.get_threshold())
#(700, 10, 10) 700  新增个数-消亡个数达到700,才会触发垃圾检测
#              10   0代每被检测10次时，才会触发0代和1代的同时检测
#              10   1代每被检测10次时，才会触发0代和1代和2代的同时检测
gc.set_threshold(200,5,5) #自己设置阈值
print(gc.get_threshold())
