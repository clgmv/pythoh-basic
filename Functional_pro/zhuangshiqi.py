
#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数


# import time
#
# def now():
#     print(time.time())
# # if __name__ == '__main__':
# #     f = now                                  #函数对象可以被赋值给变量
# #     f()                                #通过变量也能调用该函数
# #     print(f.__name__)                #函数对象有一个__name__属性，可以拿到函数的名字
#
#
#
# #现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# #本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
#
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s:' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now1():
#     print(time.time())



def log(text):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator

@log('这是测试now方法的打印日志')
def now(a,b):
    print('你是猪嘛')
    print(a,b)



#和两层嵌套的decorator相比，3层嵌套的效果是这样的：

#>>> now = log('execute')(now)

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
#
# >>> now.__name__
# 'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

#那怎么办呢？

#Python内置的functools.wraps就是干这个事的


import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

#现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。



#练习：请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
# import time,functools
# def metric(fn):
#     start_time = time.time()
#     @functools.wraps(fn)
#     def exe_time(*args,**kwargs):
#         print(args)
#         end_time = time.time()
#         print('%s executed in %s ms' % (fn.__name__, start_time - end_time))
#         return fn(*args,**kwargs)
#     return exe_time
#
#
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
# if __name__ == '__main__':
#     f = fast
#     print(f(2,3))



#小结

# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，
# 直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
#
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便




