from django.contrib import admin
from django.urls import include, path

# from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('contact/', include('contact.urls')),
    
    # path('employee/', include('index.urls')),
]

