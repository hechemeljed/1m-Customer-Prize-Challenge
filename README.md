# 1m Customer Prize Challenge

This is my solution for the [Redmart Challenge](http://geeks.redmart.com/2015/10/26/1000000th-customer-prize-another-programming-challenge/).

## Solution

As this challenge is very similar to the classic 0-1 knapsack problem, but with some rule changes, I was able to use Dynamic Programming to solve it:


`dp[volume] = [value, items, weight]`

`items = [(ID, value, volume, weight)]`

#### Base Case:
`dp[volume] = [0, [], 0] `

#### Recursive Case:
`dp[volume] = max(dp[volume], dp[old_volume] + item[1])` where `volume = old_volume - item[2]`

### Output
`(41298, (1370, 4887, 5084, 6532, 8699, 9972, 10496, 10981, 12856, 12979, 14301, 14448, 17788, 17896, 26950, 27376, 31288, 33638, 34414, 35280, 36175, 36769, 39987), 32077)`
