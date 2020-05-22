# 读取Excel，并且输出返回值
import xlrd  # 导入xlrd模块


class ExcelData():
    def __init__(self, data_path, sheetname):
        self.data_path = data_path  # excle表格路径，需传入绝对路径
        self.sheetname = sheetname  # excle表格内sheet名
        self.data = xlrd.open_workbook(self.data_path)  # 打开excel表格
        self.table = self.data.sheet_by_name(self.sheetname)  # 切换到相应sheet
        self.keys = self.table.row_values(0)  # 第一行作为key值
        self.rowNum = self.table.nrows  # 获取表格行数
        self.colNum = self.table.ncols  # 获取表格列数
        # print(self.rowNum)
        # print(self.colNum)

    def readExcel(self):
        if self.rowNum < 2:
            print("excle内数据行数小于2")
        else:
            dicts = []  # 列表L存放取出的数据
            for i in range(1, self.rowNum):  # 从第二行（数据行）开始取数据
                sheet_data = {}  # 定义一个字典用来存放对应数据
                for j in range(self.colNum):  # j对应列值
                    sheet_data[self.keys[j]] = self.table.row_values(i)[j]  # 把第i行第j列的值取出赋给第j列的键值，构成字典
                dicts.append(sheet_data)  # 一行值取完之后（一个字典），追加到L列表中
            # print(type(L))
            return dicts

    # 获取角色，并输出对应的账号密码
    def rendUser(self, dicts_value, role_id):
        for dict_item in dicts_value:
            # print(dict_item)
            user = dict_item.get("角色")
            name = dict_item.get("工号")
            password = dict_item.get("密码")
            if user == role_id:
                # print(user,name,password)
                break
        return name, password, user


if __name__ == '__main__':
    # 文件的绝对路径
    # data_path = "C:/Users/pengshaui/PycharmProjects/OA/login.xlsx"
    data_path = "D:/公文文档/20200423办公用品适配财务编码任务清单(1).xlsx"
    # sheet名称
    # sheetname = "登录账户"
    sheetname = "人员信息（光华路736）"
    # 定义get_data对象
    get_data = ExcelData(data_path, sheetname)
    login_user = get_data.readExcel()
    print(login_user)

    for value in login_user:
        print(value)
        for key in value:
            print(key, value[key])

    # role = "台领导秘书"
    # xinx = get_data.rendUser(login_user,role)
    # print(xinx[0])
    # print(xinx[1])
    # print(xinx[2])
