from django.urls import path
from .import views
from .api import UserReg
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('table/', views.table, name='table'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login_data/', views.login_data, name='login_data'),
    path('signup/',UserReg.as_view(),name='userreg'),
    path('profile/',views.profile,name='profile'),
    path('profile_data/',views.profile_data,name='profile_data'),
    path('success/',views.success,name='success')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
