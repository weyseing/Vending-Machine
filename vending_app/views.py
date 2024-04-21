from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden

item_prices = {
        "Cola": 1,
        "Pepsi": 2,
        "Sprite": 3,
    }

def main(request):
    return render(request, 'vending_app/main.html') 

def checkout(request):
    item = request.POST.get('item')

    # block direct access
    response = block_direct_access(request)
    if response is not None:
        return response 
    
    # check item price
    price = item_prices.get(item, "NOT FOUND")
    if (price == "NOT FOUND"):
        return HttpResponse("<p style='color:red;font-weight:bold;'>ERROR:</p> Item price not found.<br>Plesae contact vendor via 012-456 7890.")

    # checkout page
    context = {
        'item': item,
        'price': price,
    }
    return render(request, 'vending_app/checkout_page.html', context) 

def pay(request):
    item = request.POST.get('item')
    payment_method = request.POST.get('payment_method')
    cash_amt = request.POST.get('cash_amt')

    cash_balance = 0
    
    # block direct access
    response = block_direct_access(request)
    if response is not None:
        return response 

    # check item price
    price = item_prices.get(item, "NOT FOUND")
    if (price == "NOT FOUND"):
        return HttpResponse("<p style='color:red;font-weight:bold;'>Error:</p> Item price not found.<br>Plesae contact vendor via 012-456 7890.")

    # cash payment
    if (payment_method == "cash"):
        if (cash_amt == "" or int(cash_amt) <= 0):
            return HttpResponse("<p style='color:red;font-weight:bold;'>Error:</p> Cash amount must be greater than 0. Please insert cash.")
        if (int(cash_amt) < price):
            return HttpResponse(f"<p style='color:red;font-weight:bold;'>Error:</p> The cash amount is insufficient. Please collect the necessary cash notes from below. <Br>Item price: ${price} <Br>Cash amount: ${cash_amt}.")

        cash_balance = int(cash_amt) - price
    
    response = f"<p style='color:green;font-weight:bold;'>Payment Success:</p>Thank you for purchasing. Please collect your item & balance ${cash_balance} from below."
    return HttpResponse(response)
    
def block_direct_access(request):
    if (request.POST.get('csrfmiddlewaretoken') is None):
        return HttpResponseForbidden("<p style='color:red;font-weight:bold;'>403 Forbidden:</p> Direct access not allowed.")

        