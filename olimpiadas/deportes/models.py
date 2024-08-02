from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='archivos/')
    fecha_subida = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

class TribunalDeJusticia(models.Model):
    miembros = models.TextField()
    funciones = models.TextField()
    resoluciones = models.TextField()

    def __str__(self):
        return f"Tribunal de Justicia {self.id}"
    class Meta:
        verbose_name = "Tribunal de justicia"
        verbose_name_plural = "Tribunal de justicia"

class ConsejoDirectivo(models.Model):
    presidente = models.CharField(max_length=100)
    secretario = models.CharField(max_length=100)
    tesorero = models.CharField(max_length=100)
    otros_miembros = models.TextField()
    funciones = models.TextField()

    def __str__(self):
        return self.presidente

    class Meta:
        verbose_name = "Consejo directivo"
        verbose_name_plural = "Consejo directivo"

class CoordinadorDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    funciones = models.TextField()
    informe_final = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Coordinador deportivo"
        verbose_name_plural = "Coordinador deportivo"

class Promocion(models.Model):
    CATEGORIAS_CHOICES = [
        ('ORO-SUPER MASTER', 'Oro-Super Master'),
        ('MASTER', 'Master'),
        ('SUPER SENIORS', 'Super Seniors'),
        ('SENIORS', 'Seniors'),
        ('MAYORES', 'Mayores'),
        ('CADETES', 'Cadetes'),
        ('MENORES', 'Menores'),
        ('JUNIOR', 'Junior'),
    ]

    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS_CHOICES)
    cuota_inscripcion = models.DecimalField(max_digits=10, decimal_places=2)
    jugadores = models.ManyToManyField('Jugador', related_name='promociones')

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Promoción"
        verbose_name_plural = "Promoción"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugador"

class TablaDePosiciones(models.Model):
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    subdisciplina = models.ForeignKey(Promocion, related_name='subdisciplinas', on_delete=models.CASCADE)
    puntos = models.IntegerField()

    def __str__(self):
        return f"{self.promocion.nombre} - {self.subdisciplina.nombre}"
    class Meta:
        verbose_name = "Tabla de posiciones"
        verbose_name_plural = "Tablas de posiciones"

class ExCadete(models.Model):
    nombre = models.CharField(max_length=100)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    carnet = models.CharField(max_length=100)
    historial_sanciones = models.TextField()

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Ex cadete"
        verbose_name_plural = "Ex cadetes"

class EventoDeportivo(models.Model):
    ESTADO_EVENTO_CHOICES = [
        ('EN_JUEGO', 'En Juego'),
        ('FINALIZADO', 'Finalizado'),
        ('ACABADO', 'Acabado'),
    ]
    
    subdisciplina = models.ForeignKey(Promocion, related_name='eventos', on_delete=models.CASCADE)
    nombre_evento = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField()
    lugar = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_EVENTO_CHOICES, default='EN_JUEGO')

    def __str__(self):
        return f"{self.nombre_evento} - {self.fecha}"

    class Meta:
        verbose_name = "Evento deportivo"
        verbose_name_plural = "Eventos deportivos" 

class Participacion(models.Model):
    ex_cadete = models.ForeignKey(ExCadete, on_delete=models.CASCADE)
    evento_deportivo = models.ForeignKey(EventoDeportivo, on_delete=models.CASCADE)
    resultado = models.TextField()

    def __str__(self):
        return f"{self.ex_cadete.nombre} - {self.evento_deportivo.subdisciplina.nombre}"
    class Meta:
        verbose_name = "Participación"
        verbose_name_plural = "Participaciones"

