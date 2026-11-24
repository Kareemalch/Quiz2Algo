class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        mincost = 0
        edges = []
        for i in range(len(points)):
            xi, yi = points[i][0], points[i][1]
            print(i)
            for j  in range(len(points)-1):
                if(i == j):
                    continue
                else:
                    xj, yj = points[j][0], points[j][1]
                    mhndst = abs(xi-xj) + abs(yi-yj)
                    if((j+1,i+1,mhndst) not in edges):
                        edges.append((i+1,j+1,mhndst))
        def find(v):
            if parent.setdefault(v,v) != v:
                parent[v] = find(parent[v])
            return parent[v]
        def union(u,v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v
        edges.sort(key= lambda x:x[2])
        mintree = []
        mincost = 0
        edgedex = 0
        parent = {}
        for u, v, w in edges:
            if(find(u) != find(v)):
                union(u,v)
                mintree.append((u,v,w))
                mincost += w
        return mincost
