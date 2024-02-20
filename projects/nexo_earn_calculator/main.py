"""
Nexo Earn Calculator
"""
import pandas as pd
import sys

if __name__ == '__main__':
    # pasar el archivo por parámetro sin extensión
    df = pd.read_csv(f"{sys.argv[1]}.csv")

    # ordeno por fecha desde la más antigua
    df = df.sort_values(by='Date / Time (UTC)')

    # reemplazo el formato "$1.97" por "1.97" tipo float
    df['USD Equivalent'] = df['USD Equivalent'].str.replace('$', '').astype(float)

    # sumarizo las cantidades totales
    total_earned = df['USD Equivalent'].sum()

    # sumarizo cantidad por crypto
    total_earned_by_crypto = df.groupby('Output Currency').sum()['USD Equivalent']

    # convierto a formato fecha
    df['Date / Time (UTC)'] = pd.to_datetime(df['Date / Time (UTC)'])

    # cambio al formato día/mes/año en un nuevo campo sin hora
    df['Date (UTC)'] = df['Date / Time (UTC)'].dt.strftime('%d/%m/%Y')

    # almaceno el rango de fechas
    start_date, init_date = df['Date (UTC)'].iloc[[0, -1]]

    # devuelvo los resultados
    title = f"Ganancias en el periodo del {start_date} al {init_date}"
    print(title)
    print("-" * len(title))

    for crypto, total in total_earned_by_crypto.items():
        print(f'{crypto} | ${round(total, 2)}')

    print("-" * len(title))
    print(f"Total: ${total_earned}")


