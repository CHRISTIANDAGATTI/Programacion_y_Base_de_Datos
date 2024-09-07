import pytest
from Evidencia4_Clase import Scooter

@pytest.mark.parametrize("bateria_inicial, expected_bateria", [
    (100, 99),  # Batería inicial suficiente para encender
    (1, 0),     # Batería mínima para encender y luego quedarse en 0
])
def test_encender(bateria_inicial, expected_bateria):
    scooter = Scooter("Verde", "Honda", "Model X", 60)
    scooter.bateria = bateria_inicial
    assert scooter.encender() == "Scooter encendida."
    assert scooter.bateria == expected_bateria
