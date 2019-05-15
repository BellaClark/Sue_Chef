from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^recipe_page$', views.recipe_page),
    url(r'^add_recipe$', views.add_recipe),
    url(r'^about$', views.about),
    url(r'^ingredients$', views.ingredients),
]