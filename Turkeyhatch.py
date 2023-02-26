




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
df_copy2=df_copy1[df_copy1['Year']==2000]
a=list(df_copy2.iloc[:,1:].sort_values(by=df_copy2.index[0],ascending=False,axis=1).columns)
b=a.index('Turkey')
c=[]
for i in range(b-2,b+3):
   c.append(a[i]) 
df_copy2[c]
c.insert(0,'Year')
df_copy1=df_copy1[c]
fig,ax=plt.subplots(figsize=(15,6))
def anim(year):
    df_copy3=df_copy1[df_copy1['Year']==year]
    ax.clear()
    ax.barh(df_copy3.columns[1:],df_copy3.iloc[0,1:],color=['dimgrey'])
    ax.set_xticks([ 0, 5,  25,  45,  65,  85, 105, 125,130])
    ax.set_xticklabels(['','5 MLN','25 MLN','45 MLN','65 MLN','85 MLN','105 MLN','125 MLN',''],fontsize=15)
    ax.set_xlabel('Population [millions]',fontsize=18)

    ax.set_yticks([0,1,2,3,4])
    ax.set_yticklabels(df_copy3.columns[1:],fontsize=15,rotation=45)
    ax.set_title('Evolution of countries population between 1960-2020 that were \n most similar to Turkey at 2000',fontsize=23)
    bars = ax.patches
     
    b=[]
    for bar in bars:
         b.append(bar.get_width())
    b.sort()

    hatch=['ox','o']
    for bar in bars:  
        if bar.get_width()==b[-1]:
        
             bar.set_hatch(hatch[0])
             bar.set_edgecolor('white')
        if bar.get_width()==b[0]:
        
             bar.set_hatch(hatch[1])
             bar.set_edgecolor('white')       
    for i, (name, value) in enumerate(zip(df_copy3.columns[1:],df_copy3.iloc[0,1:])):
        ax.text(  value+ 4  ,i ,    df_copy[name][0],           size=15, weight=600, ha='center', va='top')
    ax.text(1, 0.8, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=500)    
animator=animation.FuncAnimation(fig,anim,frames=range(1960,2020),interval=300)
plt.show()





