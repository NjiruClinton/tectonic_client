from django.contrib import admin
from django.urls import path
from app.views import index, add_blog, get_blogs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add_blog/', add_blog, name='add_blog'),
    path('get_blogs/', get_blogs, name='get_blogs'),
]

