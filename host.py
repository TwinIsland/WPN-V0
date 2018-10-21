def host():
    import os,fun
    try:
        c = open("host\\result","r")
        if str(c.read()) != "yes":
            import os
            os.system(r"copy C:\Windows\System32\drivers\etc\hosts host\\backup")
            a = open("C:\Windows\System32\drivers\etc\hosts","a")
            a.write("\n\n# add by Rattlemander VPN")
            a.write("\n104.16.248.1 doub.io")
            print("Hosts 文件添加成功！")
            b = open("host\\result","w")
            b.write("yes")
            print("成功！ 配置资源代理服务器")
        else:
            print("成功！ 配置资源代理服务器")
    except BaseException:
        print("错误！ 未能成功备份")
        fun.wrong()
