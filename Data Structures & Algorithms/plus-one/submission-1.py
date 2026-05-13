class Solution:
    def plusOne(self, digits: List[int]) -> str:
        num=''
        for i in digits:
            num=num+str(i)
        res=[]
        num=int(num)+1
        num=str(num)
        for i in num:
            res.append(int(i))
        return res 
        