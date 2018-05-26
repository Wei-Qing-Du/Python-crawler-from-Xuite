
# coding: utf-8

# In[58]:

import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import re
import os


    
def save_img(img_url,cun):
       file_path='book\img'
    try:
        if not os.path.exists(file_path):
            print ('文件夾',file_path,'不存在，重新建立')
            os.makedirs(file_path)
        urlretrieve(img_url,file_path+'/'+str(cun)+'.jpg')
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('錯誤 ：',e)


url=["http://ftnr.main.jp/pandemic/1sfvxwa2v0ro/","https://photo.xuite.net/yinky0902/17787407-%E7%A8%80%E6%9C%89%E7%AB%A5%E9%A1%8F%E5%B7%A8%E4%B9%B3%E6%B8%AF%E5%A5%B"]

htm=requests.get(url[1])
result=BeautifulSoup(htm.text,'html.parser')
st=result.findAll('div','photo_item inline-block')
cun=0

for i in st:
    file=i.a.img.get('src')
    print('Writing'+str(cun)+'\n')
    cun=cun+1
    save_img(file,cun)



