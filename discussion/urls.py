from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
  path('', views.discussion, name ='discussion'),
  path('<int:pk>/', views.discussion_topic, name = 'discussion_topic'),
  path('<int:pk>/new/', views.new_topic, name = 'new_topic'),
  #path('<int:pk>/topics/<int:topic_pk>', views.topic_posts, name='topic_posts'),
  url('(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
  url('(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
  url('(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
      views.PostUpdateView.as_view(), name='edit_post'),
url('(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/delete/$',
      views.PostDeleteView.as_view(), name='delete_post'),
]