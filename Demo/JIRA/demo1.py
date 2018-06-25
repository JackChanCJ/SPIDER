# coding=utf-8
__author__ = 'JACK_CHAN'

import xlrd

class LoadBaiduSearchTestData:
    def __init__(self, path):
        self.path = path
    def load_data(self):
        excel = xlrd.open_workbook(self.path)
        table = excel.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        test_data = []
        for i in range(1, nrows):
            test_data.append(table.row_values(i))
        return test_data
    def get_sheet_names(self):
        work_book = xlrd.open_workbook(self.path)
        sheet_names = work_book.sheet_names()
        return sheet_names


def main():
    path = r"D:\02、项目文档\2018年项目\广汽三菱\广汽三菱车联网平台 - 检证资料\资料\04.结合测试成果物\GMMC.车联网平台-IT-003-结合测试CASE_V1.0.xls"
    A = LoadBaiduSearchTestData(path)
    for i in A.get_sheet_names():
        print (i)



if __name__ == '__main__':
    main()