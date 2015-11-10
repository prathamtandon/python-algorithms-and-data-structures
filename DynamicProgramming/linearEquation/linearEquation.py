# Find the number of solutions of a linear equation with n variables.

# Recursive function that returns count of solutions for given rhs 
# value and coefficients[begin...end]
def countSoln(coefficients, begin, end, rhs):
        # Base case
        if rhs == 0:
                return 1
        
        result = 0
        
        # Subtract all smaller or equal coefficients and recur
        for i in range(begin,end+1):
                if coefficients[i] <= rhs:
                        result += countSoln(coefficients, i, end, rhs-coefficients[i])
        
        return result


def countSolnOptimized(coefficient, n, rhs):
        
        # Create an array to store results of subproblems
        memo = [0] * (rhs+1)
        memo[0] = 1
        
        for i in range(n):
                for j in range(coefficient[i], rhs+1):
                        memo[j] += memo[j - coefficient[i]]
        
        return memo[rhs]
        
                
