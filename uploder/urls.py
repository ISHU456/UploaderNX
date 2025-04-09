from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_document
from django.urls import path
from .views import profile_view

urlpatterns = [
    path('',views.front_page,name="front_page"),
    path('home/',views.home,name="home"),
    path('upload/',views.upload,name="upload"),
    path('register/',views.register,name="register"),
    path('login/',views.views_login,name="login"),
    path('logout/',views.views_logout,name="logout"),
    path('about/',views.about,name="about"),
    path('delete/<int:document_id>/', delete_document, name='delete_document'),
    path('profile/', profile_view, name='profile'),
]
