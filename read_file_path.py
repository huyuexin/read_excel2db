# -*- coding:utf-8 -*-
import os
import xlrd
import xlwt

file_path = 'C:/Users/10369/PycharmProjects/file_excel/excel'
file_name = 'test.xls'
#遍历文件夹并存储文件名称
def eachfile(file_path):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    path_dir = os.listdir(file_path)
    i = 0
    for alldir in path_dir:
        #获取长目录
        child = os.path.join('%s%s' % (file_path, alldir))
        #获取文件名字的时候
        #child = str(alldir)

        sheet.write(i, 0, child)  # 第0行第0列写入内容
        i +=1
    wbk.save('test.xls')
#读取文件名
def readFile(filename):
    workbook = xlrd.open_workbook(filename)
    sheet2_name = workbook.sheet_names()
    print(sheet2_name)
    #从第一个表开始 或指定名字
    sheet2 = workbook.sheet_by_index(0)
    #sheet2 = workbook.sheet_by_name('sheet 1')
    print(sheet2.name, sheet2.nrows, sheet2.ncols)

    # 获取整行和整列的值（数组）
    # 第一行
    rows = sheet2.row_values(0)
    print(rows)
    #第一列
    cols = sheet2.col_values(0)
    print(cols)

    # 获取单元格内容
    #print(sheet2.cell(0, 0).value.encode('utf-8'))
    print(sheet2.cell(0, 0).value)
    print(sheet2.cell_value(0, 0))
    print(sheet2.row(0)[0].value)
    print(sheet2.col(0)[0].value)

    print(sheet2.cell(0,0).ctype)
#ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

readFile(file_name)


