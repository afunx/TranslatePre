#!/usr/bin/python
# -*- coding: UTF-8 -*-


# refer to https://www.cnblogs.com/insane-Mr-Li/p/9963875.html

# tag：string对象，表示数据代表的种类，当为节点时为节点名称。

# text：string对象，表示element的内容。

# attrib：dictionary对象，表示附有的属性。

# tail：string对象，表示element闭合之后的尾迹。

# <tag attrib1=1>text</tag>tail

import xml.etree.ElementTree as ET
import os
import xlsxwriter


class Project:
    # excel表格中的sheet名字
    sheetName = ""
    # 项目跟路径
    rootPath = ""
    # excel sheet
    sheet = None

    def __init__(self, sheetname, rootpath):
        self.sheetName = sheetname
        self.rootPath = rootpath

    def __str__(self):
        return 'sheetName: %s, rootPath: %s' %(self.sheetName, self.rootPath)

def readfile(path):
    print("readfile() path: " + path)
    file = open(path, "r")
    content = file.read()
    print("readfile() content: " + content)
    file.close()
    return


def parsexml(path):
    tree = ET.parse(path)
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)
        str1 = "tag is " + child.tag
        print(str1)
        str2 = "attrib.name is " + child.attrib["name"]
        print(str2)
        str3 = "text is " + child.text
        print(str3)
        break
    return


def test() -> None:
    list1 = []
    list1.append("中国")
    list1.append("china")
    list2 = []
    list2.append("水果")
    list2.append("fruit")
    dict = {}
    dict['nation'] = list1
    dict['food'] = list2

    for key in dict.keys():
        print("key: " + key)
        for value in dict[key]:
            print("value: " + value)
    return


def testlistdir(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "strings.xml":
                print(root)
                print(dirs)
                print(file)
                target = (root + "\\" + file).replace("/", "\\")
                print(target)
                parsexml(target)
    return


def testxlsxwriter(path):
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet('testSheet')
    worksheet.write(2, 2, "22")
    worksheet.write(3, 3, "33")
    workbook.close()
    return

def createproject():
    projectlist = list()
    project1 = Project("屏保", "D:\\Code\\Android\\aimbot\\AimbotScreenDisplay")
    projectlist.append(project1)
    project2 = Project("用户管理", "D:\\Code\\Android\\aimbot\\AndroidService_UserMgr")
    # projectlist.append(project2)
    return projectlist

def createsheets(workbook, projectlist):
    for project in projectlist:
        project.sheet = workbook.add_worksheet(project.sheetName)
        # 修改sheet的列宽
        project.sheet.set_column('A:A', 40)
        project.sheet.set_column('B:B', 50)
        project.sheet.set_column('C:C', 50)
        project.sheet.set_column('D:D', 50)
        project.sheet.set_column('E:E', 50)
        project.sheet.set_column('F:F', 50)
    return

def printboundary(str):
    print("=======================================" + str + "=======================================")
    return

def fillsheet(sheet, file, iddict, column, modify):
    tree = ET.parse(file)
    root = tree.getroot()

    line = len(iddict)

    print(sheet)

    for child in root:

        if modify:
            line = line + 1
            iddict[child.attrib["name"]] = line
            sheet.write(line, 0,  child.attrib["name"])
            sheet.write(line, column, child.text)

        else:
            line = iddict.get(child.attrib["name"])
            sheet.write(line, column, child.text)
    return

def generatesheet(project):
    valueslist = list()
    valueslist.append("values")
    valueslist.append("values-en")
    valueslist.append("values-zh-rCN")
    valueslist.append("values-zh-rTW")
    valueslist.append("values-th-rTH")
    # 文件列表的列表, fileslist[0]为values文件下的全部文件, fileslist[1]为values-en文件夹下的全部文件
    fileslist = list()
    # 行
    i = 0
    # 列
    j = 0
    # 第一行写列名
    project.sheet.write(i, j, "id")
    for values in valueslist:
        fileslist.append(list())
        j = j + 1
        project.sheet.write(i, j, values)

    # 根据语言对文件进行分类
    print("generatesheet() 应用路径: " + project.rootPath)
    for root, dirs, files in os.walk(project.rootPath):
        for file in files:
            if file == "strings.xml" or file == "strings_untranslated.xml":
                target = (root + "/" + file).replace("/", "\\")
                targetsplit = target.split("\\")
                index = valueslist.index(targetsplit[-2])
                fileslist[index].append(target)
                print("generatesheet() 目标文件: " + target + ", index: " + str(index))

    # id索引
    iddict = dict()
    # 处理values
    for files in fileslist:
        column = fileslist.index(files) + 1
        for file in files:
            # 只有strings可以修改iddict
            modify = column == 1
            fillsheet(project.sheet, file, iddict, column, modify)
    return

def main():
    # 获取文件列表
    projectlist = createproject()
    printboundary("获取项目名字和路径")
    for project in projectlist:
        print(project)

    # 创建xlsx
    workbook = xlsxwriter.Workbook("D:/result.xlsx")
    # 创建sheet列表
    createsheets(workbook, projectlist)
    # 处理每个项目
    for project in projectlist:
        printboundary("<" + project.sheetName + ">")
        generatesheet(project)

    workbook.close()
    return

# parsexml("d:\strings_untranslated.xml")
# test()
# testlistdir("d:/Code/Android/aimbot/AndroidService_Setting")
# testxlsxwriter("d:\\abc.xlsx")

main()