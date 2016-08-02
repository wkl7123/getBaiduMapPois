#!/usr/bin/env python
#coding=utf-8
import requests
import re
import json
import MySQLdb
import codecs
# import string
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='lbldks03200028',db='test',port=3306)
    conn.set_character_set('utf8')
    cur=conn.cursor()
    cur.execute("SET NAMES 'UTF8'")
    cur.execute("delete from city")
    cur.execute("delete from info")
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
     exit()
##########################
       #(city, code)s -> MySQL
#########################
file=codecs.open('BaiduMap_cityCode.txt', 'r', 'utf-8')
cn=[]
cc=[]
sql="insert into city(name, code) values"
for line in file.readlines():
    [name,code]=line.split('|')
    code=int(code[0:-2])          # for \r\n
    cn.append(name)
    cc.append(code)
    sql=sql+",('"+name+"', '"+str(code)+"')"
sql=sql.replace('values,', 'value')
try:
    cur.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
################
         #QUERY
################
flag=0
flag1=0
flag2=0
for city_code in cc:
    print(city_code)
    pn=0
    while True:
        flag+=1
        parameter = {  
            "newmap": "1",  
            "reqflag": "pcmap",  
            "biz": "1",  
            "from": "webmap",  
            "da_par": "direct",  
            "pcevaname": "pc4.1",  
            "qt": "con",  
            "c": city_code,            # 城市代码  
            "wd": '照相',       # 搜索关键词  
            "wd2": "",  
            "pn": pn,           # 页数  
            "nn": pn*10,  
            "db": "0",  
            "sug": "0",  
            "addr": "0",  
            "da_src": "pcmappg.poi.page",  
            "on_gel": "1",  
            "src": "7",  
            "gr": "3",  
            "l": "12",  
            "tn": "B_NORMAL_MAP",  
            # "u_loc": "12621219.536556,2630747.285024",  
            "ie": "utf-8",  
            # "b": "(11845157.18,3047692.2;11922085.18,3073932.2)",  #这个应该是地理位置坐标，可以忽略  
            "t": "1468896652886"  
        }
        url = 'http://map.baidu.com/'  
        htm = requests.get(url, params=parameter)  
        h1=json.loads(htm.text)
        try:
            h2=h1['content']
        except Exception as e:
            break
        # h2=h1['content']
        for item in h2:
            try:
                detail=item['ext']['detail_info']
            except Exception as e:
                sql="insert into info(city_code, name, address, x, y) values"
                try:
                    sql+=",('"+str(city_code)+"', '"+item['name']+"', '"+item['addr']+"', '"+str(item['diPointX'])+"', '"+str(item['diPointY'])+"')"
                    sql=sql.replace('values,', 'value')
                    cur.execute(sql)
                    flag1+=1
                    conn.commit()
                except Exception as e:
                    pass
                continue
            try:
                sql="insert into info(city_code, name, address, phone, x, y) values"
                sql+=",('"+str(city_code)+"', '"+item['name']+"', '"+item['addr']+"', '"+str(detail['phone'])+"', '"+str(item['diPointX'])+"', '"+str(item['diPointY'])+"')"
                sql=sql.replace('values,', 'value')
                cur.execute(sql)
                flag2+=1
                conn.commit()
            except Exception as e:
                print(e)
        if len(h2)<10:
            break
        pn=pn+1
print("flag="+str(flag))
print("flag1="+str(flag1))
print("flag2="+str(flag2))

