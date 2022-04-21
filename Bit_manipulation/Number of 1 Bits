// https://www.interviewbit.com/problems/number-of-1-bits/
// Write a function that takes an integer and returns the number of 1 bits it has.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while (A):
            A = A & A-1
            count += 1
        return count
