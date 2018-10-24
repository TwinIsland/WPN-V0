# -*- coding: gb2312 -*-
import os,host,get_brook,fun,catch,time,urllib.request,urllib,update_update,get_ss,random,json

def proxy_connect(ip):
    con = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f'
    os.system(con)
    con = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "' + ip + '" /f'
    os.system(con)


def update_check():
    # try:
        print("检查更新。。")
        if str(update_update.get_update().split("::")[0]) == str(fun.read_txt("version\\version.txt").split("::")[0]):
            print("成功！  程序已为最新版本")
        else:
            update_content = update_update.get_update()
            print("程序有最新版本！\n"
                  "最新版本：" + update_content.split("::")[0] + "\n"
                  "目前版本：" + fun.read_txt("version\\version.txt").split("::")[0] + "\n" 
                  "下载地址：" + update_content.split("::")[2] + "\n"
                  "释放时间：" + update_content.split("::")[1] + "\n"
                  "更新说明：" + update_content.split("::")[4] + "\n"
                  "强制更新：" + update_content.split("::")[5])

            if update_content.split("::")[5] == "1":
                print("请务必更新后在使用！")
                print("回车退出")
                input()
                os._exit(0)

            print("\n回车继续")
            input()
    # except BaseException:
    #     print("无法开启更新服务，可能是因为配置文件丢失或无网络连接")
    #     print("回车继续")
    #     input()

def initial():
    try:
        a = open("version\\version.txt","r")
        ccc = str(a.read().split("::")[3])
    except FileNotFoundError:
        print("错误！  文件不完整，请重新下载")
        fun.wrong()
    if ccc == "1":
        update_check()


    print("检查host文件完整性。。")
    host.host()
    print("检查文件重要备份点。。")
    if fun.dir("host","backup"):
        print("成功！ 备份程序重要备份点")
    else:
        try:
            os.system(r"copy C:\Windows\System32\drivers\etc\hosts host\\backup")
            print("成功！ 备份程序重要备份点")
        except BaseException:
            print("错误！ 未能成功备份")
            fun.wrong()
    print()
    time.sleep(1)
    print("检查计算机隧道效应。。。")
    try:
        html_doc = "https://doub.io/sszhfx/"
        req = urllib.request.Request(html_doc)
        urllib.request.urlopen(req)
    except BaseException:
        print("错误！  网络配置错误")
        fun.wrong()
    else:
        print("成功！  网络适配成功")
    fun.fence()

# 初始化系统
os.system("kill.bat")

# 开始
version = fun.read_txt("version/version.txt").split("::")[0]
os.system("cls")
print("|-----------------------------------------------------|\n"
      "|                                                     |\n" 
      "|               Rattlemander Free VPN                 |\n"
      "|                  Version:" +  version +"                      |\n"
      "|-----------------------------------------------------|")
initial()
time.sleep(3)
os.system("cls")
print("|-----------------------------------------------------|\n"
      "|                                                     |\n" 
      "|               Rattlemander Free VPN                 |\n"
      "|                  Version:" +  version +"                      |\n"
      "|-----------------------------------------------------|")
print("\n获取开始")
fun.fence()



## new version begin: more way allocation: ss

print("开始获取 Brook & SS GFW Broker 账号")

a = random.randint(0,3)
if a == 0:
    print("分配到 Brook 端口")
    print("正在爬取网页数据，请稍等。。")
    catch.catch()
    print("成功！  获取账号")
    print("分配接口。。")
    allocate = str(get_brook.allocate()+1)
    num = str(get_brook.vpn_num())
    content_pre = get_brook.allocate_line()
    tool = "brook"
else:
    print("分配到 SS 端口")
    print("正在爬取网页数据，请稍等。。")
    catch.catch()
    print("成功！  获取账号")
    print("分配接口。。")
    allocate = str(get_ss.allocate()+1)
    num = str(get_ss.vpn_num())
    content_pre = get_ss.allocate_line()
    tool = "ss"

