#outpuargs=None###########
#Good Morning
#******************

#1
# def decoratorcal(fun):
#     def inner():
#         print("##################")
#         fun()
#         print("******************")
#     return inner
#
# @decoratorcal
# def functionA():
#     print("Good Morning")
#
#
# functionA()

#2

# def add2(a,b):
#     z=a+b
#     print("returing Sum of 2 numbers")
#
# def add3(a,b,c):
#     z=a+b+c
#     print("returing Sum of 3 numbers")
#
# add2(10,20)
# add3(10,20,20)

#output

#returing Sum of 2 numbers
#returing Sum of 3 numbers

# def decoratorcal(func):
#     def inner(*args):
#         print("A function is called")
#         return func(*args)
#     return inner
#
# @decoratorcal
# def add2(a,b):
#     z=a+b
#     print("returing Sum of 2 numbers")
#     return z
#
# @decoratorcal
# def add3(a,b,c):
#     z=a+b+c
#     print("returing Sum of 3 numbers")
#     return z
#
# print(add2(10,20))
# print(add3(10,20,20))


#3
# def decoratorcal(func):
#     def inner(*args):
#         print(f"{func.__name__} is called")
#         return func(*args)
#     return inner
#
# @decoratorcal
# def add2(a,b):
#     z=a+b
#     return z
#
# @decoratorcal
# def add3(a,b,c):
#     z=a+b+c
#     print("returing Sum of 3 numbers")
#     return z
#
# print(add2(10,20))
# print(add3(10,20,20))

# 4
# time included
# from datetime import datetime
# def decoratorcal(func):
#     def inner(*args):
#         time=datetime.utcnow()
#         print(f"{func.__name__} is called at {time}")
#         return func(*args)
#     return inner
#
# @decoratorcal
# def add2(a,b):
#     z=a+b
#     return z
#
# @decoratorcal
# def add3(a,b,c):
#     z=a+b+c
#     print("returing Sum of 3 numbers")
#     return z
#
# print(add2(10,20))
# print(add3(10,20,20))

#5
#decarator parameter

def token_required(*args,**kwargs):
    def inner(f):
        print(f"value of optional is {kwargs['optional']} ")
        f()
    return inner

@token_required(optional=True)
def get_users():
    print("iwill give you all the users ")