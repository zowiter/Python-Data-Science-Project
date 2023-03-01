import pandas as pd
import matplotlib.pyplot as plt
import sys

sys.path.append('../')
from Library.lib import *

def pt_country_status_mission(df):
    """
    Функция создает сводную таблицу 1
    Входные данные: датафрейм
    Выходные данные: датафрейм
    Автор: Тарасенко И.
    """
    pt1 = pd.pivot_table(df,
                         index=['Country'],
                         values=['Date'],
                         columns=['Status Mission'],
                         aggfunc=[len],
                         fill_value=0)
    return pt1


def pt_2(df):
    """
    Функция создает сводную таблицу 2
    Входные данные: датафрейм
    Выходные данные: датафрейм
    Автор: Тарасенко И.
    """
    pt2 = pd.pivot_table(df,
                         index=['Year', 'Status Mission'],
                         values=['Date'],
                         columns=['Country'],
                         aggfunc=[len],
                         fill_value=0)
    return pt2


def pt_3(df):
    """
    Функция создает сводную таблицу 3
    Входные данные: датафрейм
    Выходные данные: датафрейм
    Автор: Тарасенко И.
    """
    pt3 = pd.pivot_table(df,
                         index=['Year'],
                         values=['Date'],
                         columns=[' Rocket'],
                         aggfunc=[len],
                         fill_value=0)
    return pt3


def outcomes_for_russia(save):
    """
    Функция создает круговой график, показывающий соотношение
    успешных запусков к неуспешным для России, на основе сводной таблицы
    Входные данные: булева переменная
    Выходные данные: нет
    Автор: Маркова Э.
    """
    labels = 'Failure', 'Partial failure', 'Success'
    sizes = [62, 30, 1303]
    explode = (0.5, 0.5, 0.5)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, radius=20, startangle=90)
    ax1.legend(title='Outcomes for Russia:')
    ax1.axis('equal')
    if save == 'True':
        fig1.savefig(path_graph + '/Outcomes for Russia.png')
    if save == 'False':
        plt.show()


def year_success(save):
    """
    Функция строит категоризированную диаграмму зависимости успешных
    запусков от года
    Входные данные: булева переменная
    Выходные данные: нет
    Автор: Маркова Э.
    """
    year = [1962, 1963, 1964, 1965, 1966, 1967, 1968,
            1969, 1970, 1971, 1972, 1973, 1974, 1975]
    number = [4, 7, 7, 13, 33, 37, 40, 52, 54, 56, 60, 63, 64, 71]

    plt.bar(year, number, align='center')
    plt.xlabel('Year')
    plt.ylabel('Number')
    plt.title('Year/successful missions')
    if save == 'True':
        plt.savefig(path_graph + '/Year and success.png')
    if save == 'False':
        plt.show()


def price_year(save):
    """
    Функция строит категоризированную диаграмму рассеивания
    зависимости средней стоимости от года (за 10-e года 21 века)
    Входные данные: булева переменная
    Выходные данные: нет
    Автор Маркова Э.
    """
    x = [2010, 2010, 2010, 2010, 2010, 2010, 2010, 2010, 2011, 2011, 2011, 2011, 2011, 2011, 2011, 2011, 2012, 2012,
         2012,
         2012, 2012, 2012, 2012, 2012, 2013, 2013, 2013, 2013, 2013, 2013, 2013, 2013, 2014, 2014, 2014, 2014, 2014,
         2014, 2014, 2014,
         2015, 2015, 2015, 2015, 2015, 2015, 2015, 2015, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2017, 2017,
         2017, 2017, 2017,
         2017, 2017, 2017, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2019, 2019, 2019, 2019, 2019, 2019, 2019,
         2019]
    y = [90, 47, 450, 350, 21, 200, 140, 120, 80, 450, 40, 25, 21, 164, 145, 113, 90, 42, 350, 31, 21, 164, 140, 113,
         90, 57, 350, 31, 21, 200, 140, 120,
         80, 47, 42, 350, 31, 21, 200, 164, 90, 5, 42, 37, 200, 153, 120, 65, 62, 5, 47, 350, 200, 145, 115, 90, 8, 65,
         49, 31, 200, 145, 123, 65,
         62, 5, 47, 350, 200, 145, 113, 90, 8, 62, 5, 42, 350, 200, 113, 153]
    fig3, ax3 = plt.subplots()
    ax3.scatter(x, y)
    plt.title('Year/average price')
    if save == 'True':
        fig3.savefig(path_graph + '/Price and year.png')
    if save == 'False':
        plt.show()


def number_year(save):
    """
    Функция строит столбчатую диаграмму зависимости количества запусков от года
    Входные данные: булева переменная
    Выходные данные: нет
    Автор Маркова Э.
    """
    df = pd.read_csv(path_to_csv)
    df['Year'] = df['Datum'].apply(lambda x: str(x).split(', ')[-1])
    df['Launch Date_year'] = df['Datum'].apply(lambda x: int(str(x).split()[3]))
    fig4 = plt.figure(figsize=(80, 20))
    df['Launch Date_year'].value_counts().plot(kind='bar')
    plt.xticks(rotation=90)
    plt.title('Number of launches per year')
    if save == 'True':
        fig4.savefig(path_graph + '/Launches per year.png')
    if save == 'False':
        fig4.show()


def max_min_price(save):
    """
    Функция строит категоризированную диаграмму Бокса-Вискера для средней цены запусков
    (за 10-е года 21 века)
    Автор: Маркова Э.
    """
    dict = {'2010': [21, 152, 450], '2011': [21, 450, 105], '2012': [350, 21, 122], '2013': [350, 21, 90],
            '2014': [350, 21, 103],
            '2015': [5.3, 200, 92], '2016': [5.3, 350, 76], '2017': [7.5, 200, 69], '2018': [5.3, 350, 65],
            '2019': [5.3, 350, 59]}
    fig, ax = plt.subplots()
    ax.boxplot(dict.values())
    ax.set_xticklabels(dict.keys())
    ax.set_title('Year/price')
    if save == 'True':
        fig.savefig(path_graph + '/Max and min price.png')
    if save == 'False':
        fig.show()

def success_failure(save):
    """
    Функция создает столбчатую диаграмму, показывающую количество
    успешных/неуспешных запусков, на основе сводной таблицы
    Входные данные: булева переменная
    Выходные данные: нет
    Автор: Маркова Э.
    """
    x =['Failure', 'Partial failure', 'Prelaunch failure', 'Success']
    y = [62, 30, 0, 1303]
    plt.bar(x, y)
    plt.xlabel('Outcome')
    plt.ylabel('Number')
    plt.title('Outcomes for Russia')
    if save == 'True':
        plt.savefig(path_graph + '/Outcomes.png')
    if save == 'False':
        plt.show()