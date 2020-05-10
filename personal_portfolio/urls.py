"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_page/', views.admin, name='admin'),
    path('edit_project/', views.edit_project, name='edit_project'),
    path('add_project/', views.add_project, name='add_project'),
    path('transaction/', views.transaction, name='transaction'),
    path('detail/', views.transaction_detail, name='transaction_detail'),
    path('invent_report/', views.invent_report, name='invent_report'),
    path('view_product/', views.view_product, name='view_product'),
    path('view/', views.view, name='view'),

    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)