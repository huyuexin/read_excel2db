# -*- coding:utf-8 -*-
import os
import sqlite3
import xlrd
db_name = 'party1.sqlit'
#建立数据库存储  注意只建立一次
def creat_newdate(dbname):
    connection = sqlite3.connect('party1.sqlite')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE newdate (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        xingming TEXT NOT NULL,
        suozaidangzhibu TEXT NOT NULL,
        shengfenzheng TEXT NOT NULL,
        xingbie TEXT NOT NULL,
        mignzu TEXT NOT NULL,
        chushengriqi DATE NOT NULL,
        xueli TEXT NOT NULL,
        renyuanleibie TEXT NOT NULL,
        rudangshijian DATE NOT NULL,
        zhengshidangyuan TEXT NOT NULL,
        gongzuoganwei TEXT NOT NULL,
        shoujihao TEXT NOT NULL,
        dianhua TEXT NOT NULL,
        jiatingdizhi TEXT NOT NULL);''')

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
    connection = sqlite3.connect('party1.sqlite')
    cursor = connection.cursor()
    workbook1 = xlrd.open_workbook(filename)
    #从第一个表开始 或指定名字
    sheet2 = workbook1.sheet_by_index(0)
    xingming = sheet2.cell(2, 1).value
    suozaidangzhibu= sheet2.cell(7, 5).value
    shengfenzheng= sheet2.cell(3, 3).value
    xingbie= sheet2.cell(2, 7).value
    mignzu= sheet2.cell(2, 9).value
    chushengriqi= sheet2.cell(4, 2).value
    xueli= sheet2.cell(5, 2).value
    renyuanleibie= sheet2.cell(6, 2).value
    rudangshijian= sheet2.cell(8, 4).value
    zhengshidangyuan= sheet2.cell(9, 4).value
    gongzuoganwei= sheet2.cell(10, 2).value
    shoujihao= sheet2.cell(11, 4).value
    dianhua= sheet2.cell(12, 7).value
    jiatingdizhi= sheet2.cell(13, 5).value
    cursor.execute("INSERT INTO newdate (xingming,suozaidangzhibu,shengfenzheng,xingbie,mignzu,chushengriqi,xueli,renyuanleibie,rudangshijian,zhengshidangyuan,gongzuoganwei,shoujihao,dianhua,jiatingdizhi) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(xingming,suozaidangzhibu,shengfenzheng,xingbie,mignzu,chushengriqi,xueli,renyuanleibie,rudangshijian,zhengshidangyuan,gongzuoganwei,shoujihao,dianhua,jiatingdizhi))
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





