import random, os
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
palabraAdiv = '-----'
palabraCons = 'Tunja'
fails = 0
#imagn
img = os.path.join('static')

#pagina inicio
@app.route('/')
def index():
    #   flash('letra enviada')
    file = os.path.join(img, 'ahorcado'+str(fails)+'.png')
    return render_template('index.html', image=file)

#otra pagina
@app.route('/juego', methods=['POST'])
def juego():
    if request.method == 'POST':
        # vari globales
        global fails, palabraAdiv
        char = request.form['char']
        #print(char)
        flash(str(len(palabraAdiv)) + ' Letras')
        flash(palabraAdiv)
        
        if len(char) != 1:
            flash('una letra por intento por favor')
        else:
            #registro de letra y puntos
            if char in palabraCons:
                for i, c in enumerate(palabraCons):
                    #flash(str(i) + c)
                    if c == char:
                        temp = list(palabraAdiv) 
                        temp[i] = c
                        palabraAdiv = "".join(temp)
                flash(palabraAdiv)        
            else:
                if fails == 10:
                    flash('FIN :(')
                else:
                    fails = fails+1
                    flash('no es correcto')
        
        if '-' not in palabraAdiv:
            flash('ganaste :)')

        return redirect(url_for('index'))

@app.route('/palabra', methods=['POST'])
def palabra():
    if request.method == 'POST':
        #char = request.form['char']
        #print(char)
        global palabraCons,palabraAdiv, fails
        randWord = random.randint(100,119)
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM word where idWord = ' + str(randWord))

        myresult = cur.fetchall()
        fails = 0
        for x in myresult:
            #print(x)
            
            palabraCons = x[1]
            palabraAdiv = x[1]
            #flash(x[1])

        #crear palabra vacia
        for i, c in enumerate(palabraCons):
            #flash(str(i) + c)
            temp = list(palabraAdiv) 
            temp[i] = '-'
            palabraAdiv = "".join(temp)
                
        #mostrar en pagina
        flash(str(len(palabraAdiv)) + ' Letras')
        flash(palabraAdiv)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)

