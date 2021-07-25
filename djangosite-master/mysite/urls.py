from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mysite.core import views

from mysite.core.models import info
from mysite.core.models import Intro
from mysite.core.models import mydoc
from mysite.core.models import profile
from mysite.core.models import skills
from mysite.core.models import Aboutyou

from register import views as v 
from django.conf.urls import include
from django.contrib.auth.views import LoginView
#from register import views as as_view

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    #path('upload/', views.upload, name='upload'),
    #path('uploadlist',views.book_list, name='book_list'),
    path('home/', views.Home.as_view(), name='home'),
    #path('contact_info', views.upload_book, name='upload_book'),
    #path('books/<int:pk>/', views.delete_book, name='delete_book'),
    #path('', views.BookListView.as_view(), name='class_book_list'),
    #path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    #path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    path('admin/', admin.site.urls),
    path('header',views.header,name='header'),
    #path('document',views.document,name='document'),
    path('common',views.common,name='common'),
    path('forminfo',views.forminfo,name='forminfo'),
    path('register/',v.register,name='register'),
    path('login/',v.login,name='login'),
    #path('logout/',),
    #path("",include('myapp.urls')),
    path('info/',views.upload_info, name='info'),
    path('intro/',views.upload_Intro, name='intro'),
    path('doc/',views.upload_mydoc, name='doc'),
    path('profile/',views.upload_profile, name='profile'),
    path('skills/',views.upload_skills, name='skills'),
    path('comment/', views.post_detail, name='post'),
    path('aboutyou/',views.upload_me, name='aboutyou'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
