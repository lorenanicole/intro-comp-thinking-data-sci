1. For questions 1 and 2, consider our previous problem (permutations of 3 students in a line).

When represented as a tree, each node will have how many children?

Answer: 2

2. Given two permutations, what is the maximum number of swaps it will take to reach one from the other?

Example: 
ABC

CBA
BCA # one swap
BAC # two swap
ABC # three swap

Answer: 3

3. For questions 3 and 4, consider the general case of our previous problem (permutations of n students in a line). Give your answer in terms of n.

When represented as a tree, each node will have how many children?

Answer: n-1

In any given permutation, n students are lined up. Since one may only swap the positions of two adjacent students, there are exactly n−1 pairs we are able to swap. Each of these swaps will create a distinct ordering, so there are exactly n−1 childern of each node.

4. Given two permutations, what is the maximum number of swaps it will take to reach one from the other?

n * (n-1)/ 2

Consider the case where the two permutations whose exchange would take the maximum number of swaps. Clearly these are two whose orders are opposite. It takes n−1 swaps to move the last person in line to the first position. This leaves the rest of the line's old order intact.

Next it takes n−2 swaps to move the last person in line to the second position. We continue until only one more swap is needed (switching the last two people in line). This takes (n−1)+(n−2)+...+2+1=n⋅n−12 swaps.