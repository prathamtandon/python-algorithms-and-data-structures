# Given a binary tree, print it vertically. 
          #1
        #/    \
       #2      3
      #/ \    / \
     #4   5  6   7
             #\   \
              #8   9 
               
			  
#The output of print this tree vertically will be:
#4
#2
#1 5 6
#3 8
#7
#9

# If two nodes have the same Horizontal Distance (HD), then they
# are on same vertical line. The idea of HD is simple - 
# 1. HD for root is zero.
# 2. A right edge is considered HD + 1
# 3. A left edge is considered HD - 1

def getVerticalOrder(node,hd,memo):
        if node is None:
                return
        if hd in memo:
                memo[hd].append(node)
        else:
                memo[hd] = [node]
        
        getVerticalOrder(node.left,hd-1,memo)
        getVerticalOrder(node.right,hd+1,memo)

def printVerticalOrder(root):
        memo = {}
        hd = 0
        getVerticalOrder(root,hd,memo)
        res = []
        
        for dist in memo:
                temp = []
                for node in memo[dist]:
                        temp.append(node.key)
                res.append(temp)
        
        return res
                        
        
        
