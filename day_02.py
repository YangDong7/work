# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:00:48 2018

@author: lenovo
"""

import urllib.request as r
import time
print("你好等一下")
time.sleep(3)
print("我来了")
print("欢迎使用我的天气app")
city=input('请输入城市拼音：')
city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996".format(city)
info=r.urlopen(city_address).read().decode('utf-8','ignore')
print("请查看{}的天气情况".format(city))
time.sleep(3)

import json
data=json.loads(info)
for i in range(0,37):
    day=data['list'][i]
    time=day['dt_txt']
    temp=day['main']['temp']
    description=day['weather'][0]['description']
    temp_max=day['main']['temp_max']
    pressure=day['main']['pressure']
    print('{}-当前时间：{}-温度为{}-天气情况[{}]-最高温度{}-气压为{}'.format(city,time,temp,description,temp_max,pressure))
