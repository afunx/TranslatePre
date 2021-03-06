#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import os
import xlsxwriter

from model.androidproject import AndroidProject
from model.androidmodule import AndroidModule
import constant.androidconstant as AndroidConstant

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
        project.sheet.set_column('H:H', 50)
        project.sheet.set_column('I:I', 50)
        project.sheet.set_column('J:J', 50)
        project.sheet.set_column('K:K', 50)
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
                if line is not None:
                    sheet.write(line, column, text)
                else:
                    print("WARNING:: textid: " + textid + " is invalid")

            elif child.tag == "string-array":
                childlist = list(child)
                for item in childlist:
                    textid = module + "$" + child.attrib["name"] + "$string-array$" + str(childlist.index(item))
                    text = item.text
                    line = iddict.get(textid)
                    if line is not None:
                        sheet.write(line, column, text)
                    else:
                        print("WARNING:: textid: " + textid + " is invalid")

            elif child.tag == "plurals":
                childlist = list(child)
                for item in childlist:
                    textid = module + "$" + child.attrib["name"] + "$plurals$" + item.attrib["quantity"]
                    text = item.text
                    line = iddict.get(textid)
                    sheet.write(line, column, text)

    return

def generatesheet(project):
    # “strings.xml” “strings_untranslated.xml” 等
    stringslist = AndroidConstant.getStringXmlFileNameList()
    #  "values.xml" "values-en.xml" 等
    valueslist = AndroidConstant.getValueXmlFileNameList()

    # Module列表的列表, modulelist[0]为values文件下的全部Target, modulelist[1]为values-en文件夹下的全部Module
    # Module的path为文件路径, Module的module为模块
    modulelist = list()

    for i in range(len(valueslist)):
        modulelist.append(list())

    # 根据语言对文件进行分类
    print("generatesheet() 应用路径: " + project.rootPath)
    for root, dirs, files in os.walk(project.rootPath):
        for file in files:
            if file in stringslist:
                path = (root + "/" + file).replace("/", "\\")
                pathsplit = path.split("\\")
                index = valueslist.index(pathsplit[-2])
                module = pathsplit[-6]
                modulelist[index].append(AndroidModule(path, module))
                print("generatesheet() 目标文件: " + path + ", index: " + str(index) + ", module: " + module)

    # id索引
    iddict = dict()
    # 处理values
    column = 0
    # (0,0)写id
    project.sheet.write(0, 0, "id")
    for targets in modulelist:
        if len(targets) == 0:
            continue
        column = column + 1
        project.sheet.write(0, column, valueslist[modulelist.index(targets)])
        for target in targets:
            # 只有strings可以修改iddict
            modify = column == 1
            fillsheet(project, target, iddict, column, modify)
    return

def main():
    # 获取文件列表
    projectlist = AndroidProject.getAndroidProjectList()
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