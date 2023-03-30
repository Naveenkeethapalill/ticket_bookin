from django import forms
from . models import Movie
from . models import Database

from django.contrib.auth.forms import UserChangeForm


class DateInput(forms.DateInput):
    input_type = 'date'

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
        labels = {
            'name':'Enter Name',
            'image':'Select Image',
            'dsic':'Enter Content'
        }
class DatabaseForm(forms.ModelForm):
    class Meta:
        model=Database
        fields='__all__'
        widgets = {
            'c_date': DateInput()
        }
        labels = {
            'c_name':'Select Name',
            'c_count':'Select ITEM',
            'c_date':'Select Date ',
        }

class Movie_Name(forms.ModelForm):
    class Meta:
        model=Movie
        fields='__all__'
        labels ={
            'name':'Select Movie Name',
        }



