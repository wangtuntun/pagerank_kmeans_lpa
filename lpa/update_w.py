#encoding=UTF8
#读取id对应的朋友，存在字典中
friend_ids_5000_with_huanhang=open("friend_ids_5000.txt","r+")
friend_ids_5000_list_with_huanghang=friend_ids_5000_with_huanhang.readlines()
friend_ids_5000_list=[]
for ele in friend_ids_5000_list_with_huanghang:
    friend_ids_5000_list.append(ele.strip())
friend_ids_dict={}
for ele in friend_ids_5000_list:
    try:
        id_friend=ele.strip()
        list1=id_friend.split(":")
        id_str=list1[0].strip()
        friend_ids_str=list1[1].strip()
        #print id_str,friend_ids_str
        list2=friend_ids_str.split("[")
        list3=list2[1].split("]")
        list4=list3[0].split(",")
        #print id_str,type(list4)
        friend_ids_dict[id_str]=list4
    except:
        #print ele
        pass
# for ele in friend_ids_dict:
# #    print len(friend_ids_dict[ele])

#原来的uvw
friend_f=open("check_friendship_by_check_file.txt","r+")
#修改后的uvw
update_w_f=open("update_w.txt","w+")
#开始更新w
friend=friend_f.readlines()
for ele in friend:
    ele=ele.strip()
    list1_u_v_w=ele.split(" ")
    u=list1_u_v_w[0]
    v=list1_u_v_w[1]
    #w=list1_u_v_w[2]
    try:
        u_friend_list=friend_ids_dict[u]
        v_friend_list=friend_ids_dict[v]
        print u,len(u_friend_list),v,len(v_friend_list)
        u_friend_set=set(u_friend_list)
        v_friend_list=set(v_friend_list)
        v_friend_set=set(v_friend_list)
        u_and_v=u_friend_set & v_friend_set
        u_or_v=u_friend_set | v_friend_set
        w=1.0
        w=float(float(len(u_and_v)) / float(len(u_or_v)))
        w=w+0.001
        #w=1
        #w=w*10
        #print len(u_and_v),len(u_or_v)
        #print w
        update_w_f.write(u)
        update_w_f.write(" ")
        update_w_f.write(v)
        update_w_f.write(" ")
        update_w_f.write(str(w))
        update_w_f.write("\n")
    except:
        print ele