class Resultado(models.Model):
    disciplina = models.ForeignKey(EventoDeportivo, on_delete=models.CASCADE)
    evento = models.CharField(max_length=100)
    fecha = models.DateField()
    resultado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.evento} - {self.disciplina.nombre_evento}"
    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', default='logos/descarga_1.png')

    # Campos ForeignKey para hasta 20 promociones
    promocion1 = models.ForeignKey(Promocion, related_name='categorias_promocion1', on_delete=models.SET_NULL, null=True, blank=True)
    promocion2 = models.ForeignKey(Promocion, related_name='categorias_promocion2', on_delete=models.SET_NULL, null=True, blank=True)
    promocion3 = models.ForeignKey(Promocion, related_name='categorias_promocion3', on_delete=models.SET_NULL, null=True, blank=True)
    promocion4 = models.ForeignKey(Promocion, related_name='categorias_promocion4', on_delete=models.SET_NULL, null=True, blank=True)
    promocion5 = models.ForeignKey(Promocion, related_name='categorias_promocion5', on_delete=models.SET_NULL, null=True, blank=True)
    promocion6 = models.ForeignKey(Promocion, related_name='categorias_promocion6', on_delete=models.SET_NULL, null=True, blank=True)
    promocion7 = models.ForeignKey(Promocion, related_name='categorias_promocion7', on_delete=models.SET_NULL, null=True, blank=True)
    promocion8 = models.ForeignKey(Promocion, related_name='categorias_promocion8', on_delete=models.SET_NULL, null=True, blank=True)
    promocion9 = models.ForeignKey(Promocion, related_name='categorias_promocion9', on_delete=models.SET_NULL, null=True, blank=True)
    promocion10 = models.ForeignKey(Promocion, related_name='categorias_promocion10', on_delete=models.SET_NULL, null=True, blank=True)
    promocion11 = models.ForeignKey(Promocion, related_name='categorias_promocion11', on_delete=models.SET_NULL, null=True, blank=True)
    promocion12 = models.ForeignKey(Promocion, related_name='categorias_promocion12', on_delete=models.SET_NULL, null=True, blank=True)
    promocion13 = models.ForeignKey(Promocion, related_name='categorias_promocion13', on_delete=models.SET_NULL, null=True, blank=True)
    promocion14 = models.ForeignKey(Promocion, related_name='categorias_promocion14', on_delete=models.SET_NULL, null=True, blank=True)
    promocion15 = models.ForeignKey(Promocion, related_name='categorias_promocion15', on_delete=models.SET_NULL, null=True, blank=True)
    promocion16 = models.ForeignKey(Promocion, related_name='categorias_promocion16', on_delete=models.SET_NULL, null=True, blank=True)
    promocion17 = models.ForeignKey(Promocion, related_name='categorias_promocion17', on_delete=models.SET_NULL, null=True, blank=True)
    promocion18 = models.ForeignKey(Promocion, related_name='categorias_promocion18', on_delete=models.SET_NULL, null=True, blank=True)
    promocion19 = models.ForeignKey(Promocion, related_name='categorias_promocion19', on_delete=models.SET_NULL, null=True, blank=True)
    promocion20 = models.ForeignKey(Promocion, related_name='categorias_promocion20', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

#MODELOS DE DISCIPLINAS 

class Baloncesto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='baloncesto/')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Baloncesto"
####################################################################################
class Atletismo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='atletismo/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Subdisciplina"
        verbose_name_plural = "Atletismo"

class EventosAtl(models.Model):
    subdisciplina = models.ForeignKey(Atletismo, on_delete=models.CASCADE)
    
    ESTADO_EVENTO_CHOICES = [
        ('EN_JUEGO', 'En Juego'),
        ('FINALIZADO', 'Finalizado'),
        ('ACABADO', 'Acabado'),
    ]
    
    # Campos para seleccionar promociones
    promocion1 = models.ForeignKey(Promocion, related_name='atletismo_promocion1', on_delete=models.SET_NULL, null=True, blank=True)
    promocion2 = models.ForeignKey(Promocion, related_name='atletismo_promocion2', on_delete=models.SET_NULL, null=True, blank=True)
    ####copia y pega futbol
    promocion3 = models.ForeignKey(Promocion, related_name='atletismo_promocion3', on_delete=models.SET_NULL, null=True, blank=True)
    promocion4 = models.ForeignKey(Promocion, related_name='atletismo_promocion4', on_delete=models.SET_NULL, null=True, blank=True)
    promocion5 = models.ForeignKey(Promocion, related_name='atletismo_promocion5', on_delete=models.SET_NULL, null=True, blank=True)
    ############################
    
    fecha = models.DateField(default=timezone.now)
    duracion = models.DurationField()

    def __str__(self):
        return f"{self.subdisciplina} - {self.fecha}"
    
    class Meta:
        verbose_name = "Evento de Atletismo"
        verbose_name_plural = "Eventos de Atletismo"

