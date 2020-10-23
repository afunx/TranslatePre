
class AndroidModule:

    def __init__(self, path, module):
        # 目标文件路径
        self.path = path
        # 目标文件模块
        self.module = module

    def __str__(self):
        return 'path: %s, module: %s' %(self.path, self.module)