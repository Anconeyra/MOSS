from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Añadir esta línea para incluir las URLs de internacionalización
    path('GrupoMoss/', include('deportes.urls')),
    path('frontend/', TemplateView.as_view(template_name='index.html')),
]

# Agregar las URLs de administración dentro de i18n_patterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