class ResultadosATL(models.Model):
    evento = models.ForeignKey(EventosAtl, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    primer_lugar_nombre = models.CharField(max_length=100)
    primer_lugar_puntaje = models.PositiveIntegerField()
    segundo_lugar_nombre = models.CharField(max_length=100)
    segundo_lugar_puntaje = models.PositiveIntegerField()
    tercer_lugar_nombre = models.CharField(max_length=100)
    tercer_lugar_puntaje = models.PositiveIntegerField()
    otros_puestos = models.TextField(blank=True, null=True)  # Campo de texto para otros puestos

    def __str__(self):
        return f"Resultados de {self.evento} - {self.fecha}"

    class Meta:
        verbose_name = "Resultado de Atletismo"
        verbose_name_plural = "Resultados de Atletismo"
#####################################################################################
class Fulbito(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fulbito/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Fulbito"

class Cubilete(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='cubilete/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Cubilete"

class Billas(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='billas/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Billas"

class Pena(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='pena/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Peña"
############################################################################################
class Natacion(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='natacion/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Subdisciplina"
        verbose_name_plural = "Natacion"




#############################################################################################


class TiroAlSapo(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='tiro_al_sapo/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "TiroAlSapo"

class TenisDeMesa(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='tenis_de_mesa/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "TenisDeMesa"

class Ajedrez(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='ajedrez/')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Ajedrez"


class CrossCountry(models.Model):
    ESTADO_EVENTO_CHOICES = [
        ('EN_JUEGO', 'En Juego'),
        ('FINALIZADO', 'Finalizado'),
        ('ACABADO', 'Acabado'),
    ]
    
    # Campos para seleccionar promociones
    promocion1 = models.ForeignKey(Promocion, related_name='crosscountry_promocion1', on_delete=models.SET_NULL, null=True, blank=True)
    promocion2 = models.ForeignKey(Promocion, related_name='crosscountry_promocion2', on_delete=models.SET_NULL, null=True, blank=True)
    promocion3 = models.ForeignKey(Promocion, related_name='crosscountry_promocion3', on_delete=models.SET_NULL, null=True, blank=True)
    promocion4 = models.ForeignKey(Promocion, related_name='crosscountry_promocion4', on_delete=models.SET_NULL, null=True, blank=True)
    promocion5 = models.ForeignKey(Promocion, related_name='crosscountry_promocion5', on_delete=models.SET_NULL, null=True, blank=True)
    
    nombre_evento = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateField(default=timezone.now)  # Valor predeterminado para la fecha
    lugar = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_EVENTO_CHOICES, default='EN_JUEGO')
    
    # Campo de texto para jugadores
    jugadores = models.TextField(null=True, blank=True)
    
    # Campo para la duración del evento
    duracion = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_evento} - {self.fecha}"

    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "CrossCountry"

class ResultadosCross(models.Model):
    evento = models.ForeignKey(CrossCountry, on_delete=models.CASCADE)
    primer_lugar_nombre = models.CharField(max_length=255)
    segundo_lugar_nombre = models.CharField(max_length=255)
    tercer_lugar_nombre = models.CharField(max_length=255)
    otros_puestos_nombre = models.TextField()
    
    primer_lugar_puntaje = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    segundo_lugar_puntaje = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tercer_lugar_puntaje = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    otros_puestos_puntaje = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Resultados para {self.evento.nombre_evento} - {self.evento.fecha}"

    class Meta:
        verbose_name = "Resultados Cross Country"
        verbose_name_plural = "Resultados Cross Country"



class InauguracionDesfile(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='inauguracion_desfile/')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "EVENTO"
        verbose_name_plural = "Inauguraciones"