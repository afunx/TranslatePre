
# refer to https://www.cnblogs.com/insane-Mr-Li/p/9963875.html

# tag：string对象，表示数据代表的种类，当为节点时为节点名称。

# text：string对象，表示element的内容。

# attrib：dictionary对象，表示附有的属性。

# tail：string对象，表示element闭合之后的尾迹。

# <tag attrib1=1>text</tag>tail

import os
import xml.etree.ElementTree as ET
import xlsxwriter

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
        if child.tag == "string":
            print("string.name is " + child.attrib["name"] + ", text is " + child.text)

        if child.tag == "string-array":
            childlist = list(child)
            for item in childlist:
                print("string-array item is " + child.attrib["name"]
                      + ", index is " + str(childlist.index(item))
                      + ", text is " + item.text)

        if child.tag == "plurals":
            childlist = list(child)
            for item in childlist:
                print("plurals item is " + child.attrib["name"]
                      + ", quantity is " + item.attrib["quantity"]
                      + ", text is " + item.text)
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


# parsexml("../mock/strings.xml")
# test()
testlistdir("../mock")
# testxlsxwriter("d:\\abc.xlsx")