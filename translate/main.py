#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

class Target:
    # 目标文件路径
    path = ""
    # 目标文件模块
    module = ""

    def __init__(self, path, module):
        self.path = path
        self.module = module

    def __str__(self):
        return 'path: %s, module: %s' %(self.path, self.module)

def createproject():
    projectlist = list()
    project1 = Project("屏保", "D:\\Code\\Android\\aimbot\\AimbotScreenDisplay")
    projectlist.append(project1)
    project2 = Project("用户管理", "D:\\Code\\Android\\aimbot\\AndroidService_UserMgr")
    projectlist.append(project2)
    project3 = Project("开机向导", "D:\\Code\\Android\\aimbot\\AndroidService_BootWizard")
    projectlist.append(project3)
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
        project.sheet.set_column('G:G', 50)
    return

def printboundary(str):
    print("=======================================" + str + "=======================================")
    return

def fillsheet(project, target, iddict, column, modify):
    file = target.path
    module = target.module

    sheet = project.sheet
    tree = ET.parse(file)
    root = tree.getroot()

    line = len(iddict)

    for child in root:

        if modify:
            if child.tag == "string":
                line = line + 1
                textid = module + "$" + child.attrib["name"]
                text = child.text
                iddict[textid] = line
                sheet.write(line, 0, textid)
                sheet.write(line, column, text)

            elif child.tag == "string-array":
                childlist = list(child)
                for item in childlist:
                    line = line + 1
                    textid = module + "$" + child.attrib["name"] + "$string-array$" + str(childlist.index(item))
                    text = item.text
                    iddict[textid] = line
                    sheet.write(line, 0, textid)
                    sheet.write(line, column, text)

            elif child.tag == "plurals":
                childlist = list(child)
                for item in childlist:
                    line = line + 1
                    textid = module + "$" + child.attrib["name"] + "$plurals$" + item.attrib["quantity"]
                    text = item.text
                    iddict[textid] = line
                    sheet.write(line, 0, textid)
                    sheet.write(line, column, text)

        else:
            if child.tag == "string":
                textid = module + "$" + child.attrib["name"]
                text = child.text
                line = iddict.get(textid)
                sheet.write(line, column, text)

            elif child.tag == "string-array":
                childlist = list(child)
                for item in childlist:
                    textid = module + "$" + child.attrib["name"] + "$string-array$" + str(childlist.index(item))
                    text = item.text
                    line = iddict.get(textid)
                    sheet.write(line, column, text)

            elif child.tag == "plurals":
                childlist = list(child)
                for item in childlist:
                    textid = module + "$" + child.attrib["name"] + "$plurals$" + item.attrib["quantity"]
                    text = item.text
                    line = iddict.get(textid)
                    sheet.write(line, column, text)

    return

def generatesheet(project):
    valueslist = list()
    valueslist.append("values")
    valueslist.append("values-en")
    valueslist.append("values-zh-rCN")
    valueslist.append("values-zh-rTW")
    valueslist.append("values-th-rTH")
    valueslist.append("values-ko-rKR")
    # Target列表的列表, targetlist[0]为values文件下的全部Target, targetlist[1]为values-en文件夹下的全部Target
    # Target的path为文件路径, Target的module为模块
    targetlist = list()
    # 行
    i = 0
    # 列
    j = 0
    # 第一行写列名
    project.sheet.write(i, j, "id")
    for values in valueslist:
        targetlist.append(list())
        j = j + 1
        project.sheet.write(i, j, values)

    # 根据语言对文件进行分类
    print("generatesheet() 应用路径: " + project.rootPath)
    for root, dirs, files in os.walk(project.rootPath):
        for file in files:
            if file == "strings.xml" or file == "strings_untranslated.xml":
                path = (root + "/" + file).replace("/", "\\")
                pathsplit = path.split("\\")
                index = valueslist.index(pathsplit[-2])
                module = pathsplit[-6]
                targetlist[index].append(Target(path, module))
                print("generatesheet() 目标文件: " + path + ", index: " + str(index) + ", module: " + module)

    # id索引
    iddict = dict()
    # 处理values
    for targets in targetlist:
        column = targetlist.index(targets) + 1
        for target in targets:
            # 只有strings可以修改iddict
            modify = column == 1
            fillsheet(project, target, iddict, column, modify)
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

main()