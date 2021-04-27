from django import forms
from home.models import Movie  

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name','image','ticket_price','description') 

        widgets = {
            'movie_name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','style':'height:100px','overflow':'auto'}),
            'ticket_price': forms.TextInput(attrs={'class':'form-control'}),
        }