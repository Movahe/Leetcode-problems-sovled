"""
Given two unsorted arrays of the same size, write a function that returns true if two arrays are permutations of each other,
otherwise false.(it may contain duplicates)
"""

from collections import defaultdict
import time
def arePermutations1(arr1, arr2):   # time complexity O(n)
    # Arrays cannot be permutations of one another unless they are of the same length
    if len(arr1) != len(arr2):
        return False

    # Creates an empty hashMap hM
    hM = defaultdict(int)
    # Traverse through the first array and add elements to hash map

    # for i in range (len(arr1)):
    #     x = arr1[i]
    #     hM[x] += 1

    for _, x in enumerate(arr1):
        hM[x] += 1
    # print(hM)
    # Traverse through second array and check if every element is present in hash map
    for i in range(len(arr2)):
        x = arr2[i]
        # If element is not present in hash map, or element appear less number of times than in the first arr,
        # then return false.
        if x not in hM or hM[x] == 0:
            return False
        hM[x] -= 1
    return True


def arePermutations2(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    else:
        sum1, sum2, mul1, mul2 = 0, 0, 1, 1
        for i in range(len(arr1)):
            sum1 += arr1[i]
            mul1 *= arr1[i]
        for j in range(len(arr2)):
            sum2 += arr2[j]
            mul2 *= arr2[j]
        # print("sum1:{}, sum2:{}, mul1:{}, mul2:{}".format(sum1, sum2, mul1, mul2))

        if (sum1 == sum2) and (mul1 == mul2):
            return True
        else:
            return False


def arePermutations3(arr1, arr2):  # using the sort takes O(n log n)Time
    if len(arr1) != len(arr2):
        return False
    else:
        arr1 = arr1.sort()
        arr2 = arr2.sort()
        if arr1 == arr2:
            return True
        else:
            return False


# Driver code
if __name__ == "__main__":

    arr1 = [2, 1, 2, 3, 5, 4, 3, 2]
    arr2 = [3, 2, 2, 2, 4, 5, 3, 1]
    t_i = time.time()
    if arePermutations1(arr1, arr2):
        print("Arrays are permutations of each other")
    else:
        print("Arrays are NOT permutations of each other")
    t_f = time.time()
    print("dict check time:", t_f-t_i)

    t_i = time.time()
    output2 = arePermutations2(arr1, arr2)
    t_f = time.time()
    print(output2, "time cost:", t_f - t_i)


    t_i = time.time()
    output3 = arePermutations3(arr1, arr2)
    t_f = time.time()
    print(output3, "time cost:", t_f-t_i)