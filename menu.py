# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 19:09:02 2022

@author: Admin
"""
import ConstantValues
import CreateHeader
import appendValues
import plottingFromFile



def menu():

    print('Menu\n',
          '---HEADER INFORMATIONS---\n');
    print("COINS TAKEN");
    for coin in ConstantValues.coins:
        print("__",coin)
    print('-------------------------\n',
          '0. Quit\n',
          '1. Print current values\n',
          '2. Append current values\n',
          '3. Plot all values\n',
          '4. Plot all percentages\n',
          '-------------------------\n')
    choix=5
    while (not(choix==0)):
        choix = int(input(' '))
        while (choix==' '):
            choix = int(input(' '))
        if choix == 1:
            appendValues.Access(False);
        elif choix == 2:
            appendValues.Access(True);
        elif choix == 3:
           plottingFromFile.PlottingAll("Values");
        elif choix == 4:
            plottingFromFile.PlottingAll("Percentages");
        elif choix ==0:
            print('Out\n')
        else:
            print('Invalid command\n')
    return True;
menu()