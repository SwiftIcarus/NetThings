import matplotlib.pyplot as plt
import itertools


def unit_cost(kwh_cost, standing_cost, usage=0, period=1):
    return kwh_cost*usage/100 + standing_cost*period/365


def period_cost(tariff, usage=0, period=1):
    '''
    period_cost - Calculates the total cost in £ for an arbitrary time period
    :param tariff: Dictionary of available tariffs
    :param usage: Usage in kWh of heat - Default 0
    :param period: Time period to calculate in days - Default 1
    :return:
    '''
    cost = {}
    for name, item in tariff.items():
        cost[name] = unit_cost(item[0], item[1], usage, period)
    return cost


def plot_series(tariff, kwh_start=0, kwh_end=50, period=1):
    single_tariff = [35.62, 139.28]
    x_range = range(kwh_start, kwh_end, 1)

    for name, item in tariff.items():
        y_range = [unit_cost(item[0], item[1], units, period) for units in x_range]
        plt.plot(x_range, y_range, label=name)

    plt.title(f'Plotting total cost based on a period of {period} days')
    plt.xlabel('kWh of Heat Consumed')
    plt.ylabel('Total cost in £')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    # Tariffs available in format 'NAME': [p/kWh, annual charge]
    tariffs = {'Heat 1': [35.62, 139.28],
               'Heat 2': [28.40, 264.62],
               'Heat 3': [10.76, 504.49],
               'Heat 4': [15.63, 527.75]}

    plot_series(tariffs, 0, 500, 31)

