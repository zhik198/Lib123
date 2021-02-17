import xmindparser
import os
import re

mulu=input("请输入目录\n")
leirong=input("请输入内容\n")
wenjianzonghe=[]

for dirpath,dirname,filename in os.walk(mulu):
    for filenamex in filename:
        wenjianzonghe.append(dirpath+'\\'+filenamex)

xmind_files=[]
for wenjainzonghex in wenjianzonghe:
    bianshi=os.path.splitext(wenjainzonghex)[-1]
    if bianshi==".xmind":
        xmind_files.append(wenjainzonghex)

for XFX in xmind_files:
    print(XFX)
    neirong=xmindparser.xmind_to_dict(XFX)
    panduan=re.search(leirong,str(neirong))
    if panduan != None:
        print(XFX)















