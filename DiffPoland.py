

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
df_copy2=df_copy1[df_copy1['Year']==1975]
a=list(df_copy2.iloc[:,1:].sort_values(by=df_copy2.index[0],ascending=False,axis=1).columns)
b=a.index('Poland')
c=[]
for i in range(b-2,b+3):
    c.append(a[i]) 
df_copy2[c]
c.insert(0,'Year')
df_copy1=df_copy1[c]
fig,ax=plt.subplots(figsize=(14,7))
df_copy3={'Year1':df_copy1['Year'],'Year2':df_copy1['Year'],'Year3':df_copy1['Year'],
          'Year4':df_copy1['Year'],'Year5':df_copy1['Year']}
df_copy4=pd.DataFrame(data=df_copy3)
df_copy4
def anim(year):
    ax.clear()
    
    lst=[]
    for i in df_copy4[df_copy4.Year1<=year].index-1:
        lst.append(list(df_copy4.iloc[i,:]))
    color=['orange', 'blueviolet', 'peru', 'royalblue', 'grey']
    colors=[color for i in range(1960,year+1)]
    c=[]
    for i in colors:
        c.extend(i)
    ax.set_xlim(1955, 2025)
    ax.scatter(lst,df_copy1[df_copy1.Year<=year].iloc[0:,1:],c=c)
    ax.set_xticks([1955,1960,1970,1980,1990,2000,2010,2020,2025])
    ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',''],fontsize=15)
    ax.set_yticks(list(np.arange(0,130,10)))
    ax.set_yticklabels(['0','10 mln','20 mln','30 mln','40 mln','50 mln','60 mln','70 mln','80 mln','90 mln','100 mln','110 mln','120 mln'],fontsize=15)
    ax.xaxis.grid(True, which='major')
    ax.yaxis.grid(True, which='major')
    ax.set_ylabel('Population [millions]',fontsize=18)
    ax.set_title('Evolution of countries population that were \n most similar to Poland at 1975',fontsize=23)
    for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            if code=='POL' or code=='IRN':
                ax.text( year, value, code,  size=15, weight=100, ha='left', va='bottom')
            elif code=='ESP' or code=='ETH':
                ax.text( year, value+ 1.5, code,  size=15, weight=100, ha='left', va='top')
            else:  
                ax.text( year, value+ 2.5, code,  size=15, weight=100, ha='center', va='top')
    ax.text(0.8, 0.9, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=500)    




animator=animation.FuncAnimation(fig,anim,frames=range(1960,2020),interval=300)
plt.show()





