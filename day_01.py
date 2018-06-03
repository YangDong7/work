# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:00:48 2018

@author: lenovo
"""

import urllib.request as r
city=input('请输入城市拼音：')
city_address="http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996".format(city)
info=r.urlopen(city_address).read().decode('utf-8','ignore')
print(info)


import json
data=json.loads(info)
temp=data['main']['temp']
description=data['weather'][0]
des=description['description']
temp_max=data['main']['temp_max']
pressure=data['main']['pressure']
print('当前{}温度为{}，天气情况{}，最高温度{}，气压为{}'.format(city,temp,des,temp_max,pressure))