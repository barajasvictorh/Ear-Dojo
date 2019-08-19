from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Topic
from django.http import Http404
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'eardojo/index.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.all()

class DetailView(generic.DetailView):
    model = Topic
    template_name = 'eardojo/detail.html'
