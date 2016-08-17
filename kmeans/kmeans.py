#encoding=utf-8

'''
第一步，读取源文件，生成id_list（用户的列表，一维向量）,data_set(标签向量，二维列表)
第二部，将data_set传入kmeans生成聚类结果 kmeans_result_list[tuple(cluster_id,data_set)]
第三步，利用id_list和kmeans_result_list生成cluster_id_list
第四步，构建词典 clusterId_idList_dict和clusterId_most_tags_dict
第五步，用clusterId_most_tags_dict中的most_tags与问题匹配，得到clusterId
第六步，利用clusterId和clusterId_idList_dict得到idList,将其存入文件供pagerank使用
'''
'''
对于没有标签的用户，其特性向量全为0，计算距离时出现问题，该如何解决这类用户？？
方法一：相似度设置为0，这样距离就是最大值为1.导致0向量全部分到第一个簇中。已经过滤掉了大部分，个别还存在
方法二：对于每一个用户，还是把所有人的知乎的标签也加上，因为知乎的标签都在词库里，所以不会存在全为0的用户
'''
from collections import defaultdict
from random import uniform
from math import sqrt
import numpy
def point_avg(points):#计算多个点的平均值
    """
    Accepts a list of points, each with the same number of dimensions.
    NB. points can have more dimensions than 2

    Returns a new point which is the center of all the points.

    """
    dimensions = len(points[0])#确定向量维度

    new_center = []

    for dimension in xrange(dimensions):
        dim_sum = 0  # dimension sum
        for p in points:
            dim_sum += int(p[dimension])

        # average of each dimension
        #新的中心就是这些向量的平均值
        new_center.append(dim_sum / float(len(points)))
    #一维数组，数组长度为向量长度
    return new_center


def update_centers(data_set, assignments):#data_set表示所有的点，assignments表示每个点所属的簇。根据这个重新计算每个簇的簇心
    """
    Accepts a dataset and a list of assignments; the indexes
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of unique assignments.

    """
    new_means = defaultdict(list)#生成一个字典
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)

    for points in new_means.itervalues():#对于词典中的每个簇  points表示该簇内的所有点
        centers.append(point_avg(points))#计算每个簇的中心点

    return centers#返回每个簇新的中心点

#
def assign_points(data_points, centers):#每个点所在的簇的索引
    """
    Given a data set and a list of points betweeen other points,
    assign each point to an index that corresponds to the index
    of the center point on it's proximity to that point.
    Return a an array of indexes of centers that correspond to
    an index in the data set; that is, if there are N points
    in `data_set` the list we return will have N elements. Also
    If there are Y points in `centers` there will be Y unique
    possible values within the returned list.
    """
    assignments = []#一维列表，存储每个点的所在簇的下标
    for point in data_points:#对于每一个点
        shortest = ()  # positive infinity  初始化一个正无穷大的值
        shortest_index = 0
        for i in xrange(len(centers)):# 0->x 其中x表示中心点的个数
            val = distance(point, centers[i])#计算该点和每个中心的距离
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)#该点距离第 shortest_index 个中心最近，表示该点属于该簇
    return assignments#返回每个点所在簇的下标

def cosVector(x,y):
    #计算两个向量间的相似度，方便计算距离函数的调用
    if(len(x)!=len(y)):
        print('error input,x and y is not in the same space')
        return
    result1=0.0
    result2=0.0
    result3=0.0
    result4=0.0
    result5=0.0
    result=0.0
    for i in range(len(x)):
        result1+=int(x[i])*int(y[i])   #sum(X*Y)  x和y的内积
        result2+=int(x[i])**2     #sum(X*X)  x的模未开方
        result3+=int(y[i])**2     #sum(Y*Y)  y的模未开方
    try:
        result4=result1/(result2*result3)
    except:#如果分母为0，相似度设为最小值0。距离为1-相似度 导致距离为最大值1
        result4=0.0
        print result2,result3
    result5=result4**0.5
    result=str(result5)
    return result

def distance(a, b):
    #之前的距离是向量间的欧氏距离，现在换成了相似度
    # dimensions = len(a)
    #
    # _sum = 0
    # for dimension in xrange(dimensions):
    #     difference_sq = (a[dimension] - b[dimension]) ** 2
    #     _sum += difference_sq
    # return sqrt(_sum)
    cos= cosVector( a , b )
    cos_float=float(cos)
    dist=1-cos_float#两个向量越相似，cos越大，距离越小。cos值和距离成反比
    return dist

