#encoding=utf-8
'''
功能：输入所有用户的标签 id:tag1 tag2,还有前k个度最大的用户 id degree，还有用户标签组成的几个知乎过滤的词典。
输出所有用户的标签向量，并单独输出k个用户的向量，方便kmeans用
    结果发现，有些度比较大的用户，通过知乎标签筛选，就没有标签了。就是全0向量。
    这样的话，没有标签的用户就会被分为一类。因为5000个用户里面，有很多人的标签也是全为0
    但是这样的用户最好不要当做种子。k设置为了100，但是最后写入文件的只有70个。其他30个都木有标签。
    而且度大的用户，即使有标签，也只有几个，还是会存在向量很稀疏的问题。
    但是即使很稀疏，也会把标签存在交集的用户分到一类。
    这样的话，应该不会存在极大簇，但是会把很多不相关的强制聚为一类。比如两个用户都是只有一个不同的标签，可能会把他们聚为一类。
    先这样走吧，不行再把知乎的标签加上，这样用户的标签也多，标签存在交集的用户也越多。

    实验结果发现，必须把知乎的标签加到每个用户上，否则稀疏的会聚到一个簇，出现极大簇现象
    所以说，得把知乎的标签也加到用户向量里面
'''
#写入所有用户的01向量
f_vec=open("get_0_1_vec.txt","w+")
#写入度最大的几个用户的01向量
f_max_degree_0_1_vec=open("get_max_degree_0_1_vec.txt","w+")
#读取top-k个用户的id列表
f_max_degree_id=open("get_users_by_degree.txt","r+")
top_k_ids=[]
degree_ids=f_max_degree_id.readlines()
for ele in degree_ids:
    id_degree=ele.split(" ")
    top_k_ids.append(id_degree[0].strip())

#读取字典
f_dic=open("add_filter_zhihu_dict_to_weibo_dict.txt","r+")
voc_arr_with_huanhang=f_dic.readlines()
voc_arr=[]
for voc in voc_arr_with_huanhang:
    voc_arr.append(voc.strip())

#获取用户的标签
f_tag=open("add_zhihu_tag_to_weibo_tag.txt","r+")
users_with_huanhang=f_tag.readlines()
for user in users_with_huanhang:#对每一个用户 id:tag1 tag2
    #解析id和tags
    id_user=user.split(":")
    user_id=id_user[0].strip()
    print user_id
    user_tags=id_user[1].strip()
    #开始设置用户的向量
    user_tag_number=0#统计每个用户标签的数量
    # 每个用户的标签向量开始全为0
    vec_list = []
    count = len(voc_arr)
    while count > 0:#先将每个用户的向量初始化为0
        # print count
        count -= 1
        vec_list.append(0)
    tag_list=user_tags.split(" ")
    for tag in tag_list:#用户的每一个标签
        try:#如果能找到就设置对应位置为1
            tag_index=voc_arr.index(tag)
            user_tag_number += 1
            #print tag,voc_arr[tag_index]
            vec_list[tag_index]=1
        except:
            pass
    # print user_id,user_tag_number#数量正确
    #将用户01向量写入文件 id:0 0 1 1
    f_vec.write(user_id)
    f_vec.write(":")
    for ele in vec_list:
        f_vec.write(str(ele))
        f_vec.write(" ")
    f_vec.write("\n")

    #通过id判断当前用户是否是度最大的几个，如果是，将该用户再写入另外一个文件。
    if user_id in top_k_ids:
        for tag in tag_list:  # 用户的每一个标签
            try:  # 如果能找到就设置对应位置为1
                tag_index = voc_arr.index(tag)
                user_tag_number += 1
                #print user_id,tag,voc_arr[tag_index]
                vec_list[tag_index] = 1
            except:
                pass
        #写入文件前要判断该用户的标签是否为空，如果是就不写
        if user_tags.strip() =="":
            print user_id
            pass
        else:
            #print user_id,user_tags
            f_max_degree_0_1_vec.write(str(user_id))
            f_max_degree_0_1_vec.write(":")
            for ele in vec_list:
                f_max_degree_0_1_vec.write(str(ele))
                f_max_degree_0_1_vec.write(" ")
            f_max_degree_0_1_vec.write("\n")


