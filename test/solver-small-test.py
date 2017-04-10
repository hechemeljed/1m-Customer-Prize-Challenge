from functools import reduce
	
# The main solver function
def Solver(myItems, myCapacity):

    dp = {myCapacity: (0, (), 0)}
    getKeys = dp.keys
	
    for i in range(len(myItems)):
        itemID, itemValue, itemVolume, itemWeight = myItems[i]
        for oldVolume in sorted(getKeys()):

            newVolume = oldVolume - itemVolume
			
            if newVolume >= 0:
                myValue, ListOfItems, myWeight = dp[oldVolume]
                node = (myValue + itemValue, ListOfItems + (itemID,), myWeight + itemWeight)
                if newVolume not in dp:
                    dp[newVolume] = node
                else:
                    currentValue, loi, currentWeight = dp[newVolume]
                    if currentValue < node[0] or (currentValue == node[0] and node[-1] < currentWeight):
                        dp[newVolume] = node
    return max(dp.values())

# Generate the product of all elements within a given list
def List_Multiply(myList):
    return reduce(lambda x, y: x * y, myList)
	
toteDims = [30, 35, 45]  
totalVolume = List_Multiply(toteDims)
productsList = []  

with open('100set.csv', 'r') as f:
    for line in f:
        data = [int(e) for e in line.strip().split(',')]
        item_dims = [dim for dim, max_dim in zip(sorted(data[2:5]), toteDims) if dim <= max_dim]
        if len(item_dims) == 3:
            productsList.append((data[0], data[1], List_Multiply(data[2:5]), data[5]))

print(Solver(productsList, totalVolume))