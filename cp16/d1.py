from inspect import getgeneratorstate

def simple_coroutine():
    print("-> Starting coroutine")
    x = yield
    print("-> coroutine received: ", x)


my_coro = simple_coroutine()
print("1 --> ",getgeneratorstate(my_coro))
next(my_coro)
print("2 --> ",getgeneratorstate(my_coro))
my_coro.send(2)
print("3 --> ",getgeneratorstate(my_coro))
