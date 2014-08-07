__author__ = 'lucky'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

import views

urlpatterns= patterns ('red_book.views',
                       url(r'^$', 'api_root'),
                       url(r'^questions/$', views.QuestionList.as_view(),
                           name='question-list'),
                       url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(),
                           name='question-detail'),
                       url(r'^users/$', views.UserList.as_view(),
                           name='user-list'),
                       url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),
                           name='user-detail'),
                       url(r'^questions/(?P<pk>[0-9]+)/highlight/$', views.QuestionHighlight.as_view(),
                           name='question-highlight'),

)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)