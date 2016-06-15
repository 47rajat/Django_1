from View import Staticview
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import ListView
from models import Dreamreal

urlpatterns = [
    url(r'^hello/', 'myapp.View.hello'),
    url(r'^article/(\d+)/', 'myapp.View.viewArticle'),
    url(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})', 'myapp.View.viewArticles'),
    url(r'^crudops/', 'myapp.View.crudops'),
    url(r'^datamanipulation/', 'myapp.View.datamanipulation'),
    url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', 'myapp.View.sendSimpleEmail'),
    url(r'^static/$', Staticview.as_view()),
    url(r'^dreamreals/', ListView.as_view(template_name = "dreamreal_list.html", model = Dreamreal, context_object_name = "dreamreal_objects")),
    url(r'^login/', TemplateView.as_view(template_name = "login.html")),
    url(r'^home/', 'myapp.View.login')
]