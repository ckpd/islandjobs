from django.conf.urls import url
from jobs.views import IndexListView, ArticleDetailView

app_name = 'jobs'

urlpatterns = [
    url(r'^$', IndexListView.as_view(), name='index'),
    url(r'^(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='article'),

]
