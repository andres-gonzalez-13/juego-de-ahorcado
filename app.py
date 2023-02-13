from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#contraseña de la conexion segun pc
app.config['MYSQL_PASSWORD'] = 'mimimimi'
app.config['MYSQL_DB'] = 'ahorcado'
mysql = MySQL(app)

#session

app.secret_key = 'mysecretkey'

#pagina inicio
@app.route('/')
def index():
    flash('letra enviada')
    return render_template('index.html')

#otra pagina
@app.route('/juego', methods=['POST'])
def juego():
    if request.method == 'POST':
        char = request.form['char']
        #print(char)
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM word')

        myresult = cur.fetchall()

        for x in myresult:
            #print(x)
            flash(x)

        
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

