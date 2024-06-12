class Solution:
# City of network.
# Undirected, find max-connections of 2.
# Find max number of connection.
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        from collections import defaultdict
        d = defaultdict(set)
        for road in roads:
            d[road[1]].add(road[0])
            d[road[0]].add(road[1])
        
        def get_indegree(graph,i):
            indegree = 0
            for t in range(n):
                if t != i:
                    if i in graph[t]:
                        indegree += 1
            return indegree
        
        indegree_map = defaultdict(int)
        for i in range(n):
            indegree_map[i] = get_indegree(d,i)
        
        max_infra = 0
        values = []
        for k,v in indegree_map.items():
            values.append(v)
        
        #print(values)
        values.sort()
        return values[-1] + values[-2] - 1
        #return 10
