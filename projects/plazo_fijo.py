"""
Define cuanto se puede ganar mensualmente con una determinada TNA (tasa nominal anual) y un monto.
"""

tna = 56.7
tasa_mensual = tna / 12
tasa_mensual_2f = "{:.2f}".format(tasa_mensual)
print("----------------------------------------")
print("Plazo Fijo App")
print(f"La tasa nominal anual es del {tasa_mensual_2f}%, y del {tasa_mensual}% a 30 días")
print("----------------------------------------")

monto = float(input("Monto a invertir $: "))
ganancia = "{:.2f}".format((monto * tasa_mensual) / 100 + monto)
print(f"En 30 días vas a recibir ${ganancia}")
