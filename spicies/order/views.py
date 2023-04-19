from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .Forms import OrderForm
from .models import order ,OrderItem
from basket.basket import Basket
# Create your views here.
from django.http.response import JsonResponse

from store.models import Product
from django.contrib.admin.views.decorators import staff_member_required



def placeorder(request):
    basket = Basket(request)
    
    if request.method=="POST":
        if request.user.is_authenticated:
            user_id = request.user.id
        else:
            user_id=18
        of=OrderForm(request.POST)
       
        if of.is_valid:
             
            order_creator_name=request.POST["fullname"]
            city=request.POST["City"]
            address=request.POST["address"]
            Phone=request.POST["Phone"]
            print(basket.get_total_paid())
            print(basket.get_total_after_discount())
        
            ord=order.objects.create(user_id=user_id,full_name=order_creator_name,address1=address,
                                     address2=address,city=city,
                                     phone=Phone,total_paid=basket.get_total_paid(),
                                    discount=basket.get_total_after_discount())
            order_id = ord.pk
            prods,qts=basket.get_products()
            for p ,q in zip(prods,qts):
                OrderItem.objects.create(order_id=order_id, product=p, price=p.price, quantity=q)
            
            
            
            
            basket.deletall()


            
            return redirect("user:dashboard")   
    else:
        of=OrderForm()


    response = JsonResponse({'success': 'Return something'})

    return render(request,"order/ordercreation.html",{"form":of})




def ordercontent(request,ordid ):

    ord=get_object_or_404(order,id=ordid)
    products=[]
    qts=[]
    items=OrderItem.objects.filter(order_id=ord.id)
    for i in items:
            products.append(Product.objects.get(id=i.product_id))
            qts.append(i.quantity)
    final=zip(products,qts)


    return render(request,"order/orderContent.html",{"final":final})


@staff_member_required
def allorders(request):
    ords=order.objects.all()
    final=dict()
    for ord in ords :
        products=[]
        for i in OrderItem.objects.filter(order_id=ord.id):
            products.append(Product.objects.get(id=i.product_id))
            final[ord]=products

    return render(request,"order/allords.html",{"ords":final})

def test(request):
    return render(request,"order/testorder.html")
