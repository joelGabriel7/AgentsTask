from django.forms import *

from core.agenda.models import *


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingresa  un titulo',
                    'class': 'form-control',
                }
            ),
            'description': Textarea(
                attrs={
                    'placeholder': 'Ingrese una descripcion',
                    'class': 'form-control',
                    'rows': 3,
                    'cols': 34
                }
            ),
            'time_limits': DateTimeInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
