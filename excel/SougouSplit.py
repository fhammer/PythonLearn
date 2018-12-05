#! /usr/bin/env Python3
# -*- coding:utf8 -*-
import re       #正则表达式

def split():
    p = re.compile('</doc>',re.S)
    end = '</doc>'
    fileContent = open(r'E:\news_tensite_xml.smarty.dat','r',encoding='utf8').read();  #读文件内容
    paraList = p.split(fileContent)     #根据</doc>对文本进行切片
    #print(len(paraList))

    fileWriter = open('./files/0.txt','a',encoding='utf8')  #创建一个写文件的句柄
    #遍历切片后的文本列表
    for paraIndex in range(len(paraList)):
        #print(paraList[paraIndex])
        fileWriter.write(paraList[paraIndex])   #先将列表中第一个元素写入文件中
        if(paraIndex != len(paraList)):         #不加if这两行的运行结果是所有的</doc>都没有了，除了最后分割的文本
            fileWriter.write(end)
        if((paraIndex+1)%5000==0):              #5000个切片合成一个.txt文本
            fileWriter.close()
            fileWriter = open('./files/'+str((paraIndex+1)/5000)+'.txt','a',encoding='utf8'); #重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
    fileWriter.close()          #关闭最后创建的那个写文件句柄
    print('finished')