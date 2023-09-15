from import_export import resources
from .models import Processo

class ProcessoResource(resources.ModelResource):
  class Meta:
    model = Processo