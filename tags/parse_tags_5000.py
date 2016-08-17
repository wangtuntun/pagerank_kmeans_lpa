#encoding=utf-8
'''
功能：将原来的json格式的tag解析为单个
'''
f_id_tags=open("id_tags_5000.txt","r+")
id_tags=f_id_tags.readlines()
f_save=open("parsed_tags_5000.txt","w+")
for ele in id_tags:
    list1=ele.split(":[")
    user_id=list1[0]
    f_save.write(user_id)
    f_save.write(":")
    user_tags=list1[1]
    tags2=user_tags.split("]")
    tags3=tags2[0]
    tags4=tags3.split(",")
    try:
        for single_tag in tags4:
            st=single_tag.split(":")
            st_hanzi=st[1]
            st2=st_hanzi.split("\"")
            st3=st2[1].split("\"")
            print st3[0]
            f_save.write(st3[0])
            f_save.write(" ")

    except:
        print "+++++++++++++++++++++++++++++"
    f_save.write("\n")