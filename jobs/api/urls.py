from django.conf.urls import url
from .views import PostListAPIView


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    #url(r'^(?P<pk>[-\w]+)/$', ArticleDetailView.as_view(), name='article'),
]
