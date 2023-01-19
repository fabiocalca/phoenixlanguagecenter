from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='Nome')
    last_name = forms.CharField(max_length=50, required=True, label='Sobrenome')
    email = forms.EmailField(max_length=150, required=True, label='E-mail')
    phone = forms.CharField(max_length=20, label='Telefone (Com DDD)')
    message = forms.CharField(widget=forms.Textarea, max_length=2000, required=True, label='Mensagem')