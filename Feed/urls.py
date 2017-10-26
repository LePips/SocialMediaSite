from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.feed, name='feed'),
    url(r'^profile/(?P<profile_id>\d+)', views.profile, name='profile'),
    url(r'^create_post', views.post, name='create_post'),
    url(r'^delete/(?P<post_id>\d+)', views.delete, name='delete'),
    url(r'^api$', views.api, name='api'),
    url(r'^api/posts', views.PostList.as_view()),
    url(r'^api/profiles', views.ProfileList.as_view()),
]