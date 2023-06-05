from import_export import resources
from .models import Car
class CarResource(resources.ModelResource):
    class meta:
        model=Car