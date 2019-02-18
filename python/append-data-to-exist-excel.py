import json
import xlrd
import xlwt
from xlutils.copy import copy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process



json_data = open('1.json','rb').read()
data = json.loads(json_data)
print(type(data))
print(data.get('all')[0].get('brandStyleId'))
#print(data.get('all').get('data').get('products').get('productId'))
#for item in data:



tmp = xlrd.open_workbook('sheet-sample01.xlsx')
wb = copy(tmp)
wb.get_sheet(0).write(0,11,'farfetch 匹配度')
wb.get_sheet(0).write(0,12,'farfetch-spu')
wb.get_sheet(0).write(0,13,'farfetch-sku')
wb.get_sheet(0).write(0,14,'欧元价')

# 打开第1张sheet表
sheet = tmp.sheets()[0]
# print(table)
# nrows = sheet.nrows #行数
# ncols = sheet.ncols #列数


spus0 = sheet.col_values(1) #获取第x列的数据
#去重
spus = list(set(spus0))
#sheet.row_values(0) #获取第一行的数据
#print(type(sheet.col_values(1))) #获取第x列的数据
#print(spus)
#print(sheet.nrows) #获取总共的行数
#print(sheet.ncols) #获取总共的列数

for i in data.get('all'):
    ffspu = i.get('brandStyleId')
    lista = i.get('variants')
    for k in spus: 
        if ffspu == k:
            if len(lista):
                # this list is not None
                price = lista[0].get('price').get('priceInclTaxes')
                ffsku= lista[0].get('sku')
                row = spus0.index(k)
                print(row+1)
                wb.get_sheet(0).write(row,11,'100%')
                wb.get_sheet(0).write(row,12,ffspu)
                wb.get_sheet(0).write(row,13,ffsku)
                wb.get_sheet(0).write(row,14,price)
                print(k)
            else:
                # this list is None
                row = spus0.index(k)
                print(row+1)
                wb.get_sheet(0).write(row,11,'100%')
                wb.get_sheet(0).write(row,12,ffspu)
                print(k)
        elif k.isdigit():
            continue
        elif fuzz.ratio(ffspu, k) > 75:
            if len(lista):
                # this list is not None
                price = lista[0].get('price').get('priceInclTaxes')
                ffsku= lista[0].get('sku')
                row = spus0.index(k)
                print(row+1)
                wb.get_sheet(0).write(row,11,str(fuzz.ratio(ffspu, k))+"%")
                wb.get_sheet(0).write(row,12,ffspu)
                wb.get_sheet(0).write(row,13,ffsku)
                wb.get_sheet(0).write(row,14,price)
                print("in fuzz k = "+k)
            else:
                # this list is None
                row = spus0.index(k)
                print(row+1)
                wb.get_sheet(0).write(row,11,str(fuzz.ratio(ffspu, k))+"%")
                wb.get_sheet(0).write(row,12,ffspu)
                print("in fuzz k = "+k)
        else:
            pass

wb.save('new.xls')

