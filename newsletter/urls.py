from django.urls import path
from .views import SubscribeView

app_name = "newsletter"
urlpatterns = [ path("newsletter/inscrever/", SubscribeView.as_view(), name="subscribe") ]
