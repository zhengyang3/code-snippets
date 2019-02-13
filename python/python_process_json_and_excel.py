import json
import xlrd



json_data = open('1.json','rb').read()
data = json.loads(json_data)
print(type(data))
print(data.get('all')[0].get('data').get('products')[0].get('productId'))
#print(data.get('all').get('data').get('products').get('productId'))
#for item in data:



tmp = xlrd.open_workbook('sheet-sample01.xlsx')
sheet = tmp.sheets()[0]
# print(table)
# nrows = sheet.nrows #行数
# ncols = sheet.ncols #列数


spus = sheet.col_values(1) #获取第x列的数据
spus = list(set(spus))
#sheet.row_values(0) #获取第一行的数据
#print(type(sheet.col_values(1))) #获取第x列的数据
#print(spus)
#print(sheet.nrows) #获取总共的行数
#print(sheet.ncols) #获取总共的列数

for i in data.get('all'):
    for j in i.get('data').get('products'):
        for k in spus: 
           #print(j.get('productId'))
           #print(k)
            if j.get('productId') == k:
                print(k)
