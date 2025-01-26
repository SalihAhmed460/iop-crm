from django.contrib import admin
from django.contrib.auth import views
from django.urls import path,include
from core.views import index,about


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', include('dashboard.urls')),
    path('clients/', include('client.urls')),
    path('dashboard/team', include('team.urls')),
    path('dashboard/lead/', include('lead.urls')),
    path('dashboard',include('userprofile.urls')),
    path('about/', about, name='about'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/',views.LogoutView.as_view(),name='logout'),
    path("admin/", admin.site.urls),

]
