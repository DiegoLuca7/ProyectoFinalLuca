from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import login_view, register, update_user, update_user_profile

urlpatterns = [
    path('login/', login_view, name= "login"),
    path('logout/', LogoutView.as_view(template_name = "users/logout.html")),
    path('singup/', register),
    path('update/', update_user, name= "update_user"),
    path('update/profile/', update_user_profile , name= "update_user_profile"),




]