"""
Nexo Earn Calculator
"""
import pandas as pd
import sys
import matplotlib.pyplot as plt


def get_rule(df_length):
    if df_length >= 365:
        return 'M', 'Mensual'
    else:
        return 'D', 'Diario'


def show_earn_plot(dataframe):
    # preparo un df con información más reducida mediante el muestreo de fechas
    dataframe = dataframe.groupby('Date / Time (UTC)').sum()
    date_usd_series = pd.Series(dataframe['USD Equivalent'].values, index=dataframe.index)
    rule = get_rule(dataframe.shape[0])
    grouped_df = date_usd_series.resample(rule[0]).sum()

    # armo un gráfico de ganancias en el tiempo
    plt.figure(figsize=(10, 6))
    plt.plot(
        grouped_df.index,
        grouped_df.values,
        marker='o',
        linestyle='-',
        color='b'
    )

    plt.xlabel('Date (UTC)')
    plt.ylabel('USD Equivalent')
    plt.title(f'Gráfico de ganancias a lo largo del tiempo ({rule[1]})')

    plt.xticks(rotation=45, fontsize=8)

    plt.show()


if __name__ == '__main__':
    # pasar el archivo por parámetro sin extensión
    df = pd.read_csv(f"{sys.argv[1]}.csv", sep=",")

    # elimino filas distintas del interés
    df = df.drop(df[df['Type'] != 'Interest'].index)

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

    # devuelvo los resultados en consola
    title = f"Ganancias en el periodo del {start_date} al {init_date}"
    print(title)
    print("-" * len(title))

    for crypto, total in total_earned_by_crypto.items():
        print(f'{crypto} | ${round(total, 2)}')

    print("-" * len(title))
    print(f"Total: ${total_earned}")

    # muestro un gráfico de intereses
    show_earn_plot(df)
