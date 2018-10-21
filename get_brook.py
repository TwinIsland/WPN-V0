
import re
import random

a = open("sc","r")
con = str(a.read())

reg = r'text=brook://default(.{60})'
wordreg = re.compile(reg)
wordreglist = re.findall(wordreg,con)

def vpn_num():
    count = 1
    for i in wordreglist:
        count = count + 1
        return count

def allocate():
    choose = random.randint(0, vpn_num()-1)
    return choose


def allocate_line():
    count1 = 0
    num = allocate()
    for i in wordreglist:
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

#   This line of code is for pick a adaptive allocation: print(allocate_line()
