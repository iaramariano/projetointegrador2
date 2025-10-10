from .models import MedicalEventMod
from datetime import date


######################################################FUNÇÕES PARA REGISTRAR EVENTOS MÉDICOS###############################################

def create_medical_event(patient, event, event_date=date.today, change_status=False, new_aptitude=None):
# Cria um novo evento médico para um paciente específico    
    
    if not patient or not event:
        raise ValueError("Patient e Event são obrigatórios.")
    
    medical_event = MedicalEventMod(
        patient=patient.id_pet,
        event=event,
        event_date=event_date,
        change_status=change_status
    )

    if change_status and new_aptitude:
        patient.aptitude = new_aptitude
        patient.save()

    return medical_event

def create_medical_event_bulk(patients, event, event_date=date.today):

    if patients is None or not patients:
        raise ValueError("A lista de pacientes não pode estar vazia.")
    if not event:
        raise ValueError("Event é obrigatório.")
    if not isinstance(patients, list):
        raise TypeError("Patients deve ser uma lista de pacientes.")
    
    events = [create_medical_event(patient, event, event_date) for patient in patients]

    MedicalEventMod.objects.bulk_create(events)