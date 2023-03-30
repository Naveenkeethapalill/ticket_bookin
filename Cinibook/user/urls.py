from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('single/<int:id>/',views.single,name='single'),
    path('now/<int:id>/',views.now,name='now'),
    path('singup/',views.singup,name='singup'),
    path('movies/',views.movies,name='movies'),
    path ('mytickets/',views.mytickets,name='mytickets'),
    path('contact/' ,views.contact,name='contact'),
    path('pdf/',views.pdf,name='pdf'),
]

