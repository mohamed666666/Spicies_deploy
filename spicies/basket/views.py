from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .basket import Basket
from store.models import Product
# Create your views here.


def basket_content(request ):
    basket = Basket(request)
    prods,qs, =basket.get_products()
    prices=basket.get_total_paid()
    out=zip(prods,qs)

    context={"out":out,"total":prices,"subtotal":prices}



    return  render(request ,"basket/basket_content.html",context)



def basketadd(request):

    basket = Basket(request)

    if request.POST.get('action')=='post':
        p_id=int(request.POST.get("productid"))
        qty=int(request.POST.get("productqty"))
        prod=get_object_or_404(Product,id=p_id)
        
        
        if str(prod.id) in basket.basket:
                
                qty+=int(basket.basket[str(prod.id)]["quantaty"])
                
                #print(str(prod.id)["quantaty"])
                basket.update(prod.id,qty)
        else:
            basket.add(prod,qty)
       
        bas_count=basket.__len__()
        response=JsonResponse({"qty":bas_count})
    return response



def addfromhome(request):
    basket=Basket(request)

    if request.POST.get('action')=='post':
        p_id=int(request.POST.get("productid"))
        
        prod=get_object_or_404(Product,id=p_id)
        qt=1
        
        if str(prod.id) in basket.basket:
                
                qt+=int(basket.basket[str(prod.id)]["quantaty"])
                
                #print(str(prod.id)["quantaty"])
                basket.update(prod.id,qt)
        else:
            basket.add(prod,qt)

        
        bas_count=basket.__len__()
        response=JsonResponse({"qty":bas_count})


    return response

def basketdelete(request):
    basket = Basket(request)

    if request.POST.get('action') == 'post':
        p_id = int(request.POST.get("productid"))

        basket.delete(p_id)
        prices=basket.get_total_paid()
        bas_count = basket.__len__()
        response = JsonResponse({"qty": bas_count,"subtotal":prices})
    return response







def basket_update(request):
    basket = Basket(request)
    prices = basket.get_total_paid()

    if request.POST.get('action') == 'post':
        p_id = int(request.POST.get("productid"))
        product_qty=int(request.POST.get("productqty"))
        basket.update(p_id,product_qty)

        bas_count = basket.__len__()
        response = JsonResponse({"qty": bas_count,"subtotal":prices})
    return response