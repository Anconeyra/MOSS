from django.contrib import admin
from .models import (
    ConsejoDirectivo, CoordinadorDeportivo, EventoDeportivo, ExCadete, Jugador, Participacion,
    Promocion, Resultado, TablaDePosiciones, TribunalDeJusticia, Categoria,
    Baloncesto, Atletismo, Fulbito, Cubilete, Billas, Pena, Natacion,
    TiroAlSapo, TenisDeMesa, Ajedrez, CrossCountry, ResultadosCross, EventosAtl, ResultadosATL
)

# Registros de modelos personalizados
admin.site.register(Resultado)
admin.site.register(TribunalDeJusticia)
admin.site.register(ConsejoDirectivo)
admin.site.register(CoordinadorDeportivo)
admin.site.register(Jugador)
admin.site.register(TablaDePosiciones)
admin.site.register(ExCadete)
admin.site.register(EventoDeportivo)
admin.site.register(Participacion)
admin.site.register(Categoria)

# Registro de los modelos de disciplinas
@admin.register(Baloncesto)
class BaloncestoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Atletismo)
class AtletismoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Fulbito)
class FulbitoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Cubilete)
class CubileteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Billas)
class BillasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Pena)
class PenaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Natacion)
class NatacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(TiroAlSapo)
class TiroAlSapoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(TenisDeMesa)
class TenisDeMesaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(Ajedrez)
class AjedrezAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

@admin.register(CrossCountry)
class CrossCountryAdmin(admin.ModelAdmin):
    list_display = ('nombre_evento', 'fecha', 'lugar', 'estado')

# Registro de ResultadosCross
@admin.register(ResultadosCross)
class ResultadosCrossAdmin(admin.ModelAdmin):
    list_display = ('evento', 'primer_lugar_nombre', 'segundo_lugar_nombre', 'tercer_lugar_nombre')

# Registro de EventosAtl
@admin.register(EventosAtl)
class EventosAtlAdmin(admin.ModelAdmin):
    list_display = ('subdisciplina', 'promocion1', 'promocion2', 'promocion3', 'promocion4', 'promocion5', 'fecha', 'duracion')

# Registro de ResultadosATL
@admin.register(ResultadosATL)
class ResultadosATLAdmin(admin.ModelAdmin):
    list_display = ('evento', 'fecha', 'primer_lugar_nombre', 'primer_lugar_puntaje', 
                    'segundo_lugar_nombre', 'segundo_lugar_puntaje', 
                    'tercer_lugar_nombre', 'tercer_lugar_puntaje')