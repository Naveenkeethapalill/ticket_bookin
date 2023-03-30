from django.shortcuts import render, redirect
from . models import Movie,Database, Booking
from . forms import  MovieForm,DatabaseForm,Movie_Name
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import registerFontFamily
import os

def index (request):
    movie = Movie.objects.all()
    return render (request,'index.html',{'movie':movie})

def single (request, id):
    movie = Movie.objects.filter(id=id)
    return render (request,'single.html',)

def now (request, id):
    movie = Movie.objects.filter(id=id)
    if request.method=='POST':
        user=request.POST.get('user')
        name=request.POST.get('name')
        ticket=request.POST.get('ticket')
        date=request.POST.get('date')
        add=Booking(user=user,name=name, ticket=ticket,date=date)
        add.save()
        redirect('index')
    return render (request,'now.html',{'movie':movie})

def contact(request):
    return render (request, 'contact.html')

def singup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm (request.POST)
        if form .is_valid ():
            form.save()
            return redirect ('index')
    return render (request,'singup.html',{'form':form})

def movies(request):
    movie = Movie.objects.all()
    return render (request, 'Movies.html',{'movie':movie})

@login_required
def mytickets(request):
    user = User.objects.get(username=request.user.username)
    data = Booking.objects.filter(user=user)
    return render (request, 'mytickets.html',{'data':data})

@login_required
def pdf(request):
    test=700
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    user = User.objects.get(username=request.user.username)
    data = Booking.objects.filter(user=user)
    # p.setFont("Serif",46)
    p.drawString(20, 800, "Paytm Online Movie Booking")
    # p.setFont()
    p.drawString(20, 750, "User Name :"+str(user))
    for a in data:
        test=test-50
        p.drawString(250, test, "Movie Name :"+a.name)
        p.drawString(10, test, "ticket count :"+str(a.ticket))
        p.drawString(120, test, "Date :"+str(a.date))
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Ticket.pdf')





