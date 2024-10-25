from uuid import uuid4
from django.db import models


class Rascadores(models.Model):  # Convención de Django: clases en mayúsculas
    rascador_uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name_rascador = models.CharField(max_length=64, null=False, unique=True)
    descripcion_rascador = models.TextField(blank=True)  # Corrige la ortografía
    image_url_rascador = models.URLField()
    slug_rascador = models.SlugField(max_length=75, unique=True)
    is_private = models.BooleanField()
