# print("hello world!")

# for i in range(0, 2020):
#     if i%4==0:
#         if i%100==0:
#             if i%400==0:
#                 print(i)
#         else:
#             print(i)

# l = [1, 2, 3, 4, 5]
# k = (1,2,3,4,5)
# l = {2,3}

# print(l[1])
# b = ['abc', 'dddd', '你好']

# c = [l, b]

# print(c)

# d = {'name': 'a', 'age': 20, 'c': c}


# print(d)


# y = [d]
# print(y)

# print(l[2:])

# print(d['c'][0][3])
# print(d)

# print("-----")

# for k, v in d.items():
#     print('{}: {}'.format(k, v))
# a = ['张三','李四','王五']
# b = [10,12,18]
# c = [30,40,80]
# class1 = {'name':a,'age':b,'wet':c}
# print(class1)
p1 ={'name':'zhangsan','age':10,'wet':30}
p2 ={'name':'zhangsan1','age':11,'wet':31}
p3 ={'name':'zhangsan2','age':12,'wet':32}
a =[p1,p2,p3]
for p in a:
    print(p['name'])
