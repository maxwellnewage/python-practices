"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lst = [[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1)]
    
# lst == 
        # for i in range(0, x+1):
        #     for j in range(0, y+1):
        #         for k in range(0, z+1):
        #             lst.append([i, j, k])

    
    output = [elem for elem in lst if sum(elem) != n]
    print(output)