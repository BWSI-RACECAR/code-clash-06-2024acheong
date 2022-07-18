"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #6 - Longest Distance Between Checkpoints (checkpoints.py)


Author: Chris Lai

Difficulty Level: 3/10

Prompt: The Grand Prix is an obstacle course for the RACECAR. Each of the RACECARs must traverse the course 
and navigate through checkpoints. At the beginning of each obstacle, there will be a checkpoint, at which the 
RACECAR can stop to refuel. Before the course starts, each competitor is given an array of values that indicate 
the distance of these checkpoints (in meters) relative to the starting line. In order to prepare your RACECAR 
for the final race, you want to calculate the longest distance between two checkpoints such that your car has 
enough fuel to last the entire leg.

Given an array of checkpoint distance values, return an integer to represent the longest distance between two checkpoints.

Constraints: All numbers in the array “n” will be integers 10^9 >= n >= 0. Assume the number of items in the 
array “k” will be 10^9 >= k > 0. You may not use the Python sort() method.

Test Cases:
Input: [0, 3, 4, 9] ; Output: 5
Input: [10, 8, 4, 1] ; Output: 4
Input: [5, 0, 3, 6] ; Output: 3
"""

class Solution:
    def longestdistance(self, checkpoints):
        # type checkpoints: list
        # return type: int
        
        # TODO: Write code below to return an int with the solution to the prompt
        copy_arr = []
        for num in checkpoints:
            copy_arr.append(num)
        self.merge_helper(0, len(checkpoints)-1, checkpoints, copy_arr)
        distance = 0
        for i in range(0, len(checkpoints) - 1):
            if (checkpoints[i+1] - checkpoints[i] > distance):
                distance = checkpoints[i+1] - checkpoints[i]
        return distance

    def merge_sort(self, low, mid, high, arr, copy):
        i = low
        k = mid+1
        j = low
        while (i <= mid and k<= high):
            if (arr[i] <= arr[k]):
                copy[j] = arr[i]
                i += 1
                j += 1
            elif (arr[k] <= arr[i]):
                copy[j] = arr[k]
                k += 1
                j += 1
        while (i <= mid):
            copy[j] = arr[i]
            i += 1
            j += 1
        while ( k <= high):
            copy[j] = arr[k]
            j += 1
            k += 1
        for x in range(0, (high-low) + 1):
            arr[low+x] = copy[low+x]

    def merge_helper(self, low, high, arr, copy):
        if (low < high):
            mid = (low + high) // 2
            self.merge_helper(low, mid, arr, copy)
            self.merge_helper(mid+1, high, arr, copy)
            self.merge_sort(low, mid, high, arr, copy)

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.longestdistance(array)
    print(ans)

if __name__ and "__main__":
    main()