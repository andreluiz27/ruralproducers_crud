from django import forms
from rural_producer.models import RuralProducer
from crop.models import Crop
from farm.models import Farm

# class CropsForm(forms.Form):
#     crop_name = forms.CharField(max_length=100)
#     crop_area = forms.FloatField()


class RuralProducerForm(forms.Form):
    name = forms.CharField(max_length=100)
    cpf_cnpj = forms.CharField(max_length=14, label="CPF/CNPJ")

    # related to the address
    city = forms.CharField(max_length=100)
    state = forms.ChoiceField(choices=Farm.BRAZILIAN_STATES, widget=forms.Select())

    # related to the farm
    farm_name = forms.CharField(max_length=100)
    farm_area = forms.FloatField()
    vegetation_area = forms.FloatField()
    plantable_area = forms.FloatField()

    # crops many to many fields
    crops = forms.ModelMultipleChoiceField(
        queryset=Crop.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    def clean_cpf_cnpj(self):
        cpf_cnpj = self.cleaned_data.get("cpf_cnpj")
        if not cpf_cnpj.isdigit():
            raise forms.ValidationError("CPF or CNPJ must be a number")
        # must be unique
        if RuralProducer.objects.filter(cpf_cnpj=cpf_cnpj).exists():
            raise forms.ValidationError("CPF or CNPJ already exists")

        # identifies if it is a CPF or CNPJ
        if len(cpf_cnpj) == 11:
            # CPF
            pass
        elif len(cpf_cnpj) == 14:
            # CNPJ
            pass
        else:
            raise forms.ValidationError("CPF or CNPJ must have 11 or 14 digits")

        return cpf_cnpj

    def clean_name(self):
        name = self.cleaned_data.get("name")
        # should be unique
        if RuralProducer.objects.filter(name=name).exists():
            raise forms.ValidationError("Name already exists")
        return name

    def clean(self):
        farm_area = self.cleaned_data.get("farm_area")
        vegetation_area = self.cleaned_data.get("vegetation_area")
        plantable_area = self.cleaned_data.get("plantable_area")

        if farm_area < vegetation_area + plantable_area:
            raise forms.ValidationError("Farm area must be greater than vegetation area + plantable area")

        return self.cleaned_data

    def clean_farm_name(self):
        farm_name = self.cleaned_data.get("farm_name")
        if Farm.objects.filter(farm_name=farm_name).exists():
            raise forms.ValidationError("Farm name already exists")
        return farm_name    


    def save(self):
        rural_producer = RuralProducer.objects.create(
            name=self.cleaned_data.get("name"),
            cpf_cnpj=self.cleaned_data.get("cpf_cnpj"),
            farm=Farm.objects.create(
                farm_name=self.cleaned_data.get("farm_name"),
                city=self.cleaned_data.get("city"),
                state=self.cleaned_data.get("state"),
                farm_area=self.cleaned_data.get("farm_area"),
                vegetation_area=self.cleaned_data.get("vegetation_area"),
                plantable_area=self.cleaned_data.get("plantable_area"),
            ),
        )
        for crop in self.cleaned_data.get("crops"):
            rural_producer.farm.crops.add(crop)
        rural_producer.save()
        return rural_producer    


class RuralProducerUpdateForm(forms.Form):
    # related to the address
    city = forms.CharField(max_length=100)
    state = forms.ChoiceField(choices=Farm.BRAZILIAN_STATES, widget=forms.Select())

    # related to the farm
    farm_name = forms.CharField(max_length=100)
    farm_area = forms.FloatField()
    vegetation_area = forms.FloatField()
    plantable_area = forms.FloatField()

    # crops many to many fields
    crops = forms.ModelMultipleChoiceField(
        queryset=Crop.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    def clean(self):
        farm_area = self.cleaned_data.get("farm_area")
        vegetation_area = self.cleaned_data.get("vegetation_area")
        plantable_area = self.cleaned_data.get("plantable_area")

        if farm_area < vegetation_area + plantable_area:
            raise forms.ValidationError("Farm area must be greater than vegetation area + plantable area")

        return self.cleaned_data

    def save(self, pk):
        ruralproducer_queryset = RuralProducer.objects.filter(id=int(pk))
        farm = ruralproducer_queryset.first().farm
        farm.city = self.cleaned_data.get("city")
        farm.state = self.cleaned_data.get("state")
        farm.farm_name = self.cleaned_data.get("farm_name")
        farm.farm_area = self.cleaned_data.get("farm_area")
        farm.vegetation_area = self.cleaned_data.get("vegetation_area")
        farm.plantable_area = self.cleaned_data.get("plantable_area")
        farm.save()

        # remove crops from farm
        farm.crops.clear()
        
        # adding crops to farm
        for crop in self.cleaned_data.get("crops"):
            rural_producer = RuralProducer.objects.get(id=pk)
            rural_producer.farm.crops.add(crop)

        return rural_producer
