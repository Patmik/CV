#odczytanie danych

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_games=pd.read_csv('vgsales.csv')
df_games

#top gry
top_10=df_games.sort_values('Global_Sales',ascending=False).head(10)
top_10

#Dla danego roku top 3 gry
years=[year for year, df in df_games.groupby('Year')]
for year in years:
    temp=df_games.loc[df_games['Year']==year].reset_index(drop=True)
    top=temp.sort_values('Global_Sales',ascending=False)['Name'].head(3)
    print(year)
    print(top)
    print('\t')

df_games.groupby('Name').sum()

# sprzedaż po kontynentach, wszechczasów
sales = df_games.groupby('Year').sum()

na_sales = 0
eu_sales = 0
jp_sales = 0

for index, row in sales.iterrows():
    na_sales += row['NA_Sales']
    eu_sales += row['EU_Sales']
    jp_sales += row['JP_Sales']

x = ["na_sales", "eu_sales", "jp_sales"]
y = [na_sales, eu_sales, jp_sales]

plt.bar(x, y)

plt.title('Najbradziej dochodowy kontynent', fontdict={'fontsize': 17})
plt.xlabel('Kontynent')
plt.ylabel('Sprzedaż')

plt.savefig('grafy/continent_sales.png', bbox_inches="tight", dpi=300)
plt.close()
#plt.show()

#najpopularnijeszy rodzaj gier

top_genre=df_games.groupby('Genre')['Publisher'].count()
top_genre.sort_values(ascending=False)

#najpopularniejsza platforma

top_platform=df_games.groupby('Platform')['Publisher'].count()
top_platform.sort_values(ascending=False)

###zmiany w czasie###
df_games['count'] = 1

# konsole w czasie

years = [year for year, df in df_games.groupby('Year')]
platforms = [platform for platform, df in df_games.groupby('Platform')]

x = years

y = []
for year in years:
    t = []
    for platform in platforms:
        k = df_games.loc[(df_games['Platform'] == platform) & (df_games['Year'] == year)]['Platform'].count()
        t.append(k)

    y.append(t)

for ys in y:
    plt.plot(x, y)

plt.title('Zmiany popularności konsol w czasie', fontdict={'fontsize': 20})
plt.xlabel('Rok ')
plt.ylabel('Ilość konsol')

plt.savefig('grafy/time_consoles.png', bbox_inches="tight", dpi=300)
plt.close()

#plt.show()

# rodzaj gry w czasie

years = [year for year, df in df_games.groupby('Year')]
genres = [genre for genre, df in df_games.groupby('Genre')]

x = years

y = []
for year in years:
    t = []
    for genre in genres:
        k = df_games.loc[(df_games['Genre'] == genre) & (df_games['Year'] == year)]['Genre'].count()
        t.append(k)

    y.append(t)

for ys in y:
    plt.plot(x, y)

# wykres estetyka
plt.title('Rodzaj gry w czasie', fontdict={'fontsize': 20})
plt.xlabel('Rok ')
plt.ylabel('Ilość ilość gier')

plt.savefig('grafy/time_games.png', bbox_inches="tight", dpi=300)
plt.close()
#plt.show()