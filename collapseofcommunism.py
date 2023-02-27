
import pandas as pd 
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib.pyplot as plt
import time
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

df_copy1=df_copy1[['Year','Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan']]
fig,ax=plt.subplots(figsize=(13,7))




def anim(year):

    ax.clear()
    if year==1960:
        ax.plot([],[])
        ax.set_xlim(1955,2025)
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
    elif year >= 1961 and year <=1987:
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom') 


    elif year >= 1988 and year <= 1990:
      
      
        ax.axvspan(1988,1992,color='gold' )
        year=1988
        ax.text(1992,27 , 'COLLAPSE \n OF  \n COMMUNİSM', size=7, ha='right', weight=50, color='black')       
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom') 
    elif year >= 1991 and year <= 1993:
        ax.axvspan(1988,1992,color='gold' )
        year=1989
        ax.text(1992,27 , 'COLLAPSE \n OF  \n COMMUNİSM', size=7, ha='right', weight=50, color='black')       
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom')
    elif year >= 1994 and year <= 1996:
        ax.axvspan(1988,1992,color='gold' )
        year=1989
        ax.text(1992,27 , 'COLLAPSE \n OF  \n COMMUNİSM', size=7, ha='right', weight=50, color='black')       
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom')
    elif year >= 1997 and year <= 1999:
        ax.axvspan(1988,1992,color='gold' )
        year=1990
        ax.text(1992,27 , 'COLLAPSE \n OF  \n COMMUNİSM', size=7, ha='right', weight=50, color='black')       
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom')
    elif year >= 2000 and year <= 2002:
        ax.axvspan(1988,1992,color='gold' )
        year=1991
        ax.text(1992,27 , 'COLLAPSE \n OF  \n COMMUNİSM', size=7, ha='right', weight=50, color='black')       
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom')
    elif year >= 2003 and year <= 2005:
        ax.axvspan(1988,1992,color='gold' )
        year=1992
        ax.text(1992,27 , 'COLLAPSE \n OF  \n COMMUNİSM', size=7, ha='right', weight=50, color='black')       
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')
        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value -.5, code,  size=15, weight=200, ha='left', va='bottom')
    else:
        year=year-13
        ax.plot(df_copy1[df_copy1['Year']<= year]['Year'],df_copy1.iloc[0:df_copy1.index[df_copy1.Year==year][0],1:] )
        ax.set_yticks([ 0,5,10,15,20,25,30])
        ax.set_yticklabels(['','5 mln','10 mln','15 mln','20 mln','25 mln',''],fontsize=15)
        ax.set_xticks([1955,1960, 1970, 1980, 1990, 2000, 2010, 2020, 2025])
        ax.set_xticklabels(['','1960','1970','1980','1990','2000','2010','2020',' '],fontsize=15)
        ax.legend(['Bulgaria','Hungary','Romania','Czech Republic','Kazakhstan'],loc='upper left')

        for  (value,code) in zip(list(df_copy1[df_copy1.Year==year].iloc[0,1:]),list(df_copy[list(df_copy1.columns)[1:]].iloc[0])):
            ax.text( year, value- .5, code,  size=15, weight=200, ha='left', va='bottom')
            
    ax.set_ylabel('Population [millions]',fontsize=18)
    ax.set_xlabel('Year',fontsize=18)
    ax.set_title('Change of populations of some Eastern Europe countries \n around collapse of communism',fontsize=23)           
    ax.xaxis.grid(True, which='major')
    ax.yaxis.grid(True, which='major')
    ax.text(0.35, 0.9, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=400) 
    
animator=animation.FuncAnimation(fig,anim,frames=range(1960,2033),interval=200)
animator.save('collapseofcomunism.gif')







