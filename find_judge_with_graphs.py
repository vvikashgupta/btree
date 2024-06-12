class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Let us assume that this is a graph problem.
        # In that case the judge will have an indegree of 0 and adjacencies of n-1.
        self.n = n
        self.trust = False
        def printme(g):
            for k,v in g.items():
                print(f'{k},{v}')
                
                
        def get_inorder(g, i):
            result = 0
            for j in range(1,self.n + 1):
                if j != i and i in g[j]:
                    result += 1
            #print(f'inorder of {i} is {result}')
            return result
                
        from collections import defaultdict
        graph = defaultdict(set)
        for item in trust:
            graph[item[1]].add(item[0])
            if self.trust:
                graph[item[0]].add(item[1])
        
        #printme(graph)
        
        #Now let us build an indegree dict of all the above vertices.
        inorder = defaultdict()
        #map = []
        #deq = deque()
        for i in range(1,self.n+1):
            inorder[i] = get_inorder(graph, i)
            if not inorder[i]:
                if len(graph[i]) == self.n-1:
                    return i
        else:
            return -1
                #deq.append(i)
        #print(f'Inorder dict is {inorder}')
        #print(deq)
        
        #for item in deq:
        #    print(f'{len(graph[item])}, {item}, {self.n}')
        #    if len(graph[item]) == self.n -1 :
        #        return item
        #else:
        #    return -1
