from django.db import models
from asgiref.sync import async_to_sync

# Create your models here.

class Autobus(models.Model):

    EN_ESPERA = 'EN ESPERA'
    ABORDANDO = 'ABORDANDO'
    SALIENDO = 'SALIENDO'
    EN_VIAJE = 'EN VIAJE'
    LLEGANDO = 'LLEGANDO'

    ESTADO = (
        (EN_ESPERA, EN_ESPERA),
        (ABORDANDO, ABORDANDO),
        (SALIENDO, SALIENDO),
        (EN_VIAJE, EN_VIAJE),
        (LLEGANDO, LLEGANDO)
    )
    nombre = models.CharField('Nombre', max_length=80)
    numero_placa = models.CharField(max_length=20)
    capacidad_pasajeros = models.PositiveIntegerField(verbose_name='Capacidad', default=60)
    asientos_disponibles = models.PositiveIntegerField(verbose_name='Asientos Disponibles', default=0)
    capacidad_asientos = models.PositiveIntegerField(default=40)
    activo = models.BooleanField(default=True)
    estado = models.CharField(max_length=25, choices=ESTADO, default=EN_ESPERA)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Autobus'
        verbose_name_plural = 'Autobuses'

    def __str__(self):
        return f"{self.nombre} {self.numero_placa}"
    
    @classmethod
    async def obtener_autobuses_activos(cls):
        # Consulta asíncrona utilizando Django ORM
        queryset = cls.objects.filter(activo=True)

        # Convertir la consulta en una lista en un contexto asíncrono
        autobuses_activos = await async_to_sync(queryset.all)()

        return autobuses_activos


class Chofer(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    apellidos = models.CharField('Apellidos', max_length=100)
    autobus = models.OneToOneField(Autobus, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
