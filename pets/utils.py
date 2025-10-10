#MELHORIA: Testar o módulo para que não retornem valores. Apenas modifiquem os objetos pet e petlist. Passar apenas pet, petlist no context.

#Cria classes e métodos como apoio as views

from datetime import datetime
from random import randint

class Dates: # Cria classes para gerar suporte referente a datas.
    
    def __init__(self):
        #cria o objeto e estabelece dois atributos. Ano atual e lista de tuplas com numeros e meses em português.
        
        self.months = [('01', 'JAN'), ('02', 'FEV'), ('03', 'MAR'), ('04', 'ABR'),
                        ('05', 'MAI'), ('06', 'JUN'), ('07', 'JUL'), ('08', 'AGO'),
                        ('09', 'SET'), ('10', 'OUT'), ('11', 'NOV'), ('12', 'DEZ')]
        
        self.current_year = datetime.today().year

    def year_list(self, span=20):
        #retorna uma lista de anos como string para preencher os selects do formulário de cadastro/edição.
        return [str(year) for year in range(self.current_year, self.current_year - span, -1)]
    
class BgCardColor(): #Cria classe para gerar a cor de fundo do texto do card

        def __init__(self):
             # cria o objeto e estabelece um atributo com uma lista de cores.
             self.bg_colors = ['card-bg-green', 'card-bg-blue', 'card-bg-pink', 'card-bg-yellow']
        
        def random(self):
            # Retorna uma cor de fundo aleatória para o card do pet.
            return self.bg_colors[randint(0, len(self.bg_colors) - 1)]
            
        def list(self, petlist):
            bg_color_list = [self.bg_colors[i % len(self.bg_colors)] for i in range(len(petlist))]
            return zip(petlist, bg_color_list)