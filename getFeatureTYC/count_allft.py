#计算前100条里面所有出现的法律
with open('ftlist.txt','r',encoding='utf-8') as f:
      ftlist = []
      content = f.readline()
      while content:
          ftname = content.split(',')[0].strip()
          if ftname not in ftlist:
              ftlist.append(ftname)
          content = f.readline()
      for i in ftlist:
          print(i)
