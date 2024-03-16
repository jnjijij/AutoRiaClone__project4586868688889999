from django.shortcuts import render, get_object_or_404, redirect

from .models import Moderation
from .forms import ModerationForm
from ...autoria.Ad_info.info import AdInfo


def moderation_list(request):
    moderations = Moderation.objects.all()
    return render(request, 'moderation/moderation_list.html', {'moderations': moderations})

def moderation_detail(request, pk):
    moderation = get_object_or_404(Moderation, pk=pk)
    return render(request, 'moderation/moderation_detail.html', {'moderation': moderation})

def moderation_create(request, ad_pk):
    ad = get_object_or_404(AdInfo, pk=ad_pk)
    if request.method == 'POST':
        form = ModerationForm(request.POST)
        if form.is_valid():
            moderation = form.save(commit=False)
            moderation.ad = ad
            moderation.save()
            return redirect('moderation_detail', pk=moderation.pk)
    else:
        form = ModerationForm()
    return render(request, 'moderation/moderation_create.html', {'form': form, 'ad': ad})