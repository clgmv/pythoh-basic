# A = [1,5,'val','a','val']
#
# def list_is_val():
#     for i in range(0,len(A)):
#         if A[i] == 'val':
#             print(i)
#         else:
#             continue
# if __name__ == '__main__':
#     list_is_val()


#有1，2，3，4四个数字，能组成多少个hu互不相同q且无重复数字的三位数
# def g_number():
#     n=0
#     for i in range(1,5):
#         for j in range(1,5):
#             for k in range(1,5):
#                 if (i!=j) and (i!=k) and (j!=k):
#                     n = n+1;
#                     print(i,j,k)
#     print(n)

# def test1(*args):
#     sum = 0
#     for s in args:
#         sum = sum + s*s
#     print(sum)
#
#
# def test2(name,age,**kwargs):
#     print(name,age,kwargs)

#接收一个或多个数并计算乘积
# def product(*args):
#     sum = 1
#     if len(args) == 0:
#         raise ValueError('请至少输入一个数')
#     for n in args:
#         sum = sum * n
#     print (sum)


#递归

# def sum(number):
#     if number == 1:
#         return number
#     return number * sum(number-1)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple
# def findMinAndMax(L):
#     if len(L) == 0:
#         return (None, None)
#     if len(L) == 1:
#         return (L[0], L[0])
#     max_num = L[0]
#     min_num = L[1]
#     for i in range(len(L)):
#         if L[i] > max_num:
#             max_num = L[i]
#         if L[i] < min_num:
#             min_num = L[i]
#     return (min_num, max_num)


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
# def normalize(name):
#     name = name.capitalize()
#     return name
# #测试：
#     L = ['adam', 'LISA', 'barT']
#     print(list(map(normalize,L)))




#reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算


#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# from functools import reduce
# def prod(L):
#     return reduce(multiplication,L)
# def multiplication(a,b):
#     return a * b
# #测试
#     print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#     if prod([3, 5, 7, 9]) == 945:
#         print('测试成功!')
#     else:
#         print('测试失败!')



#filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
# def is_odd(n):
#     return n % 2 == 1
#
# list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))



#排序算法

# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数
#
# Python内置的sorted()函数就可以对list进行排序：
#
# >>> sorted([36, 5, -12, 9, -21])
# [-21, -12, 5, 9, 36]
# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
#
# >>> sorted([36, 5, -12, 9, -21], key=abs)
# [5, 9, -12, -21, 36]
#
# 我们再看一个字符串排序的例子：
#
# >>> sorted(['bob', 'about', 'Zoo', 'Credit'])
# ['Credit', 'Zoo', 'about', 'bob']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
#
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
#
# 这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
#
# >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# ['about', 'bob', 'Credit', 'Zoo']
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
#
# >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']
#
#
# #练习
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# 请用sorted()对上述列表分别按名字排序：
# def by_name(t):
#     print(t[0])
#     return t[0]
# if __name__ == '__main__':
#     print(sorted(L,key=by_name))







