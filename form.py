from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'

db = mysql.connector.connect(
    host="172.19.0.2",
    user="root",
    password="jeyson13",
    database="db_production"
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        dpi = request.form['dpi']
        edad = request.form['edad']
        correo = request.form['correo']
        
        
        # Crear una consulta SQL para insertar los datos en la tabla correspondiente
        consulta = "INSERT INTO usuarios (nombre, apellido, dpi, edad, correo) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, apellido, dpi, edad, correo)
        
        # Ejecutar la consulta
        cursor.execute(consulta,valores)
        print(cursor.statement) # Imprime la consulta SQL
        
        # Guardar los cambios en la base de datos
        db.commit()

        #cursor.close()
        #db.close()

        #Devolver una respuesta al usuario
        return f'Datos recibidos:<br>Nombre: {nombre}<br>Apellido: {apellido}<br>DPI: {dpi}<br>Edad: {edad}<br>Correo: {correo}'
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run()




