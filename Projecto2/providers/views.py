from django.shortcuts import render
from providers.models import Providers
from providers.forms import ProviderForm
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin   


def providers_list(request):
    providers = Providers.objects.filter(is_active = True)
    context = {
        'providers' : providers
    }
    return render (request, 'providers/providers-list.html', context = context)

class ProvidersListView(LoginRequiredMixin, ListView):
    model = Providers
    template_name = 'providers/providers-list.html'

def providers_create(request):
    if request.method == "GET":
        context = {
            "form": ProviderForm()

        }
        return render(request, "providers/provider-create.html", context=context)
        

    elif request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            Providers.objects.create(
                name = form.cleaned_data["name"],
                address = form.cleaned_data["address"],
                phone_number = form.cleaned_data["phone_number"],
                email = form.cleaned_data["email"],
                condition = form.cleaned_data["condition"],

            )
            context= {
                "message" : "Proveedor creado"

            }
        else:
            context = {
                "form_errors" : form.errors,
                "form": ProviderForm()
            }
        return render(request, "providers/provider-create.html", context=context)

class ProvidersCreateView(CreateView):
    model = Providers
    template_name = 'providers/provider-create.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'

def provider_update(request, pk):
    provider = Providers.objects.get(id=pk)

    if request.method == "GET":
        context = {
            "form": ProviderForm(
                initial={
                    'name': provider.name,
                    'address': provider.address,
                    'phone_number': provider.phone_number,
                    'email': provider.email,
                    'condition': provider.condition,
                }
            )
        }
        return render(request, "providers/provider-update.html", context=context)
        

    elif request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
                provider.name = form.cleaned_data["name"]
                provider.address = form.cleaned_data["address"]
                provider.phone_number = form.cleaned_data["phone_number"]
                provider.email = form.cleaned_data["email"]
                provider.condition = form.cleaned_data["condition"]
                provider.save()

                context= {
                "message" : "Proveedor actualizado"

            }
        else:
            context = {
                "form_errors" : form.errors,
                "form": ProviderForm()
            }
        return render(request, "providers/provider-update.html", context=context)
        
class ProviderDeleteView(DeleteView):
    model = Providers
    template_name = 'providers/provider-delete.html'
    success_url = '/providers/providers-list/'