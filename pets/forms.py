from django import forms
from .models import PetsMod, SectorMod, MedicalEventMod
from .utils import MEDICAL_EVENTS_SECTOR

# *********************************************FORMULÁRIO PARA REGISTRO DE CÃES*********************************************

class PetsModForm(forms.ModelForm):
    class Meta:
        model = PetsMod
        fields = ['name', 'sex', 'birth', 'breed', 'size', 'sector', #dados basicos 
                  'vaccine', 'vermifuge', 'aptitude', #dados de tratamento
                  'front_photo','side_photo', 'size_photo'] # fotos
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control text-center form-field-lg', 'placeholder': 'Nome do cão'}),
                   'sex': forms.RadioSelect(attrs={'class': 'form-check-input ms-3 me-2'}),
                   #linha em branco para o nascimento
                   'breed': forms.TextInput(attrs={'class': 'form-control text-center form-field-lg', 'value': 'Sem raça definida'}),
                   'size': forms.Select(attrs={'class': 'form-select text-center form-field-md'}),
                   'sector': forms.Select(attrs={'class': 'form-select text-center form-field-md'}),
                   'aptitude': forms.Select(attrs={'class': 'form-select text-center form-field-md'}),
                   'front_photo': forms.ClearableFileInput(attrs={'class': 'form-control w-75', 'onchange': "previewImage(event, 'frontPreview')"}),
                   'side_photo': forms.ClearableFileInput(attrs={'class': 'form-control w-75', 'onchange': "previewImage(event, 'sidePreview')"}),
                    'size_photo': forms.ClearableFileInput(attrs={'class': 'form-control w-75', 'onchange': "previewImage(event, 'sizePreview')"})
                    }
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fields['sector'].empty_label = "Selecione um setor"
        self.fields['sector'].required = True
        self.fields['sex'].empty_label = None
        self.fields['sex'].required = True
        self.fields['front_photo'].widget.initial_text = 'Foto atual'
        self.fields['front_photo'].widget.input_text = 'Escolher outra'

        self.fields['size_photo'].widget.initial_text = 'Foto atual'
        self.fields['size_photo'].widget.input_text = 'Escolher outra'

        self.fields['side_photo'].widget.initial_text = 'Foto atual'
        self.fields['side_photo'].widget.input_text = "Escolher outra"

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return name.capitalize()

    def clean_breed(self):
        breed = self.cleaned_data.get('breed','')
        return breed.capitalize()

# *********************************************FORMULÁRIO PARA REGISTRO DE SETORES*********************************************


class SectorModForm(forms.ModelForm):
    class Meta:
        model = SectorMod
        fields = ['name', 'type']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control text-center field-add-sector', 'placeholder': 'Nome do setor'}),
                     'type': forms.Select(attrs={'class': 'form-select text-center field-add-type'})        
                   }
        
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return name.capitalize()
       
#******************************************FORMULÁRIO PARA CADASTRO DE EVENTO MÉDICO PARA UM PET**********************************************


class MedicalEventForm(forms.ModelForm):
    class Meta:
        model = MedicalEventMod
        fields = ['patient','event','event_date','change_status']
        widgets = {'patient': forms.Select(attrs={'class': 'form-select text-center form-field-md', 'required': 'true'}),
                    'event': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'class': 'form-control text-center form-field-lg', 'placeholder': 'Descreva o evento médico', 'required': 'true'}),
                   'event_date': forms.DateInput(attrs={'class': 'form-control text-center form-field-md', 'type': 'date', 'value': '', 'required': 'true'}),
                   'change_status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
                   }
        labels = {'event_date': 'DATA DO EVENTO', 'change_status': 'ALTERAR SITUAÇÃO DO CÃO', 'patient': 'CÃO', 'event': 'EVENTO MÉDICO'}
    
    def clean_event(self):
        event = self.cleaned_data.get('event', '')
        return event.capitalize()
    
#***************************************************FORMULÁRIO PARA ALTERAÇÃO DE STATUS DO PET)****************************************** 
#******************************************************(AUXILIAR AO DO EVENTO MÉDICO)***************************************************

class NewStatusForm(forms.ModelForm):
    class Meta:
        model = PetsMod
        fields = ['aptitude']
        widgets = {'aptitude': forms.Select(attrs={'class': 'form-select text-center form-field-md'})}
        labels = {'aptitude': 'ALTERAR SITUAÇÃO DO CÃO PARA:'}

#******************************************FORMULÁRIO PARA CADASTRO DE EVENTO MÉDICO PARA UM SETOR***************************************

class MedicalEventSectorForm(forms.ModelForm):
    event = forms.ChoiceField(choices=MEDICAL_EVENTS_SECTOR, label='EVENTO MÉDICO', widget=forms.Select(attrs={'class': 'form-select text-center form-field-md', 'required': 'true'}))

    class Meta:
        model = MedicalEventMod
        fields = ['event','event_date']
        widgets = {
                   'event_date': forms.DateInput(attrs={'class': 'form-control text-center form-field-md', 'type': 'date', 'value': '', 'required': 'true'})
                   }
        labels = {'event_date': 'DATA DO EVENTO'}

#**************************************************FORMULÁRIO PARA SELEÇÃO DE SETOR********************************************************
#************************************************(AUXILIAR AO DO EVENTO MÉDICO DE SETOR)***************************************************

class SectorSelectForm(forms.ModelForm):
    class Meta:
        model = PetsMod
        fields = ['sector']
        widgets = {'sector': forms.Select(attrs={'class': 'form-select text-center form-field-md', 'required': 'true'})}
        labels = {'sector': 'SETOR'}