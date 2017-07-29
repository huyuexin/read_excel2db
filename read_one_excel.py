# -*- coding:utf-8 -*-
import sqlite3
import xlrd

check_name = {
    #搜索的名字：【找到之后行增加，列增加】
    '单位': ['0','2'],
    '部门': ['0','2'],
    '学历': ['1','0'],
    '年度考核情况':['0','2']
}
file_name = 'C:/Users/10369/PycharmProjects/file_excel/excel/胡跃新.xls'
import sqlite3
def creat_newdate():

    connection = sqlite3.connect('test.sqlite')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE newdate (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    
                    keys TEXT NOT NULL,
                    val TEXT NOT NULL)""")

    connection.commit()
    connection.close()

def writer_date(filename):

    connection = sqlite3.connect('test.sqlite')
    cursor = connection.cursor()
    workbook1 = xlrd.open_workbook(filename)
    sheet2_name = workbook1.sheet_names()
    print(sheet2_name)
    #从第一个表开始 或指定名字
    sheet2 = workbook1.sheet_by_index(0)

    for r in range(sheet2.nrows):
        for c in range(sheet2.ncols):
            key = sheet2.cell(r, c).value

            if key in check_name.keys():
                v = check_name.get(key, 'nofound')
                print(file_name)
                print(key)
                print(sheet2.cell(r + int(v[0]), c + int(v[1])).value)
                new_value = sheet2.cell(r + int(v[0]), c + int(v[1])).value
                cursor.execute("INSERT INTO newdate (keys,val) VALUES (?,?)", (key, new_value))
                connection.commit()

    connection.close()
def read_newdate():
    connection = sqlite3.connect('test.sqlite')
    cursor = connection.cursor()
    results= cursor.execute("""SELECT * FROM newdate""")
    response =[ row[0] for row in results.fetchall()]
    connection.close()
    print('11111')

    print(response)


#creat_newdate()
writer_date(file_name)
read_newdate()

