import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#załadowanie danych
fifa = pd.read_csv('data.csv')
fifa.head()
fifa.columns

#czyszczenie
fifa=fifa.drop(columns=['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'])

fifa.columns

fifa=fifa.drop(columns=['ID','Photo','Flag','Overall', 'Potential','Club Logo', 'Special','International Reputation','Weak Foot','Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position',
       'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until','Positioning', 'Vision',
       'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle',
       'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes','Release Clause','ShortPassing', 'Volleys', 'Dribbling', 'Curve',
       'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed'])

fifa.columns
fifa.head()

#indeksy kolumn
col_names=fifa.columns
for name in col_names:
    index_no = fifa.columns.get_loc(name)
    print(" {}  : {}".format(name, index_no))

#stworzenie kolumny total z wynikiem całościowym każdego piłkarza
fifa['Total']=fifa.iloc[:,10:23].sum(axis=1)
fifa

#rank top 10 players

top_10=fifa.sort_values('Total',ascending=False)

top_10.head(10)

#top teams 10
top_10_teams=fifa.groupby(['Club'])['Total'].sum()
top_10_teams.sort_values(ascending=False).head(10)

#porównanie klubów FC barcelona i Juventus
barcelona=fifa.loc[fifa.Club=='FC Barcelona']['Total']
juventus=fifa.loc[fifa.Club=='Juventus']['Total']

plt.boxplot([barcelona,juventus],labels=['FC Barcelona', 'Juventus'])
plt.title('Porównanie FC Barcelony vs Juventus',fontdict={'fontsize':20})

plt.savefig('grafy/barcelona_juventus.png',dpi=300)
plt.close()
#plt.show()

#porównanie wszystkich zawodników  i preferencje nogi

right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]

plt.pie([right,left],labels=['right','left'], autopct='%.2f%%', pctdistance=0.7, explode=(0.11,0.11))

plt.title('Preferencje nogi',fontdict={'fontsize':20})

plt.savefig('grafy/leg_preference',dpi=300)
plt.close()

#plt.show()

fifa.Value=[str(x.strip('K'))if type(x)==str else x for x in fifa.Value]
fifa.Value=[str(x.strip('M'))if type(x)==str else x for x in fifa.Value]
fifa.Value=[float(x.strip('€'))if type(x)==str else x for x in fifa.Value]
fifa

# Wartość zawodników

bins=(0,10,20,30,40,50,60,70,80,90,100)
plt.hist(fifa.Value,bins=bins,)
plt.xticks(bins)

plt.title('Rozkład wartości zawodników',fontdict={'fontsize':20})

plt.savefig('grafy/Players value',dpi=300)
plt.close()

#plt.show()


