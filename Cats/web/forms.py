from django import forms
from .models import ContactForms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForms
        fields = ["mail_cliente", "nombre_cliente", "mensaje"]
        widgets = {
            "mail_cliente": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "sucorreo@ejemplo.com"}
            ),
            "nombre_cliente": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Juan Perez"}
            ),
            "mensaje": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "¿Cuál es el valor del ítem '001' y qué método de envío manejan?",
                }
            ),
        }
