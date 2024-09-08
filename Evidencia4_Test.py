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


@pytest.mark.parametrize("bateria_inicial, incremento, velocidad_esperada, bateria_esperada", [
    (100, 10, 10, 98),  # Aceleración normal
    (100, 70, 60, 98),  # Aceleración a velocidad máxima
    (2, 10, 10, 0),     # Aceleración con batería mínima
])
def test_acelerar(bateria_inicial, incremento, velocidad_esperada, bateria_esperada):
    scooter = Scooter("Rojo", "Honda", "Model X", 60)
    scooter.bateria = bateria_inicial
    scooter.encender()
    if bateria_inicial > 0:
        assert "Aceleramos" in scooter.acelerar(incremento)
    else:
        with pytest.raises(ValueError, match="La batería está vacía"):
            scooter.acelerar(incremento)
    assert scooter.velocidad_actual == velocidad_esperada
    assert scooter.bateria == bateria_esperada



@pytest.mark.parametrize("bateria_inicial, incremento, decremento, velocidad_esperada, bateria_esperada", [
    (100, 20, 10, 10, 98),   # Frenar después de acelerar
    (100, 20, 20, 0, 98),    # Frenar a 0 velocidad
    (3, 10, 10, 0, 1),       # Frenar con batería mínima
])
def test_frenar(bateria_inicial, incremento, decremento, velocidad_esperada, bateria_esperada):
    scooter = Scooter("Rojo", "Honda", "Model X", 60)
    scooter.bateria = bateria_inicial
    scooter.encender()
    scooter.acelerar(incremento)
    if bateria_inicial > 0:
        assert "Desaceleramos" in scooter.frenar(decremento)
    else:
        with pytest.raises(ValueError, match="La batería está vacía"):
            scooter.frenar(decremento)
    assert scooter.velocidad_actual == velocidad_esperada
    assert scooter.bateria == bateria_esperada



@pytest.mark.parametrize("bateria_inicial, expected", [
    (100, "Scooter apagada."),   # Apagar cuando está encendida
    (3, "Scooter apagada."),     # Apagar cuando está encendida y batería vacía
])
def test_apagar(bateria_inicial, expected):
    scooter = Scooter("Rojo", "Honda", "Model X", 60)
    scooter.bateria = bateria_inicial
    scooter.encender()
    assert scooter.apagar() == expected
    with pytest.raises(ValueError, match="La scooter ya está apagada"):
        scooter.apagar()
