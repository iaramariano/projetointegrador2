from django.shortcuts import render
from django.views.generic import FormView
from django.contrib import messages
from django.shortcuts import redirect
from .forms import SubscribeForm
from .services import subscribe_email, MailerLiteError

class SubscribeView(FormView):
    template_name = "newsletter/subscribe.html"
    form_class = SubscribeForm
    success_url = "/"

    def form_valid(self, form):
        name  = form.cleaned_data.get("name")
        email = form.cleaned_data["email"]
        ip    = self.request.META.get("REMOTE_ADDR")
        try:
            subscribe_email(email=email, name=name, ip=ip)
        except MailerLiteError as e:
            messages.error(self.request, "Não conseguimos concluir sua inscrição. Tente novamente.")
            return redirect(self.request.path)
        messages.success(self.request, "Inscrição confirmada! Verifique seu e-mail para confirmar o cadastro.")
        return super().form_valid(form)
