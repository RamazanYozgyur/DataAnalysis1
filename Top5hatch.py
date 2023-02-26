
import pandas as pd 
import numpy as np
import matplotlib.animation as animation

import matplotlib.pyplot as plt

df=pd.read_csv('Countriespop_Data.csv')
df_copy=df
empty_list=[]
for i in df_copy.columns[0:4]:
    empty_list.append(i)
for i in df_copy.columns[4:]:
    empty_list.append(i[0:4])
df_copy.columns=empty_list
df_copy=df_copy.drop(columns=['Series Name','Series Code','2020'])
df_copy=df_copy.transpose()
df_copy=df_copy.rename(columns=df_copy.iloc[0])
df_copy=df_copy.reset_index().loc[1:,:]
df_copy=df_copy.rename(columns={'index':'Country Code-Year'})
df_copy.reset_index(inplace=True,drop = True)
df_copy=df_copy.dropna(axis='columns')
unwanted=[]
for i in df_copy.columns:
    if '..' in list(df_copy[i]):
        unwanted.append(i)
df_copy=df_copy.drop(columns=unwanted)
df_copy.head()
df_copy1=df_copy.iloc[1:,:]
df_copy1=df_copy1.rename(columns={'Country Code-Year':'Year'})
df_copy1=df_copy1.astype('float')
df_copy1=df_copy1.astype(int)
df_copy1.head()
for i in df_copy1.columns:
    if i =='Year':
        df_copy1[i]=df_copy1[i]
    else:    
        df_copy1[i]=round(df_copy1[i]/1000000,1)
df_copy1=df_copy1[df_copy1 > 10].dropna(axis=1)
c=list(df_copy1.describe().max().nlargest(6).index)
df_copy1=df_copy1[c]
fig,ax=plt.subplots(figsize=(15,7))
def anim(year):

    ax.clear()
    ax.barh(df_copy1.columns[1:],df_copy1[df_copy1.Year==year].iloc[0,1:],color='black')
    ax.set_xticks([0,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500])
    ax.set_xticklabels(['0','100 M','200 M','300 M','400 M','500 M','600 M','700 M','800 M','900 M','1000 M','1100 M','1200 M','1300 M','1400 M','1500 M'])
    for i, (name, value) in enumerate(zip(df_copy1.columns[1:],df_copy1[df_copy1.Year==year].iloc[0,1:])):
        ax.text( value +2, i,    df_copy[name][0], size=15, weight=500, ha='left', va='top')
    bars = ax.patches
    b=[]
    for bar in bars:
         b.append(bar.get_width())
    b.sort()

    hatch='//'
    for bar in bars:  
        if bar.get_width()==b[-1]:
        
             bar.set_hatch(hatch)
             bar.set_edgecolor('white')    
            
    ax.set_title('Changes in population level for 5 most populated countries',fontsize=23)           
    ax.xaxis.grid(True, which='major')
    ax.yaxis.grid(False, which='major')
    ax.text(0.95, 0.8, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=400) 
    ax.legend(['Most populated country'],fontsize=14)




animator=animation.FuncAnimation(fig,anim,frames=range(1960,2020),interval=200)
plt.show()



