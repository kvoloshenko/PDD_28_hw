from django import forms
from blogapp.models import Hh_Response, Hh_Request

class Hh_Search_Form(forms.Form):
    hh_query = forms.CharField(label='строка поиска',
                               widget=forms.TextInput(attrs={'placeholder': 'Ключевые слова',
                                                             'class': 'form-control'}))

    hh_request = Hh_Request()
    options_list = hh_request.get_options_list()
    hh_option = forms.CharField(label='Где искать?',
                                widget=forms.Select(choices=options_list,
                                attrs={'class': 'btn btn-secondary dropdown-toggle'}))

