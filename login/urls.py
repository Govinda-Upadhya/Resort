from django.urls import path 
from . import views
from home.views import home
urlpatterns = [
    path("login",views.loginn,name="login"),
    
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout")
]
