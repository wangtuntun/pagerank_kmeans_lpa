#encoding=utf-8
#将知乎的标签添加到原来的微博用户上
f_weibo_tags=open("user_tags_with_filter_dict.txt","r+")#id:tag1 tag2
f_zhihu_tags=open("../zhihu/get_zhihu_user_tags.txt","r+")#tag1 tag2
f_save=open("add_zhihu_tag_to_weibo_tag.txt","w+")
#获取id列表和微博标签列表
id_and_weibo_tags=f_weibo_tags.readlines()
id_list=[]
weibo_tags=[]
for ele in id_and_weibo_tags:
    id_tags=ele.split(":")
    user_id=id_tags[0].strip()
    user_tags=id_tags[1].strip().split(" ")
    id_list.append(user_id)
    weibo_tags.append(user_tags)
#获取知乎标签列表
raw_zhihu_tags=f_zhihu_tags.readlines()
zhihu_tags=[]
for ele in raw_zhihu_tags:
    user_tags=ele.strip().split(" ")
    zhihu_tags.append(user_tags)
 #开始写入文件
user_index=0
while user_index < 5000:
    f_save.write(id_list[user_index])
    f_save.write(":")
    for tag in weibo_tags[user_index]:
        f_save.write(tag)
        f_save.write(" ")
    for tag in zhihu_tags[user_index]:
        f_save.write(tag)
        f_save.write(" ")
    f_save.write("\n")
    user_index+=1



