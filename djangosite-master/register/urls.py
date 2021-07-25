from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/',admin.site.urls),
    path('core/', include('core.urls')),
    path('login/',LoginView.as_view(),name='login'),

]
