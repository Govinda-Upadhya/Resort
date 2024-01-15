from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from datetime import datetime
from django.db.models import Q
from login.views import loginn 
from login.models import Userprofile
from django.utils import timezone
# Create your views here.
def booking(request):
    if request.method == 'POST':
        start_day = request.POST.get('start_date')
        end_day = request.POST.get('end_date')
        request.session['start_date']=start_day
        request.session['end_date']=end_day
        # Parse start date
        start_date = datetime.strptime(start_day, '%Y-%m-%d')
        
        available_rooms = Rooms.objects.exclude(
            id__in=Booking.objects.filter(
                Q(start_day__lte=start_day, end_day__gte=start_day) |
                Q(start_day__lte=end_day, end_day__gte=end_day) |
                Q(start_day__gte=start_date, end_day__lte=end_day)
            ).values_list('room_no', flat=True)
        )

        
        
        return render(request, "booking/booking.html", {
            "available_rooms": available_rooms
        })

    return render(request, "booking/booking.html", {
        "available_rooms": None,
    })
def details(request,room_no):
    room=Rooms.objects.get(room_no=room_no)
    
    return render(request,"booking/details.html",{
        'room':room
    })
def book_now(request,room_no):
    room=Rooms.objects.get(room_no=room_no)
    if request.method=="POST":
        user=request.user
        user_id=user.id 
        start_date = request.session.get('start_date')
        end_date=request.session.get('end_date')
        amount=room.price
        booked_on=timezone.now()
        
        booking=Booking.objects.create(room_no=room,user_id=user,start_day=start_date,end_day=end_date,amount=amount,booked_on=booked_on)
        booking.save()
        return redirect('booking')
    return render(request,'booking/book_now.html',{
        'room':room
    })