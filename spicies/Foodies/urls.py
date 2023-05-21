
from django.contrib import admin

from django.urls import path,include

from django.conf.urls.i18n import i18n_patterns

urlpatterns=[path('i18n/',include('django.conf.urls.i18n')),]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    
    path("",include('store.urls',namespace="store")),
    path("basket/",include('basket.urls', namespace='basket')),
    path("user/",include('user.urls', namespace='user')),
    path("order/",include("order.urls",namespace="order"))
)
