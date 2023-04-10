from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .froms import ( UserLoginForm)
app_name="user"

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='user/login.html',form_class=UserLoginForm)
        , name='login'),
    path("logout/",auth_views.LogoutView.as_view(next_page="/user/login/") ,name="logout"),
    path("register/",views.register,name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    path('dashboard', views.dashbord, name='dashboard'),
    path('profile/edit/', views.edit_details, name='edit_details'),


]