
import re
import random
import catch
import os

try:
    a = open("sc","r")
    con = str(a.read())
    reg_brook = r'text=brook://default(.{60})'
    wordreg = re.compile(reg_brook)
    brook_list = re.findall(wordreg,con)

    def vpn_num():
        count = 1
        for i in brook_list:
            count = count + 1
            return count

    def allocate():
        choose = random.randint(0, vpn_num()-1)
        return choose


    def allocate_line():
        count1 = 0
        num = allocate()
        for i in brook_list:
            if count1 == num:
                am = pre(i)
                return am
            count1 = count1 + 1


    def pre(i):
        str(i)
        i = i.split('"')[0]
        account = i.split("?20")[1].split("?")[0]
        door = i.split("?20")[1].split("?")[1]
        door = door[2:]
        password = i.split("?20")[2]
        merge = account + "%%" + door + "%%" + password
        return merge

    #   This line of code is for pick a adaptive allocation: print(allocate_line())

except BaseException:
    print("检测到程序问题，正在修复。。")
    import fun
    fun.fence()
    catch.catch()
    print("修复成功！ 重启软件后生效")
    input("回车后退出")
    os._exit(0)