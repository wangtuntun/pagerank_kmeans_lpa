#encoding=utf-8
'''微博词典8000个，知乎词典30000个，加起来40000多维度
一般用户的微博标签是2个，知乎100个。所有40000维度中只有100个为1。
很稀疏
而且计算起来很复杂，很慢。（最少一个小时）
必须进行压缩，按照所有用户的微博和知乎的标签的词频，只保留前5000个。如果某个用户最后一个标签都没有，把出现频次最高的那个付给它
到第5000个词的时候，出现频率是10次  55
'''
import numpy

f_dict=open("get_zhihu_dict.txt","r+")#读取知乎词典
f_tags=open("get_zhihu_user_tags.txt","r+")#读取知乎用户标签
f_save=open("filter_zhihu_dict.txt","w+")#存放过滤好的知乎词典
raw_tag=f_dict.readlines()#有空格和换行
tag_dict={}#  dict[id]=number
for ele in raw_tag:
    ele=ele.strip()#去换行和空格
    tag_dict[ele]=0
# for ele in tag_dict:
#     print ele
all_tags=f_tags.readlines()
for ele in all_tags:
    tags=ele.strip().split(" ")
    for tag in tags:
        tag=tag.strip()
        try:
            tag_dict[tag]+=1
        except:
            # print tag
            pass
most_tag_list=[tag_dict.keys()[v] for v in numpy.argsort(tag_dict.values())]#按照#出现次数，从小到大返回标签
most_tag_list.reverse()#从大到小
for ele in most_tag_list:#查看标签对应频次
     print ele,tag_dict[ele]
top_k=5000
filter_dict=most_tag_list[0:top_k]
for ele in filter_dict:
    f_save.write(ele.strip())
    f_save.write("\n")




