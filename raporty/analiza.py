import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fpdf import FPDF
from datetime import datetime, timedelta


def raport():

    day=(datetime.today()).strftime("%d/%m/%y").replace('/0','/').lstrip('0')

    WIDTH=210
    HEIGHT=297

    pdf=FPDF()

    pdf.add_page()
    pdf.set_font("Arial",'B',16)

    pdf.image("raport/tytul.png",0,0,WIDTH)
    pdf.ln(60)
    pdf.write(5,f'Raport {day}')


    pdf.image("raport/obrot_got.png",10,80,WIDTH-20, 120)


    pdf.image("raport/zyski.png",5,200,WIDTH/2-10,WIDTH/2-10)
    pdf.image("raport/marza.png",WIDTH/2+5,200,WIDTH/2-10,WIDTH/2-10)

    pdf.add_page()

    pdf.image("raport/ilosc_zlec.png",5,0,WIDTH-10)




    pdf.output("raport_SPIE.pdf",'F')










#________________________________________________________________________________________________________________
df=pd.read_excel("Raport_2020-07-27.xls")

df.head()

df_analiza = df.dropna(subset=['Data zakończenia zlecenia'])


df_analiza['count']=1

dodatki=df_analiza[df_analiza['Typ zlecenia']=='Dodatkowe']
results=dodatki.groupby(['Budynek']).sum()
objects = dodatki.groupby(['Budynek'])

buildings = [building for building ,df in objects]

money_rotation = results['Kwota']





fig,ax1=plt.subplots()

ax2=ax1.twinx()
ax1.bar(buildings,results['count'],color='g')
ax2.plot(buildings,money_rotation,'b-')

ax1.set_xlabel('Nazwa Obiektu')
ax1.set_ylabel('Ilość zleceń',color='g')
ax2.set_ylabel('Obrót gotówki',color='b')
ax1.set_xticklabels(buildings,rotation='vertical',size=8)

plt.title('Stosunek ilości zleceń do obrotu gotówki', fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.savefig('raport/obrot_got.png',bbox_inches="tight",dpi=300)
plt.figure(figsize=(5,3),dpi=300)







#dodaje kolumne z zyskiem

dodatki['zysk']=dodatki['Kwota']-dodatki['Kwota zamówień']


results2 = dodatki.groupby(['Budynek']).sum()['zysk']



plt.bar(buildings, results2)
plt.savefig('raport/zyski.png',bbox_inches="tight", dpi=300)
plt.xticks(buildings, rotation='vertical', size=8)
plt.title('Zyski', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.savefig('raport/zyski.png',bbox_inches="tight", dpi=300)
plt.figure(figsize=(5, 3), dpi=300)





#marza
money_finale = results['Kwota zamówień']

marza = (results2/money_finale)*100

plt.bar(buildings, marza)
plt.xticks(buildings,rotation='vertical',size=8)
plt.title('Marża [%]', fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.savefig('raport/marza.png',bbox_inches="tight",dpi=300)
plt.figure(figsize=(5,3),dpi=300)




#dodatki['marza']=(dodatki['zysk']/dodatki['Kwota zamówień'])*100



# dodatki['month']=dodatki['Data utworzenia'].str[5:7]

dodatki['month'] = dodatki['Data utworzenia'].apply(lambda x: x.split('-')[1])



month_orders = dodatki.groupby('month').count()['count']
months = range(1,13)


plt.plot(months,month_orders)
plt.grid()
plt.title('Ilość zleceń na dany miesiąc', fontdict={'fontname':'Comic Sans MS','fontsize':20})
plt.xlabel("miesiąc")
plt.ylabel('ilość zleceń')
plt.xticks(range(1,13))
plt.savefig('raport/ilosc_zlec.png',bbox_inches="tight",dpi=300)
plt.figure(figsize=(5,3),dpi=300)



raport()
