from django.contrib import admin
from django.urls import path, include
from apiapp.views import get_data, post_data,get_all_data, delete_data
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', post_data),
    path('delete/<int:id>/', delete_data),
    path('', get_all_data),
    path('<int:id>/', get_data)
]
