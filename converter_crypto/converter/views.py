from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
import requests
from django.urls import reverse
from converter.forms import MainForm
# Create your views here.

def index(request):
    form = MainForm()
    response_crypto = requests.get(f'https://api.coinbase.com/v2/assets/search')
    # tickers_cur = response_cur.json()['data']
    tickers_crypto = response_crypto.json()['data']
    tickers_list = []
    # for ticker in tickers_cur:
    #     coin_list.append(ticker['id'])
    for ticker in tickers_crypto:
        tickers_list.append(ticker['symbol'])


    if request.method == "POST":
        form = MainForm(data=request.POST)
        quantity = float(request.POST.get('amount'))
        from_coin = str(request.POST.get('from_curr'))
        to_coin = str(request.POST.get('to_curr'))


        response_price = requests.get(f'https://api.coinbase.com/v2/prices/{from_coin}-{to_coin}/spot') #нахождение цены
        response_error = response_price.json()

        if 'error' in response_error.keys():
            context = {
                'coin_list' : tickers_list,
                'error':'Не удалось получить курс, повторите попытку позже',
                'form':form,
                }    
            return render(request, "converter/index.html",context=context)


        get_price= response_price.json()['data']['amount']

        context = {
        'from_coin':from_coin,
        'to_coin':to_coin,
        'coin_list' : tickers_list,
        'amount': quantity,
        'form':form,
        'get_price':round((float(get_price) * quantity),2) #Округление до 2 цифр после запятой
            }
        print(context['get_price'])

        
    
    else :
        form = MainForm
        context = {
        'coin_list' : tickers_list,
        'form':form,
        }
    
    return render(request, "converter/index.html",context=context)

# def convert():
    
#     coin_list = ['BTCUSDT','ETHUSDT','SOLUSDT',"XRPUSDT",'TONUSDT',"NOTUSDT"]
#     for item in coin_list:
#         params = {'symbol':item}
#         get_info = requests.get('https://api.bybit.com/v5/asset/coin/query-info',params=item)
#         print(get_info.text)

