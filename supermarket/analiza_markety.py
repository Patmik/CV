import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db_markets = pd.read_csv('supermarket_sales - Sheet1.csv')
db_markets.head()

#dodaje kolumny miesiecy godzin oraz dni
db_markets['Date']
db_markets['Month']=db_markets['Date'].apply(lambda x :x.split('/')[0])
db_markets['Day']=db_markets['Date'].apply(lambda x :x.split('/')[1])
db_markets['Hour']=db_markets['Time'].apply(lambda x :x.split(':')[0])

db_markets

#sprawdzenie ilości klientów po miesiącach
month_results=db_markets.groupby('Month').count()

months=range(1,4)
plt.plot(months,month_results)

plt.title('Klienci w ciągu danego miesiąca',fontdict={'fontsize':20})
plt.xlabel('miesiąc')
plt.ylabel('ilość klientów')
plt.xticks([1,2,3])

plt.savefig('grafy/klient_miesiac.png',dpi=300)
plt.close()

#plt.show()

#sprawdzanie ilości klientów po dniach
day_results=db_markets.groupby('Day').count()
days=range(1,32)
plt.plot(days,day_results)
plt.title('Klienci w ciągu danego dnia miesiąca',fontdict={'fontsize':20})
plt.xlabel('dzień miesiąca')
plt.ylabel('ilość klientów')


plt.savefig('grafy/klient_dzien_miesiaca.png',dpi=300)
plt.close()
#plt.show()

#sprawdzanie ilości klientów po godzinach

hour_results=db_markets.groupby('Hour').count()
hours=[hour for hour, df in db_markets.groupby('Hour')]

plt.title('Klienci w ciągu dnia',fontdict={'fontsize':20})
plt.xlabel('godzina')
plt.ylabel('ilość klientów')


plt.plot(hours,hour_results)
plt.savefig('grafy/klient_dzien.png',dpi=300)
plt.close()

#plt.show()

# najbardziej dochodowy product line

db_markets['all_purchases']=db_markets['Unit price']*db_markets['Quantity']
results=db_markets.groupby('Product line')['all_purchases'].sum()
results

product_lines=[product_line for product_line, df in db_markets.groupby('Product line')]



plt.bar(product_lines,results)

plt.title('Najbradziej dochodowy typ produktu',fontdict={'fontsize':20})
plt.xlabel('typ produktu')
plt.ylabel('gotówka')

plt.xticks(product_lines,rotation='vertical')



plt.savefig('grafy/top_product_line.png',bbox_inches="tight",dpi=300)
plt.close()
#plt.show()

#podział na kobiety i mężczyzn
male=db_markets.loc[db_markets['Gender']=='Male']
female=db_markets.loc[db_markets['Gender']=='Female']

#podział na customer type

male_type=male.groupby('Customer type')['Gender'].count()
female_type=female.groupby('Customer type')['Gender'].count()

#podział na product line
male_product=male.groupby('Product line')['Gender'].count()
female_product=female.groupby('Product line')['Gender'].count()

male_type

#wykresy

customer_types=[customer_type for customer_type, df in db_markets.groupby('Customer type')]

#liczba parowanych wykresów
N=2


#pozycja na x

ind = np.arange(N)

#rozmiar
plt.figure(figsize=(10,5))

#grubość kolumny
width=0.3

#rysowanie

plt.bar(ind,male_type,width,label='Male')
plt.bar(ind+width,female_type,width,label='Female')

plt.xlabel('Typ klienta')
plt.ylabel('Ilość typu klientów')
plt.title('Porównanie typów klientów kobiety vs mężczyźni',fontdict={'fontsize':20})


plt.xticks(ind + width / 2, (customer_types))


plt.legend(loc='best')

plt.savefig('grafy/klienci_typ.png',bbox_inches="tight",dpi=300)
plt.close()
#plt.show()

#mężczyźni

labels=[product_type for product_type, df in db_markets.groupby('Product line')]

plt.pie(male_product,labels =labels, autopct = '%.2f%%' )
plt.title('Porównanie popularności typów produktów - mężczyźni',fontdict={'fontsize':15})
plt.savefig('grafy/male_top_product_line.png',bbox_inches="tight",dpi=300)

plt.close()
#plt.show()
male_product


#kobiety
labels=[product_type for product_type, df in db_markets.groupby('Product line')]

plt.pie(female_product,labels =labels, autopct = '%.2f%%' )
plt.title('Porównanie popularności typów produktów-kobiety',fontdict={'fontsize':20})
plt.savefig('grafy/female_top_product_line.png',bbox_inches="tight",dpi=300)

plt.close()
#plt.show()
female_product

#miasta dochodowość

cities_income=db_markets.groupby('City')['all_purchases'].sum()
cities=[city for city, df in db_markets.groupby('City')]

cities_income

plt.bar(cities,cities_income)
plt.title('Najbradziej dochodowe miasto',fontdict={'fontsize':17})
plt.xlabel('miasto')
plt.ylabel('gotówka')

plt.savefig('grafy/top_city.png',bbox_inches="tight",dpi=300)
plt.close()
#plt.show()