from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="store"

urlpatterns = [

    path("",views.homepages,name='home'),
    path("test/",views.home,name="test"),
    path("item/<slug:slug>/",views.product_details,name='prod_details'),
    path("cat/<slug:slug>/",views.list_cats,name='categories'),
   
    #path("loaddata/",views.loadingdata,name="load")
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)