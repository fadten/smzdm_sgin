# coding=utf-8
import requests
import json
import os
import requests
from requests import Session as req_Session
import time
import random
import re



def req(url):
    url = url
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = json.loads(res.text)
        return data


if __name__ == "__main__":
    #username = os.environ["SMZDM_USERNAME"]
    #password = os.environ["SMZDM_PASSWORD"]    
    userCookie = os.environ["SMZDM_COOKIE"] 
    # 设置Server酱post地址 不需要可以删除
    # serverChan = "https://sc.ftqq.com/*****************************************.send"
    # 状态地址
    current_url = 'https://zhiyou.smzdm.com/user/info/jsonp_get_current'
    # 签到地址
    checkin_url = 'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin'
    # 用用户名和密码登录后获取Cookie
    # userCookie = "**************************************************************"
    headers = {
        'Referer': 'https://www.smzdm.com/',
        'Host': 'zhiyou.smzdm.com',
        'Cookie': userCookie,
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    anum=1;
    while anum < 5:
        time.sleep( 10 )
        data = req(current_url)    
        if data['checkin']['has_checkin']:
            info = '第%s次检查签到状态 ： %s ：%s 你目前积分：%s，经验值：%s，金币：%s，碎银子：%s，威望：%s，等级：%s，已经签到：%s天' % (anum,data['sys_date'], data['nickname'], data['point'], data['exp'], data['gold'], data['silver'], data['prestige'], data['level'],data['checkin']['daily_checkin_num'])
            print(info)
            anum = 5000;
        else:            
            time.sleep( 10 )
            checkin = req(checkin_url)['data']
            info = '第%s次尝试签到：'%anum
            print(info)            
            anum = anum + 1;
        # print(checkin)
        #info = '%s 目前积分(第1次尝试签到)：%s，增加积分：%s，经验值：%s，金币：%s，威望：%s，等级：%s' % (data['nickname'], checkin['point'], checkin['add_point'], checkin['exp'], checkin['gold'], checkin['prestige'], checkin['rank'])
        #print(info)
   
            
    
