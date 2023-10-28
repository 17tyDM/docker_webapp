import os
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from mysql_model import Person

debug = os.getenv('DEBUG')
if debug == '0':
    from mysql_model import Person
    db_uri = os.getenv('DATABASE_URI')
else:
    from test_model import Person
    db_uri = os.getenv('SQLITE_URI')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['PORT'] = os.getenv('PORT')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/exercise_request/<test>')
def exercise_request(test):
    return f'exercise_request:{test}'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/show_exercise')
def show_exercise():
    myname = request.args.get("my_name")
    if myname is None:
        return render_template('exercise.html')
    else : # exercise.html の formタグのaction属性を設定しない <form action="http://127.0.0.1:5000/exercise">
        return f'これはif文で条件分岐しています。\rあなたの名前は:{request.args.get("my_name")}'
    
@app.route('/exercise')
def exercise():
    return f'あなたの名前は:{request.args.get("my_name")}'

@app.route('/answer')
def answer():
    name = request.args.get("my_name")
    return render_template('answer.html',name=f"{name}")

@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)

@app.route('/person_search')
def person_search():
    return render_template('person_search.html')

@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('person_result.html', persons=persons, search_size=search_size)

@app.route('/try_html')
def try_html():
    return render_template('try_html.html')

@app.route('/show_data', methods=['GET', 'POST'])
def show_data():
     return request.form