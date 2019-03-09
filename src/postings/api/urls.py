from django.conf.urls import url
from .views import PostRudView, PostAPIView
urlpatterns = [

    url(r'^$', PostAPIView.as_view(), name='post-create'),
    url(r'^(?P<pk>\d+)/$', PostRudView.as_view(), name='post-rud')
]
