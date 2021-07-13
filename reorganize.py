# import json
# inform = '{"code":0,"message":"0","ttl":1,"data":{"card":{"mid":"396422549","name":"椎名淅雨","approve":false,"sex":"女","rank":"10000","face":"http://i2.hdslb.com/bfs/face/c7e6a26ffc7f25a316c462b9cb176b4c433edb24.jpg","DisplayRank":"0","regtime":0,"spacesta":0,"birthday":"","place":"","description":"","article":0,"attentions":[],"fans":4,"friend":186,"attention":186,"sign":"","level_info":{"current_level":4,"current_min":0,"current_exp":0,"next_exp":0},"pendant":{"pid":0,"name":"","image":"","expire":0,"image_enhance":"","image_enhance_frame":""},"nameplate":{"nid":60,"name":"饭圈萌新","image":"http://i0.hdslb.com/bfs/face/51ca16136e570938450bca360f28761ceb609f33.png","image_small":"http://i2.hdslb.com/bfs/face/9abfa4769357f85937782c2dbc40fafda4f57217.png","level":"普通勋章","condition":"当前持有粉丝勋章最高等级\u003e=5级"},"Official":{"role":0,"title":"","desc":"","type":-1},"official_verify":{"type":-1,"desc":""},"vip":{"type":1,"status":0,"due_date":1593878400000,"vip_pay_type":0,"theme_type":0,"label":{"path":"","text":"","label_theme":"","text_color":"","bg_style":0,"bg_color":"","border_color":""},"avatar_subscript":0,"nickname_color":"","role":0,"avatar_subscript_url":"","vipType":1,"vipStatus":0}},"following":false,"archive_count":0,"article_count":0,"follower":4}}'
# data = inform
# # global inform
# inform = json.loads(data)

def info(data):
    import time
    import json

    inform = json.loads(data.text)



    fans = inform['data']['follower']  # 粉丝数
    mid = inform['data']['card']['mid']  # 用户id
    name = inform['data']['card']['name']  # 用户昵称
    sex = inform['data']['card']['sex']  # 性别
    face = inform['data']['card']['face']  # 头像，是个图片链接，也有可能是gif
    spacesta = inform['data']['card']['spacesta']  # 可能是头像框是否存在，我的是-2，有头像框


    # ***********用if判断有无头像框，影响到 pendant_name pendant_expire************


    birthday = inform['data']['card']['birthday']  # 生日
    place = inform['data']['card']['place']  # 地区
    attention = inform['data']['card']['attention']  # 关注数量
    level_info = inform['data']['card']['level_info']['current_level']  # 账号等级
    pendant_name = inform['data']['card']['pendant']['name']  # 头像框姓名
    pendant_expire = inform['data']['card']['pendant']['expire']  # 过期时间，0就是永久
    nameplate_name = inform['data']['card']['nameplate']['name']  # 勋章名
    nameplate_level = inform['data']['card']['nameplate']['level']  # 勋章等级
    nameplate_condition = inform['data']['card']['nameplate']['condition']  # 达成条件
    # Official 官方认证
    Official_role = inform['data']['card']['Official']['role']  # 认证类型
    Official_title = inform['data']['card']['Official']['title']  # 认证称号名称
    Official_type = inform['data']['card']['Official']['type']  # 1是，-1不是
    official_verify_type = inform['data']['card']['official_verify']['type']  # 1是，-1不是
    # vip 大会员功能
    vip_type = inform['data']['card']['vip']['type']  # 大会员种类
    # 0：无
    # 1：月大会员，和季度
    # 2：年度及以上大会员
    vip_status = inform['data']['card']['vip']['status']  # 1是开启，0是关闭
    # 前面不是0，这里是0就代表曾经开过
    vip_due_date = inform['data']['card']['vip']['due_date']  # 毫秒时间戳
    vip_label_text = inform['data']['card']['vip']['label']['text']  # 会员名称
    archive_count = inform['data']['archive_count']  # 视频数目
    article_count = inform['data']['article_count']  # 文章数目

    #从这里开始重定义变量
    # ***********用if判断有无头像框，影响到 pendant_name pendant_expire************
    if spacesta  == 0:
        pendant_name = "无头像框"
        pendant_expire = "无头像框"

    if pendant_expire == 0:
        pendant_expire = '永久有效'

    if Official_role == 1:
        Official_role = '知名up'
    elif Official_role == 2:
        Official_role = '知名身份认证（站外）'
    elif Official_role == 3:
        Official_role = '官方认证'
    elif Official_role == 4:
        Official_role = '政府认证'
    elif Official_role == 5:
        Official_role = '媒体认证'
    elif Official_role == 6:
        Official_role = '公益组织'
    elif Official_role == 7:
        Official_role = '专栏优质UP主'
    elif Official_role == 0:
        Official_role = '非官方账号'

    if Official_type == -1:
        Official_type ='未认证'
    elif Official_type == 1:
        Official_type = '已认证'

    if official_verify_type == -1:
        official_verify_type ='未通过验证'
    elif official_verify_type == 1:
        official_verify_type = '已通过验证'

    time_local = time.localtime(vip_due_date/1000)
    vip_due_date = time.strftime("%Y-%m-%d",time_local)

    if vip_type==0:
        vip_type ='未开通过'
    elif vip_type == 1:
        if vip_status == 0:
            vip_type = '曾经开通过月度大会员'
        else:
            vip_type = '月度大会员'
    elif vip_type == 2 :
        if vip_status == 0:
            vip_type = '曾经开通过年度大会员'
        else:
            vip_type = '年度大会员'
        # vip_type = '年度大会员'

    if vip_status == 1:
        vip_status = '已开通'
    elif vip_status == 0:
        vip_status = '未开通'


    print(fans,mid,name,sex,face,'birthday',birthday,'place',place,'attention',attention,'level_info',level_info,'pendant_name',pendant_name,'pendant_expire',pendant_expire,'nameplate_name',nameplate_name,
          'nameplate_level',nameplate_level,'nameplate_condition',nameplate_condition,'Official_role',Official_role,'Official_title',Official_title,'Official_type',Official_type,'official_verify_type',official_verify_type,'vip_type',vip_type,
          'vip_status',vip_status,'vip_due_date',vip_due_date,'vip_label_text',vip_label_text,'archive_count',archive_count,'article_count',article_count)

    return(fans,mid,name,sex,face,birthday,place,attention,level_info,pendant_name,pendant_expire,nameplate_name,
          nameplate_level,nameplate_condition,Official_role,Official_title,Official_type,official_verify_type,vip_type,
          vip_status,vip_due_date,vip_label_text,archive_count,article_count)
