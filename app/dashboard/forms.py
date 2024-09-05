from django import forms
from rural_producer.models import RuralProducer

# class CropsForm(forms.Form):
#     crop_name = forms.CharField(max_length=100)
#     crop_area = forms.FloatField()

class RuralProducerForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=11, label="CPF")

    # related to the address
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=2)

    # related to the farm
    farm_name = forms.CharField(max_length=100)
    farm_area = forms.FloatField()
    vegetation_area = forms.FloatField()

    # related to the crops, list of crops, many to many field
    # crops = forms.ModelMultipleChoiceField(queryset=None)

    class Meta:
        model = RuralProducer
        fields = ['name', 'cpf', 'city', 'state', 'farm_name', 'farm_area', 'vegetation_area']
