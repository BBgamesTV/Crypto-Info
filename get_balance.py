import requests

def eth_info():
    crypto = "render"
    URL = 'https://api.coingecko.com/api/v3/search?query='+crypto
    # print(URL)
    params = {
        'limit': '1'  # limite la réponse à 3 avions
    }
    try: 
        api_result = requests.get(URL, params)
    except:
        print('API status dead')
    api_response = api_result.json()

    ID = api_response['coins'][0]['id']
    SYMBOL = api_response['coins'][0]['symbol']
    IMG = api_response['coins'][0]['large']
    MARKET_RANK = api_response['coins'][0]['market_cap_rank']

    URL2 = 'https://api.coingecko.com/api/v3/simple/price?ids='+ID+ \
        '&vs_currencies=eur&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true'

    api_result_market = requests.get(URL2, params)
    api_response2 = api_result_market.json()
    if api_response == "error":
        print("CRYPTO ERROR")
        exit

    EUR = api_response2[ID]['eur']
    EUR_24h_CHANGE = api_response2[ID]['eur_24h_change']
    EUR_24h_CHANGE = round(EUR_24h_CHANGE, 4)

    def taux(EUR_24h_CHANGE):
        if EUR_24h_CHANGE < 0:
            EUR_24h_CHANGE = str(EUR_24h_CHANGE)+'🟥'
            return EUR_24h_CHANGE
        elif EUR_24h_CHANGE > 0:
            EUR_24h_CHANGE = "+"+str(EUR_24h_CHANGE)+'🟩'
            return EUR_24h_CHANGE
            
    
    return([ID,SYMBOL,IMG,MARKET_RANK,EUR,taux(EUR_24h_CHANGE)])

def balance_eth(add):
    if (add == ""):
        adress = "0x0c2f551EC57378818255e6BDaD07D80d0591A905"
        adress2 = "0x0E289c0F014385A4734C7c3D72Bc4428bE8bb37b"
        adress = requests.get("https://api.ethplorer.io/getAddressInfo/"+adress+"?apiKey=freekey")
        adress2 = requests.get("https://api.ethplorer.io/getAddressInfo/"+adress2+"?apiKey=freekey")
        json = adress.json()
        json2 = adress2.json()
        balance = json["ETH"]["balance"]
        balance2 = json2["ETH"]["balance"]
        balance = balance+balance2
        return balance
    else:
        adress = requests.get("https://api.ethplorer.io/getAddressInfo/"+add+"?apiKey=freekey")
        json = adress.json()
        balance = json["ETH"]["balance"]
        return balance
    


print(eth_info())
print(balance_eth("0x0c2f551EC57378818255e6BDaD07D80d0591A905"))