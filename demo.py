import time
from typing import Text
import  requests
import json
uid = eval(input("请输入up主uid："))










def info():
    global fans
    fans = inform['data']['follower']#粉丝数
    mid = inform['data']['card']['mid']#用户id
    name = inform['data']['card']['name']#用户昵称
    # approve = inform['data']['card']['approve']###未知
    sex = inform['data']['card']['sex']#性别
    rank = inform['data']['card']['rank']#帐号显示标识#未知
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




# fans = 1
# while fans > 0:
    
data = requests.get('https://api.bilibili.com/x/web-interface/card?mid=%d'%(uid))

inform = json.loads(data.text)
# fans = inform['data']['follower']
info = info()
# level_info=info()
print(info)
# info()
# time.sleep(10)

##15点27分


