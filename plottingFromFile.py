# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 00:11:07 2022

@author: Admin
"""


import pandas as pd
import plotly.express as px
import plotly.io as pio
import ConstantValues
from functions import *









def displayValues(nameFile,coins):
    file=open(nameFile,'r');
    coinDatasPercentage=pd.read_csv(nameAssemblyFilePercentageCSV,delimiter=";")
    df=pd.DataFrame(coinDatasPercentage,columns=coinsNameList)
    lastDate=df['date'][len(df['date'])-1];
    print("DATE :",lastDate);
    for coinToRecap in coins:
        print("Price of ",
              coinToRecap,
              ":",
              df[coinToRecap][len(df['date'])-1])
    return("----------------------------------------");

def PlottingAll(dataToPlot):
    pio.renderers.default='browser'
    
    dataRef=ConstantValues.dateRef;
    nameHeaderFile=ConstantValues.nameHeaderFile;
    nameFile=ConstantValues.nameFile;
    nameFilePercentage=ConstantValues.nameFilePercentage;
    nameAssemblyFileCSV=ConstantValues.nameAssemblyFileCSV;
    nameAssemblyFilePercentageCSV=ConstantValues.nameAssemblyFilePercentageCSV;
    coins=ConstantValues.coins;
    
    concatFiles(nameHeaderFile,nameFile,nameAssemblyFileCSV);
    concatFiles(nameHeaderFile,nameFilePercentage,nameAssemblyFilePercentageCSV);
    coinsNameList=extractHeader(nameHeaderFile);
    
    if (dataToPlot=="Values"):
        coinDatas=pd.read_csv(nameAssemblyFileCSV,delimiter=";");
        df=pd.DataFrame(coinDatas,columns=coinsNameList);
        fig = px.line(df, x = 'date', y = coins,
                      labels={'value': "Coins",
                              'variable':"Coin plotting"},
                      title="Coins evolution ")

    elif(dataToPlot=="Percentages"):
        coinDatasPercentage=pd.read_csv(nameAssemblyFilePercentageCSV,delimiter=";")
        df=pd.DataFrame(coinDatasPercentage,columns=coinsNameList)
        fig = px.line(df, x = 'date', y = coins,
                      labels={'value': "Coins evolution since"+dataRef,
                              'variable':"Coin plotting"},
                      title="Coins evolution with ref :"+dataRef)
    #Font sizes
    fig.update_layout(yaxis_titlefont_size=20)
    fig.update_layout(xaxis_titlefont_size=20)
    fig.update_layout(title_font_size=40)
    fig.update_layout(legend_font_size=20)

    for coinToAnnotate in coins:    
        fig.add_annotation(x=df['date'][len(df['date'])-1], y=df[coinToAnnotate][len(df['date'])-1],
                    text=str(df[coinToAnnotate][len(df['date'])-1]),
                    showarrow=False,
                    yshift=8) 
    
    # etiquettes de data
    #fig.update_traces(textposition='top center')
    #fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.show()

