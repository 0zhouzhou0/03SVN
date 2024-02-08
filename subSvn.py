import subprocess
import re

def run_svn_command(commands, svn_repo_url, svn_username = 'YangZhongJie', svn_password='mywind@2008'):
    try:
        # 使用 subprocess.run 执行 SVN 命令
        command = ['svn', commands, '--username', svn_username, '--password', svn_password, svn_repo_url]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        # 获取 SVN 命令的标准输出
        output = result.stdout
          
        return output
    except subprocess.CalledProcessError as e:
        # 如果命令执行出错，可以获取错误信息
        error_message = e.stderr
        print(f"Error executing SVN command: {error_message}")
        return None


#字符串解析：按/分割字符串,
def  strSimple(str):
    strs1 = str.split("/\n")
    strs = [s for s in strs1 if s != ""]
      
    return strs

def GenPath(p1,p2):
    p = p1+"/"+p2
    return p






# # 示例使用
# svn_repo_url = 'https://rdsvn.mywind.com.cn/svn/OffShoreControllerDepartment/工程项目-陆上/主控程序及相关文件/MySE_倍福项目-半直驱/100 MySE3.X项目'

# # 使用 SVN 命令获取仓库信息
# result_info = run_svn_command("ls",svn_repo_url)


# if result_info:
#     print("SVN Info:")
#     #print(result_info)
#     #print(type(result_info))  str
#     #print(strSimple(result_info))
    
#     strs=strSimple(result_info)
#     p = GenPath(svn_repo_url,strs[0])
#     # print(p)
#     # res = run_svn_command('ls',p)
#     # print(res)
    
    
#     p5 = GenPath(p,"01 主控程序")
#     w1 = run_svn_command('ls',p5)
#     w2 = strSimple(w1)
#     p2 = GenPath(p5,w2[0])
#     print(p2)
#     pt = run_svn_command('info',p2)
    
    
    
    
#     pattern = re.escape("Last Changed Author: ") + r'(.*?)' + re.escape("\n")
#     # 使用 re.search 查找匹配项
#     match = re.search(pattern, pt)
#     if match:
#         print(match.group(1))
#     else:
#         print('未匹配到author')
    
# else:
#     print("Failed to retrieve SVN info.")



def InfotoAuthor(info):
    pattern = re.escape("Last Changed Author: ") + r'(.*?)' + re.escape("\n")
    # 使用 re.search 查找匹配项
    match = re.search(pattern, info)
    if match:
        return match.group(1)
    else:
        print('未匹配到author')
        return None


