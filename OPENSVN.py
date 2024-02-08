import svn.remote

svn_repo_url = "https://rdsvn.mywind.com.cn/svn/OffShoreControllerDepartment/工程项目-陆上/主控程序及相关文件/MySE_倍福项目-半直驱/100 MySE3.X项目/S1-20180037-华能河北涞源老虎山项目（3.0-145）/01 主控程序/20240205"
svn_username = 'YangZhongJie'
svn_password = 'mywind@2008'
#svn list --username YangZhongJie --password mywind@2008 "https://rdsvn.mywind.com.cn/svn/OffShoreControllerDepartment/工程项目-陆上/主控程序及相关文件/MySE_倍福项目-半直驱/100 MySE3.X项目/S1-20180037-华能河北涞源老虎山项目（3.0-145）/01 主控程序"

#svn info --username YangZhongJie --password mywind@2008 "https://rdsvn.mywind.com.cn/svn/OffShoreControllerDepartment/工程项目-陆上/主控程序及相关文件/MySE_倍福项目-半直驱/100 MySE3.X项目/S1-20180037-华能河北涞源老虎山项目（3.0-145）/01 主控程序/20240205"






def get_svn_folders(repo_url, username=None, password=None):
    try:
        cl = svn.remote.RemoteClient(repo_url, username=username, password=password)
        # 
        # i = cl.info()
        # print(i)
        # 获取 SVN 仓库目录列表
        entries = cl.list()

        # 提取所有文件夹名
        folders = [entry['name'] for entry in entries if 'name' in entry and 'kind' in entry and entry['kind'] == 'dir']
        
        return entries
        
        # 获取 SVN 仓库目录列表
        # entries = client.list(extended=True)
        # for entry in entries:
        #     print(entry)        
        # 提取所有文件夹名
        #folders = [entry['name'] for entry in entries if 'name' in entry and 'kind' in entry and entry['kind'] == 'dir']
        return folders
    except Exception as e:
        print(f"Error: {e}")
        return []

folders = get_svn_folders(svn_repo_url, svn_username, svn_password)

if folders:
    print("Folders in SVN repository:")
    for folder in folders:
        print(folder)
else:
    print("No folders found or an error occurred.")
