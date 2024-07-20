from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Item(models.Model):
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z\s\-\'\.]+$',
        message='Author name can only contain letters, spaces, hyphens, apostrophes, and periods.'
    )
    author = models.CharField(max_length= 50, validators=[name_validator])
    joke = models.CharField(max_length=300)