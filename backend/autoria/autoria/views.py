from django.shortcuts import render

from .forms import AutoForm


def create_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'autos/success.html')
    else:
        form = AutoForm()
    return render(request, 'autos/create_auto.html', {'form': form})