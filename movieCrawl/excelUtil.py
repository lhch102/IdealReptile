# -*- coding: utf-8 -*-

# 读写2007 excel
import openpyxl
import xlwt

def write07Excel(i,title,rate,casts):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    worksheet.write(i,0,i+1)
    worksheet.write(i,1,title)
    worksheet.write(i,2,rate)
    worksheet.write(i,3,casts)
    workbook.save('movie.xls') #写完记得一定要保存

