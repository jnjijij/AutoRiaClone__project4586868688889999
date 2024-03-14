from django.shortcuts import render
from models import Auto
from forms import AutoPriceForm

def index(request):
    autos = Auto.objects.all()
    return render(request, 'autoriaclone/index.html', {'autos': autos})

def add_auto(request):
    if request.method == 'POST':
        form = AutoPriceForm(request.POST)
        if form.is_valid():
            auto = Auto(title=form.cleaned_data['title'], price=form.cleaned_data['price'], currency=form.cleaned_data['currency'])
            auto.save()
            return render(request, 'autoriaclone/add_auto_success.html')
    else:
        form = AutoPriceForm()
    return render(request, 'autoriaclone/add_auto.html', {'form': form})

def auto_images(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render(request, 'autoriaclone/auto_images.html', {'auto': auto})