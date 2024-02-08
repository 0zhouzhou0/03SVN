import subSvn as svn
import SvnPath as p
import func as f
import writeword as wd
ls = "ls"
info = "info"
urls1 = p.svnUrl

ciurls = []  #提交路径
ci ={}       #提交路径及author




StartDate = 20240101
EndDate   = 20240201

StartDate = int(input("StartDate: "))
EndDate   = int(input("EndDate: "))


def projectpaths(urls):
    P = []
    for u in urls:
        allpath = svn.run_svn_command(ls,u)
        arryP2 = svn.strSimple(allpath)    #风场项目名字符串数组
        arryPaths = [ f.GenPath(u,s) for s in arryP2] #项目地址
        P = P+arryPaths
    return P

windpro = projectpaths(urls1)                       #所有项目地址
windproP1 = [p+"/"+"01 主控程序" for p in windpro]

# print("总项目： ")
# print(len(windproP1))

i=0
for Pr in windproP1:
    i = i+1
    print (i)    
    arryP01 = svn.run_svn_command(ls,Pr) 
    arryP02 = svn.strSimple(arryP01)    #解析 上传文件夹名 字符串

    targetFiles = f.datecheck(arryP02, StartDate, EndDate) #判断是否是日期内，输入参数解析的文件夹名 ,日期范围 ， 返回 符合日期的数组
    if targetFiles:
        targetPath = [f.GenPath(Pr,s) for s in targetFiles]    #生成存档地址
        ciurls = ciurls + targetPath  #提交路径
        print(targetPath)
    else:
        targetPath = None
       
#print(ciurls)           


#根据存档地址查询作者
for url in ciurls:
    infomation = svn.run_svn_command(info,url)
    au = svn.InfotoAuthor(infomation)
    ci[url] = au

wd.WriteWord(ci,StartDate, EndDate )

#根据CI生成表格
print("程序执行完成！请按下回车键退出...")
input()


#pyinstaller -F  -i i9.ico searchSVN.py
