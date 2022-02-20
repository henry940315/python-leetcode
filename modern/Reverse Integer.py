class Solution(object):
    def reverse(self, x:int):
        if x>0:
            a = str(x)[::-1]
            int_a = int(a)
            
            if ((2**31)-1) <=int_a or int_a <= -2**31:
                return 0
            else:            
                return int_a
        elif x<0:
            b = str(0-x)[::-1]
            int_b = int(b)
            new_b = (0-int_b)
            if ((2**31)-1)<=new_b or new_b<= -2**31:
                return 0
            else:            
                return new_b
        elif x == 0:
            return 0
        
        
            
            
data = Solution.reverse(0,1534236469)
print(data)



        