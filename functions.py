# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 01:07:48 2022

@author: Admin
"""

def extractHeader(nameHeaderFile):
    # Liste des monnaies à tracer
    fileHeader=open(nameHeaderFile,'r');
    sCoinsHeader=fileHeader.readline();
    # Initialisation de coinsFullTable qui contiendra tous les coins et 
    # sCoinFromHeader qui contiendra un coin après l'autre
    coinsFullTable=[];
    sCoinFromHeader="";
    for i in range(len(sCoinsHeader)):
        # Caractere trouvé i
        chari=sCoinsHeader[i];
        # Test si le char est un semicolon
        if(chari==";"):
            # Ajout du nom de la monnaie si c'est le cas.
            # le header ne devra donc pas commencer par un semicolon.
            coinsFullTable.append(sCoinFromHeader);
            i+=1; 
            sCoinFromHeader="";
        else:
            sCoinFromHeader+=chari;
    fileHeader.close()
    return coinsFullTable;


def concatFiles(nameHeaderFile,nameFile,nameAssemblyFileCSV):
    fileAurevoir=open(nameAssemblyFileCSV,"w");
    fileAurevoir.close()
    data = data2 = "" 
    with open(nameHeaderFile) as fp1: 
        data = fp1.read() 
    with open(nameFile) as fp2: 
        data2 = fp2.read() 
    data += "\n"
    data += data2 
    with open (nameAssemblyFileCSV, 'w') as fp3: 
        fp3.write(data) 
    fp1.close()
    fp2.close()
    fp3.close()
    return 0;
