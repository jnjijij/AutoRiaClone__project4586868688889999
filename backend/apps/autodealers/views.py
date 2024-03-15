from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from backend.apps.autodealers.models import DealerForm, Dealer, Autosalon, Client, Advertisement


def index():

    pass

def detail(request, dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    return render(request, 'detail.html', {'dealer': dealer})

def create(request):
    if request.method == 'POST':
        form = DealerForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success-url/')
    else:
        form = DealerForm()
    return render(request, 'create.html', {'form': form})

def update(request, dealer_id):
    get_object_or_404(Dealer, pk=dealer_id)
    if request.method == 'POST':
        form = DealerForm()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success-url/')
    else:
        form = DealerForm()
    return render(request, 'update.html', {'form': form})

def delete(dealer_id):
    dealer = get_object_or_404(Dealer, pk=dealer_id)
    dealer.delete()
    return HttpResponseRedirect('/success-url/')  # Replace with the actual URL

def autosalon_list(request):
    autosalons = Autosalon.objects.all()
    return render(request, 'automatons/auto salon_list.html', {'automatons': autosalons})

def autosalon_detail(request, pk):
    autosalon = get_object_or_404(Autosalon, pk=pk)
    return render(request, 'automatons/auto salon_detail.html', {'auto salon': autosalon})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})
def index(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'autosaloons/index.html', {'advertisements': advertisements})

def detail(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    return render(request, 'autosaloons/detail.html', {'advertisement': advertisement})