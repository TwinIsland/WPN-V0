# -*- coding: gb2312 -*-
import urllib.request,re

def catch():
    import fun
    try:

        # д��brook ����
        # ���÷�����������
        print("��ʼ����ͨ���˺š���")
        a = open("sc", "w")
        html_doc = "https://doub.io/sszhfx/"
        req = urllib.request.Request(html_doc)
        webpage = urllib.request.urlopen(req)
        html = webpage.read()
        a.write(str(html))
        print("�ɹ��� ����ͳ���˺�")


        # ����ss�˺ŵ�ַ����Ҫ������������
        # ������������
        a = open("sc", "a")
        print("��ʼ����SS����������ַ����")
        # �ָ���
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
        # �ٴ�catch
        ss_list = []
        for i in ss_list_fake:
            html_doc = "https://doub.pw/qr/qr.php?text=ss://" + i
            req = urllib.request.Request(html_doc)
            webpage = urllib.request.urlopen(req)
            html = str(webpage.read())
            a = open("sc", "a")
            a.write("========================")
            a.write(str(html))
        print("�ɹ��� ����SS�˺�")

    except BaseException:
        print("����  ������������Դ��վ")
        fun.wrong()