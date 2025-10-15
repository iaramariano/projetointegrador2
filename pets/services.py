from .models import MedicalEventMod
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
        raise ValueError("A lista de pacientes não pode estar vazia.")
    if not event:
        raise ValueError("Event é obrigatório.")
    
    events = [create_medical_event(patient, event, event_date) for patient in patients]

    MedicalEventMod.objects.bulk_create(events)