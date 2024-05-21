from .datos_personales import DatosPersonales
from .domicilio import Domicilio

class Cliente:
    def __init__(self, datos_personales: DatosPersonales, domicilios: Domicilio):
        self.datos_personales = datos_personales
        self.domicilios = domicilios
    def __str__(self):
        domicilios_str = ', '.join(str(domicilio) for domicilio in self.domicilios)
        return f"DP: {self.datos_personales}, Dom: {domicilios_str}"
    def get_fullName(self):
        return self.datos_personales.get_fullName()
    def items_datos_personales(self):
        return vars(self.datos_personales).items()
    def items_domicilios(self):
        domicilios_attributes = []
        for domicilio in self.domicilios:
            domicilios_attributes.append(vars(domicilio).items())
        return domicilios_attributes
