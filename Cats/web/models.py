from uuid import uuid4
from django.db import models


class ContactForms(models.Model):

    uuid_contacto = models.UUIDField(default=uuid4, editable=False)
    mail_cliente = models.EmailField()
    nombre_cliente = models.CharField(max_length=64)
    mensaje = models.TextField()


class Rascadores(models.Model):
    rascador_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_rascador = models.CharField(max_length=64, null=False, unique=True)
    descripcion_rascador = models.TextField(blank=True)
    image_url_rascador = models.URLField()
    slug_rascador = models.SlugField(max_length=75, unique=True)
    is_private = models.BooleanField()
