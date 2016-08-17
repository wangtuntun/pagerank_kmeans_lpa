#encoding=utf-8
'''
功能：输入时没有经过分词，但是解析后的用户标签 id:tag1 tag2
    输出一个词典
'''
f_tags=open("parsed_tags_5000.txt","r+")
id_tags_list=f_tags.readlines()
tags_list=[]
tags_set=()
for id_tags in id_tags_list:
    list1=id_tags.split(":")
    tags=list1[1]
    list2=tags.split(" ")
    for tag in list2:
        tags_list.append(tag.strip())
tags_set=set(tags_list)
print len(tags_set)
f_save=open("dict_by_not_fenci.txt","w+")
for ele in tags_set:
    f_save.write(str(ele).strip())
    f_save.write("\n")