#创建节点的开销表，开销是指从“起点”到该节点的权重
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3
graph["fin"] = {}

#定义无穷大，定义开销
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

#父节点的散列表
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#已经处理过的节点，需要记录
processed = []
best_route = ""

#找出开销最低的节点
def find_lowest_cost_node(costs):
    #设置初始的开销为无穷大
    lowest_cost = infinity
    #设置初始最低开销节点为None
    lowest_cost_node = None
    #遍历所有节点
    for node in costs:
        cost = costs[node]
        #如果当前节点的开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def best_route():
#在未处理的节点中找出开销最小的节点
    node = find_lowest_cost_node(costs)
    #这个while循环在所有节点都被处理过后结束
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        #遍历当前节点的所有邻居
        for n in neighbors.keys(): 
            #最新的开销是该节点的开销和到邻居开销之和
            new_cost = cost + neighbors[n]
            #如果经当前节点前往该邻居更近
            if costs[n] > new_cost:
                #就更新该邻居的开销
                costs[n] = new_cost 
                #同时将该邻居的父节点设置为当前节点
                parents[n] = node
        #将当前节点标记为处理过
        processed.append(node) 
        #找出接下来要处理的节点，并循环
        node = find_lowest_cost_node(costs) 
    
    p = parents["fin"]
    best_route = ""
    
    while True:
        best_route += "%s<--" % p
        p = parents[p]
        
        if p is "start":
            break
        
    return "到达终点最短路径是：终点<-%s起点 \n最小开销为%s分钟" % (best_route,costs["fin"])

print(best_route())