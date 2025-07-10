import sys
from datetime import datetime
import pandas as pd

def generar_email(nombre, empresa, cargo, servicio):
    saludo = f"Hola {nombre},"
    if servicio.lower() == "headhunting":
        cuerpo = f"Trabajo con empresas que quieren comparar el talento que están atrayendo con lo que realmente ofrece el mercado. ¿Te interesa ver cómo podríamos ayudarte en {empresa}?"
    else:
        cuerpo = f"Estoy colaborando con equipos que quieren mejorar su cultura para que su gente rinda más, esté más alineada y tenga impacto real en facturación. ¿Tiene sentido hablarlo en {empresa}?"
    cierre = "Un saludo,\nJose Sastre\nRebel Talent"
    return f"{saludo}\n\n{cuerpo}\n\n{cierre}"

def registrar_envio(nombre, empresa, cargo, email, servicio, cuerpo):
    archivo = "excel_seguimiento.csv"
    try:
        df = pd.read_csv(archivo)
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "Fecha", "Nombre", "Empresa", "Cargo", "Email", "Servicio", "Email generado"
        ])
    nuevo = {
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Nombre": nombre,
        "Empresa": empresa,
        "Cargo": cargo,
        "Email": email,
        "Servicio": servicio,
        "Email generado": cuerpo
    }
    df = pd.concat([df, pd.DataFrame([nuevo])], ignore_index=True)
    df.to_csv(archivo, index=False)

if __name__ == "__main__":
    nombre, empresa, cargo, email, servicio = sys.argv[1:6]
    cuerpo = generar_email(nombre, empresa, cargo, servicio)
    registrar_envio(nombre, empresa, cargo, email, servicio, cuerpo)
    print(cuerpo)