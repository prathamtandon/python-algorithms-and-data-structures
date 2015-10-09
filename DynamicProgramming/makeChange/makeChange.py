# Given an infinte number of quarters (25 cents), dimes (10 cents),
# nickles (5 cents), and pennies (1 cent), write code to calculate the
# number of ways of representing n cents.

# let map[i][j] denote the number of ways to have amount i using only
# denominations 1,2,...,j where j goes from 1 through 4 (4 denominations)

def makeChanges(n):
	denoms = [25,10,5,1]
	amount_map  = [[0]*len(denoms)]*(n+1)
	
	makeChanges_helper(n,denoms,0,amount_map)

def makeChanges_helper(amount,denoms,index,amount_map):
	if index >= len(denoms)-1:
		return 1
	if amount_map[amount][index] > 0:
		return amount_map[amount][index]
	denomAmount = denoms[index]
	ways = 0
	i = 0
	while i*denomAmount <= amount:
		amountRemaining = amount-i*denomAmount
		ways += makeChanges_helper(amountRemaining,denoms,index+1,amount_map)
		i += 1
	amount_map[amount][index] = ways
	return ways
	
	
