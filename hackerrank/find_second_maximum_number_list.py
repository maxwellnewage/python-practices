"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
"""

if __name__ == '__main__':
    n = 5
    arr = map(int, "2 3 6 6 5".split())

    unique_arr = set(arr)
    sorted_arr = sorted(unique_arr, reverse=True)

    print(sorted_arr[1])
