from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name="order"


urlpatterns = [
  path('placeorder/',views.placeorder , name='placeorder'),
  path("order/<int:ordid>/",views.ordercontent,name='ordercontent'),
  path("all_for_admin/",views.allorders ),
  
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)