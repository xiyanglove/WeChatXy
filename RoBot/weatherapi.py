#! /usr/bin/env python
# coding=utf-8

import requests
import json
from wechatpy.replies import TextReply, ArticlesReply

def getcityweather():
    appurl = 'http://v.juhe.cn/weather/index?format=2&cityname=重庆&key=8041e0da4cfdfc756ffe1d47d788ce00'
    r = requests.get(appurl)
    return r.json()


def getWeatherMsg(msg):
    reply = ArticlesReply(message=msg)
    result = getcityweather()
    temperature = result['result']['today']['temperature']
    weather = result['result']['today']['weather']
    wind = result['result']['today']['wind']
    reply.add_article({
        'title': temperature,
    })
    reply.add_article({
        'title': weather,
    })
    reply.add_article({
        'title': wind,
    })
    return reply
