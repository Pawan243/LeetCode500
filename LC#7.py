class Solution:
    def reverse(self, x: int) -> int:
        neg_limit =-0x80000000 # hex(-2**31-1),see details in accepted answer above
        pos_limit = 0x7fffffff #hex(2**31-1)
        if x >0:
            reverse_num = int(str(x)[::-1])
            if reverse_num & pos_limit==reverse_num: #conditions explained above
                return reverse_num
            else:
                return 0

        elif x <0:
            reverse_num = -int(str(abs(x))[::-1])
            if reverse_num&neg_limit == neg_limit:
                return reverse_num
            else:
                    return 0
        else:
            return 0
