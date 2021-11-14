from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

loaded_model = joblib.load('dib_78.pkl')

@app.route('/')
def index():
    return render_template('diabetic.html')

@app.route('/homepage')
def home():
    return render_template('homepage.html')

@app.route('/diabetic')
def diabetic():
    return render_template('diabetic.html')

@app.route('/predict', methods=['POST'])
def predict():
    # fname = request.form.get('firstname')
    # lname = request.form.get('lastname')
    # email = request.form.get('email')
    # phone = request.form.get('phonenumber')

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
   
    #print (preg, plas, pres, skin, test, mass, pedi, age)
    prediction = loaded_model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if (prediction[0] == 1):
        print("You are diabetic")
        value = "You are diabetic"
    else:
        print( "You are not diabetic")
        val = "You are not diabetic"

    return render_template('result.html', value = val)

@app.route('/auth')
def auth():
    form = "Username: <input type = text name = 'uname'></input><br>Password: <input type = password name = 'pwd'></input>"
    return form


app_flask.run(host = '0.0.0.0', port=8080)
