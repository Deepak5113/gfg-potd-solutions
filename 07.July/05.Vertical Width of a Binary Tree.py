# User function Template for python3

from collections import deque
maxi = 0
mini = 0


def solve(root, distance):
    if not root:
        return
    global mini, maxi
    mini = min(mini, distance)
    maxi = max(maxi, distance)
    solve(root.left, distance-1)
    solve(root.right, distance+1)
# Function to find the vertical width of a Binary Tree.


def verticalWidth(root):
    # code here
    if not root:
        return 0
    global mini, maxi
    # Initialize mini and maxi for each new tree
    mini = float('inf')
    maxi = float('-inf')
    solve(root, 0)
    return maxi-mini+1


# {
 # Driver Code Starts


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        print(verticalWidth(root))

# } Driver Code Ends
