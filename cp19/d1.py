'''
动态属性和方法
'''

json_data = '''
{ "Schedule":
    { 
        "conferences": [{"serial": 115 }],
        "events": [
            { 
            "serial": 34505,
            "name": "Why Schools Don ́t Use Open Source to Teach Programming",
            "event_type": "40-minute conference session",
            "time_start": "2014-07-23 11:30:00",
            "time_stop": "2014-07-23 12:10:00",
            "venue_serial": 1462,
            "description": "Aside from the fact that high school programming...",
            "website_url": "http://oscon.com/oscon2014/public/schedule/detail/34505",
            "speakers": [157509],
            "categories": ["Education"] 
            }
        ],
        "speakers": [
            { 
            "serial": 157509,
            "name": "Robert Lefkowitz",
            "photo": null,
            "url": "http://sharewave.com/",
            "position": "CTO",
            "affiliation": "Sharewave",
            "twitter": "sharewaveteam",
            "bio": "Robert  ́r0ml ́ Lefkowitz is the CTO at Sharewave, a startup..." 
            }
        ],
        "venues": [
            { 
            "serial": 1462,
            "name": "F151",
            "category": "Conference Venues" 
            }
        ]
    }
}
'''
from collections import abc 
import keyword
import json 

def load():
    obj= json.loads(json_data)
    return obj


o=load()
print("============ 1. 使用字典取值的方式获取值 =============")
print(o['Schedule']['events'][0]['name'])


class FrozenJSON:
    """A read-only adapter for navigating a JSON-like object
    using attribute notation
    """
    def __init__(self, mapping):
        # self.__data = dict(mapping)
        self.__data = dict()
        for key,value in mapping.items():
            if keyword.iskeyword(key):  # 判断是否为关键字
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name: str):
        if hasattr(self.__data, name):
            # 优先使用字典的属性
            return getattr(self.__data, name)
        else:
            # 获取字典内容
            return FrozenJSON.build(self.__data[name])
    
    @classmethod
    def build(cls,obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
        


obj=FrozenJSON(o)
print("============= 2. 使用类属性取值的方式获取值 =============")
print(obj.Schedule.events[0].name)
o2 = FrozenJSON({"k1":"v1","class":"v2"})
print(o2.class_)  ## python关键字作为key时，替换后缀为_