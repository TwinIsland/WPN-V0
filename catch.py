# -*- coding: gb2312 -*-
import urllib.request,re

def catch():
    import fun
    try:

        # 写入brook 配置
        # 不用分析二级域名
        print("开始分析通配账号。。")
        a = open("sc", "w")
        html_doc = "https://doub.io/sszhfx/"
        req = urllib.request.Request(html_doc)
        webpage = urllib.request.urlopen(req)
        html = webpage.read()
        a.write(str(html))
        print("成功！ 分析统配账号")


        # 分析ss账号地址，需要分析二级域名
        # 分析二级域名
        a = open("sc", "a")
        print("开始分析SS二级域名地址。。")
        # 分隔符
        a.write("mynameiswyattandhelloworld")
        a = open("sc", "r")
        con = str(a.read())
        reg_ss = r'href="https://doub.pw/qr/qr.php(.{110})'
        wordreg = re.compile(reg_ss)
        ss_list_pre = re.findall(wordreg, con)
        ss_list_fake = []
        for i in ss_list_pre:
            i = i.split('"')[0]
            try:
                i = i.split("ss://")[1]
                ss_list_fake.append(i)
            except IndexError:
                continue
            ss_list_fake.append(i)
        # 再次catch
        ss_list = []
        for i in ss_list_fake:
            html_doc = "https://doub.pw/qr/qr.php?text=ss://" + i
            req = urllib.request.Request(html_doc)
            webpage = urllib.request.urlopen(req)
            html = str(webpage.read())
            a = open("sc", "a")
            a.write("========================")
            a.write(str(html))
        print("成功！ 分析SS账号")

    except BaseException:
        print("错误！  不能连接至资源网站")
        fun.wrong()