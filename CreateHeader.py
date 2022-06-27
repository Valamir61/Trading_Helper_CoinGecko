# -*- coding: utf-8 -*-
import json
import requests
#Liste des coins à tracer
import ConstantValues

coins = ConstantValues.coins;
nameHeaderFile=ConstantValues.nameHeaderFile;
file=open(nameHeaderFile,'w')
file.write("date;")

for coin in coins:
    res = requests.get("https://api.coingecko.com/api/v3/coins/"+coin, headers={'accept': 'application/json'})
    data = json.loads(res.text)
    currentCoinName=str(coin)
    file.write(currentCoinName)
    file.write(";")
    # print("Coin taken for", nameHeaderFile, coin)
file.close()