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

with open("products.csv", 'r') as myFile:
    for myLine in myFile:
        myData = [int(x) for x in myLine.strip().split(',')]
        itemDims = [myDim for myDim, maxDim in zip(sorted(myData[2:5]), toteDims) if myDim <= maxDim]
        if len(itemDims) == 3:
            productsList.append((myData[0], myData[1], List_Multiply(myData[2:5]), myData[5]))

print(Solver(productsList, totalVolume))

''' 
Total Value: 41298
Items: [1370, 4887, 5084, 6532, 8699, 9972, 10496, 10981, 12856, 12979, 14301, 14448, 17788, 17896, 26950, 27376, 31288, 33638, 34414, 35280, 36175, 36769, 39987]
Sum(IDs): 450166