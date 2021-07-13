import tkinter as tk
import time
from typing import Text
import  requests
import json
import io
import tkinter as tk

from urllib.request import urlopen
from PIL import Image, ImageTk


def index():
    index = tk.Tk()
    index.geometry('300x200')
    index.title("bilibili信息查询")
    


    input_uid = tk.IntVar
    tk.Label(index,text="请输入用户uid：").place(x=25,y=100)
    tk.Entry(index,textvariable=input_uid).place(x=125,y=100)
    confirm = tk.Button(index,text="确认",command=get_info(input_uid))


    index.mainloop()



def get_info(input_uid):
    data = requests.get('https://api.bilibili.com/x/web-interface/card?mid=%d'%(input_uid))
    global inform
    inform = json.loads(data.text)
    info()


def info():
    fans = inform['data']['follower']#粉丝数
    mid = inform['data']['card']['mid']#用户id
    name = inform['data']['card']['name']#用户昵称
    approve = inform['data']['card']['approve']#是否为认证帐号
    sex = inform['data']['card']['sex']#性别
    rank = inform['data']['card']['rank']#帐号显示标识
    face = inform['data']['card']['face']#头像，是个图片链接，也有可能是gif
    DisplayRank = inform['data']['card']['DisplayRank']#帐号显示标识开关
    regtime = inform['data']['card']['regtime']#注册时间
    spacesta = inform['data']['card']['spacesta']#可能是头像框是否存在，我的是-2，有头像框
    birthday = inform['data']['card']['birthday']#生日
    place = inform['data']['card']['place']#地区
    description = inform['data']['card']['description']#描述，但不是简介
    article = inform['data']['card']['article']#文章数量，就是我没写的那个
    attentions = inform['data']['card']['attentions']#关注数量
    fans = inform['data']['card']['fans']#粉丝数量
    friend = inform['data']['card']['friend']#可能是关注数
    sign = inform['data']['card']['sign']#为空，未知
    level_info = inform['data']['card']['level_info']['current_level']#账号等级
    current_min = inform['data']['card']['level_info']['current_min']#默认为0
    current_exp = inform['data']['card']['level_info']['current_exp']#默认为0
    next_exp = inform['data']['card']['level_info']['next_exp']#默认为0
    # pendant 就是头像框，下面的pid=0就是没有
    pendant_pid = inform['data']['card']['pendant']['pid']#头像框id
    pendant_name = inform['data']['card']['pendant']['name']#头像框姓名
    pendant_image = inform['data']['card']['pendant']['image']#头像框透明图层的png
    pendant_expire = inform['data']['card']['pendant']['expire']#过期时间，0就是永久
    pendant_image_enhance = inform['data']['card']['pendant']['image_enhance']#头像框不透明图层的jpg
    pendant_image_enhance_frame = inform['data']['card']['pendant']['image_enhance_frame']#不知道，为空
    # nameplate 是当前佩戴的勋章
    nameplate_nid = inform['data']['card']['nameplate']['nid']#勋章id
    nameplate_name = inform['data']['card']['nameplate']['name']#勋章名
    nameplate_image = inform['data']['card']['nameplate']['image']#透明背景勋章大图
    nameplate_image_small = inform['data']['card']['nameplate']['image_small']#透明背景勋章小图
    nameplate_level = inform['data']['card']['nameplate']['level']#勋章等级
    # 待处理！字符处理 nameplate_condition = inform['data']['card']['pendant']['condition']#达成条件
    # Official 官方认证
    Official_role = inform['data']['card']['Official']['role']#认证类型
    Official_title = inform['data']['card']['Official']['title']#认证称号名称
    Official_desc = inform['data']['card']['Official']['desc']#认证称号简介
    Official_type = inform['data']['card']['Official']['type']#1是，-1不是
    #official_verify 官方认证验证状态
    official_verify_type = inform['data']['card']['official_verify']['type']#1是，-1不是
    official_verify_desc = inform['data']['card']['official_verify']['desc']#和上一个的title一样的

    #vip 大会员功能
    vip_type = inform['data']['card']['vip']['type']#大会员种类
        # 0：无
        # 1：月大会员，和季度
        # 2：年度及以上大会员
    vip_status = inform['data']['card']['vip']['status']#1是开启，0是关闭
        #前面不是0，这里是0就代表曾经开过
    vip__due_date = inform['data']['card']['vip']['due_date']#毫秒时间戳
    vip_theme_type = inform['data']['card']['vip']['theme_type']#默认为0，不知道有什么用
    #label 大会员标识
    vip_label_path = inform['data']['card']['vip']['label']['path']#未知
    vip_label_text = inform['data']['card']['vip']['label']['text']#会员名称
    vip_label_label_theme = inform['data']['card']['vip']['label']['label_theme']#英文的大会员名称
    vip_label_text_color = inform['data']['card']['vip']['label']['text_color']#文字颜色
    vip_label_bg_style = inform['data']['card']['vip']['label']['bg_style']#背景格式
    vip_label_bg_color = inform['data']['card']['vip']['label']['bg_color']#背景颜色
    vip_label_border_color = inform['data']['card']['vip']['label']['border_color']#轮廓颜色


    vip_avatar_subscript = inform['data']['card']['vip']['avatar_subscript']#头像下标类型
    vip_nickname_color = inform['data']['card']['vip']['nickname_color']#昵称颜色
    vip_role = inform['data']['card']['vip']['role'] #未知，很多人都是3，非会员为0
    vip_avatar_subscript_url = inform['data']['card']['vip']['avatar_subscript_url']#头像下标图片
    vip_vipType = inform['data']['card']['vip']['vipType']#会员类别，和 vip_type相同
    vip_vipStatus = inform['data']['card']['vip']['vipStatus']#vip状态，1是，0不是


    archive_count = inform['data']['archive_count']#视频数目
    article_count = inform['data']['article_count']#文章数目
    follower = inform['data']['follower']#粉丝数



    return fans,level_info

    # name = inform['data']['card']['vip']
