
import pandas as pd 
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

df=pd.read_csv('Countriespop_Data.csv')
Pop_data=pd.read_csv('Popperkm.csv')
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
df_copy1=df_copy.iloc[1:,:]
df_copy1=df_copy1.rename(columns={'Country Code-Year':'Year'})
df_copy1=df_copy1.astype('float')
df_copy1=df_copy1.astype(int)
for i in df_copy1.columns:
    if i =='Year':
        df_copy1[i]=df_copy1[i]
    else:    
        df_copy1[i]=round(df_copy1[i]/1000000,1)
df_copy2=df_copy1[df_copy1['Year']==2000]
a=list(df_copy2.iloc[:,1:].sort_values(by=df_copy2.index[0],ascending=False,axis=1).columns)
b=a.index('Bulgaria')
c=[]
for i in range(b-2,b+3):
    c.append(a[i]) 
df_copy2[c]
c.insert(0,'Year')
df_copy1=df_copy1[c]
fig,ax=plt.subplots(figsize=(14,7))
def anim(year):
    df_copy3=df_copy1[df_copy1['Year']==year]
    ax.clear()
    a=[]
    for i in range(len(df_copy1[df_copy1.Year==year].columns[1:])):
        a.append(year)
    color=['yellow', 'royalblue', 'red', 'green', 'tan']
    s=Pop_data[Pop_data.Year==year][c[1:]]
    ax.set_xlim(1955, 2025)
    ax.scatter(a,df_copy1[df_copy1.Year==year].iloc[0,1:],c=color,s=s)
    ax.set_xticks([1955,1960,1970,1980,1990,2000,2010,2020,2025])
    ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',''],fontsize=15)
    ax.set_yticks([0,2,4,6,8,10,12,14,16,18])
    ax.set_yticklabels(['','2 mln','4 mln','6 mln','8 mln','10 mln','12 mln','14 mln','16 mln',''],fontsize=15)    
    ax.set_ylabel('Population [millions]',fontsize=18)
    ax.set_xlabel('Year',fontsize=18)
    ax.set_title('Evolution of countries population between 1960 and 2019 that were \n most similar to Bulgaria at 2000 where bubble size reflects population density',fontsize=23)
    for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
             ax.text( year, value, code,  size=15, weight=100, ha='right', va='bottom')
    ax.xaxis.grid(True, which='major')
    ax.yaxis.grid(True, which='major')
    ax.text(0.8, 0.9, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=500)    
animator=animation.FuncAnimation(fig,anim,frames=range(1960,2020),interval=300)
plt.show()


