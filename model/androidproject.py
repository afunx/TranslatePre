
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

    @classmethod
    def getAndroidProjectList(cls):
        # 是否为巡检版
        patrol = True
        projectlist = list()
        if patrol:
            project1 = AndroidProject("OTA升级", "D:\\Code\\Android\\aimbot\\AndroidService_OTA")
            projectlist.append(project1)
            project2 = AndroidProject("电源管理", "D:\\Code\\Android\\aimbot\\AimbotPower")
            projectlist.append(project2)
            project3 = AndroidProject("用户管理", "D:\\Code\\Android\\aimbot\\AndroidService_UserMgr")
            projectlist.append(project3)
            project4 = AndroidProject("设置", "D:\\Code\\Android\\aimbot\\AndroidService_Setting")
            projectlist.append(project4)
            project5 = AndroidProject("Launcher", "D:\\Code\\Android\\aimbot\\PatrolIndoorLanucher")
            projectlist.append(project5)
            project6 = AndroidProject("ApiRunner", "D:\\Code\\Android\\aimbot\\AndroidService_DemoCode")
            projectlist.append(project6)
            project7 = AndroidProject("开机向导", "D:\\Code\\Android\\aimbot\\AndroidService_BootWizard")
            projectlist.append(project7)
            project8 = AndroidProject("硬件诊断", "D:\\Code\\Android\\aimbot\\AndroidService_CruzrDoctor")
            projectlist.append(project8)
            project9 = AndroidProject("系统检测", "D:\\Code\\Android\\aimbot\\AndroidService_SystemFaultDetection")
            projectlist.append(project9)
            project10 = AndroidProject("地图", "D:\\Code\\Android\\aimbot\\AndroidService_Navigation")
            projectlist.append(project10)
            project10 = AndroidProject("屏保", "D:\\Code\\Android\\aimbot\\AimbotScreenDisplay")
            projectlist.append(project10)
            project11 = AndroidProject("系统自检", "D:\\Code\\Android\\aimbot\\AimbotSelfInspection")
            projectlist.append(project11)
        else:
            project1 = AndroidProject("OTA升级", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_OTA")
            projectlist.append(project1)
            project2 = AndroidProject("电源管理", "D:\\Code\\Android\\aimbot-prevention\\AimbotPower")
            projectlist.append(project2)
            project3 = AndroidProject("用户管理", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_UserMgr")
            projectlist.append(project3)
            project4 = AndroidProject("设置", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_Setting")
            projectlist.append(project4)
            project5 = AndroidProject("Launcher", "D:\\Code\\Android\\aimbot-prevention\\PatrolIndoorLanucher")
            projectlist.append(project5)
            project6 = AndroidProject("ApiRunner", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_DemoCode")
            projectlist.append(project6)
            project7 = AndroidProject("防疫应用", "D:\\Code\\Android\\aimbot-prevention\\AimbotPrevention")
            projectlist.append(project7)
            project8 = AndroidProject("开机向导", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_BootWizard")
            projectlist.append(project8)
            project9 = AndroidProject("硬件诊断", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_CruzrDoctor")
            projectlist.append(project9)
            project10 = AndroidProject("系统检测", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_SystemFaultDetection")
            projectlist.append(project10)
            project11 = AndroidProject("地图", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_Navigation")
            projectlist.append(project11)
            project12 = AndroidProject("SkillLauncher", "D:\\Code\\Android\\aimbot-prevention\\AndroidService_SkillLauncher")
            projectlist.append(project12)
        return projectlist