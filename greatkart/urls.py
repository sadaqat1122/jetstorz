from django.contrib import admin
from django.urls import path, include, re_path  # Import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^jet/', include('jet.urls', namespace='jet')),  # Correct usage of re_path and namespace
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('about/', views.about, name='about_us'),
    path('whyus/', views.whyus, name='why_us'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
   # path('grappelli/', include('grappelli.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
