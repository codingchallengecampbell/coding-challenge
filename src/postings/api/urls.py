from django.conf.urls import url
from .views import PostRudView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostRudView.as_view(), name='post-rud')
]
