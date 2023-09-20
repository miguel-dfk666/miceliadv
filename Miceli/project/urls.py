"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "app"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.Register, name="singup"),
    path("login/", views.Login, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path("", views.HomePage, name="home"),
    path('processar_opcao/', views.processar_opcao, name='processar_opcao'),
    path('importexcel/', views.simple_upload, name='simple_upload'),
    path('dashboard/numero-processo/', views.dashboard_numero_processo, name='dashboard-numero-processo'),
    path('dashboard/numero-oab/', views.dashboard_numero_oab, name='dashboard_numero_oab'),
    path('dashboard/data-criacao/', views.dashboard_data_criacao, name='dashboard_data_criacao'),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
]

urlpatters = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
