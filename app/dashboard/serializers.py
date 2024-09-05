from rest_framework import serializers
from rural_producer.models import RuralProducer

class CropsSerializer(serializers.Serializer):
    crop_name = serializers.CharField(max_length=100)
    crop_area = serializers.FloatField()

class RuralProducerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cpf = serializers.CharField(max_length=11, label="CPF")

    # related to the address
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=2)

    # related to the farm
    farm_name = serializers.CharField(max_length=100)
    farm_area = serializers.FloatField()
    vegetation_area = serializers.FloatField()


    # related to the crops, list of crops
    crops = CropsSerializer(many=True) 
