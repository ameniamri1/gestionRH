from django import forms
from .models import Leave

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['leave_type', 'start_date', 'end_date']
        labels = {
            'leave_type': 'Type de congé',
            'start_date': 'Date de début',
            'end_date': 'Date de fin',
        }
        help_texts = {
            'leave_type': 'Sélectionnez le type de congé',
            'start_date': 'Date à laquelle vous souhaitez commencer votre congé',
            'end_date': 'Date à laquelle vous prévoyez de reprendre le travail',
        }
