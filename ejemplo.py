# Ejemplo simple en Python
def saludar(nombre):
 """Función que saluda al usuario"""
 return f"¡Hola, {nombre}! Bienvenido al mundo de Python."
# Ejemplo de uso de la función
print(saludar("Estudiante"))
# Ejemplo de lista y bucle
numeros = [1, 2, 3, 4, 5]
print("Lista de números:")
for num in numeros:
 print(f" - {num} al cuadrado es {num**2}")
# Ejemplo de condicional
edad = 20
if edad >= 18:
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")








 from flask import Flask

app = Flask(__name__)


@app.post("/ingles")
def saludo():
    return "hello world"

@app.route("/japoness")
def salud():
    return "konichiwa world"


@app.route("/frances")
def salu():
    return "bonour jour"


@app.route("/portugues")
def sal():
    return "bonito dia"



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=34)