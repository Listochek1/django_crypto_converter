from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
import requests
from django.urls import reverse
from converter.forms import MainForm
import logging
# Create your views here.

def index(request):
    form = MainForm()
    if request.method == "POST":
        form = MainForm(data=request.POST)
        quantity = float(request.POST.get('amount'))
        from_coin = request.POST.get('from_curr')
        to_coin = request.POST.get('to_curr')
        output = request.POST.get('output')
        params = {
            'category':'spot',
            'symbol':from_coin+to_coin
            

        }
        response_price = requests.get('https://api.bybit.com/v5/market/tickers',params=params)
        get_price= response_price.json()['result']['list'][0]['lastPrice']
        context['get_price'] = get_price
        form = MainForm(output=output)

        return HttpResponseRedirect('')
    
    else :
        form = MainForm
    context = {
        'coin_list' : ['BTC','USDT','ETH','SOL',"XRP",'TON',"NOT"],
        'form':form
    }
    return render(request, "converter/index.html",context=context)

# def convert():
    
#     coin_list = ['BTCUSDT','ETHUSDT','SOLUSDT',"XRPUSDT",'TONUSDT',"NOTUSDT"]
#     for item in coin_list:
#         params = {'symbol':item}
#         get_info = requests.get('https://api.bybit.com/v5/asset/coin/query-info',params=item)
#         print(get_info.text)

