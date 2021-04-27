from django import forms
from home.models import Movie, Show  

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name','image','ticket_price','description') 

        widgets = {
            'movie_name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','style':'height:100px','overflow':'auto'}),
            'ticket_price': forms.TextInput(attrs={'class':'form-control'}),
        }
class DateInput(forms.DateInput):
    input_type = 'date'

class ShowForm(forms.ModelForm):
    movie: forms.ModelChoiceField(queryset=Movie.objects.all())
    data: forms.DateField()
    class Meta:
        model = Show
        fields = ('movie','date','screen','timing') 
        SCREEN = (('A','A'),('B','B'),('C','C'),('D','D'))
        TIMING = (('10AM','10AM'),('1PM','1PM'),('4PM','4PM'),('7PM','7PM'))
        screen: forms.ChoiceField(choices = SCREEN)
        timing: forms.ChoiceField(choices = TIMING)
        widgets = {
            'date': DateInput(),
            'screen': forms.Select(attrs={'class':'custom-select'}),
            'timing': forms.Select(attrs={'class':'custom-select'}),
            'movie': forms.Select(attrs={'class':'custom-select'}),
        }