from django.urls import path
from . import views
urlpatterns = [
    path("",views.booking,name="booking"),
    path("<int:room_no>/book_now",views.book_now,name="book_now"),
    path("details/<int:room_no>",views.details,name="details"),
    
]
