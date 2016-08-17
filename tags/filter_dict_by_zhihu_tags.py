#encoding=utf-8
'''
之前已经利用微博标签构成微博标签词典，这次结合知乎的标签组成的词典，将存在微博词库但不存在知乎词库的词删掉
手动添加了一个词 ：微博用户
用于过滤后没有标签的用户
'''
f_zhihu_dict=open("../zhihu/get_zhihu_dict.txt","r+")#知乎词库
zhihu_list=f_zhihu_dict.readlines()
f_weibo_dict=open("dict_by_not_fenci.txt","r+")
weibo_list=f_weibo_dict.readlines()
f_filter=open("filter_weibo_dict_by_zhihu_dict.txt","w+")
for ele in weibo_list:
    if ele in zhihu_list:
        f_filter.write(ele.strip())
        f_filter.write("\n")

