from django.shortcuts import render , get_object_or_404
from store.models import Category,Product

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from basket.basket import Basket



# Create your views here.
# 
def homepages(request):
    product_list= Product.products.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(product_list, 28)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'store/home.html', { 'products': products })






def home(request):
    context = {"products": Product.products.all()}
    return  render(request,'store/test.html',context)







def product_details(request,slug ):
    product=get_object_or_404(Product,slug=slug,instock=True)
    cat=product.category
    prods=Product.objects.filter(category=cat)[:15]
    
    return render(request,"store/product.html",{"product":product ,"prods":prods})




def list_cats(request,slug):
    categories=get_object_or_404(Category,slug=slug)
    prods=Product.objects.filter(category=categories)
    return render(request,"store/categories.html",{"cat":categories,"prods":prods})




def categories(request):
     return  {"categories":Category.objects.all()}
