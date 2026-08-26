from sample_app import app


def test_ejemplo_basico():
    resultado = 1 + 1

    if resultado != 2:
        raise AssertionError("La suma no es correcta")


def test_respuesta():
    cliente = app.test_client()

    respuesta = cliente.get("/bienvenida")

    if respuesta.status_code != 200:
        raise AssertionError(
            f"El codigo esperado era 200, pero se recibio {respuesta.status_code}"
        )