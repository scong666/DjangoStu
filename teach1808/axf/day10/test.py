from datetime import datetime

def outer(func):
    def inner(*args,**kwargs):
        start = datetime.now()
        func(*args,**kwargs)
        end = datetime.now()
        print("时长:",str(end - start))
    return inner

@outer
def f1():
    print("f1")

@outer
def f2():
    print("f2")

#装饰器有参数
def check_p(permission):
    def outer(func):
        def inner(cx,*args,**kwargs):
            if permission & cx == permission:
                return func(cx,*args,**kwargs)
            else:
                print("没权限")
        return inner
    return outer

@check_p(2)
def f3(n):
    print("有权限")
    return "hehe"

if __name__ == "__main__":
    # start = datetime.now()
    # f1()
    # f2()
    res = f3(4)
    print("res:",res)
    # end = datetime.now()
    # print(end-start)

#需求 计算f1函数的 运行时间