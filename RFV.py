# -*- coding: gb2312 -*-
import os,host,get_brook,fun,catch,time,urllib.request,urllib,update_update,get_ss,random,json

def proxy_connect(ip):
    con = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable /t REG_DWORD /d 1 /f'
    os.system(con)
    con = 'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer /d "' + ip + '" /f'
    os.system(con)


def update_check():
    # try:
        print("�����¡���")
        if str(update_update.get_update().split("::")[0]) == str(fun.read_txt("version\\version.txt").split("::")[0]):
            print("�ɹ���  ������Ϊ���°汾")
        else:
            update_content = update_update.get_update()
            print("���������°汾��\n"
                  "���°汾��" + update_content.split("::")[0] + "\n"
                  "Ŀǰ�汾��" + fun.read_txt("version\\version.txt").split("::")[0] + "\n" 
                  "���ص�ַ��" + update_content.split("::")[2] + "\n"
                  "�ͷ�ʱ�䣺" + update_content.split("::")[1] + "\n"
                  "����˵����" + update_content.split("::")[4] + "\n"
                  "ǿ�Ƹ��£�" + update_content.split("::")[5])

            if update_content.split("::")[5] == "1":
                print("����ظ��º���ʹ�ã�")
                print("�س��˳�")
                input()
                os._exit(0)

            print("\n�س�����")
            input()
    # except BaseException:
    #     print("�޷��������·��񣬿�������Ϊ�����ļ���ʧ������������")
    #     print("�س�����")
    #     input()

def initial():
    try:
        a = open("version\\version.txt","r")
        ccc = str(a.read().split("::")[3])
    except FileNotFoundError:
        print("����  �ļ�������������������")
        fun.wrong()
    if ccc == "1":
        update_check()


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
        html_doc = "https://doub.io/sszhfx/"
        req = urllib.request.Request(html_doc)
        urllib.request.urlopen(req)
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

print("��ʼ��ȡ Brook & SS GFW Broker �˺�")

a = random.randint(0,3)
if a == 0:
    print("���䵽 Brook �˿�")
    print("������ȡ��ҳ���ݣ����Եȡ���")
    catch.catch()
    print("�ɹ���  ��ȡ�˺�")
    print("����ӿڡ���")
    allocate = str(get_brook.allocate()+1)
    num = str(get_brook.vpn_num())
    content_pre = get_brook.allocate_line()
    tool = "brook"
else:
    print("���䵽 SS �˿�")
    print("������ȡ��ҳ���ݣ����Եȡ���")
    catch.catch()
    print("�ɹ���  ��ȡ�˺�")
    print("����ӿڡ���")
    allocate = str(get_ss.allocate()+1)
    num = str(get_ss.vpn_num())
    content_pre = get_ss.allocate_line()
    tool = "ss"

print("�ӿ�������" + num + " | ����ӿڣ�" + allocate + " | ����������" + " | ������鷨")
print("�ɹ���  �ɹ������ӿ�����")
print("����Դ���롣��")

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
os.system("copy mode_ss.json temp_run\\ss\\gui-config.json")
print("�ɹ���  �ѽ�ģ���ĵ�д�������ĵ�")
print("�ٴν���allocate�ַ�������")


# new version begin: also need to write to the SS allocation fold

if tool == "brook":
    IP_brook = content_pre.split("%%")[0] + ":" + content_pre.split("%%")[1]
    password = content_pre.split("%%")[2]
    merge = "brook client -l 127.0.0.1:1080 -i 127.0.0.1 -s " + IP_brook + " -p " + password + " --http"
    print("�ɹ���  ����allocate")
    print("��ʼд�������нű�����")
    try:
        a = open("temp_run\\run.bat","a")
        a.write(merge)
    except BaseException:
        print("д��ʧ��")
        fun.wrong()
    print("�ɹ���  д��ɹ�")

elif tool == "ss":
    server = content_pre.split(":")[0]
    ip = content_pre.split(':')[1].split("%%")[0]
    password = content_pre.split('%%')[1]
    method = content_pre.split('%%')[2]
    print("�ɹ���  ����allocate")
    print("��ʼд�������нű�����")
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
    print("����  ������ֲ��ɲ�Ĵ���")

# new version end


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

        proxy_connect("127.0.0.1:1080")
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