from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import (
    ConsejoDirectivoDetailView, ConsejoDirectivoListView, PromocionDetailView, PromocionListView, TribunalDeJusticiaViewSet, ConsejoDirectivoViewSet, CoordinadorDeportivoViewSet,
    PromocionViewSet, TablaDePosicionesViewSet, ExCadeteViewSet,
    EventoDeportivoViewSet, ParticipacionViewSet, ResultadoViewSet,
    TribunalDeJusticiaListView, TribunalDeJusticiaDetailView, EventoDeportivoListView, EventoDeportivoDetailView, TablaDePosicionesListView, TablaDePosicionesDetailView,
    CoordinadorDeportivoListView, CoordinadorDeportivoDetailView, ExCadeteListView, ExCadeteDetailView, ParticipacionListView, ParticipacionDetailView, ResultadoListView, ResultadoDetailView
)

# Configuración del router
router = DefaultRouter()
router.register(r'tribunal', TribunalDeJusticiaViewSet)
router.register(r'consejo', ConsejoDirectivoViewSet)
router.register(r'coordinador', CoordinadorDeportivoViewSet)
router.register(r'promocion', PromocionViewSet)
router.register(r'tabla', TablaDePosicionesViewSet)
router.register(r'excadete', ExCadeteViewSet)
router.register(r'evento', EventoDeportivoViewSet)
router.register(r'participacion', ParticipacionViewSet)
router.register(r'resultado', ResultadoViewSet)

# Rutas específicas para listas y detalles
urlpatterns = [
    path('', include(router.urls)),
    # Tribunal
    path('tribunal/', TribunalDeJusticiaListView.as_view(), name='tribunal_list'),
    path('tribunal/<int:pk>/', TribunalDeJusticiaDetailView.as_view(), name='tribunal_detail'),
    
    # Consejo Directivo
    path('consejo/', ConsejoDirectivoListView.as_view(), name='consejo_list'),
    path('consejo/<int:pk>/', ConsejoDirectivoDetailView.as_view(), name='consejo_detail'),
    
    # Coordinador Deportivo
    path('coordinador/', CoordinadorDeportivoListView.as_view(), name='coordinador_list'),
    path('coordinador/<int:pk>/', CoordinadorDeportivoDetailView.as_view(), name='coordinador_detail'),
    
    # Promoción
    path('promocion/', PromocionListView.as_view(), name='promocion_list'),
    path('promocion/<int:pk>/', PromocionDetailView.as_view(), name='promocion_detail'),
    
    # Tabla de Posiciones
    path('tabla/', TablaDePosicionesListView.as_view(), name='tabla_list'),
    path('tabla/<int:pk>/', TablaDePosicionesDetailView.as_view(), name='tabla_detail'),
    
    # Evento Deportivo
    path('evento/', EventoDeportivoListView.as_view(), name='evento_list'),
    path('evento/<int:pk>/', EventoDeportivoDetailView.as_view(), name='evento_detail'),
    
    # Resultado
    path('resultado/', ResultadoListView.as_view(), name='resultado_list'),
    path('resultado/<int:pk>/', ResultadoDetailView.as_view(), name='resultado_detail'),
    
    # Participación
    path('participacion/', ParticipacionListView.as_view(), name='participacion_list'),
    path('participacion/<int:pk>/', ParticipacionDetailView.as_view(), name='participacion_detail'),
    
    # Ex Cadete
    path('excadete/', ExCadeteListView.as_view(), name='excadete_list'),
    path('excadete/<int:pk>/', ExCadeteDetailView.as_view(), name='excadete_detail'),
]

# Configuración para servir archivos de medios en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
