from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("dashboard/cancel/<int:booking_id>",views.cancel,name="cancel")
]
