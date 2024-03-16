from django.views.generic import ListView, DetailView
from .models import Consumer

class ConsumerListView(ListView):
    model = Consumer
    template_name = "consumer_list.html"
    context_object_name = "consumers"

class ConsumerDetailView(DetailView):
    model = Consumer
    template_name = "consumer_detail.html"