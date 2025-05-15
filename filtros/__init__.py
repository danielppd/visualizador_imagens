from .grayscale import FiltroGrayscale
from .inverter import FiltroInverter
from .contraste import FiltroContraste
from .desfoque import FiltroDesfoque
from .nitidez import FiltroNitidez
from .bordas import FiltroBordas

lista_filtros = [
    FiltroGrayscale(),
    FiltroInverter(),
    FiltroContraste(),
    FiltroDesfoque(),
    FiltroNitidez(),
    FiltroBordas()
]