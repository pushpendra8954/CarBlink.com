"""
URL configuration for mycar project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mycar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home',views.index), #if matches blank '' then go to app_1 views file and execute function named as index.
    path('about',views.about),
    path('services',views.services),
    path('contactus',views.contactus),
    path('loginuser',views.loginuser),
    path('registeruser',views.registeruser),
    path('logoutuser',views.logoutuser),
    path('result',views.result),
    path('findcar',views.findcar),
    path('checkout',views.checkout),
    path('test_drive',views.test_drive),
    path('show_cars',views.show_cars),
    # path('show_books_admin',views.show_books_admin),
    # path('remove', views.remove),
    # path('delete/<int:book_id>', views.delete, name='delete'),
    # path('about_admin', views.about_admin),
    # path('cnf_order',views.cnf_order),
    path('search',views.search),
    path('calc',views.calc),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)