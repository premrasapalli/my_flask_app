from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "🚀 RASAPALLI PREM GREATEST MAN IN THE WORLD"
=======
    return "🚀 RASAPALLI PREM IS GREATEST MAN IN THE WORLD....."
>>>>>>> a69835085f8a52e660e16f4dea7720e3a056ffc3

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

