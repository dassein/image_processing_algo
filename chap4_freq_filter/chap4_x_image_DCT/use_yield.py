# https://pyzh.readthedocs.io/en/latest/the-python-yield-keyword-explained.html
# 生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:
# yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。
# 当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。
# 那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

mygenerator = (x*x for x in range(4))
for i in mygenerator:
    print(i)

def createGenerator():
    mylist = range(4) # Excuted Once
    for i in mylist:  # after each yield: i still exist in the field of createGenerator()
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
for i in mygenerator:
    print(i)