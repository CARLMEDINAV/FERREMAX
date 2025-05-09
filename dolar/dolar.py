import bcchapi
import pandas as pd
from datetime import datetime
import json

def obtener_dolar():
    try:
        siete = bcchapi.Siete("carl.medinav@duocuc.cl", "Medina04") 
        datos = siete.cuadro(
            series=["F073.TCO.PRE.Z.D"],
            nombres=["Dólar Observado"],
            desde=datetime.now().strftime("%Y-%m-%d"),
            hasta=datetime.now().strftime("%Y-%m-%d"),
            frecuencia="D",
            observado={"Dólar Observado": "last"}
        )
        df = pd.DataFrame(datos)
        valor = df.iloc[0]["Dólar Observado"]

        # Guardar en un archivo JSON
        with open("dolar.json", "w") as f:
            json.dump({
                "valor": valor,
                "fecha": datetime.now().strftime("%Y-%m-%d")
            }, f)

        return valor

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    valor = obtener_dolar()
    print(f"Dólar hoy: ${valor:.2f} CLP" if valor else "No se pudo obtener el dato.")
