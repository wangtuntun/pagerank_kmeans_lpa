#encoding=utf8

import sys
import random
import networkx as nx
import matplotlib.pyplot as plt
def list2str(mylist):
    str1 = ""
    for ele in mylist:
        str1 += str(ele)
    return str1
def read_graph_from_file(path,id_tags_dict):
    #从文件读取边关系
    graph = nx.read_edgelist(path, data = (('weight', float), ))

    #用id作为label
    for node, data in graph.nodes_iter(True):
        #data['label'] = node
        node_int=int[node]
        data['label'] = id_tags_dict[node_int]#

    return graph

def read_game_info_from_file(path):
    game = {}

    with file(path, 'r') as f:
        for line in f:
            line = line.strip()
            data = line.split('\t')
            game[data[0]] = data[1]

    return game

# label-propagation algorithm
# use asynchronous updating for better results？？？？？？？？？？？？？？？
def lpa(graph):
    def estimate_stop_cond():#设置停止传播的条件
        for node in graph.nodes_iter():#返回node的迭代器
            count = {}

            for neighbor in graph.neighbors_iter(node):#返回该节点的邻居迭代器
                neighbor_label = graph.node[neighbor]['label']#获取邻居的标签
                neighbor_weight = graph.edge[node][neighbor]['weight']#获取邻居的权值
                count[neighbor_label] = count.setdefault(neighbor_label, 0.0) + neighbor_weight#统计每个标签的数量

            #找到数量最多的那个标签
            count_items = count.items()#获取所有的标签
            count_items.sort(key = lambda x: x[1], reverse = True)#按照数量对标签进行排序

            #获取最多的那个标签。当有多个最多次数标签时，随机选一个
            labels = [k for k,v in count_items if v == count_items[0][1]]

            #当符合下面条件时，传播结束
            if graph.node[node]['label'] not in labels:#如果某一个节点的标签不在总的标签中#不再变化
                return False

        return True

    loop_count = 0

    while True:
        loop_count += 1
        print 'loop', loop_count

        for node in graph.nodes_iter():#对于每一个节点
            count = {}

            for neighbor in graph.neighbors_iter(node):#该节点的每一个邻居
                neighbor_label = graph.node[neighbor]['label']
                neighbor_weight = graph.edge[node][neighbor]['weight']
                count[neighbor_label] = count.setdefault(neighbor_label, 0.0) + neighbor_weight

            # 找到数量最多的那个标签
            count_items = count.items()
            count_items.sort(key = lambda x: x[1], reverse = True)

            # 当有多个最多次数标签时，随机选一个
            labels = [(k, v) for k, v in count_items if v == count_items[0][1]]
            label = random.sample(labels, 1)[0][0]

            graph.node[node]['label'] = label#更新该节点的label
        #对所有节点完成了一次更新，判断是否继续下轮跟新
        if estimate_stop_cond() is True or loop_count >= 10:#当到达停止传播条件或者传播次数超过10次就停止传播
            print '----------------------传播结束----------------------------------------'
            return

def print_graph_info(graph):
    all_class_nodes=[]
    game_info = read_game_info_from_file('id_name.info')
    info = {}

    for node, data in graph.nodes_iter(True):
        info.setdefault(graph.node[node]['label'], []).append(game_info.get(node, node))

    print 'node num:', len(graph.nodes())
    print 'class num:', len(info.keys())
    print 'class:', info.keys()
    print 'info:'
    for clazz in info:
        class_nodes=[]
        print '\t%s(%d):' % (clazz, len(info[clazz])),
        for label in info[clazz]:
            #print '\'%s\'' % label,
            print str(label),
            class_nodes.append(str(label))
        print '\n',
        all_class_nodes.append(class_nodes)
    return all_class_nodes

if __name__ == '__main__':
    #g = read_graph_from_file('d.data')
    id_tags_dict={}
    g=read_graph_from_file("update_w.txt",id_tags_dict)
    lpa(g)
    all_class_nodes_list_list=print_graph_info(g)
    '''
    #显示每个用户的标签
    #初始化id_labels词典
    id_labels_dict={}
    id_tags_f=open("tags_with_id.txt","r+")
    id_tags_list=id_tags_f.readlines()
    for ele in id_tags_list:
        list1=ele.split(":")
        myid=list1[0].strip()
        lables=list1[1].strip().split(" ")
        id_labels_dict[myid]=lables

    #将每个社区里面的id对应的标签写到文件里面
    cluster_tags_f = open("cluster_tags.txt", "w+")
    count=0
    for shequ in all_class_nodes_list_list:#一次是一个社区
        cluster_tags_f.write(str(count))
        cluster_tags_f.write("\n")
        for next_id in shequ:#社区里的每一个人
            next_id=str(next_id).strip()
            cluster_tags_f.write(next_id)
            cluster_tags_f.write(":")
            try:
                labels=id_labels_dict[next_id]
                for label in labels:#写入一个用户的所有标签
                    cluster_tags_f.write(str(label))
                    cluster_tags_f.write(" ")
                cluster_tags_f.write("\n")
            except:
                print next_id
        count+=1
    '''
    node_color = [float(g.node[v]['label']) for v in g]
    labels = dict([(node, node) for node, data in g.nodes_iter(True)])
    nx.draw_networkx(g, node_color = node_color)
    plt.show()