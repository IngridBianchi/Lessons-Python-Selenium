import pytest
from utils.loader_data import load_data_from_json
from src.domicilio import Domicilio
from src.datos_personales import DatosPersonales
from src.factory import ClienteFactory
from pages.demoqa import DemoqaAutomationPracticeForm ,DemoqaTextBox
from marshmallow import ValidationError


def test_crear_cliente_desde_json():
    datos_json = load_data_from_json('data/formulario.json')
    domicilios_json = load_data_from_json('data/domicilios.json')

    try:
        cliente = ClienteFactory.crear_cliente(datos_json, domicilios_json)
        assert isinstance(cliente.datos_personales, DatosPersonales)
        for domicilio in cliente.domicilios:
            assert isinstance(domicilio, Domicilio)
        return cliente

    except ValidationError as e:
        pytest.fail(f"Error de validación JSON: {e}")

def test_completar_formulario_selenium():
    cliente = test_crear_cliente_desde_json()
    try:
        test_automation_practice_form = DemoqaAutomationPracticeForm (cliente)
        test_text_box = DemoqaTextBox (cliente)
        test_automation_practice_form.testear()
        test_text_box.testear()
    except Exception as e:
        pytest.fail(f"Error en Demoqa: {e}")