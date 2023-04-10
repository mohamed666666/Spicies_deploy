from django.contrib import admin

# Register your models here.
from .models import order,OrderItem



from django.contrib.admin import AdminSite
from django.http import HttpResponse

class MyAdminSite(AdminSite):

     def get_urls(self):
         from django.urls import path
         urls = super().get_urls()
         urls += [
             path('my_view/', self.admin_view(self.my_view))
         ]
         return urls

     def my_view(self, request):
         return HttpResponse("Hello!")

admin_site = MyAdminSite()


admin.site.register(order)
#admin.site.register(OrderItem)
