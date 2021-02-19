class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        
          

        neg_limit =-0x80000000 # hex(-2**31-1),see details in accepted answer above
        pos_limit = 0x7fffffff #hex(2**31-1)
        if x==0:
            return True
        if x >0:
            reverse_num = int(str(x)[::-1])
            if reverse_num & pos_limit==reverse_num & reverse_num == x: #conditions explained above
                return True
            else:
                return False

        elif x <0:
            reverse_num = -int(str(abs(x))[::-1])
            if reverse_num&neg_limit == neg_limit & reverse_num == x:
                return True
            else:
                    return False
        else:
            return False

