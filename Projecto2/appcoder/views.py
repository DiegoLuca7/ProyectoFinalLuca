from django.shortcuts import render
from django.http import HttpResponse

from appcoder.models import Products, Category

from appcoder.forms import ProductForm

def create_products(request):
    if request.method == "GET":
        context = {
            "form": ProductForm()

        }
        return render(request, "products/create_product.html", context=context)
        

    elif request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            Products.objects.create(
                name = form.cleaned_data["name"],
                talle = form.cleaned_data["talle"],
                price = form.cleaned_data["price"],
                stock = form.cleaned_data["stock"],

            )
            context= {
                "message" : "Producto creado"

            }
            return render(request, "products/create_product.html", context=context)

        else:
            context = {
                "form_errors" : form.errors,
                "form": ProductForm()
            }
            return render(request, "products/create_product.html", context=context)
        

    
def list_products(request):
    if "Search" in request.GET:
        products = Products.objects.filter(name__contains=request.GET["Search"])
        

    else:
        products = Products.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/list_products.html", context=context)

def create_category(request, name):
    Category.objects.create(name = name )
    return HttpResponse("Categoria creada")

def list_categories(request):
    all_categories =  Category.objects.all()
    context = {"categories": all_categories
    }
    return render(request, "categories/list_categories.html", context=context)

