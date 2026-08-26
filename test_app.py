def test_ejemplo_basico():
    resultado = 1 + 1
    if resultado != 2:
        raise AssertionError("La suma no es correcta")

def test_respuesta():
    codigo = 220
    mensaje = "OK"

    if codigo != 220:
        raise AssertionError("El codigo no es 220")

    if mensaje != "OK":
        raise AssertionError("El mensaje no es OK")
