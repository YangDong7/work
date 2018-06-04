# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:28:03 2018

@author: lenovo
"""


import urllib.request as r
import time
import json
while 1:
    print("\n",
          "\n",
          "*****欢迎使用我的天气预报*****\n",
          "**********************************\n"
          " 温馨提示：\n",
          "查看城市当前的天气         请输入  1  \n",
          "查看城市未来五天的天气     请输入  2  \n",
          "退出系统                  请输入  0  \n")
    menu = input(" 请输入数字：")
    if menu == "0":
        print("你即将退出天气预报系统")
        time.sleep(2)
        print("*******感谢使用，再见！*******")
        break
    elif menu > "2":
        print(" ********************\n",
              "哈哈哈哈，你输入错了！\n",
              "请输入数字1/2")
    elif menu == "1":
        city=input('请输入城市拼音：')
        city_address="http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996".format(city)
        info=r.urlopen(city_address).read().decode('utf-8','ignore')
        print("请查看{}的天气情况:".format(city))
        time.sleep(3)
        data=json.loads(info)
        temp=data['main']['temp']
        description=data['weather'][0]['description']
        temp_max=data['main']['temp_max']
        pressure=data['main']['pressure']
        print('{}-当前温度为{}-天气情况[{}]-最高温度{}-气压为{}'.format(city,temp,description,temp_max,pressure))
    elif menu == "2":
        city=input('请输入城市拼音：')
        city_address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996".format(city)
        info=r.urlopen(city_address).read().decode('utf-8','ignore')
        print("请查看{}未来5天的天气情况:".format(city))
        time.sleep(3)
        
        data=json.loads(info)
        a=len(data['list'])
        for i in range(0,a):
            day=data['list'][i]
            time=day['dt_txt']
            temp=day['main']['temp']
            description=day['weather'][0]['description']
            temp_max=day['main']['temp_max']
            pressure=day['main']['pressure']
            if data['list'][i]['dt_txt'][9]==data['list'][i-1]['dt_txt'][9]:
                print('{}-当前时间：{}-温度为{}-天气情况[{}]-最高温度{}-气压为{}'.format(city,time,temp,description,temp_max,pressure))
            else:
                print('\n')
                print('日期：{}\n'.format(time[0:10]))
                print('{}-当前时间：{}-温度为{}-天气情况[{}]-最高温度{}-气压为{}'.format(city,time,temp,description,temp_max,pressure))