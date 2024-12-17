from inspect import getframeinfo

def simple_coro2():
    while True:
        received = yield
        print('[coro2] received:', received)




def simple_coro1(a):
    print('-> Start: a = ', a)
    b = yield a
    print('-> Received: b = ', b)
    c = yield a + b
    print('-> Received: c = ', c)