print("接口总数：" + num + " | 分配接口：" + allocate + " | 混淆方法：" + " | 随机数组法")
print("成功！  成功分析接口数据")
print("解析源代码。。")

try:
    print("成功！  解析成功")
    print("串口接口：" + content_pre)
except BaseException:
    print("错误！  解析异常")
    fun.wrong()
time.sleep(3)


# new version end


os.system("cls")
print("|-----------------------------------------------------|\n"
      "|                                                     |\n" 
      "|               Rattlemander Free VPN                 |\n"
      "|                  Version:" +  version +"                      |\n"
      "|-----------------------------------------------------|")
print("\n配置连接器")
fun.fence()
print("检查配置模板文档。。")
try:
    a = open("mode","r")
except FileNotFoundError:
    print("错误！  不能找到模板文档")
    fun.wrong()
print("成功！  已找到配置文档")
print("开始配置模板文档。。")
os.system("copy mode temp_run\\run.bat")
os.system("copy mode_ss.json temp_run\\ss\\gui-config.json")
print("成功！  已将模板文档写入运行文档")
print("再次解析allocate字符串。。")


# new version begin: also need to write to the SS allocation fold

if tool == "brook":
    IP_brook = content_pre.split("%%")[0] + ":" + content_pre.split("%%")[1]
    password = content_pre.split("%%")[2]
    merge = "brook client -l 127.0.0.1:1080 -i 127.0.0.1 -s " + IP_brook + " -p " + password + " --http"
    print("成功！  重置allocate")
    print("开始写入总运行脚本。。")
    try:
        a = open("temp_run\\run.bat","a")
        a.write(merge)
    except BaseException:
        print("写入失败")
        fun.wrong()
    print("成功！  写入成功")

elif tool == "ss":
    server = content_pre.split(":")[0]
    ip = content_pre.split(':')[1].split("%%")[0]
    password = content_pre.split('%%')[1]
    method = content_pre.split('%%')[2]
    print("成功！  重置allocate")
    print("开始写入总运行脚本。。")
    with open("temp_run\\ss\\gui-config.json", 'r') as load_f:
        load_dict = json.load(load_f)

    load_dict['configs'][0]['server'] = server
    load_dict['configs'][0]['server_port'] = ip
    load_dict['configs'][0]['password'] = password
    load_dict['configs'][0]['method'] = method

    with open("temp_run\\ss\\gui-config.json", "w") as dump_f:
        json.dump(load_dict, dump_f)
    a = open("temp_run\\run.bat","a")
    a.write("start ss\\ss.exe")

else:
    print("错误！  程序出现不可测的错误")

# new version end


time.sleep(3)
os.system("cls")
fun.succedd()
print("|-----------------------------------------------------|\n"
      "|                                                     |\n" 
      "|               Rattlemander Free VPN                 |\n"
      "|                  Version:" +  version +"                      |\n"
      "|-----------------------------------------------------|")
print("\n程序配置完成！")
fun.fence()
print("指令帮助：\n"
      "1. con: 连接VPN\n"
      "2. disc: 断开连接\n")

while True:
    a = input(">>> ")
    # 识别输入
    if a == "con":
        print("开始连接。。")
        print("设置代理。。")

        # new version change the brook mode IP number to adapt the ss account
        # ss stable IP: 127.0.0.1:1080

        proxy_connect("127.0.0.1:1080")
        os.system("run_it.bat")
        print("连接成功！")

        # nre version end


        fun.sys_say("如果想退出 VPN，请输入 disc 而不是直接关闭此窗口，否则可能会造成电脑无法联网的情况","注意！")
    if a == "disc":
        os.system("kill.bat")
        os.system("cls")
        a = 5
        while a > 0:
            print("成功退出VPN！")
            print("程序将在 " + str(a) + " 秒后关闭")
            a = a - 1
            time.sleep(1)
            os.system("cls")
        os._exit(0)