from django.shortcuts import render, redirect
from .models import AdInfo
from .forms import AdInfoForm

def ad_list(request):
    ads = AdInfo.objects.all()
    return render(request, 'ad_info/ad_list.html', {'ads': ads})

def ad_detail(request, pk):
    ad = AdInfo.objects.get(pk=pk)
    return render(request, 'ad_info/ad_detail.html', {'ad': ad})

def ad_create(request):
    if request.method == 'POST':
        form = AdInfoForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save()
            return redirect('ad_detail', pk=ad.pk)
    else:
        form = AdInfoForm()
    return render(request, 'ad_info/ad_create.html', {'form': form})