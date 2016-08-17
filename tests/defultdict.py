#encoding=utf-8
from collections import defaultdict
new_means = defaultdict(list)
print new_means
data_sets=[[0,0,0],[1,1,1],[2,2,2],[2,2,2]]
assignments=[0,1,2,2]
zip_data=zip(assignments,data_sets)#返回一个列表，每一个元素是tuple

for index,data in zip_data:
    print index,data
    #new_means[index].append(data)#跟新和覆盖某个索引的值。所以这里输出的是一个一维列表
    new_means[index].append(data)#将所有出现的值都加到该索引上，生成一个值得列表。所以这里输出的是一个二维列表。
for points in new_means.itervalues():
    print points
