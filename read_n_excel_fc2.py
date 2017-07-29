# -*- coding:utf-8 -*-
import os
import sqlite3
import xlrd
db_name = 'party2.sqlit'
#建立数据库存储  注意只建立一次
def creat_newdate(dbname):
    connection = sqlite3.connect('party2.sqlite')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE newdate (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        xingming TEXT NOT NULL,
        jiguang TEXT NOT NULL,
        ziwu TEXT NOT NULL,
        daibiao TEXT NOT NULL);''')

    connection.commit()
    connection.close()


#遍历文件夹并存储文件名称list
def eachfile(file_path):
    path_dir = os.listdir(file_path)
    i = 0
    alldirs =[]
    shotnames =[]

    for alldir in path_dir:
        #获取长目录
        child = os.path.join('%s/%s' % (file_path, alldir))
        #获取文件名字的时候
        alldirs.append(child)
        shotname = GetFileNameAndExt(alldir)
        shotnames.append(shotname[0])
        i +=1
    return alldirs,shotnames


#根据文件名，如  胡跃新.xls   = (胡跃新 , xls)拆分文件名和扩展名
def GetFileNameAndExt(filename):
    (filepath,tempfilename) = os.path.split(filename)
    (shotname,extension) = os.path.splitext(tempfilename)
    return shotname,extension

#根据文件地址读取表格后， 根据check——name 匹配数据后输入数据库

def writer_date(filename):
    connection = sqlite3.connect('party2.sqlite')
    cursor = connection.cursor()
    workbook1 = xlrd.open_workbook(filename)
    #从第一个表开始 或指定名字
    sheet2 = workbook1.sheet_by_index(0)
    xingming = sheet2.cell(2, 1).value
    jiguang= sheet2.cell(2, 11).value
    ziwu= sheet2.cell(4, 3).value
    daibiao= sheet2.cell(9, 4).value
    cursor.execute("INSERT INTO newdate (xingming,jiguang,ziwu,daibiao) VALUES (?,?,?,?)",(xingming,jiguang,ziwu,daibiao))
    connection.commit()
#
#    for r in range(sheet2.nrows):
#        for c in range(sheet2.ncols):
 #           key = sheet2.cell(r, c).value
 #           for check_name_find in check_name.keys():
#                if key == check_name_find:
#                    v = check_name.get(key, 'nofound')
 #                   new_value = sheet2.cell(r + int(v[0]), c + int(v[1])).value
#                    cursor.execute("INSERT INTO newdate (ids,keys,new_value,names) VALUES (?,?,?,?)", (ids,check_name_find,new_value,names))
 #                   connection.commit()

    connection.close()





