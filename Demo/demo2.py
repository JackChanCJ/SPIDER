# coding=utf-8
__author__ = 'JACK_CHAN'

import xlrd
import string
"""
逻辑思路：
1、格式化单元格数据，
取消sheet中的所有合并单元格，excel自带功能，选中所有内容，点击"取消合并单元格" done

"""
class print_excel:
    def __init__(self, path, sheet_index = 0):
        self.path = path
        self.sheet_index = sheet_index
        self.wb = xlrd.open_workbook(self.path)
        self.sheet_names = self.wb.sheet_names()
        self.sheet = self.wb.sheet_by_index(self.sheet_index)
        self.nrows = self.sheet.nrows

    # 返回当前表格中的全部sheet名称
    def __str__(self):
        values = []
        for i in self.sheet_names:
            values.append(i)
        return "{}  其中全部sheet名为: {}".format(self.path, values)

    # 打印某张表某一列的所有值
    def print_xcol_value(self, col_index):
        xcol_value = self.sheet.col_values(col_index)
        for i in xcol_value:
            print (i)

    # 循环取两列值，交叉组合，格式化，变成需要的样子
    def format_cell(self, col1_index, col2_index):
        col1_values = self.sheet.col_values(col1_index)
        col2_values = self.sheet.col_values(col2_index)
        n = 0
        for i,j in zip(col1_values, col2_values):
            print (str(n) + "、" + i)
            print ('    ' + j.replace("\n", "\n    "))
            n = n + 1
            print ()

    # 升级版，打印某张表某一列的所有值
    def up_print_xcol_value(self, col_index):
        xcol_value = self.sheet.col_values(col_index)
        a_col = self.sheet.col_values(4)        # a_col列：操作步骤
        for i, j in zip(a_col, xcol_value):
            ln = "\n"
            a = i.count("\n")
            b = j.count("\n")
            c = a - b + 2
            print (j + c * ln)

    #----------------------------华丽的分割线----------------------------

    # 获取B列的值
    def get_B(self):
        B_value = self.sheet.col_values(1)
        return B_value

    # 获取C列的值
    def get_C(self):
        C_value = self.sheet.col_values(2)
        return C_value

    # 获取D列的值
    def get_D(self):
        D_value = self.sheet.col_values(3)
        return D_value

    # 获取E列的值
    def get_E(self):
        E_value = self.sheet.col_values(4)
        return E_value

    # 获取F列的值
    def get_F(self):
        F_value = self.sheet.col_values(5)
        return F_value

    def d_first_element(self, li):        # 删除li中的第一个元素
        li.pop(0)
        return li

    # 根据子模块、功能描述、测试方法，格式化为：子模块--功能描述(测试方法)
    def format_BCD(self):
        B_col = self.sheet.col_values(1)
        C_col = self.sheet.col_values(2)
        D_col =self.sheet.col_values(3)
        col_value = []
        for b, c, d in zip(B_col, C_col, D_col):
            a = b + '--' + '测试范围：' +c + '（' + d + '）'
            col_value.append(a)
            # print (b + '--' + '功能点：' +c + '(' + d + ')')        # 打印 所有格式化之后的值
        new_col = []
        for i in col_value:
            if i not in new_col:
                new_col.append(i)
                print (i)        # 打印 去除重复的值

    # 功能类似于format_BCD，不过这次生成的是树状结构
    def format_BCDE(self):

        new_B = self.d_first_element(self.get_B())
        new_C = self.d_first_element(self.get_C())
        new_D = self.d_first_element(self.get_D())
        new_E = self.d_first_element(self.get_E())
        new_F = self.d_first_element(self.get_F())
        x = 0
        for i, B, C, D, E, F in zip(range(self.nrows +1), new_B, new_C, new_D, new_E, new_F):
            # print ('打印出B列去除第一行之后的长度：' ,len(new_B))
            try:
                next_B = new_B[x + 1]

                CD = ('    ' + str(i +1) + '、' + C + '(' + D + ')')
                next_CD = ('    ' + str(i + 2) + '、' + new_C[x + 1] + '(' + new_D[x + 1] + ')')

                e = (E.lstrip(string.digits)).strip("、")

                if x < len(new_B):
                    # print (x, '---------', B)
                    # print(next_CD)
                    if x == 0:
                        print(B)
                if x < len(new_C):
                    if x == 0:
                        print(CD)
                    print ('         ' + e)


                    if B != next_B:
                        print('\n' + next_B)
                    if CD != next_CD:
                        print(next_CD)
                    print ('         ' + e)


            except IndexError:
                    print ("Error：超出了数组长度")
            x += 1

    def format_F(self):
        m = 0
        for i in self.get_F():
            m += 1
            print(m, i.lstrip(string.digits).strip('、'))



def main():
    path  = r"D:\02、项目文档\2018年项目\广汽三菱\广汽三菱车联网平台 - 检证资料\资料\04.结合测试成果物\GMMC.车联网平台-IT-003-结合测试CASE_V1.0.xls"
    D_APP = r"C:\Users\40846\Desktop\CASE\广汽三菱APP端系统测试测试案例.xls"
    D_OEM = r"C:\Users\40846\Desktop\CASE\广汽三菱车厂端格式化数据.xls"
    D_4S  = r"C:\Users\40846\Desktop\CASE\广汽三菱4S端系统测试测试用例.xls"
    E = print_excel(D_OEM, sheet_index=2)
    E.format_BCDE()
    new_F = E.d_first_element(E.get_F())
    m = 0
    for i in new_F:
        m += 1
        print(m, i.lstrip(string.digits).strip('、'))

if __name__ == '__main__':
    main()