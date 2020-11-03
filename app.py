from flask import Flask,render_template,request,redirect,url_for
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(host = 'us-cdbr-east-02.cleardb.com',user = 'b13e737dd9e2c4',password = '267c9ade',database = 'heroku_2a4dc602e4cab26')

@app.route("/")
def showData():
    cur = conn.cursor()
    sql = "select * from student"
    cur.execute(sql)
    rows = cur.fetchall()
    return render_template('index.html',datas=rows)

@app.route("/student")
def showForm():
    cur = conn.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template('add.html')

@app.route("/insert",methods=['POST'])
def insert():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
    
        cur = conn.cursor()
        sql = """
            insert into `student` (`fname`,`lname`,`phone`)
            values(%s,%s,%s)
        """
        cur.execute(sql,(fname,lname,phone))
        conn.commit()

        return redirect(url_for('showData'))

@app.route("/delete/<string:id_data>",methods=['GET'])
def delete(id_data):
    cur = conn.cursor()
    sql = "delete from student where id=%s"
    cur.execute(sql,(id_data))
    conn.commit()
    return redirect(url_for('showData'))

@app.route("/update",methods=['POST'])
def update():
    if request.method == 'POST':
        id_update = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
    
        cur = conn.cursor()
        sql = """
            update student set fname=%s,lname=%s,phone=%s where id=%s
        """
        cur.execute(sql,(fname,lname,phone,id_update))
        conn.commit()

        return redirect(url_for('showData'))



if __name__ == "__main__":
    app.run(debug=True)