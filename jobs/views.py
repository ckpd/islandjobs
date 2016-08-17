from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from .models import Jobpost, Company


class IndexListView(ListView):
    template_name = 'jobs/index.html'
    paginate_by = 5   #and that's it !!
    model = Jobpost
    
    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class ArticleDetailView(DetailView):
    
    template_name = 'jobs/detail.html'
    model = Jobpost
    