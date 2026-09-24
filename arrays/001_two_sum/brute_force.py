"""
Problem: Two Sum
Difficulty: Easy
Topic: Arrays

Given an array of integers nums and an integer target,
return the indices of two numbers whose sum equals target.

Example:
    Input:
        nums = [2, 7, 11, 15]
        target = 9

    Output:
        [0, 1]

Approach: Brute Force

Compare every element with every element that appears after it.
If the sum of the two elements equals the target, return their
indices.

Time Complexity:
    O(n^2)

Space Complexity:
    O(1)
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))