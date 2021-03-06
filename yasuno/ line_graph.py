
# coding: utf-8

# In[1]:


#モジュールインポート
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
plt.style.use('ggplot')
from datetime import datetime
from PIL import Image

#テスト用(CPU取得)
import psutil


# In[2]:


#変数セット
x = []
y1 = []
i = 0


# In[3]:


#while True:
while i < 30:
    nowtime = datetime.now()
    time = nowtime.strftime("%H:%M:%S")
    x.append(time) #現在の時刻取得
    
    cpu_percent = psutil.cpu_percent(interval=1) #CPU取得(テスト用)
    y1.append(cpu_percent)
    #y2.append(i)
    i += 1
    
    if i % 10 == 0:
        # figure
        fig, ax = plt.subplots(figsize=(2.4,2.4))
        ax.xaxis.set_major_formatter(plt.NullFormatter())
        
        # plot
        ax.plot(x, y1, linestyle='-', color='b', label='ang')
        
        # x axis
        #plt.xlim([0 , 255]) #グラフの範囲
        ax.set_xlabel('日時')

        # y axis
        #ax.set_ylabel('y')
        
        # legend and title
        ax.legend(loc='best')
        ax.set_title('title')

        # save as png
        plt.savefig('figure_{0}.png'.format(i))
        
        # Convert jpeg
        im = Image.open('figure_{0}.png'.format(i))
        rgb_im = im.convert('RGB')
        rgb_im.save('figure_{0}.jpg'.format(i),'JPEG')
        
plt.close('all')

