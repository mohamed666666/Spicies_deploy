from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name="basket"


urlpatterns = [

    path("",views.basket_content,name='basket_content'),
    path("adding/",views.basketadd,name='basket_add'),
    path("delete/",views.basketdelete,name='basket_delete'),
    path("update/", views.basket_update, name='basket_update'),
    path("addingone/", views.addfromhome, name='adding')

]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)