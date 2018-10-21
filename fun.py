## All By Wyatt
def wrong():
    import os,time
    time.sleep(1)
    os.system("color 47")
    time.sleep(1)
    os.system("color 07")
    print("回车即可退出")
    input()
    os._exit(0)

def sys_say(i,slogan):
    import os
    code = "mshta vbscript:msgbox(\"" + i + "\",64,\"""" + slogan + "\")(window.close)"
    os.system(code)

def write_txt(name,content):
    try:
        a = open(name,"w")
        a.write(content)
    except BaseException:
        print("Write Error")

def read_txt(name):
    try:
        a = open(name,"r")
        content = a.read()
        return content
    except BaseException:
        print("NO FILE NAMED: " + name)
        return "nofind"

def fence():
    print("===========================================")

def hide_me(hide_name):
    import os
    merge = "attrib +s +a +h +r " + hide_name
    os.system(merge)

def hide_back(return_name):
    import os
    merge = "attrib -a -s -h -r " + return_name
    os.system(merge)

## if just want to show the dictionary, path="none"
def dir(path,find):
    import os
    filenames = os.listdir(path)
    if str(find) == "none":
        for filename in filenames:
            print(filename)
    else:
        for filename in filenames:
            if filename == str(find):
                return 1
            else:
                continue
        return 0

# help document
def bar():
    import progressbar
    import time


    total = 100

    def dosomework():
        time.sleep(0.01)

    progress = progressbar.ProgressBar()
    for i in progress(range(100)):
        dosomework()

def succedd():
    import os
    os.system("color 27")