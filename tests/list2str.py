list1=[1,2,3]
str1=""
str1=str(list1)
print str1
str1=""
for ele in list1:
    str1 += str(ele)
print str1