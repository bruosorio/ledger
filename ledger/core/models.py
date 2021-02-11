from polymorphic.models import PolymorphicModel
from django.db import models


class Project(PolymorphicModel):
    topic = models.CharField(max_length=30)

class ArtProject(Project):
    artist = models.CharField(max_length=30)

class ResearchProject(Project):
    supervisor = models.CharField(max_length=30)

class VaccineProject(Project):
    supplier = models.CharField(max_length=30)

class CoronaProject(VaccineProject):
    disease = models.CharField(max_length=30)
    