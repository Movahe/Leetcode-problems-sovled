"""
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i-1]*i)

            # generate nums= ['1', '2', '3',...'n']
            nums.append(str(i+1))
        print(factorials)
        # fit k in the interval 0 ... (n! - 1)
        k -= 1
        output = []
        # compute factorial representation of k
        for i in range(n-1, -1, -1):
            idx = k//factorials[i]
            k -= idx*factorials[i]

            output.append(nums[idx])
            del nums[idx]
        return ''.join(output)


res = Solution().getPermutation(3, 5)
print(res)
assert res == '312'


"""

The problem with permutations is that there is a much more permutations than subsets, N! grows up much faster 
than 2^N. 
k = \sum_{m=0}^{N-1} k_m * m!, where 0<= k_m <= m. 
We could map all permutations from permutation number zero: k=0=\sum_{m=0}^{N-1} 0* m! 
to permutation number N!-1: k=N!-1 = \sum_{m=0}^{N-1} m * m!
 
Permutation             permutation number                  Factorial number system representation
123                     k= 0 = 0*2!+0*1!+0*0!                  0 0 0
132                     k= 1 = 0*2!+1*1!+0*0!                  0 1 0
213                     k= 2 = 1*2!+0*1!+0*0!                  1 0 0
231                     k= 3 = 1*2!+1*1!+0*0!                  1 1 0
312                     k= 4 = 2*2!+0*1!+0*0!                  2 0 0 
321                     k= 5 = 2*2!+1*1!+0*0!                  2 1 0 


For instance, k = 2, factorial representation gives k=2=1*2!+0*1!+0*0! = (1, 0, 0), 
the first element is 1, i.e. the first element in the permutation is nums[1] = 2.
Let us use nums[1]=2 in the permutation and then delete it from nums, since each element should be used only once.
Next coefficient in factorial representation is 0, let's use nums[0]=1 in the permutation and then delete it from nums.
Next coefficient in factorial representation is 0, let's use nums[0]=3 and delete it from nums. Job is done.

"""