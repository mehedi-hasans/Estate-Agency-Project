from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('agent-single', views.agent),
    path('agents-grid', views.agents),
    path('blog-grid', views.blog),
    path('dashboard', views.dashboard),
    path('blog-single', views.blogSingle),
    path('property-grid', views.property),
    path('property-single', views.propertySingle),
]
