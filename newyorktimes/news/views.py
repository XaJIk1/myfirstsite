from django.views.generic import ListView, DetailView
from .models import *


class NewsView(ListView):
    model = News
    template_name = 'news/index.html'
    paginate_by = 2


class NewsDetails(DetailView):
    model = News
    template_name = 'news/details_news.html'
    context_object_name = 'news1'


