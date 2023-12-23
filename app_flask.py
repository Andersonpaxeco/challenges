from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

#MariaDB [store]> select * from usuarios;
#+--------+----------------+-------+-----------+------+-------------+-------+------------------+
#| iduser | name           | email | telefone  | sexo | cpf         | idade | endereco         |
#+--------+----------------+-------+-----------+------+-------------+-------+------------------+
#|      1 | 111            | NULL  | NULL      | NULL | NULL        |  NULL | NULL             |
#|      2 | anderson       | NULL  | 915648855 | M    | 83756892972 |    52 | rua da liberdade |
#|      3 | Pedro Proença  | NULL  | 923975977 | M    | 18997643651 |    16 | rua da liberdade |
#|      4 | 2              | NULL  | 2         | 2    | 2           |     2 | 2                |
#|      5 | 33             | NULL  | 3         | 3    | 3           |     2 | 3                |
#|      6 | 5              | NULL  | 5         | 5    | 5           |     5 | 5                |
#+--------+----------------+-------+-----------+------+-------------+-------+------------------+

#MariaDB [store]> desc agenda;
#+-----------+--------------+------+-----+---------+-------+
#| Field     | Type         | Null | Key | Default | Extra |
#+-----------+--------------+------+-----+---------+-------+
#| id        | int(11)      | NO   |     | NULL    |       |
#| data      | datetime     | YES  |     | NULL    |       |
#| descricao | varchar(200) | YES  |     | NULL    |       |
#+-----------+--------------+------+-----+---------+-------+



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "me",
    database = "store")




@app.route('/')
def index():
    cursor = db.cursor()
    command = "select * from usuarios"
    cursor.execute(command)
    usuarios = cursor.fetchall()
    #db.close()
    print("Passou por aqui")
    return render_template('index.html', usuarios=usuarios)

  
@app.route('/agendar')
def agenda_lista():
    cursor = db.cursor()
    command = "select * from agenda"
    cursor.execute(command)
    agenda = cursor.fetchall()
    #db.close()
    print("Passou por aqui 2")
    return render_template('agendar.html', agenda=agenda)
    
@app.route('/novo_usuario', methods=['GET','POST'])
def novo_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        cursor = db.cursor()
        command = ("insert into usuarios (name, idade, sexo, cpf, endereco, telefone) values (%s, %s, %s, %s, %s, %s)")
        data = [nome,idade,sexo,cpf,endereco,telefone]
        cursor.execute(command, data)

        db.commit()

        return redirect(url_for('index'))
    return render_template('novo_usuario.html')

@app.route('/agendar', methods=['GET','POST'])
def agendar():
    if request.method == 'POST':
        data_hora = request.form['data']+' '+request.form['hora']
        descricao = request.form['descricao']
        cursor = db.cursor()
        command = ("insert into agenda (id, data, descricao) values (%s, %s, %s)")
        data = [1, data_hora, descricao]
        cursor.execute(command, data)
        
        db.commit()
        return redirect(url_for('index'))
    return render_template('agendar.html')

@app.route('/clear_all')
def clear_all():
    cursor = db.cursor()
    command = "delete from usuarios"
    cursor.execute(command)
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
        app.run(debug=True)