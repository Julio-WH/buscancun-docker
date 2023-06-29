from rest_framework import serializers
from apps.chofer.models import Chofer, Autobus

class AutobusSerializer(serializers.ModelSerializer):
    """
    Serializer para dar formato a los datos del modelo Autobus
    """
    class Meta:
        model = Autobus
        fields = (
            'id', 'nombre', 'numero_placa', 'capacidad_pasajeros',
            'capacidad_asientos', 'asientos_disponibles', 'estado', 'activo'
        )

    def to_representation(self, instance):
        return super(AutobusSerializer, self).to_representation(instance)