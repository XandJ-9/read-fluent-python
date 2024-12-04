'''
使用__new__创建实例
'''
import shelve

from d1 import load


db_name = 'data/s_db'
db=shelve.open(db_name)
db["k1"]="abc"