class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num1=""
        l=[]
        for i in digits:
            num1=num1+str(i)
        num2=1+int(num1)
        num2=str(num2)
        for i in num2:
            l.append(int(i))
        return l        
            
        