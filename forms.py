from django import forms


class GameForm(forms.Form):
    the_letters = forms.CharField(label='Game Letters', max_length=7, min_length=7)
