from django import forms

class SubscribeForm(forms.Form):
    name = forms.CharField(
        label="Seu nome",
        max_length=60,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'})
    )
    email = forms.EmailField(
        label="Seu e-mail",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail'})
    )
    consent = forms.BooleanField(
        label="Autorizo o envio de e-mails com novidades.",
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input me-2'})
    )
