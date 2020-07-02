from django.contrib import admin
from django.urls import path
from users import views
from django.contrib.auth import views as authview
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', authview.LoginView.as_view(template_name='users/login.html')),
    path('logout/', authview.LogoutView.as_view(template_name='users/logout.html')),
    path('contact/',views.contact),
    path('profile/',views.profile,name='profile'),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
