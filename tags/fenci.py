# -*- coding: UTF-8 -*-
import pynlpir
pynlpir.open()
'''
该文件实现的功能：
根据解析后的标签先分词再生成一个词典
但是中科院的分词功能好像证书过期了
'''
# s = '欢迎健康的科研人员、技术工程师、企事业单位与个人参与NLPIR平台的建设工作。'
# s="心理咨询 临床心理学 心理治疗师"
# f_fenci_tags=open(r"fenci_tags.txt","w+")
# f_parsed_tags=open("parsed_tags.txt","r+")
f_fenci_tags=open(r"fenci_tags_with_id.txt","w+")#生成的词典
f_parsed_tags=open("id_tags_5000.txt","r+")#源数据
f_parsed_tags_arr=f_parsed_tags.readlines()
arr_dic=[]
for line in f_parsed_tags_arr:
    line=line.strip()
    list1=line.split(":")
    myid=list1[0]
    line=list1[1]
    f_fenci_tags.write(myid)
    f_fenci_tags.write(":")
    for i in pynlpir.segment(line):
        if (str(i[1]) == "verb" or str(i[1]) == "noun" or str(i[1]) == "adjective"):
            #print i[0].encode("utf-8")
            f_fenci_tags.write(i[0].encode("utf-8"))
            arr_dic.append(i[0].encode("utf-8").strip())
            f_fenci_tags.write(" ")
    f_fenci_tags.write("\n")
f_dict=open("dict.txt","w+")
print len(arr_dic)
arr_dic=list(set(arr_dic))
for ele in arr_dic:
    #print ele
    f_dict.write(ele)
    f_dict.write("\n")
print len(arr_dic)

