from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '<PASSWORD>'
app.config['MYSQL_DB'] = '<dbname>'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.form['firstname']
        surname = request.form['surname']
        email = request.form['email']
        pet = request.form['pet']
        hobby = request.form['hobby']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO persons(firstname, surname, email, petid, hobbyid) VALUES(%s, %s, %s, %s, %s)",
                    (firstname, surname, email, pet, hobby))
        mysql.connection.commit()
        cur.close()

    # Fetch all users from the database
    cur = mysql.connection.cursor()
    cur.execute("SELECT firstname, surname, email, pets.petname, hobbies.hobby, persons.personid FROM persons LEFT JOIN hobbies ON persons.hobbyid = hobbies.hobbyid LEFT JOIN pets ON persons.petid = pets.petid")
    userdetails = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("""select * from pets""")
    petsdetails = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("""select * from hobbies""")
    hobbydetails = cur.fetchall()
    cur.close()

    return render_template('index.html', userdetails=userdetails, petdetails=petsdetails, hobbydetails=hobbydetails)


@app.route('/delete/<int:personid>', methods=['POST'])
def delete_user(personid):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM persons WHERE personid = %s", [personid])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
