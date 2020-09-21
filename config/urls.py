
from django.contrib import admin
from django.urls import path, include
from .views import index, welcome, test_template


urlpatterns = [
    path('admin/', admin.site.urls),

    path('bookmark/', include('bookmark.urls')),
    #path('test/', test_template),
    #path('test/', test_template),
    #path('test/', test_template),
    path('test/', test_template),
    path('welcome/', welcome),


    path('',  index),
]
