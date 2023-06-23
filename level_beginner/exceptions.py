"""
Manejo de excepciones
"""

def print_box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbol debe ser un str de tamaño 1")
    
    if width < 2 or height < 2:
        raise Exception("width y height deben ser mayores o iguales a 1")
    
    print(symbol * width) # Top line

    # Middle
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    print(symbol * width) # Bottom line

if __name__ == '__main__':
    print_box('*', 15, 5)
    print_box('**', 15, 5)
    print_box('**', 1, 1)