"""
https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
"""

if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3

    coords = []

    for x_val in range(x + 1):
        for y_val in range(y + 1):
            for z_val in range(z + 1):
                coord = [x_val, y_val, z_val]
                coords.append(coord)

    output = [coord for coord in coords if coord[0] + coord[1] + coord[2] != n]

    print(output)
