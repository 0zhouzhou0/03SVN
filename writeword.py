from win32com.client import Dispatch
import re


def repath(path):
    # 匹配两个-之间的字符
    match_result = re.search(r'/([^/]+?)/01 主控程序', path)
    p = match_result.group(1)
    return p

def WriteWord(ci, startdate, enddate):
    namelist = []
    for x in ci :
        if ci[x] not in namelist:
            namelist.append(ci[x])
                
    # 创建Word应用程序对象
    word_app = Dispatch("Word.Application")
    # 创建一个新的文档
    doc = word_app.Documents.Add()
    # 显示Word应用程序
    word_app.Visible = True

    table = doc.Tables.Add(doc.Range(), len(ci)+1, 4)  # 在文档的开头插入一个表格
    table.Borders.Enable = True  # 启用表格的边框
    table.Columns(1).Width = 35
    table.Columns(3).Width = 180
    table.Columns(4).Width = 80

    table.Cell(1, 1).range.text = "序号"
    table.Cell(1, 2).range.text = "项目"
    table.Cell(1, 3).range.text = "存档" 
    table.Cell(1, 4).range.text = "author"

    i = 2 
    for n in namelist:
        for path in ci:
            if n == ci[path]:
                table.Cell(i, 1).range.text = i-1 
                table.Cell(i, 2).range.text = repath(path)
                table.Cell(i, 3).range.text = path    #路径
                table.Cell(i, 4).range.text = n
                i +=1


    wordname = "程序下发总结-"+str(startdate)+"-"+str(enddate)
    doc.SaveAs(wordname)
    print(wordname)
        # 关闭 Word 文档
        #doc.Close()
