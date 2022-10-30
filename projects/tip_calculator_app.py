"""
Calculadora de propinas
"""


def calculate_food_total(food: float, tip: float) -> float:
    tip_amount = food * (tip / 100)
    total = tip_amount + food
    print('---------------------------')
    print(f'🍔 Costo de la comida: ${food_amount}')
    print(f'💰 Valor de la propina: ${tip_amount}')
    print(f'💵 Total: ${total}')
    print('---------------------------')
    return total


food_amount = float(input('Ingresa el costo de la comida $: '))
tip_percentage = float(input('Ingresa el porcentaje de la propina %: '))
print(calculate_food_total(food_amount, tip_percentage))
