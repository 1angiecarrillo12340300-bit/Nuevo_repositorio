
from flask import Flask, request, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)


def conectar_bd():
    for intento in range(10):
        try:
            return mysql.connector.connect(
                host="db",
                port=3306,
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
        except mysql.connector.Error:
            print(f"Esperando MySQL... intento {intento + 1}/10")
            time.sleep(3)

    raise Exception("No fue posible conectarse a MySQL")


def crear_tabla():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aprendices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre_completo VARCHAR(100) NOT NULL,
            numero_documento VARCHAR(20) NOT NULL,
            ficha VARCHAR(20) NOT NULL,
            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexion.commit()
    cursor.close()
    conexion.close()


@app.route("/aprendices", methods=["GET"])
def obtener_aprendices():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM aprendices
        ORDER BY id DESC
    """)

    aprendices = cursor.fetchall()

    cursor.close()
    conexion.close()

    for aprendiz in aprendices:
        aprendiz["creado_en"] = str(aprendiz["creado_en"])

    return jsonify(aprendices)


@app.route("/registrar", methods=["POST"])
def registrar():
    datos = request.get_json()

    nombre = datos["nombre_completo"]
    documento = datos["numero_documento"]
    ficha = datos["ficha"]

    conexion = conectar_bd()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO aprendices
        (nombre_completo, numero_documento, ficha)
        VALUES (%s, %s, %s)
    """, (nombre, documento, ficha))

    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Aprendiz registrado correctamente"})


@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API de Registro de Aprendices funcionando"
    })


if __name__ == "__main__":
    crear_tabla()

    app.run(
        host="0.0.0.0",  # nosec B104
        port=5050,
        debug=True
    )

@app.route("/bienvenida")
def bienvenida():
    return jsonify({
        "mensaje": "Bienvenidos - actualizacion automatica mediante CI/CD"
    }),500



