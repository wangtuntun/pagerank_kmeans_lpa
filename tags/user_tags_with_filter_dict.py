#encoding=utf-8
'''
功能：用过滤后的词典表示每个用户，看每个用户还剩下多少标签。
如果一个标签都没有，则添加一个默认标签
'''
defualt_tag="微博用户"
f_filter_dict=open("filter_weibo_dict_by_zhihu_dict.txt","r+")#读取用知乎词典过滤过的微博词典
filter_dict_with_huanhang=f_filter_dict.readlines()
filter_dict=[]#去掉每个标签的空格和换行符号
for ele in filter_dict_with_huanhang:
    ele=ele.strip()
    #print ele#正常
    filter_dict.append(ele)#filter_dict正常
f_tags=open("parsed_tags_5000.txt","r+")#读取每个用户的标签
tags_list=f_tags.readlines()
f_save=open("user_tags_with_filter_dict.txt","w+")#将过滤后的标签写入文件

for users_tags in tags_list:
    id_tags=users_tags.split(":")
    user_id=id_tags[0]
    f_save.write(user_id)
    f_save.write(":")
    tags_to_write=[]
    tags=id_tags[1]
    tags_list=tags.split(" ")
    for tag in tags_list:
            if tag in filter_dict:
               tags_to_write.append(tag.strip())
    #开始写入文件
    if not tags_to_write:#如果最后得到的标签列表为空
        f_save.write(defualt_tag)
    else:#不为空
        for ele in tags_to_write:
            f_save.write(ele.strip())
            f_save.write(" ")
    f_save.write("\n")

