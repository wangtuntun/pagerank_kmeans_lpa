#encoding=utf-8
'''
功能：将知乎的 lda，回答，关注 一起组成一个词库
'''
import json
f=open("zhihu_user_vec.txt","r+")
tags_list=f.readlines()
all_words_list=[]
all_words_set=()
for tags in tags_list:
    try:
        tags=tags.strip()
        json_tags=json.loads(tags)
        lda_top=json_tags["lda_top"]
        for lda in lda_top:
            #print lda
            all_words_list.append(lda)

        ans_top=json_tags["ans_top"]
        for ans in ans_top:
            #print ans
            all_words_list.append(ans)

        follow_top=json_tags["follow_top"]
        for follow in follow_top:
            #print follow
            all_words_list.append(follow)
    except:
        print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print len(all_words_list)
all_words_set=set(all_words_list)
print len(all_words_set)
#将结果写入文件
f_write=open("get_zhihu_dict.txt","w+")
for ele in all_words_set:
    print ele
    f_write.write(ele.encode("UTF8"))
    f_write.write("\n")