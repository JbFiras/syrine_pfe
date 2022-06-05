from django.urls import path,include,re_path
from . import views


app_name="accounts"

urlpatterns = [

    path('login/',views.LoginPage, name="login-page"),
    path('',views.HomePage, name="home-page"),
    path('logout/', views.logoutUser, name="logout"),
    
    

]