# -*- coding: gb2312 -*-

def catch():
    import fun
    try:
        import urllib.request
        html_doc = "https://doub.io/sszhfx/"
        req = urllib.request.Request(html_doc)
        webpage = urllib.request.urlopen(req)
        html = webpage.read()

        a = open("sc","w")
        a.write(str(html))
    except BaseException:
        print("����  ������������Դ��վ")
        fun.wrong()