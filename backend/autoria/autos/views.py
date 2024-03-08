from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Auto, Image
from .forms import ImageForm
from django.shortcuts import render
from .forms import AutoImageForm
from .models import Auto, Autosalon, AutoImage, Report
from .forms import AutoForm, AutosalonForm, AutoImageForm, ReportForm
from django.shortcuts import render
from .models import Advertisement

class AutoListView(ListView):
    model = Auto
    template_name = 'autos/auto_list.html'
    context_object_name = 'autos'

class AutoDetailView(DetailView):
    model = Auto
    template_name = 'autos/auto_detail.html'

class AutoCreateView(CreateView):
    model = Auto
    form_class = AutoForm
    template_name = 'autos/auto_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AutoUpdateView(UpdateView):
    model = Auto
    form_class = AutoForm
    template_name = 'autos/auto_form.html'

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = 'autos/auto_confirm_delete.html'
    success_url = reverse_lazy('autos_list')

class AutosalonListView(ListView):
    model = Autosalon
    template_name = 'autos/autosalon_list.html'
    context_object_name = 'autosalons'

class AutosalonDetailView(DetailView):
    model = Autosalon
    template_name = 'autos/autosalon_detail.html'

class AutosalonCreateView(CreateView):
    model = Autosalon
    form_class = AutosalonForm
    template_name = 'autos/autosalon_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AutosalonUpdateView(UpdateView):
    model = Autosalon
    form_class = AutosalonForm
    template_name = 'autos/autosalon_form.html'

class AutosalonDeleteView(DeleteView):
    model = Autosalon
    template_name = 'autos/autosalon_confirm_delete.html'
    success_url = reverse_lazy('autosalons_list')

class AutoImageCreateView(CreateView):
    model = AutoImage
    form_class = AutoImageForm
    template_name = 'autos/auto_image_form.html'

    def form_valid(self, form):
        auto = get_object_or_404(Auto, pk=self.kwargs['auto_id'])
        form.instance.auto = auto
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('auto_images', args=[self.object.auto.pk])

class AutoImageDeleteView(DeleteView):
    model = AutoImage
    template_name = 'autos/auto_image_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('auto_images', args=[self.object.auto.pk])

class AutoImageListView(ListView):
    model = AutoImage
    template_name = 'autos/auto_images.html'
    context_object_name = 'images'

    def get_queryset(self):
        auto = get_object_or_404(Auto, pk=self.kwargs['auto_id'])
        return AutoImage.objects.filter(auto=auto)

class AutoImageUpdateView(UpdateView):
    model = Auto
class AutoImageUpdateView(UpdateView):
    model = AutoImage
    form_class = AutoImageForm
    template_name = 'autos/auto_image_form.html'

    def get_success_url(self):
        return reverse_lazy('auto_images', args=[self.object.auto.pk])

class AutoPriceUpdateView(UpdateView):
    model = Auto
    form_class = AutoPriceForm
    template_name = 'autos/auto_price_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.auto = get_object_or_404(Auto, pk=self.kwargs['auto_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('report_detail', args=[self.object.pk])

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get_queryset(self):
        auto = get_object_or_404(Auto, pk=self.kwargs['auto_id'])
        return Report.objects.filter(auto=auto, user=self.request.user)

class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report_detail.html'

class ReportResolveView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        if request.user != report.user and request.user.is_authenticated and request.user.is_staff:
            report.resolved = True
            report.save()
        return redirect('report_detail', pk=report.pk)

class ReportDismissView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        if request.user != report.user and request.user.is_authenticated and request.user.is_staff:
            report.dismissed = True
            report.save()
        return redirect('report_detail', pk=report.pk)

class ReportDeleteAllView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        auto = get_object_or_404(Auto, pk=kwargs['auto_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        auto = get_object_or_404(Auto, pk=kwargs['auto_id'])
        reports = Report.objects.filter(auto=auto, user=request.user)
        for report in reports:
            report.delete()
        return redirect('report_list', auto_id=auto.pk)
class AutoPriceUpdateView(UpdateView):
    model = Auto
    form_class = AutoPriceForm
    template_name = 'autos/auto_price_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReportCreateView(CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/report_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.auto = get_object_or_404(Auto, pk=self.kwargs['auto_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('report_detail', args=[self.object.pk])

class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get_queryset(self):
        auto = get_object_or_404(Auto, pk=self.kwargs['auto_id'])
        return Report.objects.filter(auto=auto, user=self.request.user)

class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report_detail.html'

class ReportResolveView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        if request.user != report.user and request.user.is_authenticated and request.user.is_staff:
            report.resolved = True
            report.save()
        return redirect('report_detail', pk=report.pk)

class ReportDismissView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])
        if request.user != report.user and request.user.is_authenticated and request.user.is_staff:
            report.dismissed = True
            report.save()
        return redirect('report_detail', pk=report.pk)

class ReportDeleteAllView(View):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        auto = get_object_or_404(Auto, pk=kwargs['auto_id'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        auto = get_object_or_404(Auto, pk=kwargs['auto_id'])
        reports = Report.objects.filter(auto=auto, user=request.user)
        for report in reports:
            report.delete()
        return redirect('report_list', auto_id=auto.pk)

    class AutoDeleteView(View):
        def get(self, request, pk):
            auto = Auto.objects.get(pk=pk)
            if auto is None:
                return redirect('auto_list')
            return render(request, 'autos/auto_confirm_delete.html', {'auto': auto})

        def post(self, request, pk):
            auto = Auto.objects.get(pk=pk)
            if auto is None:
                return redirect('auto_list')
            auto.delete()
            return redirect('auto_list')


def auto_image_create(request, auto_pk):
    auto = Auto.objects.get(pk=auto_pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.auto = auto
            image.save()
            return redirect('autos:auto_images', auto_pk)
    else:
        form = ImageForm()
    return render(request, 'autos/auto_image_form.html', {'form': form})

def auto_image_update(request, auto_pk, image_pk):
    image = Image.objects.get(pk=image_pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('autos:auto_images', auto_pk)
    else:
        form = ImageForm(instance=image)
    return render(request, 'autos/auto_image_form.html', {'form': form})

def auto_image_delete(request, auto_pk, image_pk):
    image = Image.objects.get(pk=image_pk)
    if request.method == 'POST':
        image.delete()
        return redirect('autos:auto_images', auto_pk)
    else:
        return render(request, 'autos/auto_image_confirm_delete.html', {'image': image})

def upload_auto_image(request):
    if request.method == 'POST':
        form = AutoImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = AutoImageForm()
    return render(request, 'auto_images.html', {'form': form})

def advertisements(request):
    ads = Advertisement.objects.all()
    return render(request, 'autos/advertisements.html', {'ads': ads})
