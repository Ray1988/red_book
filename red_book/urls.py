__author__ = 'lucky'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns= patterns ('red_book.views',
                       url(r'^questions/$', views.QuestionList.as_view()),
                       url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
