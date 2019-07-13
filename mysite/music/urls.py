from django.urls import  re_path
from . import views
app_name='music'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
    re_path(r'^register/$', views.UserFormView.as_view(), name="register"),
    re_path(r'^album/(?P<pk>[0-9]+)/songs/$', views.DetailView.as_view(), name='details'),
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update'),
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete'),
    re_path(r'^logout/$', views.logout_view, name="logout"),
    re_path(r'^songs/add_song/$', views.SongAdd.as_view(), name='song_add'),
    re_path(r'^(?P<album_id>[0-9]+)/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song_delete'),

]




























