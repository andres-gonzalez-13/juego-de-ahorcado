import random
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

#palabra a construir
palabraAdiv = ''
palabraCons = ''

#pagina inicio
@app.route('/')
def index():
    #   flash('letra enviada')
    return render_template('index.html')

#otra pagina
@app.route('/juego', methods=['POST'])
def juego():
    if request.method == 'POST':
        char = request.form['char']
        #print(char)
        randWord = random.randint(100,119)
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM word where idWord = ' + str(randWord))

        myresult = cur.fetchall()

        for x in myresult:
            #print(x)
            flash(x)

        return redirect(url_for('index'))

@app.route('/palabra', methods=['POST'])
def palabra():
    if request.method == 'POST':
        #char = request.form['char']
        #print(char)
        randWord = random.randint(100,119)
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM word where idWord = ' + str(randWord))

        myresult = cur.fetchall()

        for x in myresult:
            #print(x)
            flash(x[1])

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

