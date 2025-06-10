from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from services import views as services_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', services_views.home, name='home'),
    path('sell/', services_views.sell, name='sell'),
    path('repair/', services_views.repair, name='repair'),
    path('buy/', services_views.buy, name='buy'),
    path('build-pc/', services_views.build_pc, name='build_pc'),
    path('register/', user_views.register, name='register'),
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)