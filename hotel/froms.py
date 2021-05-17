from django import forms

class SearchForm(forms.Form):
    check_in = forms.DateField(required=True, input_formats='%Y-%m-%d')
    check_out = forms.DateField(required=True, input_formats='%Y-%m-%d')
    capacity = forms.IntegerField(required=True)