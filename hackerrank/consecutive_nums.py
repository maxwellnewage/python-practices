"""
https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""

if __name__ == '__main__':
    n = int(input())
    n_str = ""
    for num in range(1, n + 1):
        n_str += str(num)

    print(n_str)
