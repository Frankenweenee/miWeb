from django import forms


class Formulario(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}), max_length= 100, required=True)
    email= forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),max_length= 50, required=True)
    subject= forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),max_length= 100, required=True)
    message= forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),max_length= 500, required=True)



