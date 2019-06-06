from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^recipe_page/(?P<recipe_id>\d+)$', views.recipe_page),
    url(r'^add_recipe$', views.add_recipe),
    url(r'^about$', views.about),
    url(r'^ingredients/(?P<recipe_id>\d+)$', views.ingredients),
    url(r'^tools/(?P<recipe_id>\d+)$', views.tools),
    url(r'^step/(?P<recipe_id>\d+)/(?P<step_num>\d+)$', views.step),
    url(r'^create_recipe$', views.create_recipe),
    url(r'^add_ingredients/(?P<recipe_id>\d+)$', views.add_ingredients),
    url(r'^create_ingredient/(?P<recipe_id>\d+)$', views.create_ingredient),
    url(r'^add_tools/(?P<recipe_id>\d+)$', views.add_tools),
    url(r'^create_tool/(?P<recipe_id>\d+)$', views.create_tool),
    url(r'^add_steps/(?P<recipe_id>\d+)$', views.add_steps),
    url(r'^create_step/(?P<recipe_id>\d+)$', views.create_step),
    url(r'^end_recipe/(?P<recipe_id>\d+)$', views.end_recipe),
    url(r'^search$', views.search),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
