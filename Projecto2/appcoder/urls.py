from django.urls import path
from appcoder.views import create_products, list_products, list_categories, create_category
from django.urls import path

urlpatterns = [
    path("create-products/", create_products),
    path("list-products/", list_products),
    path("create-category/<str:name>/", create_category),
    path("list-categories/", list_categories),
]






