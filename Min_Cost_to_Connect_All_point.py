//
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        mincost = 0
        edges = []
        for i in range(len(points)-1):
            mindst = float('inf')
            xi, yi = points[i][0], points[i][1]
            print(i)
            for j  in range(len(points)-1):
                if(i == j):
                    continue
                else:
                    xj, yj = points[j][0], points[j][1]
                    mhndst = abs(xi-xj) + abs(yi-yj)
                    if(mhndst < mindst and  (j+1,i+1,mhndst) not in edges):
                        for u,v in edges:
                            if(find(u)!= find(v)):
                                mindst = mhndst
                                mindex = j
        
            edges.append((i+1,mindex+1,mindst))
        edges.sort(key= lambda x:x[2])
        mincost = 0
        # 1,2    2,3    2,4 , 4,5 , 
        print(edges)
        for i in edges:
            mincost+=i[2]
        return mincost
