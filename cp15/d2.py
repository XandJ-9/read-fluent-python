'''
使用with上下文管理器,
两个方法：
1. __enter__(): 进入上下文管理器时执行
2. __exit__(): 退出上下文管理器时执行
'''



class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write   # 记录标准输出
        sys.stdout.write = self.reverse_write  # 重写标准输出
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])  # 翻转字符串并输出
    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True

with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print("what:")