def generate_k(data_set, k):#返回初始中心点。随机的。返回的是二维数组。
    """
    Given `data_set`, which is an array of arrays,
    find the minimum and maximum for each coordinate, a range.
    Generate `k` random points between the ranges.
    Return an array of the random points within the ranges.
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)#生成一个空的字典，键的类型是int

    for point in data_set:
        for i in xrange(dimensions):#xrange和range差不多
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if max_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in xrange(k):
        rand_point = []
        for i in xrange(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]

            rand_point.append(uniform(min_val, max_val))#uniform，生成x和y之间的一个随机数

        centers.append(rand_point)
    #centers=[]#在此添加默认的中心点。二维数组。

    return centers


#def k_means(dataset, k):
def k_means(dataset,cluster_centers):
    #k_points = generate_k(dataset, k)#初始种子节点。二维数组
    k_points=cluster_centers
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:#kmeans的停止条件是簇心不再发生变化
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    return zip(assignments, dataset)#簇下标：向量
    #return assignments

def get_id_list(path):
    f = open(path, "r+")
    raw_list = f.readlines()
    id_list=[]
    user_data = []
    for ele in raw_list:
        list1 = ele.split(":")
        user_id = list1[0].strip()
        data_str = list1[1].strip()
        data_list = data_str.strip().split(" ") # 一维数组
        # exist_1_flag=0
        # for ele in data_list:
        #     if int(ele) == 1:
        #         exist_1_flag=1
        # if exist_1_flag==1:
        #     id_list.append(user_id)
        id_list.append(user_id)
    return id_list
def get_data_set(path):
    f = open(path, "r+")
    raw_list = f.readlines()
    user_data = []
    for ele in raw_list:
        list1 = ele.split(":")
        user_id = list1[0].strip()
        data_str = list1[1].strip()  # 一维数组
        data_list = data_str.strip().split(" ")
        # exist_1_flag = 0
        # for ele in data_list:
        #     if int(ele) == 1:
        #         exist_1_flag = 1
        # if exist_1_flag == 1:
        #     user_data.append(data_list)  # 二维数组
        user_data.append(data_list)
    return user_data
def get_max_degree_users_dataset(path):#获取初始簇心，返回二维01数组
    f=open(path,"r+")
    raw_list=f.readlines()
    user_data=[]
    for ele in raw_list:
        list1=ele.split(":")
        user_id=list1[0].strip()
        data_str=list1[1].strip()#一维数组
        data_list=data_str.strip().split(" ")
        user_data.append(data_list)#二维数组
    return user_data

def get_dic(path):
    f_dic = open(path, "r+")
    voc_arr_with_huanhang = f_dic.readlines()
    voc_arr = []
    for voc in voc_arr_with_huanhang:
        voc_arr.append(voc.strip())
    return voc_arr

def get_cluster(voc,users):
    #用什么来表示整个簇:出现最多的几个词。簇的维度和字典的一样，但是1的个数只有topk个。
    dict_voc_number={}#统计每个单词出现的次数
    count=len(voc)
    while count>0:
        count -= 1
        dict_voc_number[count]=0
    for user in users:
        count=0
        for no in user:
            if int(no) == 1:
                dict_voc_number[count] += 1
            count += 1
    #print dict_voc_number#对比vec发现基本正确。互联网词典号12，在vec统计的有11次的，但是在fenci_tags出现了15次。其他试了几个都正确
    #for ele in dict_voc_number:
    #    print ele,dict_voc_number[ele]
    #找到出现次数最多的前k个单词

    sorted_word_list=[]
    sorted_word_list=[ dict_voc_number.keys()[v] for v in numpy.argsort(dict_voc_number.values())]#词典按照value排序（从小到大），最后返回对应索引
    sorted_word_list.reverse()#从大到小
    max_word_k=100#取出现次数最高的前k个单词
    max_word_k_arr=sorted_word_list[0:max_word_k]#取去前k个索引
    #print max_word_list#对比dict_voc_number发现排序结果正确

    #最后用一个list表示该簇
    count=len(voc)
    list_cluster=[]
    while count>0:
        count -= 1
        list_cluster.append(0)
    for word in max_word_k_arr:#将字典索引的位置赋值为1，作为该簇的向量
        list_cluster[word]=1
    #print list_cluster
    return list_cluster


#开始聚类
most_degeree_users_data=get_max_degree_users_dataset("../tags/get_max_degree_0_1_vec.txt")#获取多个度最大的用户向量
cluster_number=10#这里设置的是最大可聚为几类，不是一定会聚成几类
cluster_centers=most_degeree_users_data[0:cluster_number]#根据簇的数量选择簇心数量
id_list=[]
data_set=[]
all_user_info_path="../tags/get_0_1_vec.txt"
id_list=get_id_list(all_user_info_path)
data_set=get_data_set(all_user_info_path)
#print len(id_list),len(data_set)#去掉全0 的用户，还剩3290个用户
kmeans_resul=k_means(data_set, cluster_centers)#返回的是一个元祖型的数组。根据簇心的数量决定簇的数量
cluster_dataset_dict={}
for cluster,data_set in kmeans_resul:
    cluster_dataset_dict[cluster].append(data_set)
for ele in cluster_dataset_dict:
    print ele,len(cluster_dataset_dict[ele])



