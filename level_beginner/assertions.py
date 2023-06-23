"""
Manejo de assertions
"""

def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Never is red!'

if __name__ == '__main__':
    # AssertionError: Never is red!
    traffic_light = {'ns': 'green', 'ew': 'red'}

    print(traffic_light)
    switch_lights(traffic_light)
    print(traffic_light)