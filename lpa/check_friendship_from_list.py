#encoding=utf-8
def string2list(str):
    list1=str.split("[")
    list2=list1[1].split("]")
    values=list2[0]
    values_arr_with_huanhang=values.split(",")
    values_list=[]
    for ele in values_arr_with_huanhang:
        ele=ele.strip()
        values_list.append(ele)
    return values_list
#存放查询到的关系
fp_friendship_result=open("check_friendship_by_check_file.txt","w+")
#获取5000个用户id
fp_id=open("ids_without_special.txt","r+")
id_with_huanhang=fp_id.readlines()
id_list=[]#5000个人的id
for ele in id_with_huanhang:
    ele=ele.strip()
    #print ele
    id_list.append(ele)
#将每个用户的朋友放在字典中，根据用户id查询朋友
fp_friendship=open("friend_ids_5000.txt","r+")
friendship_with_huanhang=fp_friendship.readlines()
friendship=[]#5000个人的博主.其实只有4996个
for ele in friendship_with_huanhang:
    ele=ele.strip()
    #print ele
    friendship.append(ele)
id_friend_dict={}#将列表转换为词典
for ele in friendship:
    ele=ele.strip()
    try:
        id_friends=ele.split(":")
        friend_list=string2list(id_friends[1])
        friends=friend_list
        id_friend_dict[id_friends[0]]=friends
        #print id_friends[0],friends
    except:
        print "error",ele
        pass
# myids=id_friend_dict['1197161814']
# print len(myids)

#print len(id_friend_dict)
# for key,value in id_friend_dict.iteritems():#dict的value里面的每个id有空格，导致匹配不上
#     print key,value
#print len(id_list)#没问题
for source_id in id_list:
    source_id=source_id.strip()
    for des_id in id_list:
        des_id=des_id.strip()
        try:
            if source_id in id_friend_dict[des_id]:#sourcr_id在目标des_id的的朋友列表中,说明des关注了source
                fp_friendship_result.write(des_id)
                fp_friendship_result.write(" ")
                fp_friendship_result.write(source_id)
                fp_friendship_result.write("\n")
                print des_id,source_id
        except:
            pass






