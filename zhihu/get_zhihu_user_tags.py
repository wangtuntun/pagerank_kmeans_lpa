#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

'''
功能：将知乎的 lda,answer,follow 作为用户知乎方面的标签
有41个用户没有标签，手动添加标签 “知乎用户”
'''
import json
f=open("zhihu_user_vec.txt","r+")
tags_list=f.readlines()
f_write=open("get_zhihu_user_tags.txt","w+")
defulat_tag="知乎用户"
for tags in tags_list:#对于每一个用户
    user_tags=[]
    user_tags_set=()
    try:#个别用户没有知乎标签
        tags=tags.strip()
        json_tags=json.loads(tags)
        lda_top=json_tags["lda_top"]
        for lda in lda_top:
            user_tags.append(lda)
        ans_top=json_tags["ans_top"]
        for ans in ans_top:
            user_tags.append(ans)
            follow_top = json_tags["follow_top"]
        for follow in follow_top:
            user_tags.append(follow)
    except:
        user_tags.append(defulat_tag)
    user_tags_set=set(user_tags)
    # 将用户标签写入文件
    for ele in user_tags_set:
        f_write.write(str(ele).strip())
        f_write.write(" ")
    f_write.write("\n")

