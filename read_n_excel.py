# -*- coding:utf-8 -*-
import os
import sqlite3
import xlrd
import xlwt
import read_n_excel_fc as fc
file_path = 'C:/Users/10369/PycharmProjects/file_excel/excel'
check_name = {
    #搜索的名字：【找到之后行增加，列增加】
    '中学三级教师': ['0','15'],
    '中学二级教师':['0','15'],
    '中学一级教师':['0','15'],
    '中学高级教师':['0','15'],
    '小学二级教师': ['0','15'],
    '小学一级教师':['0','15'],
    '小学高级教师': ['0', '15'],
}

db_name = 'test.sqlit'

#1\建立数据库存储
fc.creat_newdate(db_name)

#2\ 文件地址列表 获取文件名列表
(alldirs,shotnames)=fc.eachfile(file_path)


#根据文件名地址 读取checkname内容
for i in range(len(alldirs)):
    fc.writer_date(alldirs[i],check_name)



