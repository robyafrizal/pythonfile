from unicodedata import name
from django.db import models

# Create your models here.
class Skill:
    id: int
    name: str
    progress: str