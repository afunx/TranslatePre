
class AndroidProject:

    def __init__(self, sheetname, rootpath):
        # excel表格中的sheet名字
        self.sheetName = sheetname
        # 项目跟路径
        self.rootPath = rootpath
        # excel sheet
        self.sheet = None

    def __str__(self):
        return 'sheetName: %s, rootPath: %s' %(self.sheetName, self.rootPath)