import json
json_data = open('kk.json','rb').read()
data = json.loads(json_data)
print(type(data))
f=open('string.txt','a+')

# write key's value into file with no quotes. 
#  f.write(data.get("aaa"))   or f.write(str(data.get("aaa")))

#write key's value included double quotes of json into file. 
f.write(json.dumps(data.get("aaa")) + ", ")
f.close()
