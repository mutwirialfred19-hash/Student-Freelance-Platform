from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as av

admin.site.site_header = "KCA Talent Hub Admin"
admin.site.site_title = "KCA Talent Hub"
admin.site.index_title = "Platform Management"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', av.home, name='home'),
    path('dashboard/', av.dashboard, name='dashboard'),
    path('accounts/register/student/', av.register_student, name='register_student'),
    path('accounts/register/client/', av.register_client, name='register_client'),
    path('accounts/login/', av.login_view, name='login'),
    path('accounts/logout/', av.logout_view, name='logout'),
    path('projects/', include('projects.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
