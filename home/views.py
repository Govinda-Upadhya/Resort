from django.shortcuts import render,redirect
from django.http import HttpResponse
from booking.models import *
from login.models import *
from django.contrib.auth.models import AnonymousUser

# Create your views here.
def home(request):
    user=request.user
    if request.user.is_authenticated:
        return render(request,"Home/home.html",{
            'user':user
        })
    else:
        return render(request,"Home/home.html",{
            'user':None
        })


def dashboard(request):
    user=request.user
    
    if request.user.is_authenticated:
        userprofile=Userprofile.objects.get(username=user.username)
        rooms_booked=Booking.objects.filter(user_id=userprofile.id)
        print(user)
        return render(request,'home/dashboard.html',{
            'user':userprofile,
            'bookings':rooms_booked
        })
    return render(request,'home/dashboard.html',{
        'user':None,
        'bookings':None
    })
def cancel(request,booking_id):
    booking=Booking.objects.get(id=booking_id)
    
    room=booking.room_no
    if request.method=="POST":
        bookings=Booking.objects.get(id=booking_id)
        bookings.delete()
        return redirect('dashboard')
    return render(request,"booking/cancel.html",{
        'room':room,
        'booking_no':booking_id
    })
