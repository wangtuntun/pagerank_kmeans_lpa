#encoding=utf-8
'''
功能：给定用户的关注关系列表，得到几个用户，这几个用户的度最大.度是出度加入度。可以试下只有粉丝的。
某些度很大的用户的标签可能为空，不适合作为种子，所以多产生几个，方便以后删选。
'''
import numpy
dict_user_degree={}
users_set=()
users_list=[]
#获取到所有有边的用户
f_friendship=open("check_friendship_by_check_file.txt")
f_friendship_list=f_friendship.readlines()
for u_v_str in f_friendship_list:
    u_v_list=u_v_str.split(" ")
    u=str(u_v_list[0]).strip()
    v=str(u_v_list[1]).strip()
    #print v
    users_list.append(long(u))
    users_list.append(long(v))
users_set=set(users_list)
#初始化每个用户的度
for user in users_set:
    dict_user_degree[user]=0
#设置每个用户的度
for user in dict_user_degree:
    dict_user_degree[user]=users_list.count(user)
#按照度的数量从大到小返回用户id
sorted_dict_users_list=[ dict_user_degree.keys()[v] for v in numpy.argsort(dict_user_degree.values())]
sorted_dict_users_list.reverse()
#返回最大的前k个用户ID和度
return_user_number_k=100
top_k_user_list=[]
top_k_user_list=sorted_dict_users_list[0:return_user_number_k]
for ele in top_k_user_list:
    print ele,dict_user_degree[ele]
#将结果存入文件
f_save=open("get_users_by_degree.txt","w+")
for ele in top_k_user_list:
    f_save.write(str(ele))
    f_save.write(" ")
    f_save.write(str(dict_user_degree[ele]))
    f_save.write("\n")