# User function Template for python3
from collections import OrderedDict


class Solution:
    def removeDups(self, str):
        # code here
        return ''.join(OrderedDict.fromkeys(str))

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends
