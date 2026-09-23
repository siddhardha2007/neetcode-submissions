class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for point in points:
            dist=point[0]**2 + point[1]**2
            distances.append((dist,point))
        distances.sort()
        res=[]
        for i in range(k):
            res.append(distances[i][1])
        return res    

                    
        