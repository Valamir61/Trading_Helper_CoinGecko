# -*- coding: utf-8 -*-

"""
appendValues.py

Script à exécuter à chaque prise de valeur souhaiter

Réalise une ligne de valeurs de monnaie à un instant t (au run du programme)
Le header pris en compte, par exemple dataCoinHeader.txt contient les monnaies 
à traiter. Le header est ouvert et doit pas être modifié entre 2 prises de 
mesures. Créer un nouveau fichier Header et entrer un nouveau nom de fichier 
que dataCoin pour d'autres monnaies.

---------------------------Fichier dataCoinHeader.txt--------------------------
FORMAT : [extrait possible de dataCoinHeader.txt]
"bitcoin;ethereum;binancecoin;solana;chiliz;"

possible de le créer avec script CreateHeader.py

----------------------------Fichier dataCoin.txt-------------------------------
FORMAT : [extrait possible de dataCoin.txt]
    2022-06-20 23:23:11.32185820518;1120.02;215.85;34.94;0.092957
    2022-06-20 23:23:38.40056820518;1120.02;215.85;34.97;0.092995
    2022-06-20 23:23:45.21094220518;1120.02;215.85;34.97;0.092995
    2022-06-20 23:30:53.405104;20554;1120.83;215.49;34.99;0.092934
"""

from datetime import datetime
from functions import extractHeader
import json
import requests
import ConstantValues


    
def Access(append):
    dataRef=ConstantValues.dateRef;
    nameFile=ConstantValues.nameFile;
    nameFilePercentage=ConstantValues.nameFilePercentage;
    nameHeaderFile=ConstantValues.nameHeaderFile;
    coinsInitialValues=ConstantValues.coinsInitialValues;
    
    if(append):
        print("Values append...")
    else :
        print("Just checking...")
    #Ouverture fichier
    file=open(nameFile,'a');
    filePercentage=open(nameFilePercentage,'a');
    #Date actuelle au format  YYYY-MM-DD HH:mm:ss.XXXXXX
    dati=datetime.now();
    sDati=str(dati);
    print("DATE :",sDati);
    coins=extractHeader(nameHeaderFile);
    # C'est parti pour écrire un max
    if(append):
        file.write(sDati);
        filePercentage.write(sDati);
    for i in range(1,len(coins)):
        coini=coins[i];
        #Requete sur le site et chargement dans res
        res = requests.get("https://api.coingecko.com/api/v3/coins/"+coini, headers={'accept': 'application/json'});
        data = json.loads(res.text);
        #Valeur de la monnaie
        currentCoinValue=str(data["market_data"]["current_price"]["usd"]);
        currentPercentageValue=round(100*(float(currentCoinValue)-coinsInitialValues[i-1])/coinsInitialValues[i-1],2);
        #Ecriture, séparation des données par des semicolons
        if(append):
            file.write(";");
            file.write(currentCoinValue);
            filePercentage.write(";");
            filePercentage.write(str(currentPercentageValue));
        #petit print pour le con qui regarde la console
        if (currentPercentageValue>0) :
            sign="+";
        else:
            sign="";
        print("Price of", coini, ":", data["market_data"]["current_price"]["usd"],"$","\t , since "+dataRef+":",sign,currentPercentageValue,"%");
    #C'est la fin de la boucle for le python c'est quand même plutot chouette ya pas besoin de {} facile ahah bref genant :)
    if(append):    
        file.write("\n");
        filePercentage.write("\n");
    # fin de ligne et fermeture fichier. Tout est append parcequ'on a ouvert 
    file.close();
    filePercentage.close();
    return True;


