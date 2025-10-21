from django import forms

class SubscribeForm(forms.Form):
    name  = forms.CharField(label="Seu nome", max_length=60, required=False)
    email = forms.EmailField(label="Seu e-mail")
    consent = forms.BooleanField(
        label="Quero receber atualizações e concordo com a política de privacidade",
        required=True
    )
