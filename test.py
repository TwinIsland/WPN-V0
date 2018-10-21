def catch():
    import fun
    try:
        import urllib.request
        html_doc = "https://doub.pw/qr/qr.php?text=ss://Y2hhY2hhMjA6ZG91Yi5pUmsuKDqcygCCzgYI1fxaby9zc3poZngvKjYzMjdANjQuMTM3LjI1MS4xNDE6NjMyNw"
        req = urllib.request.Request(html_doc)
        webpage = urllib.request.urlopen(req)
        html = webpage.read()

        a = open("sc","w")
        a.write(str(html))
    except BaseException:
        print("错误！  不能连接至资源网站")
        fun.wrong()
catch()