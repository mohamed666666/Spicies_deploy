


from .froms import RegisterationForm,UserEditForm
from .models import UserBase
from basket.basket import Basket
from store.models import Product
from .token import account_activation_token
from order.models import OrderItem,order
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# Create your views here...


def register(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method=="POST":
        rf = RegisterationForm(request.POST)
        if rf.is_valid():
            user=rf.save(commit=False)
            user.email=rf.cleaned_data["email"]
            user.set_password(rf.cleaned_data["password"])
            user.is_active=True
            user.save()
            current_site=get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('user/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            #user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully ')
    else:
        registerForm = RegisterationForm()
    return render(request, 'user/Register.html', {'form': registerForm})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('user:dashboard')
    else:
        return render(request, 'user/activation_invalid.html')



@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)

        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                  'user/edit_details.html', {'user_form': user_form})


@login_required
def dashbord(request):
    uid=request.user.id
    basket=Basket(request)
    orders=order.objects.filter(user_id=uid,billing_status=False)
    

    final=dict()
    
    #retriving products id 

    for ord in orders :
        products=[]
        for i in OrderItem.objects.filter(order_id=ord.id):
            products.append(Product.objects.get(id=i.product_id))
            final[ord]=products
        

    
        
    #{"ords":orders,"prods":products}
    return render(request,"user/dashboard.html",{"ords":final})