#会员到期时间戳单位是毫秒
def info_view():
    info_view = tk.Tk()
    info_view.title("用户信息")

    mid = 1
    name = 2
    sex = 3
    face = "http://i0.hdslb.com/bfs/face/0a9546e9733bfb60d3000c108f0db26156d8d430.jpg" #是个链接
    tk.Label(info_view,text="id：").place(row=0,column=0)
    tk.Label(info_view,text=mid).place(row=0,column=1)

    tk.Label(info_view,text="昵称：").place(row=1,column=0)
    tk.Label(info_view,text=name).place(row=1,column=1)

    tk.Label(info_view,text="性别：").place(row=2,column=0)
    tk.Label(info_view,text=sex).place(row=2,column=1)



    url = face
    image_bytes = urlopen(url).read()

    # internal data file

    data_stream = io.BytesIO(image_bytes)

    # open as a PIL image object

    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((100,100))
    tk_image = ImageTk.PhotoImage(pil_image)




    tk.Label(info_view,text="头像").grid(row=0,column=3)
    tk.Label(info_view,image=tk_image).grid(row=1,column=3)







    info_view.mainloop()







def test():
    import io
    import tkinter as tk

    from urllib.request import urlopen

    root = tk.Tk()

    # find yourself a picture on an internet web page you like

    # (right click on the picture, under properties copy the address)

    #url = "http://www.google.com/intl/en/images/logo.gif"

    # or use image previously downloaded to tinypic.com

    #url = "http://i48.tinypic.com/w6sjn6.jpg"

    url = "http://i50.tinypic.com/34g8vo5.jpg"

    image_bytes = urlopen(url).read()

    # internal data file

    data_stream = io.BytesIO(image_bytes)

    # open as a PIL image object

    pil_image = Image.open(data_stream)

    # optionally show image info

    # get the size of the image

    w, h = pil_image.size

    # split off image file name

    fname = url.split('/')[-1]

    sf = "{} ({}x{})".format(fname, w, h)

    root.title(sf)

    # convert PIL image object to Tkinter PhotoImage object

    tk_image = ImageTk.PhotoImage(pil_image)

    # put the image on a typical widget

    label = tk.Label(root, image=tk_image, bg='brown')

    label.pack(padx=5, pady=5)

    root.mainloop()





if __name__ == '__main__':
    info_view()
