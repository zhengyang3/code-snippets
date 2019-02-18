import json
import xlrd
import xlwt
from xlutils.copy import copy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


tmp = xlrd.open_workbook('new.xls')
wb = copy(tmp)
#wb.get_sheet(0).write(0,11,'farfetch 匹配度')
#wb.get_sheet(0).write(0,12,'farfetch-spu')
#wb.get_sheet(0).write(0,13,'farfetch-sku')
#wb.get_sheet(0).write(0,14,'欧元价')

# 打开第1张sheet表
sheet = tmp.sheets()[0]
# print(table)
# nrows = sheet.nrows #行数
# ncols = sheet.ncols #列数


lista = sheet.col_values(1) #获取第x列的数据
#去重
#spus = list(set(spus0))
#sheet.row_values(0) #获取第一行的数据
#print(type(sheet.col_values(1))) #获取第x列的数据
#print(spus)
#print(sheet.nrows) #获取总共的行数
#print(sheet.ncols) #获取总共的列数


# https://blog.csdn.net/qq_33094993/article/details/53584379
# 但是有没有一个更加简单的方法获得python的list中含有重复值的index呢？
# 有的，那就是”偷梁换柱“，用一个s1来复制s。
#   s1 = s
#   i = s1.index(11)
#   s1[i]=55
# 替换s1的11为55（不一定是55只要是列表中没有的数值就可以）
# 再打印s1
#   print s1
# 输出[55, 22, 33, 44, 22, 11]
# 下一步可以得到11的位置了
#   print  s1.index(11)
# 输出为：5

for i in range(len(lista)):
    if lista[i] == 'aaaaa':
        continue
    spu = lista[i]
    lista[i] = 'aaaaa'
    while 1:
        try:
            row = lista.index(spu)
        except ValueError:
            print("this spu none!")
            break
        else:
            ffrate = sheet.cell(i,11).value
            ffspu = sheet.cell(i,12).value
            ffsku = sheet.cell(i,13).value
            ffprice = sheet.cell(i,14).value
            wb.get_sheet(0).write(row,11,ffrate)
            wb.get_sheet(0).write(row,12,ffspu)
            wb.get_sheet(0).write(row,13,ffsku)
            wb.get_sheet(0).write(row,14,ffprice)
            lista[row] = 'aaaaa'

wb.save('new.xls')

