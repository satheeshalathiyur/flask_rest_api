from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from flask_restful import reqparse, Resource, Api

app = Flask(__name__)
app.debug = True
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'scraper'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
TABLE_NAME = 'user'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


app = Flask(__name__)
api = Api(app)


class User(Resource):
    def get(self,title):
        qStr = "SELECT * from " + TABLE_NAME + " where   title='"+title+"'"
        cursor.execute(qStr)
        data = cursor.fetchall()
        dict = {i:j for i, j,k in data}
        return dict
    
    def put(self,title):
        lastname = request.form['lastname']
        print (lastname)
        qStr = "update  user set lastname='"+lastname+"'where title='"+title+"'"
        cursor.execute(qStr)
        conn.commit()
        return 'ok'

class CreateUser(Resource):
    def post(self):
        title = request.form['title']
        lastname = request.form.get('lastname',None)
        qStr = "INSERT INTO user (title) VALUES ("+title+"')"
        cursor.execute(qStr)
        conn.commit()
        return 'ok'

api.add_resource(User, '/user/<title>')
api.add_resource(CreateUser, '/createuser/')

if __name__ == '__main__':
    app.run(debug=True)