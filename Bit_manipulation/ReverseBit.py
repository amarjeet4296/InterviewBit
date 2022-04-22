## https://www.interviewbit.com/problems/reverse-bits/submissions/
## Reverse the bits of an 32 bit unsigned integer A.

class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        B = 0
        for i in range(32):
            B<<=1
            B|= A&1
            A>>=1
        return B
