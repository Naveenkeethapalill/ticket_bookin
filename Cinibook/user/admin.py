from django.contrib import admin
from . models import Movie
from . models import Database, Booking

admin.site.register(Movie)
admin.site.register(Database)
admin.site.register(Booking)

