class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        mincost = 0
        edges = []
        if len(points) < 2: return 0
        for i in range(len(points)):
            mindst = float('inf')
            xi, yi = points[i][0], points[i][1]
            for j  in range(len(points)):
                if(i == j):
                    continue
                else:
                    xj, yj = points[j][0], points[j][1]
                    mhndst = abs(xi-xj) + abs(yi-yj)
                    edge = (i+1,j+1,mhndst)
                    if(mhndst < mindst and (j+1,i+1,mhndst) not in edges):
                        mindst = mhndst
                        minedge = edge
            edges.append(minedge)
        edges.sort(key= lambda x:x[2])
        unweighted = [(x[0],x[1]) for x in edges]
        mincost = 0
        # 1,2    2,3    2,4 , 4,5
        def has_cycle(e):
            parent = {}
            def find(node):
                if parent.setdefault(node,node) != node:
                    parent[node] = find(parent[node])
                return parent[node]
            for i, (u,v) in enumerate(e):
                root_u = find(u)
                root_v = find(v)
                if root_u == root_v:
                    return i
                parent[root_u] = root_v
            return -1
        if(has_cycle(unweighted)!=-1):
            edges.pop(has_cycle(unweighted))
        print(edges)
        for i in edges:
            mincost+=i[2]
        return mincost
