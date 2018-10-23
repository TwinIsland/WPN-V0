#view-source:https://gitee.com/wyatthuang/codes/5qk9abdxo1p6ejzc4trfv87

def get_update():
    import urllib.request,re
    html_doc = "https://gitee.com/wyatthuang/codes/5qk9abdxo1p6ejzc4trfv87"
    req = urllib.request.Request(html_doc)
    webpage = urllib.request.urlopen(req)
    html = webpage.read()

    a = open("version\\temp\\update_sc","w")
    a.write(str(html))

    a = open("version\\temp\\update_sc", "r")
    con = str(a.read())

    reg = r'style="display:none;">\\n(.{100})'
    wordreg = re.compile(reg)
    wordreglist = re.findall(wordreg, con)
    for i in wordreglist:
        pre_data = i
    try:
        data = pre_data.split("<")[0]
    except BaseException:
        return 0
    return data