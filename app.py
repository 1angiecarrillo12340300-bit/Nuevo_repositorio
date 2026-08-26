from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Centro de BiotecnologÃ­a Agropecuaria</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <div class="contenedor">
            <h1>Centro de BiotecnologÃ­a Agropecuaria</h1>

            <p>API actualizada automaticamente mediante CI/CD</p>

            <p>Angie Maritza Carrillo Fuquene</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False)


