from django.urls import path
from us.views import us
from django.urls import path


urlpatterns = [
    path("us/",us),
    ]