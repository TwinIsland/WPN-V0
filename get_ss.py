## ss example : ss = "Y2hhY2hhMjA6ZG91Yi5pby9zc3poZngvKjYzMjdANjQuMTM3LjI1MS4xNDE6NjMyNw"
import re
import random
import base64

# ss账号的特殊性：必须解密使用
def decode_base64(data):
    missing_padding = (4 - len(data) % 4) % 4
    if missing_padding:
        data += "=" * missing_padding
    return base64.b64decode(data).decode()

def ss_list():
    # 分割总 source code 文件下的有效ss账号源码快
    a = open("sc", "r")
    con = str(a.read())
    ss_real_part = con.split("mynameiswyattandhelloworld")[1]
    # 所有有关联的ss账号 （因为网站有超链接，源码中每个ss账号会重复两遍，所以不能直接使用）
    reg_ss = r'href="ss://(.{100})'
    wordreg = re.compile(reg_ss)
    ss_list_pre = []
    for i in re.findall(wordreg, con):
        ss_list_pre.append(i.split('"')[0])

    count = 0
    # 找到实际ss账号的数量
    while True:
        try:
            trash = ss_real_part.split("========================")[count]
            count =count + 1
        except IndexError:
            trash_2 = ""
            break
    # 如果程序不出错的话，每个ss对应的子域名对应有两个ss码，所以，取奇数舍偶数（注意：千万不能舍偶求奇，不然爬取的ss账号会少一个）
    ss_list = []
    for i in range(1,(count -1)):
        if i%2 == 1:
            # 解码插入
            # 实例：chacha20:doub.io/sszhfx/*1498@45.62.238.147:1
            ss_list.append(decode_base64(ss_list_pre[i]))
            i = + 1
        else:
            i = + 1
    return ss_list



# 和解析brook的方法相同
def vpn_num():
    count = 1
    for i in ss_list():
        count = count + 1
        return count

def allocate():
    choose = random.randint(0, vpn_num()-1)
    return choose


def allocate_line():
    count1 = 0
    num = allocate()
    for i in ss_list():
        if count1 == num:
            am = pre(i)
            return am
        count1 = count1 + 1


def pre(i):
    str(i)
    pass_way = i.split(":")[0]
    password = i.split(":")[1].split("@")[0]
    server = i.split("@")[1]
    merge = server + "%%" + password + "%%" + pass_way
    return merge

print(allocate_line())
#   This line of code is for pick a adaptive allocation: print(allocate_line())
