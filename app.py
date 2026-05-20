# a) basic flask app
# b) containerise it 
# c) automate the build (using git)
# d) deployed it to the AWS

from flask import Flask;
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Devops Successfull!!!</h1> <p>Python + docker + Git + AWS</p>"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)