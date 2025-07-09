from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/enviar-email", methods=["POST"])
def enviar_email():
    data = request.json

    nombre = data.get("nombre")
    empresa = data.get("empresa")
    cargo = data.get("cargo")
    email = data.get("email")
    servicio = data.get("servicio")

    resultado = subprocess.run([
        "python", "enviar_email.py", nombre, empresa, cargo, email, servicio
    ], capture_output=True, text=True)

    return jsonify({
        "status": "ok",
        "stdout": resultado.stdout,
        "stderr": resultado.stderr
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)