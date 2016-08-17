#encoding=utf-8
'''
将知乎词典和过滤后的知乎词典进行合并，生成一个总的词典

'''
f_weibo_dict=open("dict_by_not_fenci.txt")#读取微博词库
f_zhihu_dict=open("../zhihu/filter_zhihu_dict.txt")#读取过滤后的知乎词库
f_save=open("add_filter_zhihu_dict_to_weibo_dict.txt","w+")#存放文件
weibo_list=f_weibo_dict.readlines()
zhihu_list=f_zhihu_dict.readlines()
all_dict_list=[]
all_dict_set=()
for ele in weibo_list:
    all_dict_list.append(ele.strip())
for ele in zhihu_list:
    all_dict_list.append(ele.strip())
all_dict_set=set(all_dict_list)
for ele in all_dict_set:
    f_save.write(ele)
    f_save.write("\n")