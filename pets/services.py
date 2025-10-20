from .models import MedicalEventMod, PetsMod
from datetime import date


######################################################FUNÇÕES PARA REGISTRAR EVENTOS MÉDICOS###############################################

def create_medical_event(patient, event, event_date=date.today(), change_status=False):
# Cria um novo evento médico para um paciente específico    
    
    if not patient or not event:
        raise ValueError("Patient e Event são obrigatórios.")
    
    medical_event = MedicalEventMod(
        patient=patient,
        event=event,
        event_date=event_date,
        change_status=change_status
    )
    
    return medical_event

def update_status_medical_event(patient, new_status):
# Atualiza o status de um paciente específico

    if not patient or not new_status:
        raise ValueError("Patient e New Status são obrigatórios.")
    
    patient.aptitude = new_status
    patient.save()

def create_medical_event_bulk(patients, event, event_date=date.today()):

    if patients is None or not patients:
        raise ValueError("Não há residentes no setor selecionado.")
    if not event:
        raise ValueError("Houve um erro no registro do evento.")
    
    events = [create_medical_event(patient, event, event_date) for patient in patients]

    MedicalEventMod.objects.bulk_create(events)

def register_medical_event_pet(MedicalEventForm, NewStatusForm):

    if MedicalEventForm.is_valid():
        
        patient = MedicalEventForm.cleaned_data.get('patient')
        event_date = MedicalEventForm.cleaned_data.get('event_date') or date.today()
        event = MedicalEventForm.cleaned_data.get('event')
        change_status = MedicalEventForm.cleaned_data.get('change_status')
        
        medical_event = create_medical_event(patient, event, event_date, change_status)
        medical_event.save()
        

        if change_status is True:
            
            if NewStatusForm.is_valid():
                
                new_status = NewStatusForm.cleaned_data.get('aptitude')
                update_status_medical_event(patient, new_status)

            else:        
                raise ValueError("Ocorreu um erro na seleção do status.")
        
        sucess_message = f"Evento médico '{event}' registrado com sucesso para {patient.name}."
        return sucess_message        
    
    else:
        raise ValueError("Ocorreu um erro na validação do formulário.")
    

def register_medical_event_sector(medical_event_form, sector_form):
# Registra um evento médico para todos os pets de um setor específico
    
    if medical_event_form.is_valid() and sector_form.is_valid():

        sector = sector_form.cleaned_data.get('sector')

        sector_residents = list(PetsMod.objects.filter(sector=sector.id_sector))
        event = medical_event_form.cleaned_data.get('event')
        event_date = medical_event_form.cleaned_data.get('event_date') or date.today()

        try: 
            create_medical_event_bulk(sector_residents, event, event_date)

        except Exception as e:
            raise e
   
        sucess_message = f"Evento médico '{event}' registrado com sucesso para todos os residentes do setor {sector.name}."
        return sucess_message
    
    else:
        raise ValueError("Ocorreu um erro na validação do formulário.")