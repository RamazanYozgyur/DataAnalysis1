
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
df_copy2.index[0]
a=list(df_copy2.iloc[:,1:].sort_values(by=df_copy2.index[0],ascending=False,axis=1).columns)
b=a.index('Poland')
c=[]
for i in range(b-2,b+3):
   c.append(a[i]) 
df_copy2[c]
c.insert(0,'Year')
df_copy1=df_copy1[c]
df_copy1[df_copy1['Year']==1975]
fig,ax=plt.subplots(figsize=(15,6))
def anim(year):
    df_copy3=df_copy1[df_copy1['Year']==year]
    ax.clear()
    ax.barh(df_copy3.columns[1:],df_copy3.iloc[0,1:],color=['dimgray'])
    ax.set_xticks(list(np.arange(0,130,10)))
    ax.set_xticklabels(['0','10 mln','20 mln','30 mln','40 mln','50 mln','60 mln','70 mln','80 mln','90 mln','100 mln','110 mln','120 mln'],fontsize=15)
    
    ax.set_xlabel('Population [millions]',fontsize=18)
    ax.set_title('Evolution of countries population that were \n most similar to Poland at 1975',fontsize=23)
    bars = ax.patches
    b=[]
    for bar in bars:
         b.append(bar.get_width())
    b.sort()

    hatch='*'
    for bar in bars:  
        if bar.get_width()==b[-1]:
        
             bar.set_hatch(hatch)
             bar.set_edgecolor('white')
    for i, (name, value) in enumerate(zip(df_copy3.columns[1:],df_copy3.iloc[0,1:])):
        ax.text( value+ 5.5, i+0.15, str(value) + ' MLN',size=14, weight=800, ha='center', va='bottom')
        ax.text( value+ 2.5, i,    df_copy[name][0],           size=15, weight=600, ha='center', va='top')
    ax.text(1, 0.1, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=500)    
animator=animation.FuncAnimation(fig,anim,frames=range(1960,2020),interval=300)
plt.show()
