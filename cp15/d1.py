'''
else 块
'''

import sys

# else子句抛出的异常不会被except子句捕获  ????

def call_method():
    print('call_method()')
    raise Exception('exception in call_method()')

def after_try():
    print('after_try()')


try:
    call_method()
except Exception as e:
    print('Exception:', e)
else:
    after_try()
    print('No exception')
