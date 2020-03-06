from flask import Flask,request,render_template
import pickle
import pymongo

app = Flask(__name__)

@app.route('/')
def hello_world():
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

    mydb = client['login']

    information = mydb.login_table

    records = [{
        'username': 'nachi',
        'password': '123'
    },
        {
            'username': 'aki',
            'password': 'aki123'
        }
    ]

    information.insert_many(records)

    database = information.find_one()


    return render_template("index.html")

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    print(name1)
    print(pwd)

    client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

    mydb = client['login']

    information = mydb.login_table

    database = information.find_one()
    # database = {nachi:123}
    print(database)

    if name1 not in database:
	    return render_template('index.html',info='Innvalid User')
    else:
        if database[name1]!=pwd:
            return render_template('index.html',info='Invalid Password')
        else:
	         return render_template('home.html',name=name1)

if __name__ == '__main__':
    app.run()