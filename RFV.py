# -*- coding: gb2312 -*-
import os,host,get_brook,fun,catch,time,urllib.request,urllib,update_update

def proxy_connect(ip):
    con = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f'
    os.system(con)
    con = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "' + ip + '" /f'
    os.system(con)


def update_check():
    try:
        print("�����¡���")
        if str(update_update.get_update().split("::")[0]) == str(fun.read_txt("version\\version.txt").split("::")[0]):
            print("�ɹ���  ������Ϊ���°汾")
        else:
            print("���������°汾��\n"
                  "���°汾��" + update_update.get_update().split("::")[0] + "\n"
                  "���ص�ַ��" + update_update.get_update().split("::")[2] + "\n"
                  "�ͷ�ʱ�䣺" + update_update.get_update().split("::")[1])
            print("\n�س�����")
            input()
    except BaseException:
        print("�޷��������·��񣬿�������Ϊ�����ļ���ʧ������������")
        print("�س�����")
        input()

def initial():
    try:
        a = open("version\\version.txt","r")
        ccc = str(a.read().split("::")[3])
        if ccc == "1":
            update_check()
    except FileNotFoundError:
        print("����  �ļ�������������������")
        fun.wrong()

    print("���host�ļ������ԡ���")
    host.host()
    print("����ļ���Ҫ���ݵ㡣��")
    if fun.dir("host","backup"):
        print("�ɹ��� ���ݳ�����Ҫ���ݵ�")
    else:
        try:
            os.system(r"copy C:\Windows\System32\drivers\etc\hosts host\\backup")
            print("�ɹ��� ���ݳ�����Ҫ���ݵ�")
        except BaseException:
            print("���� δ�ܳɹ�����")
            fun.wrong()
    print()
    time.sleep(1)
    print("����������ЧӦ������")
    try:
        urllib.request.Request("https://example.com")
    except BaseException:
        print("����  �������ô���")
        fun.wrong()
    else:
        print("�ɹ���  ��������ɹ�")
    fun.fence()

# ��ʼ��ϵͳ
os.system("kill.bat")

# ��ʼ
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
print("\n��ȡ��ʼ")
fun.fence()



## new version begin: more way allocation: ss


print("��ʼ��ȡ Brook GFW Broker �˺�")
print("������ȡ��ҳ���ݣ����Եȡ���")
catch.catch()
print("�ɹ���  ��ȡ�˺�")
print("����ӿڡ���")
a = str(get_brook.allocate()+1)
num = str(get_brook.vpn_num())
print("�ӿ�������" + num + " | ����ӿڣ�" + a + " | ����������" + " | ������鷨")
print("�ɹ���  �ɹ������ӿ�����")
print("����Դ���롣��")
content_pre = get_brook.allocate_line()
try:
    print("�ɹ���  �����ɹ�")
    print("���ڽӿڣ�" + content_pre)
except BaseException:
    print("����  �����쳣")
    fun.wrong()
time.sleep(3)


# new version end


os.system("cls")
print("|-----------------------------------------------------|\n"
      "|                                                     |\n" 
      "|               Rattlemander Free VPN                 |\n"
      "|                  Version:" +  version +"                      |\n"
      "|-----------------------------------------------------|")
print("\n����������")
fun.fence()
print("�������ģ���ĵ�����")
try:
    a = open("mode","r")
except FileNotFoundError:
    print("����  �����ҵ�ģ���ĵ�")
    fun.wrong()
print("�ɹ���  ���ҵ������ĵ�")
print("��ʼ����ģ���ĵ�����")
os.system("copy mode temp_run\\run.bat")
print("�ɹ���  �ѽ�ģ���ĵ�д�������ĵ�")
print("�ٴν���allocate�ַ�������")


# new version begin: also need to write to the SS allocation fold


IP_brook = content_pre.split("%%")[0] + ":" + content_pre.split("%%")[1]
password = content_pre.split("%%")[2]
merge = "brook client -l 127.0.0.1:8080 -i 127.0.0.1 -s " + IP_brook + " -p " + password + " --http"
print("�ɹ���  ����allocate")
print("��ʼд�������нű�����")
try:
    a = open("temp_run\\run.bat","a")
    a.write(merge)
except BaseException:
    print("д��ʧ��")
    fun.wrong()
print("�ɹ���  д��ɹ�")


# nre version end


time.sleep(3)
os.system("cls")
fun.succedd()
print("|-----------------------------------------------------|\n"
      "|                                                     |\n" 
      "|               Rattlemander Free VPN                 |\n"
      "|                  Version:" +  version +"                      |\n"
      "|-----------------------------------------------------|")
print("\n����������ɣ�")
fun.fence()
print("ָ�������\n"
      "1. con: ����VPN\n"
      "2. disc: �Ͽ�����\n")

while True:
    a = input(">>> ")
    # ʶ������
    if a == "con":
        print("��ʼ���ӡ���")
        print("���ô�����")

        # new version change the brook mode IP number to adapt the ss account
        # ss stable IP: 127.0.0.1:1080

        proxy_connect("127.0.0.1:8080")
        os.system("run_it.bat")
        print("���ӳɹ���")

        # nre version end


        fun.sys_say("������˳� VPN�������� disc ������ֱ�ӹرմ˴��ڣ�������ܻ���ɵ����޷����������","ע�⣡")
    if a == "disc":
        os.system("kill.bat")
        os.system("cls")
        a = 5
        while a > 0:
            print("�ɹ��˳�VPN��")
            print("������ " + str(a) + " ���ر�")
            a = a - 1
            time.sleep(1)
            os.system("cls")
        os._exit(0)