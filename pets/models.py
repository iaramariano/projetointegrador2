from django.db import models
from django.forms import MultiWidget, TextInput
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime


class SectorMod(models.Model):
    TYPE = [("I", "Individual"), ("C", "Coletivo")] # Cria as opções de tipo de setor
    id_sector = models.AutoField(primary_key=True)
    name = models.CharField(max_length=65)
    type = models.CharField(max_length=1, choices=TYPE, default="C") # Aplica as opções ao campo

    def __str__(self):
        return f"{self.name}"

class PetsMod(models.Model):
        
        #Criando as opções de escolha para o sexo, porte e aptidão do animal.
        
        APTITUDE = [("AP", "Apto"), ("IN", "Inapto"), ("PR", "Em preparo"), ("AD", "Adotado")]
        SEXES = [("M", "Macho"), ("F", "Fêmea")]
        SIZES = [("P", "Pequeno"), ("PM", "Peq/Médio"), ("M", "Médio"), ("MG", "Med/Grande"), ("G", "Grande")]
        # MONTHS_PT = {1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN", 7: "JUL", 8: "AGO",
        #9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ"}

            
        #Campos em si na mesma ordem em que aparecem no formulário.
        
        #Dados básicos do cão
        id_pet = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100)
        sex = models.CharField(max_length=10, choices=SEXES, default="M")  # 'Masculino', 'Feminino'
        birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
        
        breed = models.CharField(max_length=100, null=True, blank=True)
        size = models.CharField(max_length=20, choices=SIZES, blank= True, default="P")
        sector = models.ForeignKey(SectorMod, on_delete=models.SET_NULL, null=True, related_name='pets')        
        
        #Dados de tratamento

        vaccine = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
        vermifuge = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
        aptitude = models.CharField(max_length=2, choices=APTITUDE, default="AP")

        #Fotos      
        front_photo = models.ImageField(upload_to='pets/photos/front/%Y/%m/')
        side_photo = models.ImageField(upload_to='pets/photos/side/%Y/%m/', blank=True, null=True)
        size_photo = models.ImageField(upload_to='pets/photos/size/%Y/%m/', blank=True, null=True)

        #Metadados
        created_at = models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)
        bg_color = models.CharField(max_length=20, blank=True, null=True, default='')

        
        def __str__(self):
            return self.name