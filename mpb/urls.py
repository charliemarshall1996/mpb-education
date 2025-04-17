
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('admin/', include('mpbadmin.urls')),
    path('', include('core.urls')),
    path("contact/", include("django_contact_form.urls")),
    path('curricula/', include('curricula.urls')),
    path('students/', include('students.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
